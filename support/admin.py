from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models

from .models import Activiteiten, ActivityStatus, ActivityType, Bedrijf,\
                    Cases, CaseStatus, CaseType, Contactpersoon, Contract, \
                    Leverancier, SLA, UserProfile

class ActiviteitenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('caseId', 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datumUitgevoerd')

class BedrijvenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('bedrijfsnaam', 'telefoonnummer', 'primair_contact', 'klantpartner', 'emailadres')    

class CaseActivities(admin.TabularInline):
    model = Activiteiten
    extra = 1

class CasesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['klant', 'contactpersoon', 'onderwerp']}),
        ("Detail informatie", {'fields': ['status', 'omschrijving', 'datumMelding', 'uitvoerende']})
    ]
    inlines = [
        CaseActivities
    ]
    list_display= ('slug', 'onderwerp', 'omschrijving', 'datumMelding', 'status', 'klant', 'contactpersoon', 'uitvoerende')
    list_filter = ('status', 'klant')

class ContactpersonenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('contactnaam', 'telefoonnummer', 'functie', 'mobielnummer', 'emailadres', 'bedrijf')  

class ContractenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('projectcode', 'startdatum', 'einddatum', 'klantpartner', 'contract_bij')  

class LeveranciersAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('leveranciernaam', 'telefoonnummer', 'emailadres', 'klantpartner')  

class SLAAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('leverancier', 'omschrijving', 'classificatie', 'bevestiging', 'oplossingsplan', 'workaround', 'oplossing') 


class UserProfileAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('user', 'website', 'picture') 
#
# Register your models here.
#
admin.site.register(Activiteiten, ActiviteitenAdmin)
admin.site.register(ActivityStatus)
admin.site.register(ActivityType)
admin.site.register(Bedrijf, BedrijvenAdmin)
admin.site.register(Cases, CasesAdmin)
admin.site.register(CaseStatus)
admin.site.register(CaseType)
admin.site.register(Contactpersoon, ContactpersonenAdmin)
admin.site.register(Contract, ContractenAdmin)
admin.site.register(Leverancier, LeveranciersAdmin)
admin.site.register(SLA, SLAAdmin)
admin.site.register(UserProfile, UserProfileAdmin)






