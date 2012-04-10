from koppelvlak1.models import Koppelvlak1, Concession
from django.contrib import admin

class ConcessionInline(admin.StackedInline):
    model = Concession

class Koppelvlak1Admin(admin.ModelAdmin):
    list_display = ('dataowner', 'valid_from_date', 'character_encoding')

    fieldsets = [
        ('Ingangsdatum', {'fields': ['valid_from_date']}),
        ('Bestand (ZIP)', {'fields': ['filename']}),
        # IMPORTANT! Note, don't ever change this without changing get_form below - it's hardcoded for now
        ('Meta informatie', {'fields': ['dataowner', 'character_encoding']}) 
    ]

    inlines = [ConcessionInline]
    
    def queryset(self, request):
        """Limit Pages to those that belong to the request's user."""
        qs = super(Koppelvlak1Admin, self).queryset(request)
        if request.user.is_superuser: 
            # It is mine, all mine. Just return everything.
            return qs
        # Now we just add an extra filter on the queryset
        return qs.filter(dataowner=request.user)
    
    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            if len(self.fieldsets) == 3 and len(self.fieldsets[2]) == 2 and 'fields' in self.fieldsets[2][1] and 'dataowner' in self.fieldsets[2][1]['fields']:  
                self.fieldsets[2][1]['fields'].remove('dataowner')
        return super(Koppelvlak1Admin, self).get_form(request, obj, **kwargs)
    
    def save_model(self, request, obj, form, change):
        '''Set the dataowner '''
        if not request.user.is_superuser:
            obj.dataowner = request.user
            obj.save()

admin.site.register(Koppelvlak1, Koppelvlak1Admin)

