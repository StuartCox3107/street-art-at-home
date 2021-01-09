from django.contrib import admin
from .models import Blogentry


class BlogentryAdmin(admin.ModelAdmin):
    list_display = (
        'blogid',
        'blogtitle',
    )

    ordering = ('blogid',)


admin.site.register(Blogentry, BlogentryAdmin)
