# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.contrib.gis.db import models


class Adyacencia2Gto3GAdjw(models.Model):
    id = models.AutoField()
    source_name = models.TextField(blank=True, null=True)
    source_refarming = models.TextField(blank=True, null=True)
    source_bscid = models.IntegerField(blank=True, null=True)
    source_cellid = models.IntegerField(blank=True, null=True)
    target_rncid = models.IntegerField(blank=True, null=True)
    target_sac = models.IntegerField(blank=True, null=True)
    target_status = models.TextField(blank=True, null=True)
    target_wcelstate = models.IntegerField(blank=True, null=True)
    target_uarfcn = models.IntegerField(blank=True, null=True)
    linea = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adyacencia_2gto3g_adjw'


class Adyacencia3Gto2GAdjg(models.Model):
    id = models.AutoField()
    source_rncid = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    target_refarming = models.TextField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    linea = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adyacencia_3gto2g_adjg'


class Adyacencias2G(models.Model):
    id = models.AutoField()
    source_name = models.TextField(blank=True, null=True)
    source_refarming = models.IntegerField(blank=True, null=True)
    source_bscid = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    target_bscid = models.IntegerField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    target_status = models.TextField(blank=True, null=True)
    target_adminstate = models.IntegerField(blank=True, null=True)
    target_refarming = models.IntegerField(blank=True, null=True)
    target_initfreq = models.IntegerField(blank=True, null=True)
    linea = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adyacencias_2g'


class Adyacencias3G(models.Model):
    source_rncid = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    target_rncid = models.IntegerField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    linea = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adyacencias_3g'


