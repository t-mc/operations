from django.contrib import admin
from django.db import models
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from projecten.forms import VerkoopkansForm, OmzetpermaandForm

from .models import Verkoopkans, Omzetpermaand, Orders, Verkoopstadium
from crm.models import Bedrijf, Contactpersoon
from notities.models import Notitie
from notities.forms import NotitieProjectForm, NotitieProjectFormSet

# Register your models here.

class NotitieAdmin(admin.TabularInline):
    model = Notitie
    form = NotitieProjectForm
    formset = NotitieProjectFormSet
    exclude = ('last_modified_user',)
    readonly_fields = ('datumtijd',)
    extra = 1
    classes = ['collapse']
    show_change_link = True

class OmzetpermaandAdmin(admin.TabularInline):
    model = Omzetpermaand
    form = OmzetpermaandForm
    exclude = ('last_modified_user',)
    extra = 1
    classes = ['collapse']
    show_change_link = True

class VerkoopkansAdmin(admin.ModelAdmin):
    save_on_top = True
    form = VerkoopkansForm
    inlines = [ NotitieAdmin, OmzetpermaandAdmin]

    def get_queryset(self, request):
        qs = super(VerkoopkansAdmin, self).get_queryset(request)
        return qs.exclude(verkoopstadium__verkoopstadium__contains='Order')

    list_display = ('projectcode', 'omschrijving', 'totaal_omzet', 'bedrijf', 'opdrachtgever', 'kwo_ontvanger', 'klantpartner', 'ordereigenaar', 'verkoopstadium', 'productgroep')
    exclude = ('last_modified_user',)
    list_filter = (('verkoopstadium', admin.RelatedOnlyFieldListFilter),
                    ('klantpartner', admin.RelatedOnlyFieldListFilter), 
                    ('ordereigenaar', admin.RelatedOnlyFieldListFilter), 
                    ('bedrijf', RelatedDropdownFilter), 
                    ('opdrachtgever', RelatedDropdownFilter),                    
                    ('productgroep', RelatedDropdownFilter))                    
    readonly_fields = ('totaal_omzet',)
    search_fields = ('projectcode', 'bedrijf__bedrijfsnaam', 'omschrijving')

    fieldsets = (
        (None, {
           'fields': (('projectcode', 'omschrijving', 'productgroep'), ('bedrijf', 'opdrachtgever', 'kwo_ontvanger'), ('verkoopstadium', 'klantpartner', 'ordereigenaar'), 'actief')
        }),
        ('Details', {
            'fields': (('startdatum_project', 'einddatum_project'), ('geschatte_omzet', 'werkelijke_omzet', 'totaal_omzet'),('onenote_doc'))
        }),
    )

    def totaal_omzet(self, obj):
        return '€ %s' % obj.totaal_omzet()

class OrderAdmin(admin.ModelAdmin):
    save_on_top = True
    form = VerkoopkansForm
    # model = Verkoopkans
    inlines = [NotitieAdmin, OmzetpermaandAdmin]
    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        return qs.filter(verkoopstadium__verkoopstadium__contains='Order')

    list_display = ('projectcode', 'omschrijving', 'totaal_omzet', 'bedrijf', 'opdrachtgever', 'kwo_ontvanger', 'klantpartner', 'ordereigenaar', 'verkoopstadium')
    exclude = ('last_modified_user',)
    list_filter = (('verkoopstadium', admin.RelatedOnlyFieldListFilter),
                    ('klantpartner', admin.RelatedOnlyFieldListFilter), 
                    ('ordereigenaar', admin.RelatedOnlyFieldListFilter), 
                    ('bedrijf', RelatedDropdownFilter), 
                    ('opdrachtgever', RelatedDropdownFilter))                    
    readonly_fields = ('totaal_omzet',)
    search_fields = ('projectcode', 'bedrijf__bedrijfsnaam', 'omschrijving')

    fieldsets = (
        (None, {
           'fields': (('projectcode', 'omschrijving', 'productgroep'), ('bedrijf', 'opdrachtgever', 'kwo_ontvanger',), ('verkoopstadium', 'klantpartner', 'ordereigenaar'), 'actief')
        }),
        ('Details', {
            'fields': (('startdatum_project', 'einddatum_project'), ('geschatte_omzet', 'werkelijke_omzet', 'totaal_omzet'),('onenote_doc')),
        }),
    )

    def totaal_omzet(self, obj):
        return '€ %s' % obj.totaal_omzet()


class VerkoopstadiumAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Verkoopstadium

    list_display = ('verkoopstadium', 'verkoopkans')
    exclude = ('last_modified_user',)

class OmzetpermaandAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Omzetpermaand

    list_display = ('projectcode', 'jaar', 'maand', 'omzet')
    exclude = ('last_modified_user',)


admin.site.register(Verkoopkans, VerkoopkansAdmin)
admin.site.register(Orders, OrderAdmin)
# admin.site.register(Order, OrderAdmin)
admin.site.register(Verkoopstadium, VerkoopstadiumAdmin)
admin.site.register(Omzetpermaand, OmzetpermaandAdmin)
# admin.site.register(Orderstadium)