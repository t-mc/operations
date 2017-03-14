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


class ActivityForm(forms.ModelForm):
    datum_uitgevoerd = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), initial=datetime.date.today)
    omschrijving = forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))
    # case_id = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = Activiteiten
        fields = ( 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datum_uitgevoerd',)

class CaseForm(forms.ModelForm):
    datum_melding = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), initial=datetime.date.today)
    datum_gereed = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=False)
    omschrijving = forms.CharField(widget=forms.Textarea(attrs={'rows':'4'}))

    class Meta:
        model = Cases
        fields = ['onderwerp', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'bedrijf', 'contact', 'uitvoerende']
    """
    Init voor Crispy Forms
    """
    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs) 
        
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset('Case informatie', 'onderwerp', 'bedrijf', 'contact',),
            Fieldset('Case details', 'omschrijving', 'datum_melding', 'datum_gereed', 'status', 'uitvoerende'),
            ButtonHolder(
                Submit('save', ('Opslaan'), css_class='btn btn-primary '),
                Reset('reset', ('Annuleren'), css_class='btn')
                ),
        )

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
