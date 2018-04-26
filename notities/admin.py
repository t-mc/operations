from django.contrib import admin
from notities.models import Notitie
# Register your models here.
from notities.forms import NotitieBedrijfForm, NotitieForm


class NotitieAdmin(admin.ModelAdmin):
    save_on_top = True
    form = NotitieForm
    exclude = ('last_modified_user',)
    list_display = ('onderwerp', 'bedrijf', 'contactpersoon', 'verkoopkans', 'onderwerp', 'datumtijd')
    search_fields = ('bedrijf__bedrijfsnaam', 'contactpersoon__volledige_naam', 'verkoopkans__projectcode')
    show_change_link = False

    list_filter = ( ('bedrijf', admin.RelatedOnlyFieldListFilter), 
                    ('contactpersoon', admin.RelatedOnlyFieldListFilter),
                    ('verkoopkans', admin.RelatedOnlyFieldListFilter)
                    )

admin.site.register(Notitie, NotitieAdmin)