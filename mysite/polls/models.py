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




class Webcell4G(models.Model):
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
    sector = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'webcell_4g'
