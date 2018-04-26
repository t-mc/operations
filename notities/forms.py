from django import forms
from django.forms import TextInput, DateTimeInput, Textarea
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
            'notitie': Textarea(attrs={'cols': 40, 'rows': 4}),
            'contactpersoon': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
            'verkoopkans': autocomplete.ModelSelect2(url='verkoopkans-autocomplete', forward=['bedrijf']),
        }

    # def __init__(self, *args, **kwargs):
    #     super(NotitieBedrijfForm, self).__init__(*args, **kwargs)

# Zet het bedrijf veld gelijk aan bedrijf van het parent form 
        # bedrijf = self.parent.fields['bedrijf']
        # self.fields['bedrijf'].initial = "T-MC"

       
class NotitieContactForm(forms.ModelForm):

    class Meta:
        model = Notitie
        fields = ('onderwerp', 'notitie', 'verkoopkans', 'datumtijd' )

        widgets={'notitie': Textarea(attrs={'cols': 80, 'rows': 4}),
            'datumtijd': DateTimeInput(format='%d-%m-%Y %H:%M:%S')}

class NotitieProjectFormSet(forms.BaseInlineFormSet):
  
    def get_form_kwargs(self, index):
        kwargs = super(NotitieProjectFormSet, self).get_form_kwargs(index)
        kwargs.update({'parent': self.instance})
        return kwargs

class NotitieProjectForm(forms.ModelForm):

    class Meta:
        model = Notitie
        fields = '__all__'
        widgets = {
            'notitie': Textarea(attrs={'cols': 40, 'rows': 4}),
            'contactpersoon': autocomplete.ModelSelect2(url='contactpersoon-autocomplete', forward=['bedrijf']),
        }
       
    def __init__(self, *args, **kwargs):
        parent = kwargs.pop('parent')
        super(NotitieProjectForm, self).__init__(*args, **kwargs)
    #     if hasattr(self, 'instance'):
    #         if ( self.instance ):
    #             print('Koekoek')
    #     else:
    #         print('Oops')
                # print(self.instance)  
        # print(parent.bedrijf)
        # print(self.fields['bedrijf'].to_field_name)
        # print(self.instance)
        # if (self.fields['bedrijf'] != ''):
        #     print(self.fields['bedrijf'])
        # else:
        #     print('Leeg')
        