from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.sessions.models import Session
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
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
    template_name = 'support/activity_add.html'
    # success_url = "/support/case/list"

    def get_success_url(self):
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

    def form_valid(self, form):
        form.instance.case_id = Cases.objects.get(case_code = self.kwargs['case_code'])
        return super(ActivityCreate, self).form_valid(form)


class ActivityDelete(DeleteView):
    model = Activiteiten
    template_name = "support/activity_confirm_delete.html"
    # success_url = "/support/case/list"
    fields = '__all__'

    def get_success_url(self):
        print(self.request.session['pk'])
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ActivityDelete, self).post(request, *args, **kwargs)

class ActivityListView(ListView):
    model = Activiteiten
    template_name = 'support/activity_list.html'
    context_object_name = 'activities'


class ActivityUpdate(UpdateView):
    model = Activiteiten
    form_class = ActivityForm
    # success_url = "/support/case/list"
    template_name = 'support/activity_update.html'
    # fields = '__all__'

    def get_success_url(self):
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

"""
Case views
"""

class CaseCreate(CreateView):
    model = Cases
    form_class = CaseForm
    template_name = 'support/case_add.html'
    success_url = '/support/case/list'


class CaseDelete(DeleteView):
    model = Cases
    success_url = "/support/case/list"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super(CaseDelete, self).get_context_data(**kwargs)
        act_count = Activiteiten.objects.filter(case_id=self.request.session['pk']).count()
        print(act_count)
        context['act_count'] = act_count
        return context

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            success_url = "/support/case/list"
            return super(CaseDelete, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

class CaseDetail(UpdateView):
    model = Cases
    form_class = CaseDetailForm
    template_name = 'support/case_activities.html'
    success_url = "/support/case/list"
    context_object_name = 'cases'
    
    def get_context_data(self, **kwargs):
        self.request.session['pk'] = self.kwargs['pk']
        context = super(CaseDetail, self).get_context_data(**kwargs)
        context['activities'] = Activiteiten.objects.filter(case_id=context['cases'])
        context['case_id'] = context['cases']
        return context

    def get_success_url(self):
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})


class CaseListView(ListView):
    model = Cases
    template_name = 'support/case_list.html'
    context_object_name = 'cases'

    def get_context_data(self, **kwargs):
        context = super(CaseListView, self).get_context_data(**kwargs)
        # Filter aanpassen zodat enkel actieve case naar boven komen
        # En sortering toepassen oudste case eerst
        # context['cases'] = Cases.objects.filter(id="1")
        return context


class CaseUpdate(UpdateView):
    model = Cases
    form_class = CaseForm
    template_name = 'support/case_update.html'
    success_url = "/support/case/list"

    def get_success_url(self):
        print(self)
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

