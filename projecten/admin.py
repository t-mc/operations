from django.contrib import admin
from django.contrib.admin import site
from django.db import models
from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter
import decimal

from projecten.forms import VerkoopkansForm, OmzetpermaandForm, UrenpermedewerkerForm, OrderregelForm

from .models import Verkoopkans, Omzetpermaand, Orders, Orderregel, Verkoopstadium, Trainingregistratie, Urenpermedewerker
from crm.models import Bedrijf, Contactpersoon
from notities.models import Notitie
from notities.forms import NotitieProjectForm, NotitieProjectFormSet
from producten.models import Product

# Register your models here.


class NotitieAdmin(admin.TabularInline):
    model = Notitie
    form = NotitieProjectForm
    formset = NotitieProjectFormSet
    exclude = ("last_modified_user",)
    readonly_fields = ("datumtijd",)
    extra = 0
    classes = ["collapse"]
    show_change_link = True


class OmzetpermaandAdmin(admin.TabularInline):
    model = Omzetpermaand
    form = OmzetpermaandForm
    exclude = ("last_modified_user",)
    extra = 0
    classes = ["collapse"]
    show_change_link = True


class UrenpermedewerkerInline(admin.TabularInline):
    model = Urenpermedewerker
    form = UrenpermedewerkerForm
    exclude = ("last_modified_user",)
    extra = 0
    classes = ["collapse"]
    show_change_link = True


class ProductenInline(admin.TabularInline):
    model = Product
    # form = UrenpermedewerkerForm
    exclude = ("last_modified_user",)
    extra = 0
    classes = ["collapse"]
    show_change_link = True


class OrderregelInline(admin.TabularInline):
    model = Orderregel
    form = OrderregelForm
    exclude = ("last_modified_user",)
    extra = 0
    classes = ["collapse"]
    show_change_link = True


class VerkoopkansAdmin(admin.ModelAdmin):
    save_on_top = True
    form = VerkoopkansForm
    inlines = [NotitieAdmin, OrderregelInline, UrenpermedewerkerInline, OmzetpermaandAdmin,]

    # search_fields = ['bedrijf']

    def get_queryset(self, request):
        qs = super(VerkoopkansAdmin, self).get_queryset(request)
        return qs.exclude(verkoopstadium__verkoopstadium__contains="Order")

    list_display = (
        "projectcode",
        "productgroep",
        "omschrijving",
        "totaal_omzet",
        "bedrijf",
        "opdrachtgever",
        "kwo_ontvanger",
        "klantpartner",
        "ordereigenaar",
        "verkoopstadium",
        "productgroep",
    )
    exclude = ("last_modified_user",)
    list_filter = (
        ("verkoopstadium", admin.RelatedOnlyFieldListFilter),
        ("klantpartner", admin.RelatedOnlyFieldListFilter),
        ("ordereigenaar", admin.RelatedOnlyFieldListFilter),
        ("productgroep", admin.RelatedOnlyFieldListFilter),
        ("bedrijf", RelatedDropdownFilter),
        ("opdrachtgever", RelatedDropdownFilter),
    )
    readonly_fields = ("totaal_omzet",)
    search_fields = ("projectcode", "bedrijf__bedrijfsnaam", "omschrijving")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("projectcode", "omschrijving", "productgroep"),
                    ("bedrijf", "opdrachtgever"),
                    "kwo_ontvanger",
                    "verkoopstadium",
                    "klantpartner",
                    "ordereigenaar",
                    "actief",
                )
            },
        ),
        (
            "Details",
            {
                "classes": ("collapse", "open"),
                "fields": (
                    ("einddatum_project", "totaal_omzet"),
                    ("startdatum_project", "geschatte_omzet"),
                ),
            },
        ),
    )

    def totaal_omzet(self, obj):
        return obj.totaal_omzet()


class OrderAdmin(admin.ModelAdmin):
    save_on_top = True
    form = VerkoopkansForm
    # model = Verkoopkans
    inlines = [
        NotitieAdmin,
        OrderregelInline,
        UrenpermedewerkerInline,
        OmzetpermaandAdmin,
    ]

    def get_queryset(self, request):
        qs = super(OrderAdmin, self).get_queryset(request)
        return qs.filter(verkoopstadium__verkoopstadium__contains="Order")

    list_display = (
        "projectcode",
        "productgroep",
        "omschrijving",
        "totaal_omzet",
        "bedrijf",
        "opdrachtgever",
        "kwo_ontvanger",
        "klantpartner",
        "ordereigenaar",
        "verkoopstadium",
        "productgroep",
    )
    exclude = ("last_modified_user",)
    list_filter = (
        ("verkoopstadium", admin.RelatedOnlyFieldListFilter),
        ("klantpartner", admin.RelatedOnlyFieldListFilter),
        ("ordereigenaar", admin.RelatedOnlyFieldListFilter),
        ("productgroep", admin.RelatedOnlyFieldListFilter),
        ("bedrijf", RelatedDropdownFilter),
        ("opdrachtgever", RelatedDropdownFilter),
    )
    readonly_fields = ("totaal_omzet",)
    search_fields = ("projectcode", "bedrijf__bedrijfsnaam", "omschrijving")

    fieldsets = (
        (
            None,
            {
                "fields": (
                    ("projectcode", "omschrijving", "productgroep"),
                    ("bedrijf", "opdrachtgever"),
                    "kwo_ontvanger",
                    "verkoopstadium",
                    "klantpartner",
                    "ordereigenaar",
                    "actief",
                )
            },
        ),
        (
            "Details",
            {
                "classes": ("collapse", "open"),
                "fields": (
                    ("einddatum_project", "totaal_omzet"),
                    ("startdatum_project", "geschatte_omzet"),
                ),
            },
        ),
    )

    def totaal_omzet(self, obj):
        return obj.totaal_omzet()


class VerkoopstadiumAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Verkoopstadium

    list_display = ("verkoopstadium", "verkoopkans")
    exclude = ("last_modified_user",)


class OmzetpermaandAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Omzetpermaand

    list_display = ("projectcode", "jaar", "maand", "omzet")
    exclude = ("last_modified_user",)

class OrderregelAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Orderregel

    list_display = ("projectcode", "product", "aantal_eenheden")
    exclude = ("last_modified_user",)


class TrainingregistratieAdmin(admin.ModelAdmin):
    save_on_top = True
    model = Trainingregistratie

    list_display = (
        "contactpersoon",
        "training",
        "order",
        "trainer",
        "bijzonderheden",
        "datum",
    )
    exclude = ("last_modified_user",)
    list_filter = (
        ("training", RelatedDropdownFilter),
        ("order", RelatedDropdownFilter),
        ("trainer", RelatedDropdownFilter),
    )


class UrenpermedewerkerAdmin(admin.ModelAdmin):
    model = Urenpermedewerker

    list_display = (
        "projectcode",
        "medewerker",
        "product",
        "jaar",
        "maand",
        "uren",
    )
    exclude = ("last_modified_user",)
    list_filter = (
        ("projectcode", admin.RelatedOnlyFieldListFilter),
        ("medewerker", admin.RelatedOnlyFieldListFilter),
        ("product", admin.RelatedOnlyFieldListFilter),
    )


admin.site.register(Verkoopkans, VerkoopkansAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Orderregel)
admin.site.register(Verkoopstadium, VerkoopstadiumAdmin)
admin.site.register(Omzetpermaand, OmzetpermaandAdmin)
admin.site.register(Trainingregistratie, TrainingregistratieAdmin)
admin.site.register(Urenpermedewerker, UrenpermedewerkerAdmin)

