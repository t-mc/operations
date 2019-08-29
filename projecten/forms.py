from django import forms
from django.forms import DateTimeInput, CharField, ChoiceField, DecimalField, Select, TextInput
from dal import autocomplete
import datetime

from .models import Verkoopkans, Omzetpermaand, Urenpermedewerker
from crm.models import Contactpersoon

class VerkoopkansForm(forms.ModelForm):
    
    projectcode = forms.CharField(widget=forms.TextInput(attrs={'size': '20'}))
    omschrijving = forms.CharField(widget=forms.TextInput(attrs={'size': '77'}))

    class Meta:
        model = Verkoopkans
        fields = '__all__'

        widgets = {
            'opdrachtgever': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
            'kwo_ontvanger': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
        }


MAAND_KEUZE = (
    (1, 'Januarie'),
    (2, 'Februari'),
    (3, 'Maart'),
    (4, 'April'),
    (5, 'Mei'),
    (6, 'Juni'),
    (7, 'Juli'),
    (8, 'Augustus'),
    (9, 'September'),
    (10, 'Oktober'),
    (11, 'November'),
    (12, 'December'),
)
JAAR_KEUZE = (
    (1, '2018'),
    (2, '2019'),
    (3, '2020'),
    (4, '2021'),
    (5, '2022'),
    (6, '2023'),
    (7, '2024'),
    (8, '2025'),
    (9, '2026'),
    (10, '2027'),
)

class OmzetpermaandForm(forms.ModelForm):
    
    class Meta:
        model = Omzetpermaand
        fields = '__all__'
       
    def __init__(self, *args, **kwargs):
        super(OmzetpermaandForm, self).__init__(*args, **kwargs)

# Zet het jaar veld gelijk aan huidige jaar
        year = datetime.date.today().year
        for jaar in JAAR_KEUZE:
            if jaar[1] == str(year):
                self.fields['jaar'].initial = jaar[0]
                
# Zet het maand veld gelijk een de huidige maand 
        month = datetime.date.today().month
        self.fields['maand'].initial = month


class UrenpermedewerkerForm(forms.ModelForm):
    
    class Meta:
        model = Urenpermedewerker
        fields = '__all__'
       
    def __init__(self, *args, **kwargs):
        super(UrenpermedewerkerForm, self).__init__(*args, **kwargs)

# Zet het jaar veld gelijk aan huidige jaar
        year = datetime.date.today().year
        for jaar in JAAR_KEUZE:
            if jaar[1] == str(year):
                self.fields['jaar'].initial = jaar[0]
                