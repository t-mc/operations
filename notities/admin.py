from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from notities.models import Notitie, NotitieType
# Register your models here.
from notities.forms import NotitieBedrijfForm, NotitieForm


class NotitieAdmin(admin.ModelAdmin):
    save_on_top = True
    form = NotitieForm
    # exclude = ('last_modified_user',)
    readonly_fields = ('datumtijd', 'last_modified_user')
    list_display = ('onderwerp', 'bedrijf', 'contactpersoon', 'verkoopkans', 'last_modified_user', 'datumtijd')
    search_fields = ('bedrijf__bedrijfsnaam', 'contactpersoon__volledige_naam', 'verkoopkans__projectcode', 'notitie', 'notitietype', 'onderwerp')
    show_change_link = False
  
    list_filter = ( ('bedrijf', RelatedDropdownFilter), 
                    ('contactpersoon', RelatedDropdownFilter),                    
                    ('verkoopkans', RelatedDropdownFilter),)
                    # ('bedrijf', admin.RelatedOnlyFieldListFilter), 
                    # ('contactpersoon', admin.RelatedOnlyFieldListFilter),
                    # ('verkoopkans', admin.RelatedOnlyFieldListFilter),)

    def save_model(self, request, obj, form, change):
        obj.last_modified_user=request.user
        obj.save()

admin.site.register(Notitie, NotitieAdmin)
admin.site.register(NotitieType)
