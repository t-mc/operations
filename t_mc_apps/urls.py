"""t_mc_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from django.conf import settings

from crm.views import AdressenAutocomplete, ContacpersoonAutocomplete
from projecten.views import VerkoopkansAutocomplete, OmzettenView

if (settings.ENVIRONMENT == 'prod'):
    admin.site.site_header = 'T-MC - CRM APP'
else:
    admin.site.site_header = 'T-MC - CRM APP [ DEV - TEST ]'
    
# app_name = 'home'

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    # url(r'^pcoverzicht/', include('pcoverzicht.urls')),
    url(r'^support/', include('support.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^contactpersoon-autocomplete/$', ContacpersoonAutocomplete.as_view(), name= 'contactpersoon-autocomplete'),
    url(r'^adres-autocomplete/$', AdressenAutocomplete.as_view(), name= 'adres-autocomplete'),
    url(r'^verkoopkans-autocomplete/$', VerkoopkansAutocomplete.as_view(), name= 'verkoopkans-autocomplete'),
    path('omzetten/', OmzettenView.as_view(), name= 'omzetten'),
    path('omzetten/<int:search_year>/', OmzettenView.as_view(), name= 'omzetten'),
    url(r'^', RedirectView.as_view(url='/admin/'), name="home"),
]

