using System;
using System.IO;
using MonteCarlo.External.MuxRemoting;
using CommandLine;
using System.Threading;
using System.Diagnostics;
using System.Runtime.Remoting;
using System.ComponentModel;
using System.Net.Sockets;
using System.Text;

namespace MuxServerHelper
{
    public class Program
    {
        class CliArgs
        {
            [Option("project", Required = true, HelpText = "Path to project xml file.")]
            public string ProjectFile { get; set; }

            [Option("clip", Default = 1, HelpText = "Clip Number for the project.")]
            public int ClipCount { get; set; }

            [Option("server", Required = true, HelpText = "Path to the Mux Server executable.")]
            public string MuxServerExecutable { get; set; }

            [Option("port", Default = "9920", HelpText = "Port of the Mux Server.")]
            public string Port { get; set; }

            [Option("wait", Default = true, HelpText = "Whether program waits and exits on muxing complete or cancelled.")]
            public bool WaitFinish { get; set; }

        }
        public static void InitConsoleRedirect(Action<string> callback)
        {
            Console.SetOut(new RealTimeWriter(callback));
        }
        public static int Run(string[] args)
        {
            return Parser.Default.ParseArguments<CliArgs>(args)
                .MapResult(opts => InvokeMuxServer(opts), _ => -1);
        }
        static IMuxRemotingService ConnectMuxService(string Port)
        {
            IMuxRemotingService muxService = (IMuxRemotingService)Activator.GetObject(typeof(IMuxRemotingService), $"tcp://localhost:{Port}/MuxRemotingService");
            muxService.GetServiceStatus();
            return muxService;
        }
        static void DisposeProcess(ref Process Proc)
        {
            if (Proc != null)
            {
                Proc.Dispose();
                Proc = null;
            }
        }
        static IMuxRemotingService StartMuxServerAndService(string MuxServerExecutable, string Port)
        {
            IMuxRemotingService muxService;
            FileInfo MuxServiceExecutableFile = new FileInfo(MuxServerExecutable);
            Process muxProc = null;
            try
            {
                muxService = ConnectMuxService(Port);  //assume muxer already started.
                if (muxProc == null || muxProc.HasExited)
                {
                    DisposeProcess(ref muxProc);
                    var tProcesses = Process.GetProcessesByName(MuxServiceExecutableFile.Name);
                    if (tProcesses.Length > 0)
                    {
                        muxProc = tProcesses[0];
                    }
                }
                return muxService;
            }
            catch (RemotingException) { }
            catch (SocketException) { }

            try
            {
                DisposeProcess(ref muxProc);
                ProcessStartInfo tStartInfo = new ProcessStartInfo(MuxServiceExecutableFile.FullName);
                tStartInfo.CreateNoWindow = true;
                muxProc = Process.Start(tStartInfo);
                muxService = ConnectMuxService(Port);  //retry.
                return muxService;
            }
            catch (InvalidOperationException) { }
            catch (FileNotFoundException) { }
            catch (RemotingException) { }
            catch (Win32Exception) { }

            return null;
        }
        static int InvokeMuxServer(CliArgs opts)
        {
            if (!File.Exists(opts.MuxServerExecutable))
            {
                Console.WriteLine($"MuxServerHelper.dll File Path Not Found.");
                Environment.Exit(-2);
            }

            bool IsProcessRunning(string processName)
            {
                Process[] processes = Process.GetProcessesByName(processName);
                return processes.Length > 0;
            }

            string target = "UHDMuxRemotingServer";
            string timestamp_0 = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            if (IsProcessRunning(target))
            {
                Console.WriteLine($"               Startup Finished - {timestamp_0}");
            }
            else
            {
                Console.WriteLine($"               Startup...");
            }
       
            var muxService = StartMuxServerAndService(opts.MuxServerExecutable, opts.Port);
            if (muxService.Equals(null))
            {
                return -2;
            }

            MuxEnqueueStruct tMuxTaskDef = new MuxEnqueueStruct(opts.ProjectFile, opts.ClipCount);
            var muxTaskId = muxService.Enqueue(tMuxTaskDef);
            if (opts.WaitFinish)
            {
                bool processStarted = false;
                bool fsPrinted = false;
                string timestamp_1 = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");

                for (; ; )
                {
                    var tInfo = muxService.GetRequestInfo(muxTaskId);
                    var tStatus = tInfo.Status;

                    if (!processStarted && tInfo.LastMuxStatusString.Contains("TS Component Processing"))
                    {
                        Console.WriteLine($"               Start Processing - {timestamp_1}");
                        processStarted = true;
                    }

                    if (!fsPrinted && tInfo.LastMuxStatusString.Contains("FS Component Processing"))
                    {
                        fsPrinted = true;
                    }

                    if (tStatus.HasFlag(MuxRequestStatus.EndFlag))
                    {

                        while (tInfo.LastMuxStatusCode == MuxCommon.MuxStatusCode.MUX_SN_S_PROC_TS)
                        {
                            Thread.Sleep(1000);
                            tInfo = muxService.GetRequestInfo(muxTaskId);
                        }

                        string timestamp_2 = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");

                        if (tInfo.LastMuxStatusCode == MuxCommon.MuxStatusCode.MUX_SN_S_DONE)
                        {
                            Console.WriteLine($"               Mux Complete - {timestamp_2}");
                            Console.WriteLine($"               Elapsed Time: {tInfo.ElapsedTime:hh\\:mm\\:ss}");
                            Console.WriteLine("\ntsSCB INFO : Closed gracefully tsSCB process.");
                        }
                        else
                        {
                            Console.WriteLine($"               Last Error Code: {tInfo.LastMuxStatusCode.ToString()}");
                            Console.WriteLine($"               Last MUX Status: {tInfo.LastMuxStatusString}");
                            Console.WriteLine($"               Elapsed Time: {tInfo.ElapsedTime:hh\\:mm\\:ss}");
                            Console.WriteLine($"               Note: For more log info, please see Mux Remoting Server in Details... -> Show Log...");
                            Console.WriteLine("\ntsSCB INFO : Closed abruptly tsSCB process.");
                        }

                        var tIsOk = tStatus.HasFlag(MuxRequestStatus.Processed);
                        tIsOk &= tInfo.LastMuxStatusCode == MuxCommon.MuxStatusCode.MUX_SN_S_DONE;
                        muxService.Confirm(muxTaskId);
                        if (tIsOk) { return 0; } else { return 1; }
                    }
                    Thread.Sleep(1000);
                }
            }
            return 0;
        }
    }

    public class RealTimeWriter : TextWriter
    {
        private readonly Action<string> _callback;

        public RealTimeWriter(Action<string> callback)
        {
            _callback = callback;
        }

        public override Encoding Encoding => Encoding.UTF8;

        public override void WriteLine(string value)
        {
            _callback?.Invoke(value);
        }

        public override void Write(string value)
        {
            _callback?.Invoke(value);
        }
    }
}