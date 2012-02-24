from koppelvlak6.models import Koppelvlak6
from django.contrib import admin

class Koppelvlak6Admin(admin.ModelAdmin):
    list_display = ('dataowner', 'sourceip', 'destinationport')

    fieldsets = [
        ('Toegangsgegevens', {'fields': ['sourceip', 'destinationport']}),
        ('Meta informatie', {'fields': ['dataowner']}),
    ]

admin.site.register(Koppelvlak6, Koppelvlak6Admin)

