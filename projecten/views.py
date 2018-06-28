from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from dal import autocomplete
import datetime

# from projecten.models import Adres, Contactpersoon
from projecten.models import Verkoopkans, Omzetpermaand

JAAR_KEUZE = [
    (1, '2018'),
    (2, '2019'),
    (3, '2020'),
    (4, '2021'),
    (5, '2022'),
    (6, '2023'),
    (7, '2024'),
    (8, '2025'),
    (9, '2026'),
    (10,'2027'),
]
MAAND_KEUZE = (
    (1, 'Januari'),
    (2, 'Februari'),
    (3, 'Maart'),
    (4, 'April'),
    (5, 'Mei'),
    (6, 'Juni'),
    (7, 'Juli'),
    (8, 'Augustus'),
    (9, 'September'),
    (10,'Oktober'),
    (11,'November'),
    (12,'December'),
)
# Default maandlijst met omzet per maand
MAANDLIJST = [  '0', 
                '0', 
                '0', 
                '0', 
                '0', 
                '0', 
                '0', 
                '0', 
                '0', 
                '0', 
                '0', 
                '0', ]
# Bepaal huidige jaar als default zoekjaar
current_year = datetime.datetime.now().year

class VerkoopkansAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        gekozen_bedrijf = self.forwarded.get('bedrijf', None)
        qs = Verkoopkans.objects.all()
        qs = qs.filter(bedrijf=gekozen_bedrijf)
        if self.q:
            qs = qs.filter(volledige_naam__icontains=self.q)
        
        return qs


class OmzettenView(View):
    
    def get(self, request):
        # Haal eventueel opgegeven zoekjaar, anders default current_year
        search_year = request.GET.get('search_year')
        maand_in_jaar = 1
        if search_year is not None:
            for jaar in JAAR_KEUZE:
                if jaar[1] == search_year:
                    maand_in_jaar = jaar[0]

        # Zet context op
        context = {}
        context['orders'] = list()
        omzet_per_maand = []
        # Haal alle orders op voor huidige of gekozen jaar
        if search_year is None:
            orders = Verkoopkans.objects.filter().exclude(verkoopstadium__verkoopstadium = '9 - Order gemist')
            context['orders'] = orders
        else :
            orders = Verkoopkans.objects.filter().exclude(verkoopstadium__verkoopstadium = '9 - Order gemist')
            context['orders'] = orders
            

        # Loop alle orders door
        for order in orders:
            # Reset maandlijst met default MAANDLIJST
            omzet_totaal = 0
            maandlijst = MAANDLIJST.copy()
            # Voor iedere order haal omzetten op
            omzetten = Omzetpermaand.objects.filter(projectcode__id = order.id).filter(jaar = maand_in_jaar)
            # Voor iedere maand vul de juiste omzet per maan in
            if len(omzetten) > 0:
                for omzet in omzetten:
                    maandlijst[omzet.maand - 1] = int(omzet.omzet)
                    omzet_totaal = omzet_totaal + omzet.omzet

                try :
                    if omzet.jaar == maand_in_jaar:
                        omzet_per_maand_item = dict()
                        omzet_per_maand_item['Verkoopstadium'] = str(order.verkoopstadium)
                        omzet_per_maand_item['Productgroup'] = str(order.productgroep)
                        omzet_per_maand_item['Projectcode'] = order.projectcode
                        omzet_per_maand_item['Klant'] = str(order.bedrijf)
                        omzet_per_maand_item['opdrachtgever'] = str(order.opdrachtgever)
                        omzet_per_maand_item['Omschrijving'] = order.omschrijving
                        omzet_per_maand_item['Klantpartner'] = str(order.klantpartner)
                        omzet_per_maand_item['Ordereigenaar'] = str(order.ordereigenaar)
                        omzet_per_maand_item['Januari'] = maandlijst[0]
                        omzet_per_maand_item['Februari'] = maandlijst[1]
                        omzet_per_maand_item['Maart'] = maandlijst[2]
                        omzet_per_maand_item['April'] = maandlijst[3]
                        omzet_per_maand_item['Mei'] = maandlijst[4]
                        omzet_per_maand_item['Juni'] = maandlijst[5]
                        omzet_per_maand_item['Juli'] = maandlijst[6]
                        omzet_per_maand_item['Augustus'] = maandlijst[7]
                        omzet_per_maand_item['September'] = maandlijst[8]
                        omzet_per_maand_item['Oktober'] = maandlijst[9]
                        omzet_per_maand_item['November'] = maandlijst[10]
                        omzet_per_maand_item['December'] = maandlijst[11]
                        omzet_per_maand_item['Year end'] = int(omzet_totaal)

                        omzet_per_maand.append(omzet_per_maand_item)
                except:
                    print('Niets gevonden!')

        return JsonResponse(omzet_per_maand, json_dumps_params={'indent': 3}, safe=False)
    