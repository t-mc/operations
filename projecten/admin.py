from django.contrib import admin
from django.db import models
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from projecten.forms import VerkoopkansForm

# Register your models here.
from .models import Verkoopkans, Orders, Verkoopstadium


class VerkoopkansAdmin(admin.ModelAdmin):
    # form = VerkoopkansForm
    model = Verkoopkans
    def get_queryset(self, request):
        qs = super(VerkoopkansAdmin, self).get_queryset(request)
        return qs.exclude(verkoopstadium__verkoopstadium__contains='Order')

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'klantpartner', 'verkoopstadium')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)
    list_filter = (('verkoopstadium', RelatedDropdownFilter),
                    ('klantpartner', RelatedDropdownFilter), 
                    ('bedrijf', RelatedDropdownFilter), 
                    ('opdrachtgever', RelatedDropdownFilter))
    search_fields = ('projectcode', 'bedrijf__bedrijfsnaam')

    fieldsets = (
        (None, {
           'fields': (('projectcode', 'omschrijving'), ('bedrijf', 'opdrachtgever'), ('verkoopstadium', 'klantpartner'), 'actief')
        }),
        ('Details', {
            'fields': (('geschatte_omzet', 'werkelijke_omzet'), ('startdatum_project', 'einddatum_project'), \
                        'broncampagne', 'onenote_doc'),
        }),
    )

class OrderAdmin(admin.ModelAdmin):
    model = Verkoopkans
    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        return qs.filter(verkoopstadium__verkoopstadium__contains='Order')

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'klantpartner', 'verkoopstadium')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)
    list_filter = (('verkoopstadium', RelatedDropdownFilter),
                    ('klantpartner', RelatedDropdownFilter), 
                    ('bedrijf', RelatedDropdownFilter), 
                    ('opdrachtgever', RelatedDropdownFilter))
    search_fields = ('projectcode', 'bedrijf__bedrijfsnaam')

    fieldsets = (
        (None, {
           'fields': (('projectcode', 'omschrijving'), ('bedrijf', 'opdrachtgever'), ('verkoopstadium', 'klantpartner'), 'actief')
        }),
        ('Details', {
            'fields': (('geschatte_omzet', 'werkelijke_omzet'), ('startdatum_project', 'einddatum_project'), \
                        'broncampagne', 'onenote_doc'),
        }),
    )

# class OrderAdmin(admin.ModelAdmin):
#     model = Order

#     list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'orderstadium')
#     # list_display_links = ('volledige_naam', )
#     exclude = ('last_modified_user',)


class VerkoopstadiumAdmin(admin.ModelAdmin):
    model = Verkoopstadium

    list_display = ('verkoopstadium', 'verkoopkans')
    exclude = ('last_modified_user',)


admin.site.register(Verkoopkans, VerkoopkansAdmin)
admin.site.register(Orders, OrderAdmin)
# admin.site.register(Order, OrderAdmin)
admin.site.register(Verkoopstadium, VerkoopstadiumAdmin)
# admin.site.register(Orderstadium)