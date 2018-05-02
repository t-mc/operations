from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
from notities.models import Notitie
# Register your models here.
from notities.forms import NotitieBedrijfForm, NotitieForm


class NotitieAdmin(admin.ModelAdmin):
    save_on_top = True
    form = NotitieForm
    exclude = ('last_modified_user',)
    readonly_fields = ('datumtijd',)
    list_display = ('onderwerp', 'bedrijf', 'contactpersoon', 'verkoopkans', 'datumtijd')
    search_fields = ('bedrijf__bedrijfsnaam', 'contactpersoon__volledige_naam', 'verkoopkans__projectcode', 'notitie', 'onderwerp')
    show_change_link = False
  
    list_filter = ( ('bedrijf', RelatedDropdownFilter), 
                    ('contactpersoon', RelatedDropdownFilter),                    
                    ('verkoopkans', RelatedDropdownFilter),
                    ('bedrijf', admin.RelatedOnlyFieldListFilter), 
                    ('contactpersoon', admin.RelatedOnlyFieldListFilter),
                    ('verkoopkans', admin.RelatedOnlyFieldListFilter),)

admin.site.register(Notitie, NotitieAdmin)
