from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from dal import autocomplete
import datetime
import collections

# from projecten.models import Adres, Contactpersoon
from projecten.models import Verkoopkans, Omzetpermaand, Urenpermedewerker

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
MAANDLIJST = [  0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00,
                0.00, ]
# Default weekurenlijst met uren per maand
WEEKURENLIJST = [   0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    0,
                    ]
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
            # vermenigvuldigingsfactor per stadium voor omzetten
            omzet_gewicht = order.verkoopstadium.verkoopkans
            # Voor iedere order haal omzetten op
            omzetten = Omzetpermaand.objects.filter(projectcode__id = order.id).filter(jaar = maand_in_jaar)
            # Voor iedere maand vul de juiste omzet per maan in
            if len(omzetten) > 0:
                for omzet in omzetten:
                    maandlijst[omzet.maand - 1] = (omzet.omzet * omzet_gewicht)
                    omzet_totaal = omzet_totaal + (omzet.omzet * omzet_gewicht)


                try:
                    if omzet.jaar == maand_in_jaar:
                        omzet_per_maand_item = collections.OrderedDict()
                        omzet_per_maand_item['Verkoopstadium'] = str(order.verkoopstadium)
                        omzet_per_maand_item['Productgroup'] = str(order.productgroep)
                        omzet_per_maand_item['Projectcode'] = order.projectcode
                        omzet_per_maand_item['Klant'] = str(order.bedrijf)
                        omzet_per_maand_item['Branche'] = order.bedrijf.branche.branch
                        omzet_per_maand_item['opdrachtgever'] = str(order.opdrachtgever)
                        omzet_per_maand_item['Omschrijving'] = order.omschrijving
                        omzet_per_maand_item['Klantpartner'] = str(order.klantpartner)
                        omzet_per_maand_item['Ordereigenaar'] = str(order.ordereigenaar)
                        omzet_per_maand_item['Januari'] = float(maandlijst[0])
                        omzet_per_maand_item['Februari'] = float(maandlijst[1])
                        omzet_per_maand_item['Maart'] = float(maandlijst[2])
                        omzet_per_maand_item['April'] = float(maandlijst[3])
                        omzet_per_maand_item['Mei'] = float(maandlijst[4])
                        omzet_per_maand_item['Juni'] = float(maandlijst[5])
                        omzet_per_maand_item['Juli'] = float(maandlijst[6])
                        omzet_per_maand_item['Augustus'] = float(maandlijst[7])
                        omzet_per_maand_item['September'] = float(maandlijst[8])
                        omzet_per_maand_item['Oktober'] = float(maandlijst[9])
                        omzet_per_maand_item['November'] = float(maandlijst[10])
                        omzet_per_maand_item['December'] = float(maandlijst[11])
                        omzet_per_maand_item['Year end'] = float(omzet_totaal)


                        omzet_per_maand.append(omzet_per_maand_item)
                except:
                    print('Niets gevonden!')

        return JsonResponse(omzet_per_maand, json_dumps_params={'indent': 3}, safe=False)

class UrenMedewerkerView(View):
    
    def get(self, request):
        # Haal eventueel opgegeven zoekjaar, anders default current_year
        search_year = request.GET.get('search_year')
        week_in_jaar = 1
        if search_year is not None:
            for jaar in JAAR_KEUZE:
                if jaar[1] == search_year:
                    week_in_jaar = jaar[0]

        # Zet context op
        context = {}
        context['orders'] = list()
        uren_per_week = []
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
            uren_totaal = 0
            weekurenlijst = WEEKURENLIJST.copy()
            # Voor iedere order haal omzetten op
            urenlist = Urenpermedewerker.objects.filter(projectcode__id = order.id).filter(jaar = week_in_jaar)
            # Voor iedere maand vul de juiste omzet per maan in
            if len(urenlist) > 0:
                for uren in urenlist:
                    weekurenlijst[uren.week] = uren.uren
                    uren_totaal = uren_totaal + uren.uren

                    try:
                        if uren.jaar == week_in_jaar:
                            uren_per_week_item = collections.OrderedDict()
                            uren_per_week_item['Verkoopstadium'] = str(order.verkoopstadium)
                            uren_per_week_item['Productgroup'] = str(order.productgroep)
                            uren_per_week_item['Projectcode'] = order.projectcode
                            uren_per_week_item['Klant'] = str(order.bedrijf)
                            uren_per_week_item['Branche'] = order.bedrijf.branche.branch
                            uren_per_week_item['opdrachtgever'] = str(order.opdrachtgever)
                            uren_per_week_item['Omschrijving'] = order.omschrijving
                            uren_per_week_item['Klantpartner'] = str(order.klantpartner)
                            uren_per_week_item['Ordereigenaar'] = str(order.ordereigenaar)
                            uren_per_week_item['Medewerker'] = str(uren.medewerker)
                            for week in range(1, 54):
                                uren_per_week_item[week] = weekurenlijst[week]

                            uren_per_week_item['Year end'] = float(uren_totaal)

                            uren_per_week.append(uren_per_week_item)
                    except:
                        print('Niets gevonden!')

        return JsonResponse(uren_per_week, json_dumps_params={'indent': 3}, safe=False)
