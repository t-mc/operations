from django.conf.urls import url
from support import views
from support.views import CaseListView, CaseCreate, CaseDetail, CaseUpdate, CaseNoUpdate, CaseDelete, \
                          ActivityListView, ActivityCreate, ActivityUpdate, ActivityDelete, \
                          ZoekContactAutocomplete, ZoekContractAutocomplete
app_name = 'support'

urlpatterns = [
        url(r'^case/list/$',                  CaseListView.as_view(),     name='case_list'),
        url(r'^case/new/$',                   CaseCreate.as_view(),       name='case_new'),
        url(r'^case/detail/(?P<pk>\d+)/$',    CaseDetail.as_view(),       name='case_detail'),
        url(r'^case/update/(?P<pk>\d+)/$',    CaseUpdate.as_view(),       name='case_update'),
        url(r'^case/no_update/(?P<pk>\d+)/$', CaseNoUpdate.as_view(),     name='case_no_update'),        
        url(r'^case/delete/(?P<pk>\d+)/$',    CaseDelete.as_view(),       name='case_delete'),
        url(r'^activity/list/$',              ActivityListView.as_view(), name='activity_list'),
        url(r'^activity/new/(?P<case_code>\w+)/$', ActivityCreate.as_view(),   name='activity_new'),        
        url(r'^activity/new/$',               ActivityCreate.as_view(),   name='activity_new'),
        url(r'^activity/update/(?P<pk>\d+)/$',ActivityUpdate.as_view(),   name='activity_update'),
        url(r'^activity/delete/(?P<pk>\d+)/$',ActivityDelete.as_view(),   name='activity_delete'),
        url(r'^register/$',                   views.register,             name='register'),
        url(r'^login/$',                      views.user_login,           name='login'),
        url(r'^logout/$',                     views.user_logout,          name='logout'),
        url(r'^zoekcontact-autocomplete/$',   ZoekContactAutocomplete.as_view(), name = 'zoekcontact-autocomplete'),
        url(r'^zoekcontract-autocomplete/$',  ZoekContractAutocomplete.as_view(), name = 'zoekcontract-autocomplete'),
]