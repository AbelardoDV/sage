from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', views.index, name='index'),
    path('crear_4g/',crear_4g_view, name='crear_4g'),
]