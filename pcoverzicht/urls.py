from django.conf.urls import url
from support import views

from pcoverzicht.views import ComputerCreate, ComputerDelete, ComputerUpdate, ComputerListView,\
                                 SoftwareCreate, SoftwareDelete, SoftwareUpdate, SoftwareListView

urlpatterns = [
        url(r'^computer/list/$', ComputerListView.as_view(), name='computer_list'),
        url(r'^computer/new$', ComputerCreate.as_view(), name='computer_new'),
        url(r'^computer/update/(?P<pk>\d+)$', ComputerUpdate.as_view(), name='computer_update'),
        url(r'^computer/delete/(?P<pk>\d+)$', ComputerDelete.as_view(), name='computer_delete'),
        url(r'^software/list/$', SoftwareListView.as_view(), name='software_list'),
        url(r'^software/new$', SoftwareCreate.as_view(), name='software_new'),
        url(r'^software/update/(?P<pk>\d+)$', SoftwareUpdate.as_view(), name='software_update'),
        url(r'^software/delete/(?P<pk>\d+)$', SoftwareDelete.as_view(), name='software_delete'),
        ]
