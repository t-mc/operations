from django.contrib import admin
from django.db import models
from django.forms import Textarea, TextInput
from django.utils.html import format_html
from django_admin_listfilter_dropdown.filters import (DropdownFilter,
                                                      RelatedDropdownFilter)

from crm.models import Bedrijf, Contactpersoon

from .models import (Activiteiten, ActivityStatus, ActivityType, Cases,
                     CaseStatus, CaseType, Contract, Tijdsduur, UserProfile)

from .forms import CaseForm

class ActiviteitenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    exclude = ('last_modified_user',)
    list_display = ('case_id', 'activiteit', 'status', 'omschrijving', 'uitvoerende', 'datum_uitgevoerd')
    list_filter = ('status', ('case_id', RelatedDropdownFilter ))

class CaseActivities(admin.TabularInline):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    model = Activiteiten
    classes = ['collapse']
    extra = 0
    exclude = ('last_modified_user',)

class CasesAdmin(admin.ModelAdmin):
    form = CaseForm
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'80'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    fieldsets = [
        (None, {'fields': ['bedrijf', 'contact', 'onderwerp']}),
        ("Detail informatie", {'fields': ['contract', 'case_type', 'status', 'omschrijving', 'datum_melding', 'uitvoerende']})
    ]
    inlines = [
        CaseActivities
    ]
    list_display= ('case_code', 'case_type', 'onderwerp', 'datum_melding', 'status', 'bedrijf', 'contact', 'uitvoerende')
    list_filter = (('case_type', admin.RelatedOnlyFieldListFilter ), 
                    ('status', admin.RelatedOnlyFieldListFilter ), 
                    ('bedrijf', RelatedDropdownFilter ))

class ContractenAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }

    list_display = ('projectcode', 'startdatum', 'einddatum', 'klantpartner', 'contract_bij')  


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
admin.site.register(Cases, CasesAdmin)
admin.site.register(CaseStatus)
admin.site.register(CaseType)
admin.site.register(Contract, ContractenAdmin)
# admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Tijdsduur)
