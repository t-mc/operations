from django import forms
from dal import autocomplete

from .models import Verkoopkans

class VerkoopkansForm(forms.ModelForm):

    class Meta:
        model = Verkoopkans
        fields = '__all__'
        widgets = {
            'opdrachtgever': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf'])
        }
       