from django.contrib import admin
from producten.models import Productgroep, Product, Training, Marketinguiting

# Register your models here.


class ProductgroepAdmin(admin.ModelAdmin):
    save_on_top = True
    exclude = ("last_modified_user",)
    list_display = ("productcode", "omschrijving", "productowner", "leverancier")
    # search_fields = ('bedrijf__bedrijfsnaam', 'contactpersoon__volledige_naam', 'verkoopkans__projectcode')
    show_change_link = True

    list_filter = (
        ("productowner", admin.RelatedOnlyFieldListFilter),
        ("leverancier", admin.RelatedOnlyFieldListFilter),
    )


class ProductAdmin(admin.ModelAdmin):
    exclude = ("last_modified_user",)
    list_display = (
        "code",
        "omschrijving",
        "productgroep",
        "eenheid",
        "prijs_per_eenheid",
    )
    show_change_link = True
    search_fields = ["prijs_per_eenheid"]

    list_filter = ("productgroep",)


class MarketinguitingAdmin(admin.ModelAdmin):
    exclude = ("last_modified_user",)
    list_display = ("omschrijving",)
    show_change_link = True
    search_fields = ["omschrijving"]


admin.site.register(Product, ProductAdmin)
admin.site.register(Productgroep, ProductgroepAdmin)
admin.site.register(Training)
admin.site.register(Marketinguiting, MarketinguitingAdmin)
