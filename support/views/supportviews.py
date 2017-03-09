from django.core.urlresolvers import reverse_lazy
from django.forms import formset_factory
from django.shortcuts import render 
from django.views.generic import DetailView, FormView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

import datetime

from support.forms import ActivityForm, CaseForm, CaseDetailForm, CasesList
from support.models import Cases, Activiteiten

"""
Activity views
"""
class ActivityCreate(CreateView):
    model = Activiteiten
    form_class = ActivityForm
    template_name = 'support/activity_form.html'
    success_url = "/support/case/list"
    # fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ActivityCreate, self).__init__(*args, **kwargs)
        set.fields['case_id'].initial = kwargs['case_code']

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ActivityCreate, self).get_context_data(**kwargs)
    #     context['case_id'] = self.kwargs['case_code']
    #     print(context['case_id'])
    #     return context

class ActivityDelete(DeleteView):
    model = Activiteiten
    template_name = "support/activity_confirm_delete.html"
    success_url = "/support/case/list"
    fields = '__all__'

class ActivityListView(ListView):
    model = Activiteiten
    template_name = 'support/activity_list.html'
    context_object_name = 'activities'

class ActivityUpdate(UpdateView):
    model = Activiteiten
    form_class = ActivityForm
    success_url = "/support/case/list"
    template_name = 'support/activity_update.html'
    # fields = '__all__'

"""
Case views
"""

class CaseCreate(CreateView):
    model = Cases
    form_class = CaseForm
    template_name = 'support/case_add.html'
    success_url = '/support/case/list'
    # fields = '__all__'

class CaseDelete(DeleteView):
    model = Cases
    success_url = "/support/case/list"
    fields = '__all__'

class CaseDetail(UpdateView):
    model = Cases
    form_class = CaseDetailForm
    template_name = 'support/case_activities.html'
    success_url = "/support/case/list"
    context_object_name = 'cases'
    # fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CaseDetail, self).get_context_data(**kwargs)
        context['activities'] = Activiteiten.objects.filter(case_id=context['cases'])
        context['case_id'] = context['cases']
        print(context['cases'].case_code)
        return context
        
class CaseListView(ListView):
    model = Cases
    template_name = 'support/case_list.html'
    context_object_name = 'cases'

class CaseUpdate(UpdateView):
    model = Cases
    form_class = CaseForm
    template_name = 'support/case_update.html'
    success_url = "/support/case/list"
    # fields = '__all__'



