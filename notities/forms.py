from django import forms
from dal import autocomplete

from notities.models import Notitie

class NotitieForm(forms.ModelForm):

    class Meta:
        model = Notitie
        fields = '__all__'
        widgets = {
            'contactpersoon': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
            'verkoopkans': autocomplete.ModelSelect2(url='verkoopkans-autocomplete', forward=['bedrijf'])
        }
       