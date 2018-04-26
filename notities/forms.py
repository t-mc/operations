from django import forms
from django.forms import TextInput, DateTimeInput, Textarea
# from django.forms import BaseInlineFormSet

from dal import autocomplete

from crm.models import Bedrijf
from notities.models import Notitie

class NotitieForm(forms.ModelForm):  

    class Meta:
        model = Notitie
        fields = ('contactpersoon', 'verkoopkans', 'onderwerp', 'notitie', 'datumtijd', 'bedrijf')
        widgets = {
            'notitie': Textarea(attrs={'cols': 80, 'rows': 4}),
            'contactpersoon': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
            'verkoopkans': autocomplete.ModelSelect2(url='verkoopkans-autocomplete', forward=['bedrijf']),
        }

class NotitieBedrijfForm(forms.ModelForm):  

    class Meta:
        model = Notitie
        fields = ('onderwerp', 'contactpersoon', 'verkoopkans', 'notitie', 'datumtijd')
        widgets = {
            'notitie': Textarea(attrs={'cols': 60, 'rows': 4}),
            'contactpersoon': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
            'verkoopkans': autocomplete.ModelSelect2(url='verkoopkans-autocomplete', forward=['bedrijf']),
        }

class NotitieContactFormSet(forms.BaseInlineFormSet):
      
    def get_form_kwargs(self, index):
        kwargs = super(NotitieContactFormSet, self).get_form_kwargs(index)
        # print(self[0])
        kwargs.update({'parent': self.instance})
        kwargs.update({'bedrijf': self.instance.bedrijf})
        return kwargs
       
class NotitieContactForm(forms.ModelForm):

    class Meta:
        model = Notitie
        fields = ('onderwerp', 'notitie', 'verkoopkans', 'datumtijd', 'bedrijf' )

        widgets={'notitie': Textarea(attrs={'cols': 80, 'rows': 4}),
            'datumtijd': DateTimeInput(format='%d-%m-%Y %H:%M:%S')}

    def __init__(self, *args, **kwargs):
        parent = kwargs.pop('parent')
        bedrijfsnaam = kwargs.pop('bedrijf')
        bedrijf = Bedrijf.objects.get(bedrijfsnaam = bedrijfsnaam)
        print(bedrijf)
        super(NotitieContactForm, self).__init__(*args, **kwargs)

        self.fields['bedrijf'].initial = bedrijf



class NotitieProjectFormSet(forms.BaseInlineFormSet):
  
    def get_form_kwargs(self, index):
        kwargs = super(NotitieProjectFormSet, self).get_form_kwargs(index)
        # print(self[0])
        kwargs.update({'parent': self.instance})
        kwargs.update({'bedrijf': self.instance.bedrijf})
        return kwargs

class NotitieProjectForm(forms.ModelForm):

    class Meta:
        model = Notitie
        fields = ('onderwerp', 'notitie', 'verkoopkans', 'datumtijd', 'bedrijf' )
        widgets = {
            'notitie': Textarea(attrs={'cols': 80, 'rows': 4}),
            'contactpersoon': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
        }

    def __init__(self, *args, **kwargs):
        parent = kwargs.pop('parent')
        bedrijfsnaam = kwargs.pop('bedrijf')
        bedrijf = Bedrijf.objects.get(bedrijfsnaam = bedrijfsnaam)
        print(bedrijf)
        super(NotitieProjectForm, self).__init__(*args, **kwargs)

        self.fields['bedrijf'].initial = bedrijf
