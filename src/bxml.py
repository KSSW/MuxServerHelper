# -*- coding: utf-8 -*-

import os
from pgtc import pg

def maked_playlist(in_time, out_time, out_tc_dv, value_chap, timestamps, sct, vfv, vfps, a_ves_pid_list, pg_all_value_list, video, a_ves_paths, s_pes_paths, aci_list, apt_list, sf_list, f_count, fdv_count, a_count, s_count, dp_x0_value, dp_y0_value, dp_x1_value, dp_y1_value, dp_x2_value, dp_y2_value, wp_x_value, wp_y_value, max_dml_value, min_dml_value, maxCLL_value, maxFALL_value, dynamic_range_type, sct_dv_value, video_dv_format_code, fps_code_0_dv, dm_value, cpf_value_mode_dv, color_space_dv, dynamic_range_type_dv, hdr10pf_value_mode_dv):
    if video:
        primary_video_stream = f"""
              <primary_video_stream>
                <stream_entry>
                  <type>1</type>
                  <Select_type>
                    <type_1>
                      <ref_to_stream_PID_of_mainClip>4113</ref_to_stream_PID_of_mainClip>
                    </type_1>
                  </Select_type>
                </stream_entry>
                <stream_attributes>
                  <stream_coding_type>{sct}</stream_coding_type>
                  <Select_stream_coding_type>
                    <video_stream>
                      <video_format>{vfv}</video_format>
                      <frame_rate>{vfps}</frame_rate>
                    </video_stream>
                  </Select_stream_coding_type>
                </stream_attributes>
              </primary_video_stream>
            """.strip()

        primary_audio_streams = []
        nodess = []
        nodes_not = []
        dv_noss = []
        dv_noss_final = []
        dv_noss_not_values = []
        number_of_SubPaths = []
        nos_numbers = []
        lp_dvs = []
        all_info_number_of_SubPaths_final = []
        
        if sct == '24':
                
            nodes = (
                f"          <static_metadata>\n"
                f"            <number_of_data_entries>1</number_of_data_entries>\n"
                f"            <Loop_static_metadata_entries>\n"
                f"              <static_metadata_entry>\n"
                f"                <dynamic_range_type_ref>{dynamic_range_type}</dynamic_range_type_ref>\n"
                f"                <number_of_display_primaries>3</number_of_display_primaries>\n"
                f"                <Loop_display_primaries>\n"
                f"                  <display_primaries>\n"
                f"                    <display_primaries_x>{dp_x0_value}</display_primaries_x>\n"
                f"                    <display_primaries_y>{dp_y0_value}</display_primaries_y>\n"
                f"                  </display_primaries>\n"
                f"                  <display_primaries>\n"
                f"                    <display_primaries_x>{dp_x1_value}</display_primaries_x>\n"
                f"                    <display_primaries_y>{dp_y1_value}</display_primaries_y>\n"
                f"                  </display_primaries>\n"
                f"                  <display_primaries>\n"
                f"                    <display_primaries_x>{dp_x2_value}</display_primaries_x>\n"
                f"                    <display_primaries_y>{dp_y2_value}</display_primaries_y>\n"
                f"                  </display_primaries>\n"
                f"                </Loop_display_primaries>\n"
                f"                <white_point_x>{wp_x_value}</white_point_x>\n"
                f"                <white_point_y>{wp_y_value}</white_point_y>\n"
                f"                <max_display_mastering_luminance>{max_dml_value}</max_display_mastering_luminance>\n"
                f"                <min_display_mastering_luminance>{min_dml_value}</min_display_mastering_luminance>\n"
                f"                <MaxCLL>{maxCLL_value}</MaxCLL>\n"
                f"                <MaxFALL>{maxFALL_value}</MaxFALL>\n"
                f"              </static_metadata_entry>\n"
                f"            </Loop_static_metadata_entries>\n"
                f"          </static_metadata>"
            )
            nodess.append(nodes)
            
        if dm_value:

            dv_nos = (

                f'            <Loop_enhancement_layer_video_stream>\n'
                f'              <enhancement_layer_video_stream>\n'
                f'                <stream_entry>\n'
                f'                  <type>4</type>\n'
                f'                  <Select_type>\n'
                f'                    <type_4>\n'
                f'                      <ref_to_SubPath_id>0</ref_to_SubPath_id>\n'
                f'                      <ref_to_stream_PID_of_mainClip>4117</ref_to_stream_PID_of_mainClip>\n'
                f'                    </type_4>\n'
                f'                  </Select_type>\n'
                f'                </stream_entry>\n'
                f'                <stream_attributes>\n'
                f'                  <stream_coding_type>{sct_dv_value}</stream_coding_type>\n'
                f'                  <Select_stream_coding_type>\n'
                f'                    <video_stream>\n'
                f'                      <video_format>{video_dv_format_code}</video_format>\n'
                f'                      <frame_rate>1</frame_rate>\n'
                f'                      <dynamic_range_type>{dynamic_range_type_dv}</dynamic_range_type>\n'
                f'                      <color_space>{color_space_dv}</color_space>\n'
                f'                      <cri_usage_flag>{cpf_value_mode_dv}</cri_usage_flag>\n'
                f'                    </video_stream>\n'
                f'                  </Select_stream_coding_type>\n'
                f'                </stream_attributes>\n'
                f'              </enhancement_layer_video_stream>\n'
                f'            </Loop_enhancement_layer_video_stream>'
            )

            dv_noss.append(dv_nos)

            number_of_SubPaths = (
                f'      <number_of_SubPaths>1</number_of_SubPaths>'

            )

            nos_numbers.append(number_of_SubPaths)

            lp_dv = (

                f'      </Loop_PlayItem>\n'
                f'      <Loop_SubPath>\n'
                f'        <SubPath>\n'
                f'          <SubPath_type>10</SubPath_type>\n'
                f'          <is_repeat_SubPath>false</is_repeat_SubPath>\n'
                f'          <number_of_SubPlayItems>1</number_of_SubPlayItems>\n'
                f'          <Loop_SubPlayItem>\n'
                f'            <SubPlayItem>\n'
                f'              <Clip_Information_file_name>88888</Clip_Information_file_name>\n'
                f'              <Clip_codec_identifier>M2TS</Clip_codec_identifier>\n'
                f'              <sp_connection_condition>1</sp_connection_condition>\n'
                f'              <is_multi_Clip_entries>false</is_multi_Clip_entries>\n'
                f'              <ref_to_STC_id>0</ref_to_STC_id>\n'
                f'              <SubPlayItem_IN_time>{in_time}</SubPlayItem_IN_time>\n'
                f'              <SubPlayItem_OUT_time>{out_tc_dv}</SubPlayItem_OUT_time>\n'
                f'              <sync_PlayItem_id>0</sync_PlayItem_id>\n'
                f'              <sync_start_PTS_of_PlayItem>{in_time}</sync_start_PTS_of_PlayItem>\n'
                f'              <Select_is_multi_Clip_entries />\n'
                f'            </SubPlayItem>\n'
                f'          </Loop_SubPlayItem>\n'
                f'        </SubPath>\n'
                f'      </Loop_SubPath>'          
            )

            lp_dvs.append(lp_dv)
                            
        else:
            
            nodes_not = (
                f"          <static_metadata>\n"
                f"            <number_of_data_entries>0</number_of_data_entries>\n"
                f"            <Loop_static_metadata_entries />\n"
                f"          </static_metadata>"
            )

            nodess.append(nodes_not)

            number_of_SubPaths = (
                f'      <number_of_SubPaths>0</number_of_SubPaths>'

            )

            nos_numbers.append(number_of_SubPaths)

            dv_noss_not_value = (
                f'            <Loop_enhancement_layer_video_stream />'
            )

            dv_noss.append(dv_noss_not_value)

            number_of_SubPaths_not = (
                    f'      </Loop_PlayItem>\n'
                    f'      <Loop_SubPath />'
            )

            lp_dvs.append(number_of_SubPaths_not)

    nodess_final = "\n".join(nodess)
    dv_noss_final = "\n".join(dv_noss)
    nos_numbers_final = "\n".join(nos_numbers)
    all_info_number_of_SubPaths_final = "\n".join(lp_dvs)

    for idx, (pid, a_path, lang), in enumerate(a_ves_pid_list):
        aci_code = aci_list[idx]
        apt_value = apt_list[idx]
        sf_value = sf_list[idx]
        final_stream = []
                
        if a_ves_paths:
            audio_stream_block = (
                               f"              <primary_audio_stream>\n"
                               f"                <stream_entry>\n"
                               f"                  <type>1</type>\n"
                               f"                  <Select_type>\n"
                               f"                    <type_1>\n"
                               f"                      <ref_to_stream_PID_of_mainClip>{pid}</ref_to_stream_PID_of_mainClip>\n"
                               f"                    </type_1>\n"
                               f"                  </Select_type>\n"
                               f"                </stream_entry>\n"
                               f"                <stream_attributes>\n"
                               f"                  <stream_coding_type>{aci_code}</stream_coding_type>\n"
                               f"                  <Select_stream_coding_type>\n"
                               f"                    <audio_stream>\n"
                               f"                      <audio_presentation_type>{apt_value}</audio_presentation_type>\n"
                               f"                      <sampling_frequency>{sf_value}</sampling_frequency>\n"
                               f"                      <audio_language_code>{lang}</audio_language_code>\n"
                               f"                    </audio_stream>\n"
                               f"                  </Select_stream_coding_type>\n"
                               f"                </stream_attributes>\n"
                               f"              </primary_audio_stream>"
            )
            primary_audio_streams.append(audio_stream_block)

    for s_pid, s_path, s_lang, sin_timecode, pg_value in pg_all_value_list:

        if s_pes_paths:
            subtitles = (
                f"              <PG_textST_stream>\n"
                f"                <stream_entry>\n"
                f"                  <type>1</type>\n"
                f"                  <Select_type>\n"
                f"                    <type_1>\n"
                f"                      <ref_to_stream_PID_of_mainClip>{s_pid}</ref_to_stream_PID_of_mainClip>\n"
                f"                    </type_1>\n"
                f"                  </Select_type>\n"
                f"                </stream_entry>\n"
                f"                <stream_attributes>\n"
                f"                  <stream_coding_type>90</stream_coding_type>\n"
                f"                  <Select_stream_coding_type>\n"
                f"                    <PG_stream>\n"
                f"                      <PG_language_code>{s_lang}</PG_language_code>\n"
                f"                    </PG_stream>\n"
                f"                  </Select_stream_coding_type>\n"
                f"                </stream_attributes>\n"
                f"              </PG_textST_stream>"
            )
            final_stream.append(subtitles)

    all_audio_streams_final = "\n".join(primary_audio_streams)
    all_sub_streams_final = "\n".join(final_stream)

    pl_marks = ""
    for ts in value_chap:
        pl_marks = "".join(f"""
        <PL_Mark>
          <mark_type>01</mark_type>
          <ref_to_PlayItem_id>0</ref_to_PlayItem_id>
          <mark_time_stamp>{ts}</mark_time_stamp>
          <entry_ES_PID>65535</entry_ES_PID>
          <duration>0</duration>
        </PL_Mark>""" for ts in value_chap)

    xml_template = f"""
<?xml version="1.0" encoding="UTF-8"?>
<MoviePlayListFile Version="0099" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="MoviePlayList.xsd">
  <MPLS FileName="00000">
    <type_indicator>MPLS</type_indicator>
    <version_number>0300</version_number>
    <AppInfoPlayList>
      <PlayList_playback_type>1</PlayList_playback_type>
      <Select_PlayList_playback_type />
      <UO_mask_table>
        <reserved_for_menu_call_mask>false</reserved_for_menu_call_mask>
        <reserved_for_title_search_mask>false</reserved_for_title_search_mask>
        <chapter_search_mask>false</chapter_search_mask>
        <time_search_mask>false</time_search_mask>
        <skip_to_next_point_mask>false</skip_to_next_point_mask>
        <skip_back_to_previous_point_mask>false</skip_back_to_previous_point_mask>
        <stop_mask>false</stop_mask>
        <pause_on_mask>false</pause_on_mask>
        <still_off_mask>false</still_off_mask>
        <forward_play_mask>false</forward_play_mask>
        <backward_play_mask>false</backward_play_mask>
        <resume_mask>false</resume_mask>
        <move_up_selected_button_mask>false</move_up_selected_button_mask>
        <move_down_selected_button_mask>false</move_down_selected_button_mask>
        <move_left_selected_button_mask>false</move_left_selected_button_mask>
        <move_right_selected_button_mask>false</move_right_selected_button_mask>
        <select_button_mask>false</select_button_mask>
        <activate_button_mask>false</activate_button_mask>
        <select_button_and_activate_mask>false</select_button_and_activate_mask>
        <primary_audio_stream_number_change_mask>false</primary_audio_stream_number_change_mask>
        <angle_number_change_mask>false</angle_number_change_mask>
        <popup_on_mask>false</popup_on_mask>
        <popup_off_mask>false</popup_off_mask>
        <PG_textST_enable_disable_mask>false</PG_textST_enable_disable_mask>
        <PG_textST_stream_number_change_mask>false</PG_textST_stream_number_change_mask>
        <secondary_video_enable_disable_mask>true</secondary_video_enable_disable_mask>
        <secondary_video_stream_number_change_mask>true</secondary_video_stream_number_change_mask>
        <secondary_audio_enable_disable_mask>true</secondary_audio_enable_disable_mask>
        <secondary_audio_stream_number_change_mask>true</secondary_audio_stream_number_change_mask>
        <PiP_PG_textST_stream_number_change_mask>true</PiP_PG_textST_stream_number_change_mask>
      </UO_mask_table>
      <PlayList_random_access_flag>false</PlayList_random_access_flag>
      <audio_mix_app_flag>true</audio_mix_app_flag>
      <lossless_may_bypass_mixer_flag>false</lossless_may_bypass_mixer_flag>
      <MVC_Base_view_R_flag>false</MVC_Base_view_R_flag>
      <SDR_conversion_notification_flag>false</SDR_conversion_notification_flag>
    </AppInfoPlayList>
    <Loop_padding_word_1 />
    <PlayList>
      <number_of_PlayItems>1</number_of_PlayItems>
{nos_numbers_final}
      <Loop_PlayItem>
        <PlayItem>
          <Clip_Information_file_name>88888</Clip_Information_file_name>
          <Clip_codec_identifier>M2TS</Clip_codec_identifier>
          <is_multi_angle>false</is_multi_angle>
          <connection_condition>1</connection_condition>
          <ref_to_STC_id>0</ref_to_STC_id>
          <IN_time>{in_time}</IN_time>
          <OUT_time>{out_time}</OUT_time>
          <UO_mask_table>
            <reserved_for_menu_call_mask>false</reserved_for_menu_call_mask>
            <reserved_for_title_search_mask>false</reserved_for_title_search_mask>
            <chapter_search_mask>false</chapter_search_mask>
            <time_search_mask>false</time_search_mask>
            <skip_to_next_point_mask>false</skip_to_next_point_mask>
            <skip_back_to_previous_point_mask>false</skip_back_to_previous_point_mask>
            <stop_mask>false</stop_mask>
            <pause_on_mask>false</pause_on_mask>
            <still_off_mask>false</still_off_mask>
            <forward_play_mask>false</forward_play_mask>
            <backward_play_mask>false</backward_play_mask>
            <resume_mask>false</resume_mask>
            <move_up_selected_button_mask>false</move_up_selected_button_mask>
            <move_down_selected_button_mask>false</move_down_selected_button_mask>
            <move_left_selected_button_mask>false</move_left_selected_button_mask>
            <move_right_selected_button_mask>false</move_right_selected_button_mask>
            <select_button_mask>false</select_button_mask>
            <activate_button_mask>false</activate_button_mask>
            <select_button_and_activate_mask>false</select_button_and_activate_mask>
            <primary_audio_stream_number_change_mask>false</primary_audio_stream_number_change_mask>
            <angle_number_change_mask>false</angle_number_change_mask>
            <popup_on_mask>false</popup_on_mask>
            <popup_off_mask>false</popup_off_mask>
            <PG_textST_enable_disable_mask>false</PG_textST_enable_disable_mask>
            <PG_textST_stream_number_change_mask>false</PG_textST_stream_number_change_mask>
            <secondary_video_enable_disable_mask>true</secondary_video_enable_disable_mask>
            <secondary_video_stream_number_change_mask>true</secondary_video_stream_number_change_mask>
            <secondary_audio_enable_disable_mask>true</secondary_audio_enable_disable_mask>
            <secondary_audio_stream_number_change_mask>true</secondary_audio_stream_number_change_mask>
            <PiP_PG_textST_stream_number_change_mask>true</PiP_PG_textST_stream_number_change_mask>
          </UO_mask_table>
          <PlayItem_random_access_flag>false</PlayItem_random_access_flag>
          <still_mode>00</still_mode>
          <Select_still_mode />
          <Select_is_multi_angle />
          <STN_table>
            <number_of_primary_video_stream_entries>{f_count}</number_of_primary_video_stream_entries>
            <number_of_primary_audio_stream_entries>{a_count}</number_of_primary_audio_stream_entries>
            <number_of_PG_textST_stream_entries>{s_count}</number_of_PG_textST_stream_entries>
            <number_of_IG_stream_entries>0</number_of_IG_stream_entries>
            <number_of_secondary_audio_stream_entries>0</number_of_secondary_audio_stream_entries>
            <number_of_secondary_video_stream_entries>0</number_of_secondary_video_stream_entries>
            <number_of_PiP_PG_textST_stream_entries_plus>0</number_of_PiP_PG_textST_stream_entries_plus>
            <number_of_enhancement_layer_video_stream_entries>{fdv_count}</number_of_enhancement_layer_video_stream_entries>
            <Loop_primary_video_stream>
              {primary_video_stream}
            </Loop_primary_video_stream>
            <Loop_primary_audio_stream>
{all_audio_streams_final}
            </Loop_primary_audio_stream>
            <Loop_PG_textST_stream>
{all_sub_streams_final}
            </Loop_PG_textST_stream>
            <Loop_IG_stream />
            <Loop_secondary_audio_stream />
            <Loop_secondary_video_stream />
{dv_noss_final}
          </STN_table>
        </PlayItem>
{all_info_number_of_SubPaths_final}
    </PlayList>
    <Loop_padding_word_2 />
    <PlayListMark>
      <number_of_PlayList_marks>{len(value_chap)}</number_of_PlayList_marks>
      <Loop_PL_Mark>{pl_marks}
      </Loop_PL_Mark>
    </PlayListMark>
    <Loop_padding_word_3 />
    <ExtensionData>
      <number_of_ext_data_entries>1</number_of_ext_data_entries>
      <Loop_ext_data_entries>
        <ext_data_entry>
          <ID1>3</ID1>
          <ID2>5</ID2>
        </ext_data_entry>
      </Loop_ext_data_entries>
      <Loop_padding_word />
      <Loop_data_block>
        <data_block>
{nodess_final}
        </data_block>
      </Loop_data_block>
    </ExtensionData>
    <Loop_padding_word_4 />
  </MPLS>
</MoviePlayListFile>
    """.strip()

    return xml_template

