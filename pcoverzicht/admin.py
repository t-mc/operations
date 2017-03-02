from django.contrib import admin

# Register your models here.
from .models import Computer, Software

admin.site.register(Computer)
admin.site.register(Software)
