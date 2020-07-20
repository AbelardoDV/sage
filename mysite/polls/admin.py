from django.contrib import admin
from .models import Sage_lncel
from .models import Sage_wcel
from .models import Sage_bts
from .models import Adyacencias3G
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class Sage_lnceladmin(LeafletGeoAdmin):
    search_fields = ('cellname',)
    pass
admin.site.register(Sage_lncel,Sage_lnceladmin)


class Sage_wceladmin(LeafletGeoAdmin):
    search_fields = ('name',)
    pass
admin.site.register(Sage_wcel,Sage_wceladmin)

class Sage_btsadmin(LeafletGeoAdmin):
    search_fields = ('cellname',)
    pass
admin.site.register(Sage_bts,Sage_btsadmin)

class Adyacencias3Gadmin(admin.ModelAdmin):
    search_fields = ('source_id',)
    pass
admin.site.register(Adyacencias3G,Adyacencias3Gadmin)