def maked_clip(fu, in_time, out_time, timestamps, v_ves_path, dv_ves_path, sct, vfv, vfps, a_ves_paths, s_pes_paths, aci_list, apt_list, sf_list, adps_list, ca_list, bps_list, v_idc, lidc, frame_mbs_only_flag, long_GOP,
               dts_stream_type_value_list, ast_value_list, src_value_list, bsid_value_list, brc_value_list, dsurmod_value_list, bsmod_value_list, nc_value_list, full_svc_value_list, langcod_value_list, langcod2_value_list, mainid_value_list, asvcflags_value_list, tcflag_value_list, mlp_sampling_rate_value_list,
               a_ves_pid_list, pg_all_value_list, cri_present_flag, dynamic_range_type, colour_primaries, HDR10plus_present_flag, sct_dv_value, video_dv_format_code, fps_code_0_dv, cpf_value_mode_dv, color_space_dv, dynamic_range_type_dv, hdr10pf_value_mode_dv, nosip, mp):

    # Output
    TSIntermediate = r"Output\MUX\BDROM\TSIntermediate\88888"
    STREAM = r"Output\MUX\BDROM\DB\BDMV\STREAM"
    TSmediate = os.path.join(mp, TSIntermediate)
    m2ts = os.path.join(mp, STREAM)
    os.makedirs(TSmediate, exist_ok=True)
    os.makedirs(m2ts, exist_ok=True)

    a_pid = ""
    s_pid = ""
    blocks_a = []
    blocks_s = []
    pmss = []
    spsts = []
    spstss = []
    total_a = len(a_ves_paths)
    total_s = len(s_pes_paths)

    for ((a_pid, a_ves_path, a_lang), (s_pid, s_path, s_lang, sin_timecode, pg_value)) in zip(a_ves_pid_list, pg_all_value_list):
        a, _ = os.path.splitext(a_ves_path)
        a_mui_path = a + ".mui"

        s, _ = os.path.splitext(s_path)
        s_mui_path = s_path + ".mui"

        if sin_timecode:
            spsts = (
                f"                <stream_presentation_start_time>{pg_value}</stream_presentation_start_time>\n"
        )
            spstss.append(spsts)
        else:
            if sin_timecode != "00:00:00:00":
                spsts = ""

        block_a = (
              f"              <ESData_TS>\n"
              f"                <stream_PID>{a_pid}</stream_PID>\n"
              f"                <VES_InputFilename>{a_ves_path}</VES_InputFilename>\n"
              f"                <MUI_InputFilename>{a_mui_path}</MUI_InputFilename>\n"
              f"                <ESData_RwBufferSize>10240</ESData_RwBufferSize>\n"
              f"              </ESData_TS>"
        )
        blocks_a.append(block_a)

        block_s = (
              f"              <ESData_TS>\n"
              f"                <stream_PID>{s_pid}</stream_PID>\n"
              f"{spsts}"
              f"                <VES_InputFilename>{s_path}</VES_InputFilename>\n"
              f"                <MUI_InputFilename>{s_mui_path}</MUI_InputFilename>\n"
              f"                <ESData_RwBufferSize>10240</ESData_RwBufferSize>\n"
              f"              </ESData_TS>"
        )
        blocks_s.append(block_s)

        if s_path:
            pms = (
            f"            <streams_in_ps>\n"
            f"              <stream_PID>{s_pid}</stream_PID>\n"
            f"              <StreamCodingInfo>\n"
            f"                <stream_coding_type>90</stream_coding_type>\n"
            f"                <Select_stream_coding_type>\n"
            f"                  <PG_stream>\n"
            f"                    <PG_language_code>{s_lang}</PG_language_code>\n"
            f"                    <ISRC>\n"
            f"                      <country_code />\n"
            f"                      <copyright_holder />\n"
            f"                      <recording_year />\n"
            f"                      <recording_number />\n"
            f"                    </ISRC>\n"
            f"                  </PG_stream>\n"
            f"                </Select_stream_coding_type>\n"
            f"              </StreamCodingInfo>\n"
            f"            </streams_in_ps>"
            )
            pmss.append(pms)

    apid = "\n".join(blocks_a + blocks_s)
    all_streams_in_ps = "\n".join(pmss)

    v, _ = os.path.splitext(v_ves_path)
    v_mui_path = v + ".mui"

    if dv_ves_path:
        dv, _= os.path.splitext(dv_ves_path)
        dv_mui_path = dv + ".mui"

    video_stream_avc = f"""  <MPEG4_video_stream>
                        <profile_idc>{v_idc}</profile_idc>
                        <level_idc>{lidc}</level_idc>
                        <frame_mbs_only_flag>{frame_mbs_only_flag}</frame_mbs_only_flag>
                        <long_GOP>{long_GOP}</long_GOP>
                      </MPEG4_video_stream>"""

    video_stream_hevc = f"""  <HEVC_video_stream>
                        <cri_present_flag>{cri_present_flag}</cri_present_flag>
                        <dynamic_range_type>{dynamic_range_type}</dynamic_range_type>
                        <color_space>{colour_primaries}</color_space>
                        <HDR10plus_present_flag>{HDR10plus_present_flag}</HDR10plus_present_flag>
                      </HEVC_video_stream>"""

    if sct == '1B':
        video_stream = video_stream_avc
    elif sct == '24':
        video_stream = video_stream_hevc

    syyqs = []
    dv_ves = ''
    dv_ves_block = ''
    dv_ves_all_info = ''

    if v_ves_path:
        syys = f"""<ESData_TS>
                <stream_PID>4113</stream_PID>
                <VES_InputFilename>{v_ves_path}</VES_InputFilename>
                <MUI_InputFilename>{v_mui_path}</MUI_InputFilename>
                <ESData_RwBufferSize>10240</ESData_RwBufferSize>
              </ESData_TS>"""
         
        sip_v = f"""  <streams_in_ps>
              <stream_PID>4113</stream_PID>
              <StreamCodingInfo>
                <stream_coding_type>{sct}</stream_coding_type>
                <Select_stream_coding_type>
                  <Video_stream>
                    <video_format>{vfv}</video_format>
                    <frame_rate>{vfps}</frame_rate>
                    <aspect_ratio>3</aspect_ratio>
                    <cc_flag>false</cc_flag>
                    <ISRC>
                      <country_code />
                      <copyright_holder />
                      <recording_year />
                      <recording_number />
                    </ISRC>
                    <Select_Video_stream>
                    {video_stream}
                    </Select_Video_stream>
                  </Video_stream>
                </Select_stream_coding_type>
              </StreamCodingInfo>
            </streams_in_ps>"""

    if dv_ves_path:
        syyq = (
            f'              <ESData_TS>\n'
            f'                <stream_PID>4117</stream_PID>\n'
            f'                <VES_InputFilename>{dv_ves_path}</VES_InputFilename>\n'
            f'                <MUI_InputFilename>{dv_mui_path}</MUI_InputFilename>\n'
            f'                <ESData_RwBufferSize>10240</ESData_RwBufferSize>\n'    
            f'              </ESData_TS>' 
         )
        syyqs.append(syyq)
              
        f_dv_value = "\n".join(syyqs)
        dv_ves_block = f"\n{f_dv_value}" if f_dv_value else ""


        sip_dv = f"""            <streams_in_ps>
              <stream_PID>4117</stream_PID>
              <StreamCodingInfo>
                <stream_coding_type>{sct_dv_value}</stream_coding_type>
                <Select_stream_coding_type>
                  <Video_stream>
                    <video_format>{video_dv_format_code}</video_format>
                    <frame_rate>{fps_code_0_dv}</frame_rate>
                    <aspect_ratio>3</aspect_ratio>
                    <cc_flag>false</cc_flag>
                    <ISRC>
                      <country_code />
                      <copyright_holder />
                      <recording_year />
                      <recording_number />
                    </ISRC>
                    <Select_Video_stream>
                      <HEVC_video_stream>
                        <cri_present_flag>{cpf_value_mode_dv}</cri_present_flag>
                        <dynamic_range_type>{dynamic_range_type_dv}</dynamic_range_type>
                        <color_space>{color_space_dv}</color_space>
                        <HDR10plus_present_flag>{hdr10pf_value_mode_dv}</HDR10plus_present_flag>
                      </HEVC_video_stream>
                    </Select_Video_stream>
                  </Video_stream>
                </Select_stream_coding_type>
              </StreamCodingInfo>
            </streams_in_ps>"""

        dv_ves_all_info = f"\n{sip_dv}" if sip_dv else ""
    
    audio_stream = ""
    blocks = []
    blocks_80 = []
    blocks_816 = []
    blocks_8256 = []
    dts_index = 0
    dolby_index = 0

    for idx, (pid, a_path, lang) in enumerate(a_ves_pid_list):
        aci_code = aci_list[idx]
        apt_value = apt_list[idx]
        sf_value = sf_list[idx]

        if idx < len(adps_list) and idx < len(ca_list) and idx < len(bps_list) and apt_list[idx] and ca_list[idx] and bps_list[idx]:
            adps_value= adps_list[idx]
            ca_value = ca_list[idx]
            bps_value = bps_list[idx]
        else:
            adps_value = None
            ca_value = None
            bps_value = None

        if a_ves_paths:
            if aci_code == '80':
                block_80 = (
                    f"            <streams_in_ps>\n"
                    f"              <stream_PID>{pid}</stream_PID>\n"
                    f"              <StreamCodingInfo>\n"
                    f"                <stream_coding_type>{aci_code}</stream_coding_type>\n"
                    f"                <Select_stream_coding_type>\n"
                    f"                  <Audio_stream>\n"
                    f"                    <audio_presentation_type>{apt_value}</audio_presentation_type>\n"
                    f"                    <sampling_frequency>{sf_value}</sampling_frequency>\n"
                    f"                    <audio_language_code>{lang}</audio_language_code>\n"
                    f"                    <ISRC>\n"
                    f"                      <country_code />\n"
                    f"                      <copyright_holder />\n"
                    f"                      <recording_year />\n"
                    f"                      <recording_number />\n"
                    f"                    </ISRC>\n"
                    f"                    <Select_Audio_stream>\n"
                    f"                      <LPCM_audio>\n"
                    f"                        <audio_data_payload_size>{adps_value}</audio_data_payload_size>\n"
                    f"                        <channel_assignment>{ca_value}</channel_assignment>\n"
                    f"                        <bits_per_sample>{bps_value}</bits_per_sample>\n"
                    f"                      </LPCM_audio>\n"
                    f"                    </Select_Audio_stream>\n"
                    f"                  </Audio_stream>\n"
                    f"                </Select_stream_coding_type>\n"
                    f"              </StreamCodingInfo>\n"
                    f"            </streams_in_ps>"
                )
                blocks_80.append(block_80)

            elif aci_code in ['81', '83', '84']:

                    if dolby_index < len(ast_value_list) and dolby_index < len(src_value_list) and dolby_index < len(bsid_value_list) and dolby_index < len(brc_value_list) and dolby_index < len(dsurmod_value_list) and dolby_index < len(bsmod_value_list) and \
                        dolby_index < len(nc_value_list) and dolby_index < len(full_svc_value_list) and dolby_index < len(langcod_value_list) and dolby_index < len(langcod2_value_list) and dolby_index < len(mainid_value_list) and dolby_index < len(asvcflags_value_list) and dolby_index < len(tcflag_value_list):
                        
                        ast_types = ast_value_list[dolby_index]
                        src_types = src_value_list[dolby_index]
                        bsid_types = bsid_value_list[dolby_index]
                        brc_types = brc_value_list[dolby_index]
                        dsurmod_types = dsurmod_value_list[dolby_index]
                        bsmod_types = bsmod_value_list[dolby_index]
                        nc_types = nc_value_list[dolby_index]
                        full_svc_types = full_svc_value_list[dolby_index]
                        langcod_types = langcod_value_list[dolby_index]
                        langcod2_types = langcod2_value_list[dolby_index]
                        mainid_types = mainid_value_list[dolby_index]
                        asvcflags_types = asvcflags_value_list[dolby_index]
                        tcflag_types = tcflag_value_list[dolby_index]

                        if aci_code == '83':
                            if dolby_index < len(mlp_sampling_rate_value_list):
                                mlp_sampling_rate_value_types = mlp_sampling_rate_value_list[dolby_index]

                            else:
                                mlp_sampling_rate_value_types = ""
                        
                    else:
                        ast_types = ""
                        src_types = ""
                        bsid_types = ""
                        brc_types = ""
                        dsurmod_types = ""
                        bsmod_types = ""
                        nc_types = ""
                        full_svc_types = ""
                        langcod_types = ""
                        langcod2_types = ""
                        mainid_types = ""
                        asvcflags_types = ""
                        tcflag_types = ""
                        
                    mlp = ""
                    if aci_code == '83' and mlp_sampling_rate_value_types:
                        mlp = f"                        <mlp_sampling_rate>{mlp_sampling_rate_value_types}</mlp_sampling_rate>\n"
                                                
                    dolby_index += 1

                    block_816 = (
                        f"            <streams_in_ps>\n"
                        f"              <stream_PID>{pid}</stream_PID>\n"
                        f"              <StreamCodingInfo>\n"
                        f"                <stream_coding_type>{aci_code}</stream_coding_type>\n"
                        f"                <Select_stream_coding_type>\n"
                        f"                  <Audio_stream>\n"
                        f"                    <audio_presentation_type>{apt_value}</audio_presentation_type>\n"
                        f"                    <sampling_frequency>{sf_value}</sampling_frequency>\n"
                        f"                    <audio_language_code>{lang}</audio_language_code>\n"
                        f"                    <ISRC>\n"
                        f"                      <country_code />\n"
                        f"                      <copyright_holder />\n"
                        f"                      <recording_year />\n"
                        f"                      <recording_number />\n"
                        f"                    </ISRC>\n"
                        f"                    <Select_Audio_stream>\n"
                        f"                      <AC3_audio>\n"
                        f"                        <ac3_stream_type>{ast_types}</ac3_stream_type>\n"
                        f"                        <sample_rate_code>{src_types}</sample_rate_code>\n"
                        f"                        <bsid>{bsid_types}</bsid>\n"
                        f"                        <bit_rate_code>{brc_types}</bit_rate_code>\n"
                        f"                        <dsurmod>{dsurmod_types}</dsurmod>\n"
                        f"                        <bsmod>{bsmod_types}</bsmod>\n"
                        f"                        <num_channels>{nc_types}</num_channels>\n"
                        f"                        <full_svc>{full_svc_types}</full_svc>\n"
                        f"                        <langcod>{langcod_types}</langcod>\n"
                        f"                        <langcod2>{langcod2_types}</langcod2>\n"
                        f"                        <mainid>{mainid_types}</mainid>\n"
                        f"                        <asvcflags>{asvcflags_types}</asvcflags>\n"
                        f"                        <text_code>{tcflag_types}</text_code>\n"
                        f"                        <text />\n"
                        f"{mlp}"
                        f"                      </AC3_audio>\n"
                        f"                    </Select_Audio_stream>\n"
                        f"                  </Audio_stream>\n"
                        f"                </Select_stream_coding_type>\n"
                        f"              </StreamCodingInfo>\n"
                        f"            </streams_in_ps>"
                    )
                    blocks_816.append(block_816)

            elif aci_code in ['82', '85', '86']:

                if dts_index < len(dts_stream_type_value_list):
                    dts_types = dts_stream_type_value_list[dts_index]
                else:
                    dts_types = ""
                dts_index += 1
                     
                block_8256 = (
                    f"            <streams_in_ps>\n"
                    f"              <stream_PID>{pid}</stream_PID>\n"
                    f"              <StreamCodingInfo>\n"
                    f"                <stream_coding_type>{aci_code}</stream_coding_type>\n"
                    f"                <Select_stream_coding_type>\n"
                    f"                  <Audio_stream>\n"
                    f"                    <audio_presentation_type>{apt_value}</audio_presentation_type>\n"
                    f"                    <sampling_frequency>{sf_value}</sampling_frequency>\n"
                    f"                    <audio_language_code>{lang}</audio_language_code>\n"
                    f"                    <ISRC>\n"
                    f"                      <country_code />\n"
                    f"                      <copyright_holder />\n"
                    f"                      <recording_year />\n"
                    f"                      <recording_number />\n"
                    f"                    </ISRC>\n"
                    f"                    <Select_Audio_stream>\n"
                    f"                      <DTS_audio>\n"
                    f"                        <dts_stream_type>{dts_types}</dts_stream_type>\n"
                    f"                      </DTS_audio>\n"
                    f"                    </Select_Audio_stream>\n"
                    f"                  </Audio_stream>\n"
                    f"                </Select_stream_coding_type>\n"
                    f"              </StreamCodingInfo>\n"
                    f"            </streams_in_ps>"
                )
                blocks_8256.append(block_8256)

        audio_stream = "\n".join(blocks_80 + blocks_816 + blocks_8256)
                                                        
    xml_template = f"""
<?xml version="1.0" encoding="UTF-8"?>
<CLIPDescriptorFile Version="0099" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="CLIPDescriptor.xsd">
  <CLPI FileName="88888">
    <type_indicator>HDMV</type_indicator>
    <version_number>0300</version_number>
    <ClipInfo>
      <Clip_stream_type>1</Clip_stream_type>
      <application_type>1</application_type>
      <is_ATC_delta>false</is_ATC_delta>
      <TS_type_info_block>
        <Validity_flags>80</Validity_flags>
        <Format_identifier>48444D56</Format_identifier>
        <Network_information>000000000000000000</Network_information>
        <Stream_format_name>00000000000000000000000000000000</Stream_format_name>
      </TS_type_info_block>
      <Select_is_ATC_delta />
      <Select_application_type />
    </ClipInfo>
    <Loop_padding_word_1 />
    <SequenceInfo>
      <number_of_ATC_sequences>1</number_of_ATC_sequences>
      <Loop_ATC_sequence>
        <ATC_sequence>
          <number_of_STC_sequences>1</number_of_STC_sequences>
          <Loop_STC_sequence>
            <STC_sequence>
              <presentation_start_time>{in_time}</presentation_start_time>
              <presentation_end_time>{out_time}</presentation_end_time>
              {syys}\n{apid}{dv_ves_block}
            </STC_sequence>
          </Loop_STC_sequence>
        </ATC_sequence>
      </Loop_ATC_sequence>
    </SequenceInfo>
    <Loop_padding_word_2 />
    <ProgramInfo>
      <number_of_program_sequences>1</number_of_program_sequences>
      <Loop_program_sequences>
        <program_sequences>
          <SPN_program_sequence_start>0</SPN_program_sequence_start>
          <program_map_PID>256</program_map_PID>
          <number_of_streams_in_ps>{nosip}</number_of_streams_in_ps>
          <Loop_stream_in_ps>
          {sip_v}\n{audio_stream}\n{all_streams_in_ps}{dv_ves_all_info}
          </Loop_stream_in_ps>
        </program_sequences>
      </Loop_program_sequences>
    </ProgramInfo>
    <Loop_padding_word_3 />
    <CPI>
      <Select_CPI_data />
    </CPI>
    <Loop_padding_word_4 />
    <ClipMark>
      <length>0</length>
    </ClipMark>
    <Loop_padding_word_5 />
    <Loop_padding_word_6 />
    <HDMV_TS_Descriptor>
      <HDMV_copy_control_descriptor>
        <private_data_byte1>
          <Reserved>01</Reserved>
          <RetentionMoveMode>01</RetentionMoveMode>
          <RetentionState>07</RetentionState>
          <EPN>01</EPN>
          <CCI>03</CCI>
        </private_data_byte1>
        <private_data_byte2>
          <Reserved2>1F</Reserved2>
          <ImageConstraintToken>00</ImageConstraintToken>
          <APS>00</APS>
        </private_data_byte2>
      </HDMV_copy_control_descriptor>
    </HDMV_TS_Descriptor>
    <TP_extra_header>
      <copy_permission_indicator>3</copy_permission_indicator>
    </TP_extra_header>
    <M2TSDirectoryList>
      <TS_Intermediatefile_dir>{mp}{fu}{TSIntermediate}</TS_Intermediatefile_dir>
      <TS_Intermediatefile_RwBufferSize>10240</TS_Intermediatefile_RwBufferSize>
      <TS_M2TS_output_dir>{mp}{fu}{STREAM}</TS_M2TS_output_dir>
      <TS_M2TS_output_RwBufferSize>10240</TS_M2TS_output_RwBufferSize>
    </M2TSDirectoryList>
  </CLPI>
</CLIPDescriptorFile>
""".strip()

    return xml_template

