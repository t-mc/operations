from django.contrib import admin
from django.db import models
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from projecten.forms import VerkoopkansForm

from .models import Verkoopkans, Orders, Verkoopstadium
from crm.models import Contactpersoon
from notities.models import Notitie

# Register your models here.

class NotitieAdmin(admin.TabularInline):
    model = Notitie
    exclude = ('last_modified_user', 'datumtijd')
    extra = 1
    classes = ['collapse']
    show_change_link = True

class VerkoopkansAdmin(admin.ModelAdmin):
    form = VerkoopkansForm
    inlines = [NotitieAdmin]
    def get_queryset(self, request):
        qs = super(VerkoopkansAdmin, self).get_queryset(request)
        return qs.exclude(verkoopstadium__verkoopstadium__contains='Order')

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'klantpartner', 'ordereigenaar', 'verkoopstadium', 'productgroep')
    exclude = ('last_modified_user',)
    list_filter = (('verkoopstadium', admin.RelatedOnlyFieldListFilter),
                    ('klantpartner', admin.RelatedOnlyFieldListFilter), 
                    ('ordereigenaar', admin.RelatedOnlyFieldListFilter), 
                    ('bedrijf', RelatedDropdownFilter), 
                    ('opdrachtgever', RelatedDropdownFilter),                    
                    ('productgroep', RelatedDropdownFilter))                    
    search_fields = ('projectcode', 'bedrijf__bedrijfsnaam', 'omschrijving')

    fieldsets = (
        (None, {
           'fields': (('projectcode', 'omschrijving', 'productgroep'), ('bedrijf', 'opdrachtgever'), ('verkoopstadium', 'klantpartner', 'ordereigenaar'), 'actief')
        }),
        ('Details', {
            'fields': ('startdatum_project', 'einddatum_project','onenote_doc'),
        }),
    )

class OrderAdmin(admin.ModelAdmin):
    model = Verkoopkans
    inlines = [NotitieAdmin]
    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        return qs.filter(verkoopstadium__verkoopstadium__contains='Order')

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'klantpartner', 'ordereigenaar', 'verkoopstadium')
    exclude = ('last_modified_user',)
    list_filter = (('verkoopstadium', admin.RelatedOnlyFieldListFilter),
                    ('klantpartner', admin.RelatedOnlyFieldListFilter), 
                    ('ordereigenaar', admin.RelatedOnlyFieldListFilter), 
                    ('bedrijf', RelatedDropdownFilter), 
                    ('opdrachtgever', RelatedDropdownFilter))                    
    search_fields = ('projectcode', 'bedrijf__bedrijfsnaam', 'omschrijving')

    fieldsets = (
        (None, {
           'fields': (('projectcode', 'omschrijving', 'productgroep'), ('bedrijf', 'opdrachtgever'), ('verkoopstadium', 'klantpartner', 'ordereigenaar'), 'actief')
        }),
        ('Details', {
            'fields': (('startdatum_project', 'einddatum_project'), 'onenote_doc'),
        }),
    )

class VerkoopstadiumAdmin(admin.ModelAdmin):
    model = Verkoopstadium

    list_display = ('verkoopstadium', 'verkoopkans')
    exclude = ('last_modified_user',)


admin.site.register(Verkoopkans, VerkoopkansAdmin)
admin.site.register(Orders, OrderAdmin)
# admin.site.register(Order, OrderAdmin)
admin.site.register(Verkoopstadium, VerkoopstadiumAdmin)
# admin.site.register(Orderstadium)