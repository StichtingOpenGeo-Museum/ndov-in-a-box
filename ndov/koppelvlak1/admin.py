from koppelvlak1.models import Koppelvlak1, Concession
from django.contrib import admin

class ConcessionInline(admin.StackedInline):
    model = Concession

class Koppelvlak1Admin(admin.ModelAdmin):
    list_display = ('dataowner', 'valid_from_date', 'character_encoding')

    fieldsets = [
        ('Ingangsdatum', {'fields': ['valid_from_date']}),
        ('Bestand (ZIP)', {'fields': ['filename']}),
        ('Meta informatie', {'fields': ['dataowner', 'character_encoding', 'pub_date']}),
    ]

    inlines = [ConcessionInline]

admin.site.register(Koppelvlak1, Koppelvlak1Admin)

