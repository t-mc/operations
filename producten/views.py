from django.shortcuts import render
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