def maked_fsdescriptor(fu, mp):
    # Output
    TSIntermediate = r"Output\MUX\BDROM\TSIntermediate\88888"
    FSIntermediate = r"Output\MUX\BDROM\FSIntermediate"
    DBIntermediate = r"Output\MUX\BDROM\DBIntermediate"
    STREAM = r"Output\MUX\BDROM\DB\BDMV\STREAM"
    BDMV = r"Output\MUX\BDROM\DB\BDMV"
    PLAYLIST = r"Output\MUX\BDROM\DB\BDMV\PLAYLIST"
    CLIPINF = r"Output\MUX\BDROM\DB\BDMV\CLIPINF"
    CERTIFICATE = r"Output\MUX\BDROM\DB\CERTIFICATE"
    BACKUP = r"Output\MUX\BDROM\DB\CERTIFICATE\BACKUP"
    AACS = r"Output\MUX\BDROM\DB\AACS"
    DUPLICATE = r"Output\MUX\BDROM\DB\AACS\DUPLICATE"
    image = r"image\BDROM"
    FSIntermediate = r"Output\MUX\BDROM\FSIntermediate"
    BACKUP_CLIPINF = r"Output\MUX\BDROM\DB\BDMV\BACKUP\CLIPINF"
    BACKUP_PLAYLIST = r"Output\MUX\BDROM\DB\BDMV\BACKUP\PLAYLIST"
    META = r"Output\MUX\BDROM\DB\BDMV\META"
    AACS = r"Output\MUX\BDROM\DB\AACS"
    AACS_DUPLICATE = r"Output\MUX\BDROM\DB\AACS\DUPLICATE"

    image = os.path.join(mp, image)
    PLAYLIST = os.path.join(mp, PLAYLIST)
    CLIPINF = os.path.join(mp, CLIPINF)
    BACKUP_CLIPINF = os.path.join(mp, BACKUP_CLIPINF)
    BACKUP_PLAYLIST = os.path.join(mp, BACKUP_PLAYLIST)
    META = os.path.join(mp, META)
    FSIntermediate = os.path.join(mp, FSIntermediate)
    DBIntermediate = os.path.join(mp, DBIntermediate)
    os.makedirs(image, exist_ok=True)
    os.makedirs(PLAYLIST, exist_ok=True)
    os.makedirs(CLIPINF, exist_ok=True)
    os.makedirs(BACKUP_CLIPINF, exist_ok=True)
    os.makedirs(BACKUP_PLAYLIST, exist_ok=True)
    os.makedirs(META, exist_ok=True)
    os.makedirs(FSIntermediate, exist_ok=True)
    os.makedirs(DBIntermediate, exist_ok=True)

    xml_template = f"""
<?xml version="1.0" encoding="UTF-8"?>
<FSDescriptor Version="0099" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="FSDescriptor.xsd">
  <ForBDCMFCreator>
    <ApplicationInfo>
      <Software>N{fu}A</Software>
      <Version>N{fu}A</Version>
    </ApplicationInfo>
  </ForBDCMFCreator>
  <Volume>
    <Volume_ID>BLURAY_DISC</Volume_ID>
    <Volume_Set_ID>045AF019        BLURAY_DISC</Volume_Set_ID>
    <Application_ID>*N{fu}A</Application_ID>
    <Implementation_ID>*N{fu}A</Implementation_ID>
    <Implementation_Use>*N{fu}A</Implementation_Use>
    <Logical_Volume_ID>BLURAY_DISC</Logical_Volume_ID>
    <File_Set_ID>BLURAY_DISC</File_Set_ID>
  </Volume>
  <Logical_dir_struct>
    <directory File_ID="0">
      <File_entry File_ID="1">
        <Filename>BDMV</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="23">
        <Filename>CERTIFICATE</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="27">
        <Filename>AACS</Filename>
        <is_dir>true</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="1">
      <File_entry File_ID="2">
        <Filename>index.bdmv</Filename>
        <Sourcepath>{mp}{fu}{BDMV}{fu}index.bdmv</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="3">
        <Filename>MovieObject.bdmv</Filename>
        <Sourcepath>{mp}{fu}{BDMV}{fu}MovieObject.bdmv</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="5">
        <Filename>PLAYLIST</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="7">
        <Filename>CLIPINF</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="9">
        <Filename>STREAM</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="10">
        <Filename>AUXDATA</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="11">
        <Filename>META</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="12">
        <Filename>BDJO</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="13">
        <Filename>JAR</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="14">
        <Filename>BACKUP</Filename>
        <is_dir>true</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="5">
      <File_entry File_ID="4">
        <Filename>00000.mpls</Filename>
        <Sourcepath>{PLAYLIST}{fu}00000.mpls</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="7">
      <File_entry File_ID="6">
        <Filename>88888.clpi</Filename>
        <Sourcepath>{CLIPINF}{fu}88888.clpi</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="9">
      <File_entry File_ID="8">
        <Filename>88888.m2ts</Filename>
        <Sourcepath>{mp}{fu}{STREAM}{fu}88888.m2ts</Sourcepath>
        <is_dir>false</is_dir>
        <TS_Intermediatefile_dir>{mp}{fu}{TSIntermediate}</TS_Intermediatefile_dir>
      </File_entry>
    </directory>
    <directory File_ID="14">
      <File_entry File_ID="15">
        <Filename>index.bdmv</Filename>
        <Sourcepath>{mp}{fu}{BDMV}{fu}index.bdmv</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="16">
        <Filename>MovieObject.bdmv</Filename>
        <Sourcepath>{mp}{fu}{BDMV}{fu}MovieObject.bdmv</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="18">
        <Filename>PLAYLIST</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="20">
        <Filename>CLIPINF</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="21">
        <Filename>BDJO</Filename>
        <is_dir>true</is_dir>
      </File_entry>
      <File_entry File_ID="22">
        <Filename>JAR</Filename>
        <is_dir>true</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="18">
      <File_entry File_ID="17">
        <Filename>00000.mpls</Filename>
        <Sourcepath>{PLAYLIST}{fu}00000.mpls</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="20">
      <File_entry File_ID="19">
        <Filename>88888.clpi</Filename>
        <Sourcepath>{CLIPINF}{fu}88888.clpi</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="23">
      <File_entry File_ID="24">
        <Filename>id.bdmv</Filename>
        <Sourcepath>{mp}{fu}{CERTIFICATE}{fu}id.bdmv</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="26">
        <Filename>BACKUP</Filename>
        <is_dir>true</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="26">
      <File_entry File_ID="25">
        <Filename>id.bdmv</Filename>
        <Sourcepath>{mp}{fu}{BACKUP}{fu}id.bdmv</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="27">
      <File_entry File_ID="28">
        <Filename>Content002.cer</Filename>
        <Sourcepath>{mp}{fu}{AACS}{fu}Content002.cer</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="30">
        <Filename>Content001.cer</Filename>
        <Sourcepath>{mp}{fu}{AACS}{fu}Content001.cer</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="32">
        <Filename>Content000.cer</Filename>
        <Sourcepath>{mp}{fu}{AACS}{fu}Content000.cer</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="33">
        <Filename>DH_Pairing_Server.cer</Filename>
        <Sourcepath>{mp}{fu}{AACS}{fu}DH_Pairing_Server.cer</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="34">
        <Filename>MKB_RO.inf</Filename>
        <Sourcepath>{mp}{fu}{AACS}{fu}MKB_RO.inf</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="35">
        <Filename>Unit_Key_RO.inf</Filename>
        <Sourcepath>{mp}{fu}{AACS}{fu}Unit_Key_RO.inf</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="36">
        <Filename>CPSUnit00001.cci</Filename>
        <Sourcepath>{mp}{fu}{AACS}{fu}CPSUnit00001.cci</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="37">
        <Filename>ContentRevocation.lst</Filename>
        <Sourcepath>{mp}{fu}{AACS}{fu}ContentRevocation.lst</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="50">
        <Filename>DUPLICATE</Filename>
        <is_dir>true</is_dir>
      </File_entry>
    </directory>
    <directory File_ID="50">
      <File_entry File_ID="40">
        <Filename>Content001.cer</Filename>
        <Sourcepath>{mp}{fu}{DUPLICATE}{fu}Content001.cer</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="42">
        <Filename>Content000.cer</Filename>
        <Sourcepath>{mp}{fu}{DUPLICATE}{fu}Content000.cer</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="43">
        <Filename>DH_Pairing_Server.cer</Filename>
        <Sourcepath>{mp}{fu}{DUPLICATE}{fu}DH_Pairing_Server.cer</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="44">
        <Filename>MKB_RO.inf</Filename>
        <Sourcepath>{mp}{fu}{DUPLICATE}{fu}MKB_RO.inf</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="45">
        <Filename>Unit_Key_RO.inf</Filename>
        <Sourcepath>{mp}{fu}{DUPLICATE}{fu}Unit_Key_RO.inf</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="46">
        <Filename>CPSUnit00001.cci</Filename>
        <Sourcepath>{mp}{fu}{DUPLICATE}{fu}CPSUnit00001.cci</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="47">
        <Filename>ContentRevocation.lst</Filename>
        <Sourcepath>{mp}{fu}{DUPLICATE}{fu}ContentRevocation.lst</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
      <File_entry File_ID="49">
        <Filename>Content002.cer</Filename>
        <Sourcepath>{mp}{fu}{DUPLICATE}{fu}Content002.cer</Sourcepath>
        <is_dir>false</is_dir>
      </File_entry>
    </directory>
  </Logical_dir_struct>
  <Physical_dir_struct>
    <Sequence_unit RequiredLayer="0">
      <Sequence_File_ID>32</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit>
      <Sequence_File_ID>37</Sequence_File_ID>
      <Sequence_File_ID>36</Sequence_File_ID>
      <Sequence_File_ID>33</Sequence_File_ID>
      <Sequence_File_ID>34</Sequence_File_ID>
      <Sequence_File_ID>35</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit>
      <Sequence_File_ID>2</Sequence_File_ID>
      <Sequence_File_ID>3</Sequence_File_ID>
      <Sequence_File_ID>4</Sequence_File_ID>
      <Sequence_File_ID>6</Sequence_File_ID>
      <Sequence_File_ID>24</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit>
      <Sequence_File_ID>47</Sequence_File_ID>
      <Sequence_File_ID>46</Sequence_File_ID>
      <Sequence_File_ID>43</Sequence_File_ID>
      <Sequence_File_ID>44</Sequence_File_ID>
      <Sequence_File_ID>45</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit>
      <Sequence_File_ID>15</Sequence_File_ID>
      <Sequence_File_ID>16</Sequence_File_ID>
      <Sequence_File_ID>17</Sequence_File_ID>
      <Sequence_File_ID>19</Sequence_File_ID>
      <Sequence_File_ID>25</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit RequiredLayer="0">
      <Sequence_File_ID>42</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit>
      <Sequence_File_ID>8</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit RequiredLayer="1">
      <Sequence_File_ID>40</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit RequiredLayer="1">
      <Sequence_File_ID>30</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit RequiredLayer="2">
      <Sequence_File_ID>28</Sequence_File_ID>
    </Sequence_unit>
    <Sequence_unit RequiredLayer="2">
      <Sequence_File_ID>49</Sequence_File_ID>
    </Sequence_unit>
  </Physical_dir_struct>
  <FS_OutputFilename>
    <Is_Output_CMF>false</Is_Output_CMF>
    <IMAGE>{image}{fu}FSImage0.img</IMAGE>
    <MDC_IMAGE>{image}{fu}MDC_Image0.dat</MDC_IMAGE>
    <UCD>{image}{fu}ucd0.dat</UCD>
    <BDCMF_Filename>
      <BDCMF />
      <FAI>{image}{fu}FAI.DAT</FAI>
      <FMTSMap />
    </BDCMF_Filename>
    <PIC_info_mux>{image}{fu}Pic_info_mux.dat</PIC_info_mux>
    <File_addr_map>{image}{fu}file_addr.map</File_addr_map>
    <FS_Intermediatefile_dir>{FSIntermediate}{fu}</FS_Intermediatefile_dir>
  </FS_OutputFilename>
</FSDescriptor>
""".strip()

    return xml_template

