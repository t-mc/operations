from django.contrib import admin
from producten.models import Productgroep
# Register your models here.

class ProductgroepAdmin(admin.ModelAdmin):
    save_on_top = True
    exclude = ('last_modified_user',)
    list_display = ('productcode', 'omschrijving', 'productowner', 'leverancier')
    # search_fields = ('bedrijf__bedrijfsnaam', 'contactpersoon__volledige_naam', 'verkoopkans__projectcode')
    show_change_link = True

    list_filter = (('productowner', admin.RelatedOnlyFieldListFilter), 
                    ('leverancier', admin.RelatedOnlyFieldListFilter),
                    )

admin.site.register(Productgroep, ProductgroepAdmin)
