from django.contrib import admin
from .models import Webcell4G
from .models import Adyacencias3G
# Register your models here.

class webcell4gadmin(admin.ModelAdmin):
    search_fields = ('cellname',)
    pass
admin.site.register(Webcell4G,webcell4gadmin)

class Adyacencias3Gadmin(admin.ModelAdmin):
    search_fields = ('=source_id',)
    pass
admin.site.register(Adyacencias3G,Adyacencias3Gadmin)