from django.core.urlresolvers import reverse_lazy
from django.forms import formset_factory
from django.shortcuts import render 
from django.views.generic import DetailView, FormView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from support.forms import ActivityForm, CaseForm, CaseDetailForm, CasesList
from support.models import Cases, Activiteiten


#############################################################################
# Alle views die specifiek zijn voor de support app worden hieronder gebracht
#############################################################################


# Placeholder view voor het testen van de / of index route

class CaseListView(ListView):
    model = Cases
    template_name = 'support/case_list.html'
    context_object_name = 'cases'


class CaseCreate(CreateView):
    model = Cases
    form_class = CaseForm
    template_name = 'support/case_form.html'
    success_url = "/support/case/list"
    # fields = '__all__'


class CaseUpdate(UpdateView):
    model = Cases
    form_class = CaseForm
    template_name = 'support/case_form.html'
    success_url = "/support/case/list"
    # fields = '__all__'


class CaseDelete(DeleteView):
    model = Cases
    success_url = reverse_lazy('case_list')
    fields = '__all__'

class ActivityListView(ListView):
    model = Activiteiten
    template_name = 'support/index.html'
    context_object_name = 'cases'


class ActivityCreate(CreateView):
    model = Activiteiten
    success_url = reverse_lazy('case_list')
    fields = '__all__'


class ActivityUpdate(UpdateView):
    model = Activiteiten
    success_url = reverse_lazy('case_list')
    fields = '__all__'


class ActivityDelete(DeleteView):
    model = Activiteiten
    success_url = reverse_lazy('case_list')
    fields = '__all__'
