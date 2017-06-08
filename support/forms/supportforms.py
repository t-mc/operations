from django import forms

from django.forms import widgets
from django.db import models
import datetime

"""
Import voor Crispy Forms
"""
from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Fieldset, Layout, Reset, Submit

from support.models import Activiteiten, Cases

class Readonly(object):
    # def __init__(self, *args, **kwargs):
    #     self.ReadOnly = kwargs.pop("ReadOnly", False)
    # super(object, object).__init__(*args, **kwargs)
    # # SetReadonly(self, self.ReadOnly)
    # for name, field in form_object.fields.items():
    #     form_object.fields[name].widget.attrs['readonly'] = self.ReadOnly
    pass

class ActivityForm(forms.ModelForm):
    datum_uitgevoerd = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), initial=datetime.date.today)
    omschrijving = forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))
    # tijdsduur = forms.DurationField()
    # case_id = forms.CharField(widget=forms.HiddenInput)


    class Meta:
        model = Activiteiten
        fields = ['case_id', 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datum_uitgevoerd', 'tijdsduur']

class CaseForm(forms.ModelForm):
    datum_melding = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), initial=datetime.date.today)
    datum_gereed = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    omschrijving = forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))
    ReadOnly = False

    class Meta:
        model = Cases
        fields = ['onderwerp', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'bedrijf', 'contact', 'contract', 'uitvoerende']


    def __init__(self, *args, **kwargs):
        self.ReadOnly = kwargs.pop("ReadOnly", False)
        super(CaseForm, self).__init__(*args, **kwargs)
        SetReadonly(self, self.ReadOnly)


class CaseDetailForm(forms.ModelForm):
    datum_melding = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    datum_gereed = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    omschrijving = forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))

    class Meta:
        model = Cases
        fields = ('id', 'onderwerp', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'bedrijf', 'contact', 'uitvoerende')


class CasesList(forms.ModelForm):
    datum_melding = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Cases
        fields = ('onderwerp', 'datum_melding', 'status', 'bedrijf', 'contact', 'uitvoerende')


#
# Vlag alle formulier velden disabled[Flag]
#  Flag = True | False
def SetReadonly(form_object, Flag):
    for name, field in form_object.fields.items():
        form_object.fields[name].widget.attrs['readonly'] = Flag