def maked_indextable():
    xml_template = f"""
<?xml version="1.0" encoding="UTF-8"?>
<IndexTableFile Version="0099" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="IndexTable.xsd">
  <type_indicator>INDX</type_indicator>
  <version_number>0300</version_number>
  <AppInfoBDMV>
    <initial_output_mode_preference>0</initial_output_mode_preference>
    <SS_content_exist_flag>0</SS_content_exist_flag>
    <initial_dynamic_range_type>0</initial_dynamic_range_type>
    <video_format>0</video_format>
    <frame_rate>0</frame_rate>
    <content_provider_user_data>Not</content_provider_user_data>
  </AppInfoBDMV>
  <Loop_padding_word_1 />
  <Indexes>
    <FirstPlayback>
      <FirstPlayback_object_type>01</FirstPlayback_object_type>
      <Select_FirstPlayback_object>
        <FirstPlayback_mobj>
          <HDMV_Title_playback_type>00</HDMV_Title_playback_type>
          <FirstPlayback_mobj_id_ref>0</FirstPlayback_mobj_id_ref>
        </FirstPlayback_mobj>
      </Select_FirstPlayback_object>
    </FirstPlayback>
    <TopMenu>
      <TopMenu_object_type>01</TopMenu_object_type>
      <Select_TopMenu_object>
        <TopMenu_mobj>
          <HDMV_Title_playback_type>01</HDMV_Title_playback_type>
          <TopMenu_mobj_id_ref>1</TopMenu_mobj_id_ref>
        </TopMenu_mobj>
      </Select_TopMenu_object>
    </TopMenu>
    <number_of_Titles>1</number_of_Titles>
    <Loop_Title>
      <Title>
        <Title_object_type>01</Title_object_type>
        <Title_access_type>00</Title_access_type>
        <Select_Title_object>
          <Title_mobj>
            <HDMV_Title_playback_type>00</HDMV_Title_playback_type>
            <Title_mobj_id_ref>2</Title_mobj_id_ref>
          </Title_mobj>
        </Select_Title_object>
      </Title>
    </Loop_Title>
  </Indexes>
  <Loop_padding_word_2 />
  <ExtensionData>
    <number_of_ext_data_entries>1</number_of_ext_data_entries>
    <Loop_ext_data_entries>
      <ext_data_entry>
        <ID1>3</ID1>
        <ID2>1</ID2>
      </ext_data_entry>
    </Loop_ext_data_entries>
    <Loop_padding_word />
    <Loop_data_block>
      <data_block>
        <Disc_Info>
          <disc_type>5</disc_type>
          <is_4K_content_exist>false</is_4K_content_exist>
          <HDR_content_exist_flags>0</HDR_content_exist_flags>
        </Disc_Info>
      </data_block>
    </Loop_data_block>
  </ExtensionData>
  <Loop_padding_word_3 />
</IndexTableFile>
""".strip()

    return xml_template

