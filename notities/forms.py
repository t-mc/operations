from django import forms
from django.forms import HiddenInput, TextInput, DateTimeInput, Textarea
# from django.forms import BaseInlineFormSet

from dal import autocomplete

from crm.models import Bedrijf
from notities.models import Notitie

class NotitieForm(forms.ModelForm):  

    class Meta:
        model = Notitie
        fields = ('bedrijf', 'contactpersoon', 'verkoopkans', 'onderwerp', 'notitie', 'datumtijd')
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
        # kwargs.update({'parent': self.instance})
        try: 
            kwargs.update({'bedrijf': self.instance.bedrijf})
        except:
            kwargs.update({'bedrijf': ''})
        return kwargs
       
class NotitieContactForm(forms.ModelForm):

    class Meta:
        model = Notitie
        fields = ('onderwerp', 'notitie', 'verkoopkans', 'datumtijd', 'bedrijf' )

        widgets={'notitie': Textarea(attrs={'cols': 80, 'rows': 4}),
                'verkoopkans': autocomplete.ModelSelect2(url='verkoopkans-autocomplete', forward=['bedrijf']),
                'bedrijf': HiddenInput(),
                }

    def __init__(self, *args, **kwargs):
        # parent = kwargs.pop('parent')
        bedrijfsnaam = kwargs.pop('bedrijf')
        # if bedrijfsnaam != '':
        try:
            bedrijf = Bedrijf.objects.get(bedrijfsnaam = bedrijfsnaam)
            super(NotitieContactForm, self).__init__(*args, **kwargs)
            self.fields['bedrijf'].initial = bedrijf
        except:
            super(NotitieContactForm, self).__init__(*args, **kwargs)

class NotitieProjectFormSet(forms.BaseInlineFormSet):
  
    def get_form_kwargs(self, index):
        kwargs = super(NotitieProjectFormSet, self).get_form_kwargs(index)
        # kwargs.update({'parent': self.instance})
        try: 
            kwargs.update({'bedrijf': self.instance.bedrijf})
        except:
            kwargs.update({'bedrijf': ''})
        return kwargs

class NotitieProjectForm(forms.ModelForm):

    class Meta:
        model = Notitie
        fields = ('onderwerp', 'notitie', 'verkoopkans', 'contactpersoon', 'datumtijd', 'bedrijf' )
        widgets = {
            'notitie': Textarea(attrs={'cols': 80, 'rows': 4}),
            'contactpersoon': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
            'bedrijf': HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        # parent = kwargs.pop('parent')
        bedrijfsnaam = kwargs.pop('bedrijf')
        if bedrijfsnaam != '':
            bedrijf = Bedrijf.objects.get(bedrijfsnaam = bedrijfsnaam)
            super(NotitieProjectForm, self).__init__(*args, **kwargs)
            self.fields['bedrijf'].initial = bedrijf
        else:
            super(NotitieProjectForm, self).__init__(*args, **kwargs)
            
