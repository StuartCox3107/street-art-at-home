from django.contrib import admin
from .models import Citiesentry

# Register your models here.
class CitiesentryAdmin(admin.ModelAdmin):
    list_display = (
        'citiesid',
        'citiestitle',
    )

    ordering = ('citiesid',)
    
admin.site.register(Citiesentry, CitiesentryAdmin)
