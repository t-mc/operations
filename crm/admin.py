from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html
from django.forms import BaseInlineFormSet
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter

from .forms import ContactpersoonForm
from projecten.models import Verkoopkans, Orders, Trainingregistratie, Marketingregistratie
from notities.models import Notitie
from notities.forms import NotitieBedrijfForm, NotitieContactForm, NotitieContactFormSet

# Register your models here.
from .models import Adres, Bedrijf, Branche, Contactpersoon, Relatietype
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
    extra = 0

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium', 'geschatte_omzet', 'werkelijke_omzet', 'einddatum_project', 'broncampagne', 'klantpartner', 'actief')
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
    extra = 0
    fields = ('volledige_naam', 'initialen', ('voornaam', 'tussenvoegsel', 'achternaam'), 'sexe', \
                ('telefoonnummer', 'mobielnummer', 'email'), ('functie', 'afdeling'), ('assistent', 'manager' ), \
                ('overige_contactgegevens', 'actief', 'nieuwsbrief' ),
                'klantpartner')

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
    extra = 0
    verbose_name_plural = "Contactpersonen aanpassen"
    exclude = ('last_modified_user', )

class ContactNotitieAdmin(admin.TabularInline):
    model = Notitie
    form = NotitieContactForm
    formset = NotitieContactFormSet
    readonly_fields = ('datumtijd',)
    # exclude = ('last_modified_user',)
    extra = 0
    classes = ['collapse']
    show_change_link = True

class ContactTrainingsregistratieAdmin(admin.TabularInline):
    model = Trainingregistratie
    exclude = ('last_modified_user',)
    extra = 0
    classes = ['collapse']
    show_change_link = True

class MarketingregistratieAdmin(admin.TabularInline):
    model = Marketingregistratie
    exclude = ('last_modified_user',)
    extra = 0
    classes = ['collapse']
    show_change_link = True

class ContactpersoonAdmin(admin.ModelAdmin):
    save_on_top = True
    # model = Contactpersoon
    form = ContactpersoonForm
    inlines = [ContactNotitieAdmin, ContactTrainingsregistratieAdmin, MarketingregistratieAdmin]

    list_display = ('volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'klantpartner', 'actief')
    list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)
    search_fields = ('volledige_naam', 'bedrijf__bedrijfsnaam', 'klantpartner__username')
    list_filter = ('klantpartner', )

    fieldsets = (
        (None, {
            'fields': (('title', 'initialen', 'voornaam', 'tussenvoegsel', 'achternaam', 'sexe'), 
            ('volledige_naam', 'klantpartner'), 'telefoonnummer', 'mobielnummer', 'email')
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': (('bedrijf', 'standplaats'), ('functie', 'afdeling'), ('manager', 'assistent'), 
                        ('overige_contactgegevens'), ('nieuwsbrief' , 'actief')),
        }),
    ) 

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
    extra = 0
    classes = ['collapse']
    show_change_link = True
    fieldsets = [
        (None, {'fields': []}),
        ('Advanced settings', {
            'classes': ('collapse',), # Specify fieldset classes here
            'fields': ['bedrijf', 'adrestype', 'adresregel_1', 'adresregel_2', 'postcode', 'plaats', 'Land']}),
    ]

class BedrijfNotitieAdmin(admin.TabularInline):
    model = Notitie
    form = NotitieBedrijfForm
    # exclude = ('last_modified_user',)
    readonly_fields = ('datumtijd', )    
    extra = 0
    classes = ['collapse']
    show_change_link = True

    def save_model(self, request, obj, form, change):
        print(obj)
        obj.last_modified_user=request.user
        obj.save()

class AdresAdmin(admin.ModelAdmin):
    save_on_top = True
    exclude = ('last_modified_user',)
    list_display = ('bedrijf', 'adrestype', 'adresregel_1', 'adresregel_2', 'postcode', 'plaats', 'Land')
    search_fields = ('bedrijf__bedrijfsnaam', 'adresregel_1', 'plaats', 'postcode')
    show_change_link = True


class VerkoopkansInlineAdmin(admin.TabularInline):
    model = Verkoopkans
    def get_queryset(self, request):
        qs = super(VerkoopkansInlineAdmin, self).get_queryset(request)
        return qs.exclude(verkoopstadium__verkoopstadium__contains='Order')

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    readonly_fields = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user', 'onenote_doc')
    extra = 0
    classes = ['collapse']

class OrdersInlineAdmin(admin.TabularInline):
    model = Orders
    def get_queryset(self, request):
        qs = super(OrdersInlineAdmin, self).get_queryset(request)
        return qs.exclude(verkoopstadium__verkoopstadium__contains='Order')
    
    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    readonly_fields = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user', 'onenote_doc')
    extra = 0
    classes = ['collapse']

def apply_klant(modeladmin, request, queryset):
    relatietype = Relatietype.objects.get(relatietype = 'Klant')
    for bedrijf in queryset:
        bedrijf.relatietype = relatietype
        bedrijf.save()
apply_klant.short_description = 'Maak selectie klant'


def apply_leverancier(modeladmin, request, queryset):
    relatietype = Relatietype.objects.get(relatietype = 'Leverancier')
    for bedrijf in queryset:
        bedrijf.relatietype = relatietype
        bedrijf.save()
apply_leverancier.short_description = 'Maak selectie leverancier'


class BedrijvenAdmin(admin.ModelAdmin):
    save_on_top = True
    # inlines = [BedrijfAdresAdmin, ContactpersoonListAdmin, OrdersInlineAdmin, VerkoopkansInlineAdmin]
    inlines = [BedrijfNotitieAdmin, BedrijfAdresAdmin, ContactpersoonListAdmin]
    list_display = ('bedrijfsnaam', 'telefoonnummer', 'klantpartner', 'relatietype')
    actions = [apply_klant, apply_leverancier,]

    fieldsets = (
        (None, {
            'fields': (('bedrijfsnaam', 'telefoonnummer', 'relatietype'), ('klantpartner'))
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': (('email', 'website'), ('kvk_nummer', 'branche'), 'actief'),
        }),
    ) 

    search_fields = ('bedrijfsnaam',)
    list_filter = (('klantpartner', admin.RelatedOnlyFieldListFilter), 
                    ('relatietype', admin.RelatedOnlyFieldListFilter), 
                    'actief',
                    )

    def save_model(self, request, obj, form, change):
        # obj.last_modified_user=request.user

        obj.save()                    

admin.site.register(Bedrijf, BedrijvenAdmin)    
admin.site.register(Adres, AdresAdmin)
admin.site.register(Branche)
admin.site.register(Relatietype)
admin.site.register(Contactpersoon, ContactpersoonAdmin)
