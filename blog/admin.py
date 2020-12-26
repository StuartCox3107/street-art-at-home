from django.contrib import admin
from .models import Blogentry

# Register your models here.
class BlogentryAdmin(admin.ModelAdmin):
    list_display = (
        'blogid',
        'blogtitle',
    )

    ordering = ('blogid',)
    
admin.site.register(Blogentry, BlogentryAdmin)