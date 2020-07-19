from django.urls import path

from . import views
from .views import dibujar_lncel,dibujar_3g_adj,geojson_webcell_4g


urlpatterns = [
    path('', views.index, name='index'),
    path('dibujar_lncel/',dibujar_lncel, name='dibujar_lncel'),
    path('dibujar_3g_adj/',dibujar_3g_adj, name='dibujar_3g_adj'),
    path('geojson_webcell_4g/',geojson_webcell_4g,name='geojson_webcell_4g'),
 
]