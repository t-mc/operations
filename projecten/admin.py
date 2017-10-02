from django.contrib import admin
from django.db import models

# Register your models here.
from .models import Verkoopkans, Order, Verkoopstadium, Orderstadium


class VerkoopkansAdmin(admin.ModelAdmin):
    model = Verkoopkans

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'verkoopstadium')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)


class OrderAdmin(admin.ModelAdmin):
    model = Order

    list_display = ('projectcode', 'omschrijving', 'bedrijf', 'opdrachtgever', 'orderstadium')
    # list_display_links = ('volledige_naam', )
    exclude = ('last_modified_user',)


class VerkoopstadiumAdmin(admin.ModelAdmin):
    model = Verkoopstadium

    list_display = ('verkoopstadium', 'verkoopkans')
    exclude = ('last_modified_user',)


admin.site.register(Verkoopkans, VerkoopkansAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Verkoopstadium, VerkoopstadiumAdmin)
admin.site.register(Orderstadium)