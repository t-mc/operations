from django.http import HttpResponse
from django.shortcuts import render
import json
from dal import autocomplete
# Create your views here.
from .models import Product

class ProductpriceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        gekozen_product = self.forwarded.get('product', None)
        qs = Product.objects.all()
        qs = qs.filter(code=gekozen_product)
        if self.q:
            qs = qs.filter(code__icontains=self.q)

        return qs


def vw_product_zoek_ajax(request):
    # search_text in zoveel stukken knippen als je maar wil op ##
    print('gekozen_product =' + request.POST.get('gekozen_product', ''))
    zoek_product = request.POST.get('gekozen_product', '')
    gevonden_product = Product.objects.filter(code=zoek_product)
    gevonden_prijs = gevonden_product[0].prijs_per_eenheid
    print('gevonden_product =' + str(gevonden_prijs))

    response_json = json.dumps(str(gevonden_prijs))
    return HttpResponse(response_json, content_type='application/json')
