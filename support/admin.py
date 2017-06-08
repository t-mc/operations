from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea
from django.utils.html import format_html

from .models import Activiteiten, ActivityStatus, ActivityType, Bedrijf,\
                    Cases, CaseStatus, CaseType, Contactpersoon, Contract, \
                    Leverancier, SLA, UserProfile, Tijdsduur

class ActiviteitenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('case_id', 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datum_uitgevoerd')

class BedrijfContacten(admin.TabularInline):
    model = Contactpersoon
    classes = ['collapse']
    extra = 1

class BedrijfContracten(admin.TabularInline):
    model = Contract
    classes = ['collapse']
    extra = 1

class BedrijvenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    inlines = [
        BedrijfContracten,
        BedrijfContacten
    ]
    list_display = ('bedrijfsnaam', 'telefoon', 'telefoonnummer', 'primair_contact', 'klantpartner', 'emailadres')    

class CaseActivities(admin.TabularInline):
    model = Activiteiten
    classes = ['collapse']
    extra = 1

class CasesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['bedrijf', 'contact', 'onderwerp', 'contract']}),
        ("Detail informatie", {'fields': ['case_code', 'status', 'omschrijving', 'datum_melding', 'uitvoerende']})
    ]
    inlines = [
        CaseActivities
    ]
    list_display= ('onderwerp', 'omschrijving', 'datum_melding', 'status', 'bedrijf', 'contact', 'uitvoerende')
    list_filter = ('status', 'bedrijf')

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

class LeverancierContract(admin.TabularInline):
    model = Contract
    classes = ['collapse']
    extra = 1

class LeverancierSLA(admin.TabularInline):
    model = SLA
    classes = ['collapse']
    extra = 1

class LeveranciersAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    inlines = [
        LeverancierContract,
        LeverancierSLA
    ]
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
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        image_field = getattr(obj, 'picture', '')
        print(image_field.url)
        return format_html(u'<img src="/static/{}" width="200" height="200" />', image_field.url)

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
admin.site.register(Tijdsduur)






