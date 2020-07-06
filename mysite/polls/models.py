from django.db import models
from django.utils import timezone
import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text



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
    linea = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'adyacencia_2gto3g_adjw'


class Adyacencia3Gto2GAdjg(models.Model):
    id = models.AutoField()
    source_rncid = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    target_refarming = models.TextField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    linea = models.TextField(blank=True, null=True)  # This field type is a guess.

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
    linea = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'adyacencias_2g'


class Adyacencias3G(models.Model):
    id = models.AutoField()
    source_rncid = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    target_rncid = models.IntegerField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    linea = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'adyacencias_3g'


class Adyacencias4G(models.Model):
    id = models.AutoField()
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
    linea = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'adyacencias_4g'


class PoligonosVoronoi(models.Model):
    intersecta = models.BooleanField(blank=True, null=True)
    site_name = models.TextField(blank=True, null=True)
    poligonos = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'poligonos_voronoi'


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
    bin_geografico = models.TextField(blank=True, null=True)  # This field type is a guess.

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
    bin_geografico = models.TextField(blank=True, null=True)  # This field type is a guess.
    rncid = models.IntegerField(blank=True, null=True)

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
    bin_geografico = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'propagacion_para_fotos'


class Sitios(models.Model):
    id = models.AutoField()
    site_name = models.TextField(blank=True, null=True)
    lat_site = models.FloatField(blank=True, null=True)
    lon_site = models.FloatField(blank=True, null=True)
    codigounico = models.TextField(blank=True, null=True)
    cluster = models.IntegerField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    ubicacion = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sitios'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True, null=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True, null=True)
    proj4text = models.CharField(max_length=2048, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'


class Temporal(models.Model):
    lat_site = models.FloatField(blank=True, null=True)
    lon_site = models.FloatField(blank=True, null=True)
    az = models.SmallIntegerField(blank=True, null=True)
    bw = models.SmallIntegerField(blank=True, null=True)
    rd = models.FloatField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)  # This field type is a guess.
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


class Webcell2G(models.Model):
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
    sector = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'webcell_2g'


class Webcell3G(models.Model):
    id = models.AutoField()
    uarfcn = models.SmallIntegerField(blank=True, null=True)
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
    mpd_voice = models.TextField(blank=True, null=True)
    rab_dr_amr_voice_usr = models.FloatField(blank=True, null=True)
    amr_ccssr = models.FloatField(blank=True, null=True)
    prach_km = models.FloatField(blank=True, null=True)
    wcelstate = models.IntegerField(blank=True, null=True)
    sector = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'webcell_3g'


class Webcell4G(models.Model):
    id = models.AutoField()
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
    sector = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'webcell_4g'
