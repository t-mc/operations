from django import forms
from dal import autocomplete

from crm.models import Bedrijf, Contactpersoon


class ContactpersoonForm(forms.ModelForm):
    
    class Meta:
        model = Contactpersoon
        fields = '__all__'
        widgets = {
            'standplaats': autocomplete.ModelSelect2(url='adres-autocomplete', forward=['bedrijf'])
        }
 