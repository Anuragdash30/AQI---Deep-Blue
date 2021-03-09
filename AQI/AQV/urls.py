"""coronaDash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from firstPage import views
from django.conf.urls import url
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',views.index,name='Mainpage'),
    url(r'^template/mapop', TemplateView.as_view(template_name="mappop.html"),name='mapop'),
    url(r'^template/testgame', TemplateView.as_view(template_name="map.html"),name='testgame'),
    
 
    url('Regionwise',views.drillDownACountry,name='drillDown'),
    url('Social',views.social,name='social'),
    url('compare',views.compare,name='compare')

]
