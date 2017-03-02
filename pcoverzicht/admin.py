from django.contrib import admin
from django.db import models
from django.forms import TextInput, Textarea

# Register your models here.
from .models import Computer, Software

class ComputerSoftware(admin.TabularInline):
    model = Software
    classes = ['collapse']
    extra = 1

class ComputerAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':80})},
    }
    inlines = [
        ComputerSoftware
    ]
    fieldsets = (
        (None, {
            'fields': ('naam', 'gebruiker')
            }),
        ('Details', {
            'classes': ('collapse',),
            'fields': ('merkentype', 'kenmerken', 'aanschafdatum', 'serienummer')
            }),
        )

    list_display = ('naam', 'gebruiker', 'merkentype', 'kenmerken', 'aanschafdatum', 'serienummer')   

admin.site.register(Computer, ComputerAdmin)
admin.site.register(Software)
