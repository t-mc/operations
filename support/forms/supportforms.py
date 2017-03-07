from django import forms

from django.forms import widgets
from django.db import models

from support.models import Activiteiten, Cases


class ActivityForm(forms.ModelForm):

    class Meta:
        model = Activiteiten
        fields = ('case_id', 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datum_uitgevoerd',)


class CaseForm(forms.ModelForm):
    datum_melding = forms.DateField()
    omschrijving = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Cases
        fields = ('onderwerp', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'bedrijf', 'contact', 'uitvoerende')


class CaseDetailForm(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ('onderwerp', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'bedrijf', 'contact', 'uitvoerende')


class CasesList(forms.ModelForm):
    class Meta:
        model = Cases
        fields = ('onderwerp', 'datum_melding', 'status', 'bedrijf', 'contact', 'uitvoerende')
