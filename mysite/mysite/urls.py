"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('upload/', simple_upload_view,name='upload_csv'),
    path('mapper_view/',mapper_view,name='mapper_view'),
    path('', index, name='index'),
    path('upload_kpis/',mapper_view,name='upload_kpis'),
    path('wbts_list/',wbts_list_view,name='wbts_list'),


]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)