def maked_movieobject(id_1, id_2):
    xml_template = f"""
<?xml version="1.0" encoding="UTF-8"?>
<MovieObjectFile Version="0099" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="MovieObject.xsd">
  <type_indicator>MOBJ</type_indicator>
  <version_number>0300</version_number>
  <MovieObjects>
    <number_of_mobjs>3</number_of_mobjs>
    <Loop_MovieObject>
      <MovieObject>
        <TerminalInfo>
          <resume_intention_flag>true</resume_intention_flag>
          <menu_call_mask>true</menu_call_mask>
          <title_search_mask>true</title_search_mask>
        </TerminalInfo>
        <number_of_navigation_commands>5</number_of_navigation_commands>
        <Loop_navigation_command>
          <navigation_command>504000010000000000000000</navigation_command>
          <navigation_command>504000010000000200000001</navigation_command>
          <navigation_command>50400001000000030000FFFF</navigation_command>
          <navigation_command>504000010000000400000000</navigation_command>
          <navigation_command>218100000000000000000000</navigation_command>
        </Loop_navigation_command>
      </MovieObject>
      <MovieObject>
        <TerminalInfo>
          <resume_intention_flag>true</resume_intention_flag>
          <menu_call_mask>true</menu_call_mask>
          <title_search_mask>true</title_search_mask>
        </TerminalInfo>
        <number_of_navigation_commands>9</number_of_navigation_commands>
        <Loop_navigation_command>
          <navigation_command>500000010000000A00000003</navigation_command>
          <navigation_command>50400001000000030000FFFF</navigation_command>
          <navigation_command>484003000000000A0000FFFF</navigation_command>
          <navigation_command>220000000000000A00000000</navigation_command>
          <navigation_command>500000010000000A00000004</navigation_command>
          <navigation_command>504000010000000400000000</navigation_command>
          <navigation_command>484003000000000A00000000</navigation_command>
          <navigation_command>210100000000000A00000000</navigation_command>
          <navigation_command>218100000000000100000000</navigation_command>
        </Loop_navigation_command>
      </MovieObject>
      <MovieObject>
        <TerminalInfo>
          <resume_intention_flag>true</resume_intention_flag>
          <menu_call_mask>true</menu_call_mask>
          <title_search_mask>true</title_search_mask>
        </TerminalInfo>
        <number_of_navigation_commands>6</number_of_navigation_commands>
        <Loop_navigation_command>
          <navigation_command>500000010000000A00000000</navigation_command>
          <navigation_command>504000010000000000000000</navigation_command>
          <navigation_command>514000010000C00100000000</navigation_command>
          <navigation_command>504000010000000000000000</navigation_command>
          <navigation_command>42820000000000000000000A</navigation_command>
          <navigation_command>000200000000000000000000</navigation_command>
        </Loop_navigation_command>
      </MovieObject>
    </Loop_MovieObject>
  </MovieObjects>
  <Loop_padding_word_1 />
  <Loop_padding_word_2 />
</MovieObjectFile>
""".strip()

    return xml_template

