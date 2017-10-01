from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crm.models import Bedrijf


class MyCrispyForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_id = 'id-my-form'
        self.helper.form_class = 'my-form'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Bedrijf
        # See note here: https://docs.djangoproject.com/en/1.10/ref/contrib/admin/#django.contrib.admin.ModelAdmin.form
        fields = ['bedrijfsnaam', 'telefoonnummer', 'onenote', 'klantpartner', 'email', 'website', 'kvk_nummer', 'branche', 'actief',]

