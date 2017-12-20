from django import forms
from dal import autocomplete

from .models import Verkoopkans

class VerkoopkansForm(forms.ModelForm):

    class Meta:
        model = Verkoopkans
        fields = '__all__'
        # exclude = ['last_modified_user', ] 
        # fields = ['projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium', 'geschatte_omzet', 'werkelijke_omzet', 'startdatum_project', 'einddatum_project', 'broncampagne', 'onenote_doc', 'klantpartner', 'actief']
        widgets = {
            'opdrachtgever': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf'])
        }
       