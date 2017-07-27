from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.sessions.models import Session
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
from django.views.generic import DetailView, FormView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from dal import autocomplete

import datetime

from support.forms import ActivityForm, CaseForm, CaseDetailForm, CasesList
from support.models import Cases, Activiteiten, Contactpersoon

"""
Activity views
"""
class ActivityCreate(CreateView):
    model = Activiteiten
    form_class = ActivityForm
    template_name = 'support/activity_add.html'
    # success_url = "/support/case/list"

    def get_context_data(self, **kwargs):
        context = super(ActivityCreate, self).get_context_data(**kwargs)
        case_code = self.kwargs['case_code']
        case_pk = Cases.objects.filter(case_code = self.kwargs['case_code']).values_list('id', flat=True)
        context['case_pk'] = case_pk[0]
        print("case_pk")
        print(case_pk[0])
        return context

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
    template_name = 'support/activity_update.html'

    def get_success_url(self):
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

"""
Case views
"""

class CaseCreate(CreateView):
    # model = Cases
    form_class = CaseForm
    template_name = 'support/case_add.html'
    # success_url = '/support/case/new'

    def form_valid(self, form):
        print("Koekoek")
        form.save()
        return super(CaseCreate, self).form_valid(form)

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
        # print(context)
        # queryset = Cases.objects.filter(status__status='In behandeling')
        context['cases'] = Cases.objects.filter(~Q(status__status='Afgehandeld'))
        return context


class CaseUpdate(UpdateView):
    model = Cases
    template_name = 'support/case_update.html'
    success_url = "/support/case/list"
    form_class = CaseForm

    def get_success_url(self):
        print(self)
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})


class CaseNoUpdate(UpdateView):
    model = Cases
    template_name = 'support/case_update.html'
    success_url = "/support/case/list"
    form_class = CaseForm

    # Zet de formuliervelden op read only
    # door ReadOnly = True als argument mee te geven.
    def get_form_kwargs(self):
        kwargs = super(CaseNoUpdate, self).get_form_kwargs()
        kwargs.update({'ReadOnly': True})
        return kwargs

    def get_success_url(self):
        print(self)
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

class ZoekContactAutocomplete(autocomplete.Select2QuerySetView):
    """
    Autocomplete view voor contacten. De lijst wordt gefilterd op bedrijf
    """
    def get_queryset(self):

        if not self.request.user.is_authenticated():
            return Contactpersoon.objects.none()

        qs = Contactpersoon.objects.all()

        bedrijf = self.forwarded.get('bedrijf', None)

        if bedrijf:
             qs = qs.filter(bedrijf=bedrijf)
        # if self.q:
        #      qs = qs.filter(omschrijving_default__icontains=self.q)

        return qs