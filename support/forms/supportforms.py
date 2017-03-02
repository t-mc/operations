from django import forms
from django.forms import widgets
from django.db import models

from support.models import Activiteiten, Cases


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activiteiten
        fields = ('caseId', 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datumUitgevoerd',)


class CaseForm(forms.ModelForm):
    datumMelding = forms.DateField(widget=forms.DateInput)
    omschrijving = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Cases
        fields = ('onderwerp', 'omschrijving', 'datumMelding', 'datumGereed', 'status', 'klant', 'contactpersoon', 'uitvoerende')


class CaseDetailForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ('onderwerp', 'omschrijving', 'datumMelding', 'datumGereed', 'status', 'klant', 'contactpersoon', 'uitvoerende')


class CasesList(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ('onderwerp', 'datumMelding', 'status', 'klant', 'contactpersoon', 'uitvoerende')
