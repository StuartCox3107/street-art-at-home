from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'city',
        'price_s',
        'price_m',
        'price_l',
        'image',
    )

    ordering = ('sku',)


admin.site.register(Product, ProductAdmin)
