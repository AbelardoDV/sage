from django.urls import path

from . import views
from .views import dibujar_lncel,dibujar_3g_adj


urlpatterns = [
    path('', views.index, name='index'),
    path('dibujar_lncel/',dibujar_lncel, name='dibujar_lncel'),
    path('dibujar_3g_adj/',dibujar_3g_adj, name='dibujar_3g_adj'),
]