def maked_projectdefinition(hypermux_final, fu, mp):
    xml_dir = os.path.join(mp, "Output", "MUX", "BDROM")
    DBIntermediate = r"Output\MUX\BDROM\DBIntermediate"
    BDMV = r"Output\MUX\BDROM\DB\BDMV"

    xml_template = f"""
<?xml version="1.0" encoding="UTF-8"?>
<mstns:ProjectDefinition Version="0099" xmlns:mstns="http://tempuri.org/ProjectDefinition.xsd" xmlns:msdata="urn:schemas-microsoft-com:xml-msdata" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://tempuri.org/ProjectDefinition.xsd ProjectDefinition.xsd">
  <mstns:Information>
    <mstns:ProjectName />
    <mstns:Author>N{fu}A</mstns:Author>
    <mstns:Manufacturer>N{fu}A</mstns:Manufacturer>
    <mstns:DriveType>BD66/100_TR_122</mstns:DriveType>
  </mstns:Information>
  <mstns:XML_List>
    <mstns:IndexTableFile>{xml_dir}{fu}IndexTable.xml</mstns:IndexTableFile>
    <mstns:MovieObjectFile>{xml_dir}{fu}MovieObject.xml</mstns:MovieObjectFile>
    <mstns:MoviePlayListFile>{xml_dir}{fu}MoviePlayList.xml</mstns:MoviePlayListFile>
    <mstns:CLIPDescriptorFile>{xml_dir}{fu}CLIPDescriptor.xml</mstns:CLIPDescriptorFile>
    <mstns:FSDescriptorFile>{xml_dir}{fu}FSDescriptor.xml</mstns:FSDescriptorFile>
  </mstns:XML_List>
  <mstns:Transaction>
    <mstns:TS_process mstns:hypermux="{hypermux_final}">
      <mstns:M2TS_List mstns:All_M2TS="false">
        <mstns:CLIP_id>88888</mstns:CLIP_id>
      </mstns:M2TS_List>
      <mstns:TP_extra_header>
        <mstns:copy_permission_indicator>3</mstns:copy_permission_indicator>
      </mstns:TP_extra_header>
    </mstns:TS_process>
    <mstns:DB_Allocate_process>
      <mstns:Execute_process>true</mstns:Execute_process>
      <mstns:Execute_Allocate>true</mstns:Execute_Allocate>
      <mstns:IndexTable_process>true</mstns:IndexTable_process>
      <mstns:MovieObject_process>true</mstns:MovieObject_process>
      <mstns:MoviePlayList_List mstns:All_PlayLists="false">
        <mstns:Playlist_id>00000</mstns:Playlist_id>
      </mstns:MoviePlayList_List>
      <mstns:CLPI_List mstns:All_CLPI="false">
        <mstns:CLIP_id>88888</mstns:CLIP_id>
      </mstns:CLPI_List>
      <mstns:DB_dirs>
        <mstns:DB_Intermediatefile_dir>{mp}{fu}{DBIntermediate}{fu}</mstns:DB_Intermediatefile_dir>
        <mstns:DB_output_dir>{mp}{fu}{BDMV}{fu}</mstns:DB_output_dir>
      </mstns:DB_dirs>
    </mstns:DB_Allocate_process>
    <mstns:FS_process>true</mstns:FS_process>
  </mstns:Transaction>
</mstns:ProjectDefinition>
""".strip()

    return xml_template