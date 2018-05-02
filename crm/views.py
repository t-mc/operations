from django.shortcuts import render

# Create your views here.
from dal import autocomplete

from .models import Adres, Contactpersoon

class ContacpersoonAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        gekozen_bedrijf = self.forwarded.get('bedrijf', None)
        qs = Contactpersoon.objects.all()
        qs = qs.filter(bedrijf=gekozen_bedrijf)
        if self.q:
            qs = qs.filter(volledige_naam__icontains=self.q)
        
        return qs

class AdressenAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        gekozen_bedrijf = self.forwarded.get('bedrijf', None)
        qs = Adres.objects.all()
        qs = qs.filter(bedrijf=gekozen_bedrijf)
        if self.q:
            qs = qs.filter(volledige_naam__icontains=self.q)
        
        return qs