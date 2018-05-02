from django.shortcuts import render

from dal import autocomplete

# from projecten.models import Adres, Contactpersoon
from projecten.models import Verkoopkans

class VerkoopkansAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        gekozen_bedrijf = self.forwarded.get('bedrijf', None)
        qs = Verkoopkans.objects.all()
        qs = qs.filter(bedrijf=gekozen_bedrijf)
        if self.q:
            qs = qs.filter(volledige_naam__icontains=self.q)
        
        return qs