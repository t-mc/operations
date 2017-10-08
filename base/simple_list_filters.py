from django.contrib.admin import SimpleListFilter

# admin.py
class BedrijfFilter(SimpleListFilter):
    title = 'bedrijf' # or use _('country') for translated title
    parameter_name = 'bedrijf'

    def lookups(self, request, model_admin):
        bedrijven = set([c.bedrijf for c in model_admin.model.objects.all()])
        return [(c.id, c.bedrijfsnaam) for c in bedrijven]
        # You can also use hardcoded model name like "Country" instead of 
        # "model_admin.model" if this is not direct foreign key filter

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(bedrijf__id__exact=self.value())
        else:
            return queryset