from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html
from django.forms import BaseInlineFormSet
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from .forms import MyCrispyForm
from projecten.models import Verkoopkans, Orders

# Register your models here.
from .models import Adres, Bedrijf, Branche, Contactpersoon
from projecten.models import Verkoopkans, Order

class MyInline(BaseInlineFormSet): 
    def __init__(self, *args, **kwargs): 
        super(MyInline, self).__init__(*args, **kwargs) 
        self.can_delete = False 

class VerkoopkansAdmin(admin.StackedInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }    
    model = Verkoopkans
    classes = ['collapse']
    extra = 1

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium', 'geschatte_omzet', 'werkelijke_omzet', 'einddatum_project', 'broncampagne', 'onenote_doc', 'klantpartner', 'actief')
    exclude = ('last_modified_user', )

class ContactpersoonListAdmin(admin.StackedInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    model = Contactpersoon
    formset = MyInline 
    classes = ['collapse']
    verbose_name_plural = "Contactpersonen overzicht"
    # can_delete = False
    extra = 1
    fields = ('volledige_naam', 'initialen', ('voornaam', 'tussenvoegsel', 'achternaam'), 'sexe', \
                ('telefoonnummer', 'mobielnummer', 'email'), ('functie', 'afdeling'), ('assistent', 'manager' ), \
                ('actief', 'overige_contactgegevens'))

    list_display = ('volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    list_display_links = ('volledige_naam', 'bedrijf')
    exclude = ('last_modified_user',)

class ContactpersoonAddAdmin(admin.StackedInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'40'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    model = Contactpersoon
    classes = ['collapse']
    extra = 1
    verbose_name_plural = "Contactpersonen aanpassen"
    exclude = ('last_modified_user', )

class ContactpersoonAdmin(admin.ModelAdmin):
    model = Contactpersoon

    list_display = ('volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)
    search_fields = ('volledige_naam', 'bedrijf__bedrijfsnaam')

class ContactpersoonInline(admin.TabularInline):
    model = Contactpersoon
    list_display = ('volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    # list_display_links = ('volledige_naam', )
    list_display_links = ('volledige_naam', 'bedrijf')
    exclude = ('last_modified_user', 'initialen', 'voornaam', 'tussenvoegsel', 'achternaam', 'standplaats', 'afdeling', 'assistent', 'manager', 'overige_contactgegevens', 'sexe')
    readonly_fields = ('pk', 'volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    extra = 1
    classes = ['collapse']


class BedrijfAdresAdmin(admin.TabularInline):
    model = Adres
    exclude = ('last_modified_user',)
    extra = 1
    classes = ['collapse']


class AdresAdmin(admin.ModelAdmin):
    exclude = ('last_modified_user',)
    list_display = ('bedrijf', 'adrestype', 'adresregel_1', 'adresregel_2', 'postcode', 'plaats', 'Land')
    search_fields = ('bedrijf__bedrijfsnaam', 'adresregel_1', 'plaats', 'postcode')

class VerkoopkansInlineAdmin(admin.TabularInline):
    model = Verkoopkans
    def get_queryset(self, request):
        qs = super(VerkoopkansInlineAdmin, self).get_queryset(request)
        return qs.exclude(verkoopstadium__verkoopstadium__contains='Order')

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    readonly_fields = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)
    extra = 1
    classes = ['collapse']

class OrdersInlineAdmin(admin.TabularInline):
    model = Orders
    def get_queryset(self, request):
        qs = super(OrdersInlineAdmin, self).get_queryset(request)
        return qs.exclude(verkoopstadium__verkoopstadium__contains='Order')
    
    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    readonly_fields = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)
    extra = 1
    classes = ['collapse']


class BedrijvenAdmin(admin.ModelAdmin):
    inlines = [BedrijfAdresAdmin, ContactpersoonListAdmin, OrdersInlineAdmin, VerkoopkansInlineAdmin]
    list_display = ('bedrijfsnaam', 'telefoonnummer', 'klantpartner')
    fieldsets = (
        (None, {
            'fields': (('bedrijfsnaam', 'telefoonnummer'), ('klantpartner', 'onenote'))
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': (('email', 'website'), ('kvk_nummer', 'branche'), 'actief'),
        }),
    ) 

    search_fields = ('bedrijfsnaam',)
    list_filter = (('klantpartner', RelatedDropdownFilter), 
                    'actief',
                    )


admin.site.register(Bedrijf, BedrijvenAdmin)    
admin.site.register(Adres, AdresAdmin)
admin.site.register(Branche)
admin.site.register(Contactpersoon, ContactpersoonAdmin)
