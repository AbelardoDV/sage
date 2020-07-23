from django.urls import path

from . import views
from .views import draw_lncel,draw_wcel,draw_3gta,draw_bts,draw_2gta,dibujar_3g_adj,geojson_sage_lncel

from polls.views import Get_tiers_view

urlpatterns = [
    path('', views.index, name='index'),
    path('draw_lncel/',draw_lncel, name='draw_lncel'),
    path('geojson_sage_lncel/',geojson_sage_lncel,name='geojson_sage_lncel'),

    path('draw_wcel/',draw_wcel,name='draw_wcel'),
    path('draw_3gta/',draw_3gta,name='draw_3gta'),
    path('dibujar_3g_adj/',dibujar_3g_adj, name='dibujar_3g_adj'),

    path('draw_bts/',draw_bts,name='draw_bts'),
    path('draw_2gta/',draw_2gta,name='draw_2gta'),


    path('get_tiers/',Get_tiers_view.as_view(),name='get_tiers')
    
]