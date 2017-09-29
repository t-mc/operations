from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html
from django.forms import BaseInlineFormSet

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

class ContactpersoonListAdmin(admin.TabularInline):
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

    readonly_fields = ('pk', 'volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    list_display = ('volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    list_display_links = ('volledige_naam', 'bedrijf')
    exclude = ('last_modified_user', 'initialen', 'voornaam', 'tussenvoegsel', 'achternaam', 'standplaats', 'afdeling', 'assistent', 'manager', 'overige_contactgegevens', 'sexe')

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


# class BedrijvenAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         models.CharField: {'widget': TextInput(attrs={'size':'40'})},
#         models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
#     }
#     inlines = [
#         ContactpersoonListAdmin,
#          VerkoopkansAdmin
#     ]
#     list_display = ('bedrijfsnaam', 'telefoonnummer', 'adres', 'onenote', 'klantpartner') 
#     exclude = ('last_modified_user', )

class ContactpersoonAdmin(admin.ModelAdmin):
    model = Contactpersoon

    list_display = ('volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)
    search_fields = ('volledige_naam', 'bedrijf__bedrijfsnaam')

class ContactpersoonInline(admin.TabularInline):
    model = Contactpersoon
    suit_classes = 'suit-tab suit-tab-contact'
    # list_display = ('volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    # readonly_fields = ('volledige_naam', 'telefoonnummer', 'mobielnummer', 'email', 'bedrijf', 'functie', 'actief')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user', 'standplaats', 'functie', 'afdeling', 'assistent', 'manager', 'overige_contactgegevens', 'actief', 'sexe',)


class BedrijvenAdmin(admin.ModelAdmin):
    inlines = [ContactpersoonListAdmin]
    list_display = ('bedrijfsnaam', 'telefoonnummer', 'adres', 'onenote', 'klantpartner')
    search_fields = ('bedrijfsnaam', )

    fieldsets = (
        (None, {
            'fields': ('bedrijfsnaam', 'klantpartner')
        }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('telefoonnummer', 'adres'),
        }),
    )

admin.site.register(Bedrijf, BedrijvenAdmin)    
admin.site.register(Adres)
# admin.site.register(Bedrijf)
admin.site.register(Branche)
admin.site.register(Contactpersoon, ContactpersoonAdmin)
