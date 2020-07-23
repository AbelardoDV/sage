from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
from leaflet.admin import LeafletGeoAdmin
import django_filters


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

class Adyacencias3G(models.Model):
    id = models.AutoField(primary_key=True)
    source_rncid = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    target_rncid = models.IntegerField(blank=True, null=True)
    target_id = models.IntegerField(blank=True, null=True)
    linea = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'adyacencias_3g'
    def __str__(self):
        return str(self.source_id) + "|"+ str(self.target_id)
    



class Sage_lncel(models.Model):

    id = models.AutoField(primary_key=True)
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
    cambiopcidinamico =models.IntegerField(blank=True, null=True)
    sector = models.PolygonField(srid=4326,blank=True, null=True)  # This field type is a guess.
    objects = GeoManager()
    class Meta:
        managed = True
        db_table = 'sage_lncel'



    def __str__(self):
        return self.cellname



class SageSites(models.Model):
    id = models.AutoField(primary_key=True)
    site_name = models.TextField(blank=True, null=True)
    mrbts_id = models.IntegerField(blank=True, null=True)
    lat_site = models.FloatField(blank=True, null=True)
    lon_site = models.FloatField(blank=True, null=True)
    codigounico = models.TextField(blank=True, null=True)
    cluster = models.IntegerField(blank=True, null=True)
    distrito = models.TextField(blank=True, null=True)
    ubicacion = models.PointField(srid=4326, blank=True, null=True)
    objects = GeoManager()
    class Meta:
        managed = True
        db_table = 'sage_sites'

    def url_first_tier(self):
        return "/get_first_tier/"+self.site_name


class SageSitesFilter (django_filters.FilterSet):
    class Meta:
            model = SageSites
            fields = ['site_name',]


class Sage_wcel(models.Model):
    id = models.AutoField(primary_key=True)
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
    wcelstate = models.IntegerField(blank=True, null=True)
    sector = models.PolygonField(srid=4326,blank=True, null=True)  # This field type is a guess.
    objects = GeoManager()
    class Meta:
        managed = True
        db_table = 'sage_wcel'



    def __str__(self):
        return self.name


class Sage_bts(models.Model):
    id = models.AutoField(primary_key=True)
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
    sector = models.PolygonField(blank=True, null=True)  # This field type is a guess.
    objects = GeoManager()
    class Meta:
        managed = False
        db_table = 'sage_bts'

    def __str__(self):
        return self.cellname