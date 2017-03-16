from django import forms
from django.forms.models import ModelForm

from django.forms import widgets
from django.db import models
import datetime

from crispy_forms.helper import FormHelper
from crispy_forms.layout import ButtonHolder, Fieldset, HTML, Layout, Reset, Submit

from pcoverzicht.models import Computer, Software

class ComputerForm(forms.ModelForm):
    aanschafdatum = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Computer
        fields = ['naam', 'gebruiker', 'merkentype', 'aanschafdatum', 'serienummer']

    def __init__(self, *args, **kwargs):
        super(ComputerForm, self).__init__(*args, **kwargs) 
        
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset('PC informatie', 'naam', 'gebruiker'),
            Fieldset('PC details', 'merkentype', 'aanschafdatum', 'serienummer'),
            ButtonHolder(
                Submit('save', ('Opslaan'), css_class='btn btn-custom'),
                Submit('cancel', ('Annuleren'), css_class='btn btn-custom'),
                # HTML("<button type='submit' class='btn btn-primary btn-custom' value='Sla op'>Opslaan</button>"),
                # HTML("<a href='/pcoverzicht/computer/list' class='btn btn-primary btn-custom'>Annuleren</a>")
                ),
        )
