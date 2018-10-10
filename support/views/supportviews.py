from django.urls import reverse_lazy, reverse
from django.contrib.sessions.models import Session
from django.db.models import Q
from django.forms import formset_factory
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render
from django.views.generic import DetailView, FormView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.forms.utils import flatatt
from django.views.generic.base import TemplateView
from django_propeller.views import NavBarMixin

from dal import autocomplete

import datetime

from support.forms import ActivityForm, CaseForm, CaseDetailForm, CasesList, Contract
from support.models import Cases, Activiteiten 
from crm.models import Contactpersoon
from support.navbars import MainNavBar


"""
Activity views
"""
class ActivityCreate(CreateView, NavBarMixin):
    model = Activiteiten
    form_class = ActivityForm
    template_name = 'support/activity_add.html'
    # success_url = "/support/case/list"
    navbar_class = MainNavBar
    
    def get_context_data(self, **kwargs):
        context = super(ActivityCreate, self).get_context_data(**kwargs)
        case_code = (self.kwargs['case_code'], None)
        if case_code != None:
            case_pk = Cases.objects.filter(case_code = self.kwargs['case_code']).values_list('id', flat=True)
            context['case_pk'] = case_pk[0]
        print("case_pk")
        print(case_pk[0])
        return context

    def get_success_url(self):
        print("In get succes url")
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

    def form_valid(self, form):
        print("In form valid!")
        form.instance.case_id = Cases.objects.get(case_code = self.kwargs['case_code'])
        return super(ActivityCreate, self).form_valid(form)


class ActivityDelete(DeleteView, NavBarMixin):
    model = Activiteiten
    template_name = "support/activity_confirm_delete.html"
    # success_url = "/support/case/list"
    fields = '__all__'
    navbar_class = MainNavBar

    def get_success_url(self):
        print(self.request.session['pk'])
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

    def post(self, request, *args, **kwargs):
        if "cancel" in request.POST:
            url = self.get_success_url()
            return HttpResponseRedirect(url)
        else:
            return super(ActivityDelete, self).post(request, *args, **kwargs)

class ActivityListView(ListView, NavBarMixin):
    model = Activiteiten
    template_name = 'support/activity_list.html'
    context_object_name = 'activities'
    navbar_class = MainNavBar


class ActivityUpdate(UpdateView, NavBarMixin):
    model = Activiteiten
    form_class = ActivityForm
    template_name = 'support/activity_update.html'
    navbar_class = MainNavBar

    def get_success_url(self):
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})

"""
Case views
"""  
class CaseCreate(CreateView, NavBarMixin):
    model = Cases
    fields = ['onderwerp', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'bedrijf', 'contact', 'contract']
    # fields = '__all__'
    # form_class = CaseForm
    template_name = 'support/case_add.html'
    success_url = '/support/case/list'
    navbar_class = MainNavBar

    def form_valid(self, form):
        print("Koekoek")
        form.save()
        return super(CaseCreate, self).form_valid(form)

class CaseDelete(DeleteView, NavBarMixin):
    model = Cases
    success_url = "/support/case/list"
    fields = '__all__'
    navbar_class = MainNavBar

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

class CaseDetail(UpdateView, NavBarMixin):
    model = Cases
    form_class = CaseDetailForm
    template_name = 'support/case_activities.html'
    success_url = "/support/case/list"
    context_object_name = 'cases'
    navbar_class = MainNavBar

    def get_context_data(self, **kwargs):
        self.request.session['pk'] = self.kwargs['pk']
        context = super(CaseDetail, self).get_context_data(**kwargs)
        context['activities'] = Activiteiten.objects.filter(case_id=context['cases'])
        context['case_id'] = context['cases']
        return context

    def get_success_url(self):
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})


class CaseListView(ListView, NavBarMixin):
    model = Cases
    template_name = 'support/case_list.html'
    context_object_name = 'cases'
    navbar_class = MainNavBar

    def get_context_data(self, **kwargs):
        context = super(CaseListView, self).get_context_data(**kwargs)
        # Filter aanpassen zodat enkel actieve case naar boven komen
        # En sortering toepassen oudste case eerst
        # print(context)
        # queryset = Cases.objects.filter(status__status='In behandeling')
        context['cases'] = Cases.objects.filter(~Q(status__status='Afgehandeld'))
        return context


class CaseUpdate(UpdateView, NavBarMixin):
    model = Cases
    template_name = 'support/case_update.html'
    success_url = "/support/case/list"
    form_class = CaseForm
    navbar_class = MainNavBar

    def get_success_url(self):
        print(self)
        return reverse('support:case_detail', kwargs={'pk': self.request.session['pk']})


class CaseNoUpdate(UpdateView, NavBarMixin):
    model = Cases
    template_name = 'support/case_update.html'
    success_url = "/support/case/list"
    form_class = CaseForm
    navbar_class = MainNavBar

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
        print("Bedrijf in DAL is: " + bedrijf)
        if bedrijf:
             qs = qs.filter(bedrijf=bedrijf)
        # if self.q:
        #      qs = qs.filter(omschrijving_default__icontains=self.q)

        return qs

class ZoekContractAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        gekozen_bedrijf = self.forwarded.get('bedrijf', None)
        qs = Contract.objects.all()
        qs = qs.filter(bedrijf=gekozen_bedrijf)
        if self.q:
            qs = qs.filter(volledige_naam__icontains=self.q)
        
        return qs