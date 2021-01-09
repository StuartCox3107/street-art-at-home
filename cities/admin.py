from django.contrib import admin
from .models import Citiesentry


class CitiesentryAdmin(admin.ModelAdmin):
    list_display = (
        'citiesid',
        'citiestitle',
    )

    ordering = ('citiesid',)


admin.site.register(Citiesentry, CitiesentryAdmin)