class Adyacencias4G(models.Model):
    fecha = models.TextField(blank=True, null=True)
    source_plmn_name = models.TextField(blank=True, null=True)
    source_mrbts_sbts_name = models.TextField(blank=True, null=True)
    source_lnbts_type = models.TextField(blank=True, null=True)
    source_lnbts_name = models.TextField(blank=True, null=True)
    source_lncel_name = models.TextField(blank=True, null=True)
    target_plmn_name = models.TextField(blank=True, null=True)
    target_mrbts_sbts_name = models.TextField(blank=True, null=True)
    target_lnbts_type = models.TextField(blank=True, null=True)
    target_lnbts_name = models.TextField(blank=True, null=True)
    target_lnbts_id = models.TextField(blank=True, null=True)
    target_lncel_name = models.TextField(blank=True, null=True)
    target_lncel_tac = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    target_lcr_id = models.DecimalField(max_digits=8, decimal_places=4, blank=True, null=True)
    mcc_id = models.IntegerField(blank=True, null=True)
    mnc_id = models.IntegerField(blank=True, null=True)
    eci_id = models.IntegerField(blank=True, null=True)
    intra_enb_neighbor_ho_prep_sr = models.DecimalField(db_column='intra_enb_neighbor_ho__prep_sr', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    intra_enb_neighbor_ho_sr = models.DecimalField(db_column='intra_enb_neighbor_ho__sr', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    intra_enb_neighbor_ho_att = models.IntegerField(db_column='intra_enb_neighbor_ho__att', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    intra_enb_neighbor_ho_cancel_r = models.DecimalField(db_column='intra_enb_neighbor_ho__cancel_r', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    inter_enb_neighbor_ho_prep_sr = models.DecimalField(db_column='inter_enb_neighbor_ho__prep_sr', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    inter_enb_neighbor_ho_sr = models.DecimalField(db_column='inter_enb_neighbor_ho__sr', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    inter_enb_neighbor_ho_att = models.IntegerField(db_column='inter_enb_neighbor_ho__att', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    inter_enb_neighbor_ho_fr = models.DecimalField(db_column='inter_enb_neighbor_ho__fr', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    load_balancing_ho_per_neighbor_sr = models.DecimalField(db_column='load_balancing_ho_per_neighbor__sr', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    load_balancing_ho_per_neighbor_att = models.IntegerField(db_column='load_balancing_ho_per_neighbor__att', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    late_early_ho_ratio_per_neighbor_late_ho = models.DecimalField(db_column='late_early_ho_ratio_per_neighbor__late_ho', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    late_early_ho_ratio_per_neighbor_early_ho_type_1 = models.DecimalField(db_column='late_early_ho_ratio_per_neighbor__early_ho_type_1', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    late_early_ho_ratio_per_neighbor_early_ho_type_2 = models.DecimalField(db_column='late_early_ho_ratio_per_neighbor__early_ho_type_2', max_digits=8, decimal_places=4, blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    linea = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adyacencias_4g'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GrafanaSystemprogram3G(models.Model):
    period_start_time = models.DateTimeField(blank=True, null=True)
    plmn_name = models.TextField(blank=True, null=True)
    rnc_name = models.TextField(blank=True, null=True)
    wbts_name = models.TextField(blank=True, null=True)
    wbts_id = models.IntegerField(blank=True, null=True)
    wcel_name = models.TextField(blank=True, null=True)
    wcel_id = models.IntegerField(blank=True, null=True)
    cell_availability_cell_avail = models.FloatField(blank=True, null=True)
    cell_availability_cell_avail_excl_blu = models.FloatField(blank=True, null=True)
    rrc_connections_rrc_stp_att = models.FloatField(blank=True, null=True)
    rrc_connections_rrc_stp_and_acc_cr_nw = models.FloatField(blank=True, null=True)
    rrc_connections_rrc_stp_and_acc_cr_ue = models.FloatField(blank=True, null=True)
    rrc_connections_rrc_conn_setup_sr = models.FloatField(blank=True, null=True)
    rrc_connections_rrc_conn_sr = models.FloatField(blank=True, null=True)
    rrc_connections_rrc_reg_att = models.FloatField(blank=True, null=True)
    rrc_connections_regist_sr = models.FloatField(blank=True, null=True)
    rrc_connections_cch_att = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_cssr_cs_voice = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_cssr_voice_rrcpluscu = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_rab_att_voice = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_rab_sr_voice = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_rab_stp_and_acc_cr_voice = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_peak_amr_calls = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_rab_sr_amr_voice = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_duration_min_per_drop_voice = models.FloatField(blank=True, null=True)
    amr_rab_cs_voice_duration_cs_serv_dur_voice = models.FloatField(blank=True, null=True)
    udi_rab_udi_cssr = models.FloatField(blank=True, null=True)
    udi_rab_rab_att_udi = models.FloatField(blank=True, null=True)
    udi_rab_rab_stp_acc_sr_udi = models.FloatField(blank=True, null=True)
    udi_rab_rab_sr_udi = models.FloatField(blank=True, null=True)
    udi_rab_duration_min_per_drop_udi = models.FloatField(blank=True, null=True)
    udi_rab_duration_cs_serv_dur_conv = models.FloatField(blank=True, null=True)
    ps_rab_nrt_cssr_ps_nrt = models.FloatField(blank=True, null=True)
    ps_rab_nrt_ps_nrt_rab_att = models.FloatField(blank=True, null=True)
    ps_rab_nrt_ps_nrt_rab_cr = models.FloatField(blank=True, null=True)
    ps_rab_nrt_ps_nrt_rab_sr_nw = models.FloatField(blank=True, null=True)
    ps_rab_nrt_ps_nrt_rab_sr_user = models.FloatField(blank=True, null=True)
    ps_rab_nrt_ps_rab_drops_data_vol_user = models.FloatField(blank=True, null=True)
    ps_rab_nrt_duration_ps_nrt_serv_dur = models.FloatField(blank=True, null=True)
    packet_session_max_nbr_ps_act = models.FloatField(blank=True, null=True)
    packet_session_ps_att = models.FloatField(blank=True, null=True)
    packet_session_r99_ps_att = models.FloatField(blank=True, null=True)
    packet_session_ps_stp_sr = models.FloatField(blank=True, null=True)
    packet_session_r99_setup_sr = models.FloatField(blank=True, null=True)
    packet_session_ps_sr = models.FloatField(blank=True, null=True)
    packet_session_r99_sr = models.FloatField(blank=True, null=True)
    packet_session_duration_nrt_dur = models.FloatField(blank=True, null=True)
    packet_session_duration_ps_rab_min_per_drop = models.FloatField(blank=True, null=True)
    packet_session_duration_ps_dch_min_per_drop = models.FloatField(blank=True, null=True)
    multi_rab_m_rab_att = models.FloatField(blank=True, null=True)
    multi_rab_m_rab_stp_and_acc_sr = models.FloatField(blank=True, null=True)
    multi_rab_m_rab_sr = models.FloatField(blank=True, null=True)
    sho_soft_ho_update_att_rt = models.FloatField(blank=True, null=True)
    sho_soft_ho_update_att_nrt = models.FloatField(blank=True, null=True)
    sho_sr_rt = models.FloatField(blank=True, null=True)
    sho_sr_nrt = models.FloatField(blank=True, null=True)
    sho_sho_overhead = models.FloatField(blank=True, null=True)
    inter_sys_hho_isho_att_rt = models.FloatField(blank=True, null=True)
    inter_sys_hho_isho_att_nrt = models.FloatField(blank=True, null=True)
    inter_sys_hho_rt_sr = models.FloatField(blank=True, null=True)
    inter_sys_hho_nrt_sr = models.FloatField(blank=True, null=True)
    inter_sys_hho_rt_dr = models.FloatField(blank=True, null=True)
    inter_sys_hho_nrt_dr = models.FloatField(blank=True, null=True)
    intra_rnc_ifho_rt_att = models.FloatField(blank=True, null=True)
    intra_rnc_ifho_rt_sr = models.FloatField(blank=True, null=True)
    intra_rnc_ifho_nrt_att = models.FloatField(blank=True, null=True)
    intra_rnc_ifho_nrt_sr = models.FloatField(blank=True, null=True)
    inc_inter_sys_change_cs_att = models.FloatField(blank=True, null=True)
    inc_inter_sys_change_ps_att = models.FloatField(blank=True, null=True)
    csfb_rrc_setup_att = models.FloatField(blank=True, null=True)
    csfb_rrc_stp_acc_cr = models.FloatField(blank=True, null=True)
    csfb_inc_lte_csfb_ps_ho_sr = models.FloatField(blank=True, null=True)
    lte_isho_att = models.FloatField(blank=True, null=True)
    lte_isho_sr = models.FloatField(blank=True, null=True)
    lte_inter_rrc_rel_redir = models.FloatField(blank=True, null=True)
    lte_inter_inc_cs_srvcc_isho_prep_req = models.FloatField(blank=True, null=True)
    lte_inter_inc_cs_hho_prep_sr = models.FloatField(blank=True, null=True)
    lte_inter_inc_cs_hho_sr = models.FloatField(blank=True, null=True)
    lte_inter_inc_csfb_ho_prep_req = models.FloatField(blank=True, null=True)
    lte_inter_inc_csfb_ho_prep_sr = models.FloatField(blank=True, null=True)
    lte_inter_inc_ps_isho_prep_req = models.FloatField(blank=True, null=True)
    lte_inter_inc_ps_isho_prep_sr = models.FloatField(blank=True, null=True)
    lte_inter_inc_ps_isho_rel_comp_sr = models.FloatField(blank=True, null=True)
    hsdpa_hs_dsch_selections = models.FloatField(blank=True, null=True)
    hsdpa_hsdpa_res_acc_nrt = models.FloatField(blank=True, null=True)
    hsdpa_hsdpa_att = models.FloatField(blank=True, null=True)
    hsdpa_hsdpa_stp_sr = models.FloatField(blank=True, null=True)
    hsdpa_hsdpa_sr = models.FloatField(blank=True, null=True)
    hsdpa_data_act_hs_dsch_mac_d_thp_nw = models.FloatField(blank=True, null=True)
    hsdpa_data_avg_hsdpa_end_usr_thp = models.FloatField(blank=True, null=True)
    hsdpa_data_hsdpa_dl_data_rcvd_in_nodeb = models.FloatField(blank=True, null=True)
    hsdpa_data_hsdpa_mac_hs_data_vol_at_rnc = models.FloatField(blank=True, null=True)
    mass_event_handler_duration = models.FloatField(blank=True, null=True)
    cqi_avg_cqi = models.FloatField(blank=True, null=True)
    power_avg_rtwp = models.FloatField(blank=True, null=True)
    hsdpa_data_per_drop_hsdpa_data_per_drop = models.FloatField(blank=True, null=True)
    hsdpa_data_per_drop_hsdpa_data_per_drop_pch_excl = models.FloatField(blank=True, null=True)
    hsdpa_data_integrity_hsdpa_mac_hs_efficiency = models.FloatField(blank=True, null=True)
    hsdpa_scc_hsdpa_scc_att = models.FloatField(blank=True, null=True)
    hsdpa_scc_hsdpa_scc_sr = models.FloatField(blank=True, null=True)
    hsupa_e_dch_selections = models.FloatField(blank=True, null=True)
    hsupa_hsupa_res_acc_nrt = models.FloatField(blank=True, null=True)
    hsupa_hsupa_att = models.FloatField(blank=True, null=True)
    hsupa_hsupa_stp_sr = models.FloatField(blank=True, null=True)
    hsupa_hsupa_sr = models.FloatField(blank=True, null=True)
    hsupa_data_hsupa_act_cell_thp = models.FloatField(blank=True, null=True)
    hsupa_data_avg_hsupa_user_thp = models.FloatField(blank=True, null=True)
    hsupa_data_hsupa_mac_es_data_vol_at_rnc = models.FloatField(blank=True, null=True)
    hsupa_data_integrity_hsupa_mac_es_bler = models.FloatField(blank=True, null=True)
    fach_dl_usr_data_thr_enh_fach = models.FloatField(blank=True, null=True)
    fach_ul_ctrl_dat_thr_enh_fach = models.FloatField(blank=True, null=True)
    fach_ul_usr_data_thr_enh_fach = models.FloatField(blank=True, null=True)
    fach_enh_fach_data_vol_dl = models.FloatField(blank=True, null=True)
    fach_enh_fach_data_vol_ul = models.FloatField(blank=True, null=True)
    cs_traffic_total_cs_traffic = models.FloatField(blank=True, null=True)
    sms_service_inc_sms_att = models.FloatField(blank=True, null=True)
    sms_service_mtc_share = models.FloatField(blank=True, null=True)
    rel99_data_call_allo_dl_dch_cap_data_call = models.FloatField(blank=True, null=True)
    rel99_data_call_allo_ul_dch_cap_data_call = models.FloatField(blank=True, null=True)
    iu_ps_data_iu_ps_peak_throughput = models.FloatField(blank=True, null=True)
    srns_relocations_cs_att_ue_not_inv = models.FloatField(blank=True, null=True)
    srns_relocations_cs_sr_ue_not_inv = models.FloatField(blank=True, null=True)
    srns_relocations_ps_att_ue_not_inv = models.FloatField(blank=True, null=True)
    srns_relocations_ps_sr_ue_not_inv = models.FloatField(blank=True, null=True)
    srns_relocations_cs_att_ue_inv = models.FloatField(blank=True, null=True)
    srns_relocations_cs_sr_ue_inv = models.FloatField(blank=True, null=True)
    srns_relocations_ps_att_ue_inv = models.FloatField(blank=True, null=True)
    srns_relocations_ps_sr_ue_inv = models.FloatField(blank=True, null=True)
    number_of_active_elements_rncs = models.FloatField(blank=True, null=True)
    number_of_active_elements_wbtss = models.FloatField(blank=True, null=True)
    number_of_active_elements_wcels = models.FloatField(blank=True, null=True)
    number_of_active_elements_rrc_users = models.FloatField(blank=True, null=True)
    number_of_hsxpa_users_avg_hsdpa_cell = models.FloatField(blank=True, null=True)
    number_of_hsxpa_users_avg_hsupa_srv_cell = models.FloatField(blank=True, null=True)
    ue_supported_capabilities_3gpp_rel_8_rat = models.FloatField(blank=True, null=True)
    ue_supported_capabilities_3gpp_rel_9_rat = models.FloatField(blank=True, null=True)
    ue_supported_capabilities_3gpp_rel_10_rat = models.FloatField(blank=True, null=True)
    ue_supported_capabilities_3gpp_rel_11_rat = models.FloatField(blank=True, null=True)
    ue_supported_capabilities_dpcch_dtx_rat = models.FloatField(blank=True, null=True)
    ue_supported_capabilities_hs_fach_rat = models.FloatField(blank=True, null=True)
    ue_supported_capabilities_hs_rach_rat = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grafana_systemprogram_3g'


class PoligonosVoronoi(models.Model):
    intersecta = models.BooleanField(blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    poligonos = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'poligonos_voronoi'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class Prach3G(models.Model):
    id = models.AutoField()
    period_start_time = models.TextField(blank=True, null=True)
    plmn_name = models.TextField(blank=True, null=True)
    rnc_name = models.TextField(blank=True, null=True)
    wname = models.TextField(blank=True, null=True)
    wbts_id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    wcel_id = models.IntegerField(blank=True, null=True)
    prachconf = models.SmallIntegerField(blank=True, null=True)
    prach0 = models.IntegerField(blank=True, null=True)
    prach1 = models.IntegerField(blank=True, null=True)
    prach2 = models.IntegerField(blank=True, null=True)
    prach3 = models.IntegerField(blank=True, null=True)
    prach4 = models.IntegerField(blank=True, null=True)
    prach5 = models.IntegerField(blank=True, null=True)
    prach6 = models.IntegerField(blank=True, null=True)
    prach7 = models.IntegerField(blank=True, null=True)
    prach8 = models.IntegerField(blank=True, null=True)
    prach9 = models.IntegerField(blank=True, null=True)
    prach10 = models.IntegerField(blank=True, null=True)
    prach11 = models.IntegerField(blank=True, null=True)
    prach12 = models.IntegerField(blank=True, null=True)
    prach13 = models.IntegerField(blank=True, null=True)
    prach14 = models.IntegerField(blank=True, null=True)
    prach15 = models.IntegerField(blank=True, null=True)
    prach16 = models.IntegerField(blank=True, null=True)
    prach17 = models.IntegerField(blank=True, null=True)
    prach18 = models.IntegerField(blank=True, null=True)
    prach19 = models.IntegerField(blank=True, null=True)
    prach20 = models.IntegerField(blank=True, null=True)
    prach21 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prach_3g'


class Propagacion(models.Model):
    id = models.AutoField()
    dia = models.TextField(blank=True, null=True)
    bts_name = models.TextField(blank=True, null=True)
    bin_ta = models.SmallIntegerField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    cant = models.IntegerField(blank=True, null=True)
    refarming = models.TextField(blank=True, null=True)
    band = models.SmallIntegerField(blank=True, null=True)
    initialfreq = models.IntegerField(blank=True, null=True)
    bin_geografico = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propagacion'


class Propagacion3G(models.Model):
    id = models.AutoField()
    dia = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    bin_prach = models.SmallIntegerField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    cant = models.IntegerField(blank=True, null=True)
    uarfcn = models.SmallIntegerField(blank=True, null=True)
    priscrcode = models.IntegerField(blank=True, null=True)
    bin_geografico = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propagacion_3g'


class PropagacionParaFotos(models.Model):
    id = models.AutoField()
    dia = models.TextField(blank=True, null=True)
    bts_name = models.TextField(blank=True, null=True)
    bin_ta = models.SmallIntegerField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    cant = models.IntegerField(blank=True, null=True)
    bin_geografico = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'propagacion_para_fotos'


class Sage2Gta(models.Model):
    id = models.AutoField()
    period_start_time = models.TextField(blank=True, null=True)
    bsc_name = models.TextField(blank=True, null=True)
    bcf_name = models.TextField(blank=True, null=True)
    bts_name = models.TextField(blank=True, null=True)
    ta0 = models.IntegerField(blank=True, null=True)
    ta1 = models.IntegerField(blank=True, null=True)
    ta2 = models.IntegerField(blank=True, null=True)
    ta3 = models.IntegerField(blank=True, null=True)
    ta4 = models.IntegerField(blank=True, null=True)
    ta5 = models.IntegerField(blank=True, null=True)
    ta6 = models.IntegerField(blank=True, null=True)
    ta7 = models.IntegerField(blank=True, null=True)
    ta8 = models.IntegerField(blank=True, null=True)
    ta9 = models.IntegerField(blank=True, null=True)
    ta10 = models.IntegerField(blank=True, null=True)
    ta11 = models.IntegerField(blank=True, null=True)
    ta12 = models.IntegerField(blank=True, null=True)
    ta13 = models.IntegerField(blank=True, null=True)
    ta14 = models.IntegerField(blank=True, null=True)
    ta15 = models.IntegerField(blank=True, null=True)
    ta16 = models.IntegerField(blank=True, null=True)
    ta17 = models.IntegerField(blank=True, null=True)
    ta18 = models.IntegerField(blank=True, null=True)
    ta19 = models.IntegerField(blank=True, null=True)
    ta20 = models.IntegerField(blank=True, null=True)
    ta21 = models.IntegerField(blank=True, null=True)
    ta22 = models.IntegerField(blank=True, null=True)
    ta23 = models.IntegerField(blank=True, null=True)
    ta24 = models.IntegerField(blank=True, null=True)
    ta25 = models.IntegerField(blank=True, null=True)
    ta26 = models.IntegerField(blank=True, null=True)
    ta27 = models.IntegerField(blank=True, null=True)
    ta28 = models.IntegerField(blank=True, null=True)
    ta29 = models.IntegerField(blank=True, null=True)
    ta30 = models.IntegerField(blank=True, null=True)
    ta31 = models.IntegerField(blank=True, null=True)
    ta32 = models.IntegerField(blank=True, null=True)
    ta33 = models.IntegerField(blank=True, null=True)
    ta34 = models.IntegerField(blank=True, null=True)
    ta35 = models.IntegerField(blank=True, null=True)
    ta36 = models.IntegerField(blank=True, null=True)
    ta37 = models.IntegerField(blank=True, null=True)
    ta38 = models.IntegerField(blank=True, null=True)
    ta39 = models.IntegerField(blank=True, null=True)
    ta40 = models.IntegerField(blank=True, null=True)
    ta41 = models.IntegerField(blank=True, null=True)
    ta42 = models.IntegerField(blank=True, null=True)
    ta43 = models.IntegerField(blank=True, null=True)
    ta44 = models.IntegerField(blank=True, null=True)
    ta45 = models.IntegerField(blank=True, null=True)
    ta46 = models.IntegerField(blank=True, null=True)
    ta47 = models.IntegerField(blank=True, null=True)
    ta48 = models.IntegerField(blank=True, null=True)
    ta49 = models.IntegerField(blank=True, null=True)
    ta50 = models.IntegerField(blank=True, null=True)
    ta51 = models.IntegerField(blank=True, null=True)
    ta52 = models.IntegerField(blank=True, null=True)
    ta53 = models.IntegerField(blank=True, null=True)
    ta54 = models.IntegerField(blank=True, null=True)
    ta55 = models.IntegerField(blank=True, null=True)
    ta56 = models.IntegerField(blank=True, null=True)
    ta57 = models.IntegerField(blank=True, null=True)
    ta58 = models.IntegerField(blank=True, null=True)
    ta59 = models.IntegerField(blank=True, null=True)
    ta60 = models.IntegerField(blank=True, null=True)
    ta61 = models.IntegerField(blank=True, null=True)
    ta62 = models.IntegerField(blank=True, null=True)
    ta63 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_2gta'


class Sage2GtaPrach(models.Model):
    id = models.AutoField()
    dia = models.TextField(blank=True, null=True)
    bts_name = models.TextField(blank=True, null=True)
    bin_ta = models.SmallIntegerField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    cant = models.IntegerField(blank=True, null=True)
    refarming = models.TextField(blank=True, null=True)
    band = models.SmallIntegerField(blank=True, null=True)
    initialfreq = models.IntegerField(blank=True, null=True)
    bin_geografico = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_2gta_prach'


class Sage3Gta(models.Model):
    id = models.AutoField()
    period_start_time = models.TextField(blank=True, null=True)
    plmn_name = models.TextField(blank=True, null=True)
    rnc_name = models.TextField(blank=True, null=True)
    wname = models.TextField(blank=True, null=True)
    wbts_id = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    wcel_id = models.IntegerField(blank=True, null=True)
    prachconf = models.SmallIntegerField(blank=True, null=True)
    prach0 = models.IntegerField(blank=True, null=True)
    prach1 = models.IntegerField(blank=True, null=True)
    prach2 = models.IntegerField(blank=True, null=True)
    prach3 = models.IntegerField(blank=True, null=True)
    prach4 = models.IntegerField(blank=True, null=True)
    prach5 = models.IntegerField(blank=True, null=True)
    prach6 = models.IntegerField(blank=True, null=True)
    prach7 = models.IntegerField(blank=True, null=True)
    prach8 = models.IntegerField(blank=True, null=True)
    prach9 = models.IntegerField(blank=True, null=True)
    prach10 = models.IntegerField(blank=True, null=True)
    prach11 = models.IntegerField(blank=True, null=True)
    prach12 = models.IntegerField(blank=True, null=True)
    prach13 = models.IntegerField(blank=True, null=True)
    prach14 = models.IntegerField(blank=True, null=True)
    prach15 = models.IntegerField(blank=True, null=True)
    prach16 = models.IntegerField(blank=True, null=True)
    prach17 = models.IntegerField(blank=True, null=True)
    prach18 = models.IntegerField(blank=True, null=True)
    prach19 = models.IntegerField(blank=True, null=True)
    prach20 = models.IntegerField(blank=True, null=True)
    prach21 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_3gta'


class Sage3GtaPrach(models.Model):
    id = models.AutoField()
    dia = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    bin_prach = models.SmallIntegerField(blank=True, null=True)
    porcentaje = models.FloatField(blank=True, null=True)
    cant = models.IntegerField(blank=True, null=True)
    uarfcn = models.SmallIntegerField(blank=True, null=True)
    priscrcode = models.IntegerField(blank=True, null=True)
    bin_geografico = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_3gta_prach'


class SageAdj(models.Model):
    source_rncid = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    target_rncid = models.IntegerField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    linea = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_adj'


class SageBts(models.Model):
    id = models.AutoField()
    band = models.IntegerField(blank=True, null=True)
    cellname = models.TextField(blank=True, null=True)
    lat_site = models.FloatField(blank=True, null=True)
    lon_site = models.FloatField(blank=True, null=True)
    az = models.SmallIntegerField(blank=True, null=True)
    bw = models.SmallIntegerField(blank=True, null=True)
    rd = models.FloatField(blank=True, null=True)
    cell_id = models.IntegerField(blank=True, null=True)
    bscid = models.IntegerField(blank=True, null=True)
    bsc_name = models.TextField(blank=True, null=True)
    bcfid = models.IntegerField(blank=True, null=True)
    btsid = models.IntegerField(blank=True, null=True)
    trxid = models.SmallIntegerField(blank=True, null=True)
    initialfreq = models.IntegerField(blank=True, null=True)
    preferredbcch = models.SmallIntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    hoppingsequencenumber1 = models.SmallIntegerField(blank=True, null=True)
    bsidentitycodebcc = models.SmallIntegerField(blank=True, null=True)
    bsidentitycodencc = models.SmallIntegerField(blank=True, null=True)
    bts_state = models.SmallIntegerField(blank=True, null=True)
    trx_state = models.SmallIntegerField(blank=True, null=True)
    lac = models.IntegerField(blank=True, null=True)
    rac = models.IntegerField(blank=True, null=True)
    refarming = models.TextField(blank=True, null=True)
    sector = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_bts'


class SageLncel(models.Model):
    dl_ch = models.SmallIntegerField(blank=True, null=True)
    sitename = models.TextField(blank=True, null=True)
    cellname = models.TextField(blank=True, null=True)
    lat_site = models.FloatField(blank=True, null=True)
    lon_site = models.FloatField(blank=True, null=True)
    az = models.SmallIntegerField(blank=True, null=True)
    bw = models.SmallIntegerField(blank=True, null=True)
    rd = models.FloatField(blank=True, null=True)
    rd_normal = models.FloatField(blank=True, null=True)
    separar = models.TextField(blank=True, null=True)
    mme = models.TextField(blank=True, null=True)
    mme_id = models.TextField(blank=True, null=True)
    lnbtsid = models.IntegerField(blank=True, null=True)
    cell_id = models.IntegerField(blank=True, null=True)
    te = models.SmallIntegerField(blank=True, null=True)
    tm = models.SmallIntegerField(blank=True, null=True)
    alt = models.SmallIntegerField(blank=True, null=True)
    pci = models.IntegerField(blank=True, null=True)
    tac = models.IntegerField(blank=True, null=True)
    rac = models.IntegerField(blank=True, null=True)
    rootseqindex = models.TextField(blank=True, null=True)
    admincellstate = models.TextField(blank=True, null=True)
    e_utran_avg_prb_usage_per_tti_dl = models.FloatField(blank=True, null=True)
    e_utran_avg_ip_sched_thp_dl_qci9 = models.FloatField(blank=True, null=True)
    average_cqi = models.FloatField(blank=True, null=True)
    avg_ue_distance = models.FloatField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    refarming = models.TextField(blank=True, null=True)
    cambiopcidinamico = models.IntegerField(blank=True, null=True)
    sector = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_lncel'


class SageSites(models.Model):
    id = models.AutoField()
    site_name = models.TextField(blank=True, null=True)
    mrbts_id = models.IntegerField(blank=True, null=True)
    lat_site = models.FloatField(blank=True, null=True)
    lon_site = models.FloatField(blank=True, null=True)
    codigounico = models.TextField(blank=True, null=True)
    cluster = models.IntegerField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    ubicacion = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_sites'


class SageVoronoiPolygons(models.Model):
    intersecta = models.BooleanField(blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    poligonos = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_voronoi_polygons'


class SageWcel(models.Model):
    id = models.AutoField()
    uarfcn = models.SmallIntegerField(blank=True, null=True)
    sitename = models.TextField(blank=True, null=True)
    sitecode = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    lat_site = models.FloatField(blank=True, null=True)
    lon_site = models.FloatField(blank=True, null=True)
    az = models.SmallIntegerField(blank=True, null=True)
    bw = models.SmallIntegerField(blank=True, null=True)
    rd = models.FloatField(blank=True, null=True)
    expr1 = models.TextField(blank=True, null=True)
    bsc_rnc_mme_name = models.TextField(blank=True, null=True)
    rncid = models.IntegerField(blank=True, null=True)
    wbtsid = models.IntegerField(blank=True, null=True)
    lcrid = models.IntegerField(blank=True, null=True)
    te = models.FloatField(blank=True, null=True)
    tm = models.FloatField(blank=True, null=True)
    alt = models.FloatField(blank=True, null=True)
    priscrcode = models.IntegerField(blank=True, null=True)
    lac = models.IntegerField(blank=True, null=True)
    rac = models.IntegerField(blank=True, null=True)
    rootseqindex = models.IntegerField(blank=True, null=True)
    admincellstate = models.TextField(blank=True, null=True)
    wcelstate = models.IntegerField(blank=True, null=True)
    sector = models.GeometryField(srid=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sage_wcel'


class Temporal(models.Model):
    lat_site = models.FloatField(blank=True, null=True)
    lon_site = models.FloatField(blank=True, null=True)
    az = models.SmallIntegerField(blank=True, null=True)
    bw = models.SmallIntegerField(blank=True, null=True)
    rd = models.FloatField(blank=True, null=True)
    sector = models.GeometryField(srid=0, blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    eutracelid = models.TextField(blank=True, null=True)
    lnbtsid = models.TextField(blank=True, null=True)
    vendor = models.TextField(blank=True, null=True)
    id_unico = models.SmallIntegerField(blank=True, null=True)
    lncelid = models.IntegerField(blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    site_type = models.TextField(blank=True, null=True)
    carrier = models.IntegerField(blank=True, null=True)
    administrativestate = models.TextField(blank=True, null=True)
    swversion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'temporal'


class TimingAdvance2G(models.Model):
    id = models.AutoField()
    period_start_time = models.TextField(blank=True, null=True)
    bsc_name = models.TextField(blank=True, null=True)
    bcf_name = models.TextField(blank=True, null=True)
    bts_name = models.TextField(blank=True, null=True)
    ta0 = models.IntegerField(blank=True, null=True)
    ta1 = models.IntegerField(blank=True, null=True)
    ta2 = models.IntegerField(blank=True, null=True)
    ta3 = models.IntegerField(blank=True, null=True)
    ta4 = models.IntegerField(blank=True, null=True)
    ta5 = models.IntegerField(blank=True, null=True)
    ta6 = models.IntegerField(blank=True, null=True)
    ta7 = models.IntegerField(blank=True, null=True)
    ta8 = models.IntegerField(blank=True, null=True)
    ta9 = models.IntegerField(blank=True, null=True)
    ta10 = models.IntegerField(blank=True, null=True)
    ta11 = models.IntegerField(blank=True, null=True)
    ta12 = models.IntegerField(blank=True, null=True)
    ta13 = models.IntegerField(blank=True, null=True)
    ta14 = models.IntegerField(blank=True, null=True)
    ta15 = models.IntegerField(blank=True, null=True)
    ta16 = models.IntegerField(blank=True, null=True)
    ta17 = models.IntegerField(blank=True, null=True)
    ta18 = models.IntegerField(blank=True, null=True)
    ta19 = models.IntegerField(blank=True, null=True)
    ta20 = models.IntegerField(blank=True, null=True)
    ta21 = models.IntegerField(blank=True, null=True)
    ta22 = models.IntegerField(blank=True, null=True)
    ta23 = models.IntegerField(blank=True, null=True)
    ta24 = models.IntegerField(blank=True, null=True)
    ta25 = models.IntegerField(blank=True, null=True)
    ta26 = models.IntegerField(blank=True, null=True)
    ta27 = models.IntegerField(blank=True, null=True)
    ta28 = models.IntegerField(blank=True, null=True)
    ta29 = models.IntegerField(blank=True, null=True)
    ta30 = models.IntegerField(blank=True, null=True)
    ta31 = models.IntegerField(blank=True, null=True)
    ta32 = models.IntegerField(blank=True, null=True)
    ta33 = models.IntegerField(blank=True, null=True)
    ta34 = models.IntegerField(blank=True, null=True)
    ta35 = models.IntegerField(blank=True, null=True)
    ta36 = models.IntegerField(blank=True, null=True)
    ta37 = models.IntegerField(blank=True, null=True)
    ta38 = models.IntegerField(blank=True, null=True)
    ta39 = models.IntegerField(blank=True, null=True)
    ta40 = models.IntegerField(blank=True, null=True)
    ta41 = models.IntegerField(blank=True, null=True)
    ta42 = models.IntegerField(blank=True, null=True)
    ta43 = models.IntegerField(blank=True, null=True)
    ta44 = models.IntegerField(blank=True, null=True)
    ta45 = models.IntegerField(blank=True, null=True)
    ta46 = models.IntegerField(blank=True, null=True)
    ta47 = models.IntegerField(blank=True, null=True)
    ta48 = models.IntegerField(blank=True, null=True)
    ta49 = models.IntegerField(blank=True, null=True)
    ta50 = models.IntegerField(blank=True, null=True)
    ta51 = models.IntegerField(blank=True, null=True)
    ta52 = models.IntegerField(blank=True, null=True)
    ta53 = models.IntegerField(blank=True, null=True)
    ta54 = models.IntegerField(blank=True, null=True)
    ta55 = models.IntegerField(blank=True, null=True)
    ta56 = models.IntegerField(blank=True, null=True)
    ta57 = models.IntegerField(blank=True, null=True)
    ta58 = models.IntegerField(blank=True, null=True)
    ta59 = models.IntegerField(blank=True, null=True)
    ta60 = models.IntegerField(blank=True, null=True)
    ta61 = models.IntegerField(blank=True, null=True)
    ta62 = models.IntegerField(blank=True, null=True)
    ta63 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timing_advance_2g'
