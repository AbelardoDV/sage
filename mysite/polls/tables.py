import django_tables2 as tables
from .models import SageSites

class SageSitesTable(tables.Table):
    
    First_Tier= tables.TemplateColumn('<a style="color: #000000;cursor:pointer;text-decoration: underline;" onclick="viewFirstTier(\'{{record.site_name}}\');">Tier1</a>')
    # record.(Model's column)
    First_Tier.orderable=False
    class Meta:
        model = SageSites
        attrs = {"class":"table table-striped jambo_table bulk_action col-12"
               
         }
        template_name = "django_tables2/bootstrap4.html"
        fields = ("site_name","mrbts_id","distrito",'First_Tier')
        

