from django import forms

from django.forms import widgets
from django.db import models
import datetime

from support.models import Activiteiten, Cases


class ActivityForm(forms.ModelForm):
    datum_uitgevoerd = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y')), initial=datetime.date.today)
    omschrijving = forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))

    class Meta:
        model = Activiteiten
        fields = ('case_id', 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datum_uitgevoerd',)


class CaseForm(forms.ModelForm):
    datum_melding = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y')))
    datum_gereed = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y')), required=False)
    omschrijving = forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))
    
    class Meta:
        model = Cases
        fields = ('onderwerp', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'bedrijf', 'contact', 'uitvoerende')


class CaseDetailForm(forms.ModelForm):
    datum_melding = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y')))
    datum_gereed = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y')))
    omschrijving = forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))

    class Meta:
        model = Cases
        fields = ('id', 'onderwerp', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'bedrijf', 'contact', 'uitvoerende')


class CasesList(forms.ModelForm):
    datum_melding = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y')))

    class Meta:
        model = Cases
        fields = ('onderwerp', 'datum_melding', 'status', 'bedrijf', 'contact', 'uitvoerende')
