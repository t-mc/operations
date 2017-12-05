from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_propeller.views import NavBarMixin

from pcoverzicht.models import Computer, Software
from pcoverzicht.forms import ComputerForm
from support.navbars import MainNavBar
# Create your views here.


class ComputerListView(ListView, NavBarMixin):
    model = Computer
    template_name = 'computer_list.html'
    navbar_class = MainNavBar

class ComputerCreate(CreateView, NavBarMixin):
    model = Computer
    success_url = reverse_lazy('computer:computer_list')
    # template_name = 'pcoverzicht/computer_form.html'
    fields = '__all__'
    navbar_class = MainNavBar

class ComputerUpdate(UpdateView, NavBarMixin):
    model = Computer
    form_class = ComputerForm
    success_url = reverse_lazy('computer:computer_list')
    template_name = 'pcoverzicht/computer_update.html'
    # fields = '__all__'
    navbar_class = MainNavBar

class ComputerDelete(DeleteView, NavBarMixin):
    model = Computer
    template_name = 'pcoverzicht/computer_confirm_delete.html'
    success_url = reverse_lazy('computer:computer_list')
    navbar_class = MainNavBar

class SoftwareListView(ListView, NavBarMixin):
    model = Software
    navbar_class = MainNavBar

class SoftwareCreate(CreateView, NavBarMixin):
    model = Software
    success_url = reverse_lazy('computer:software_list')
    template_name = 'pcoverzicht/software_form.html'
    fields = '__all__'
    navbar_class = MainNavBar

class SoftwareUpdate(UpdateView, NavBarMixin):
    model = Software
    success_url = reverse_lazy('computer:software_list')
    template_name = 'pcoverzicht/software_update.html'
    fields = '__all__'
    navbar_class = MainNavBar

class SoftwareDelete(DeleteView, NavBarMixin):
    model = Software
    success_url = reverse_lazy('computer:software_list')
    navbar_class = MainNavBar
