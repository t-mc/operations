from django.conf.urls import url
from support import views
from support.views import AddCaseView, UpdateCaseView, CasesListView

urlpatterns = [
    url(r'^$', CasesListView.as_view(), name='index'),
    url(r'^case_add/$', views.case_add, name="case_add"),
    url(r'^add_case/$', AddCaseView.as_view(), name="add_case"),
    url(r'^update_case/(?P<slug>[\w\-]+)/$', UpdateCaseView.as_view(), name="update_case"),
    #url(r'^case_detail/(?P<case_id>[\w\-]+)/$', views.case_detail, name="case_detail"),
    url(r'^activity_add/$', views.activity_add, name="activity_add"),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]