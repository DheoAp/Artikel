from django.contrib import admin

# Register your models here.

from .models import ModelArtikel

class ArtikelAdmin(admin.ModelAdmin):
    readonly_fields = ['publish','update','slug']

admin.site.register(ModelArtikel,ArtikelAdmin)