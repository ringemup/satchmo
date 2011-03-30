from django.contrib import admin
from django.utils.translation import get_language, ugettext_lazy as _
from local_product.models import Location
from local_product.forms import LocationForm
        
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'admin_area', 'country',]
    list_filter = ['admin_area', 'country',]
    list_display_links = ['name',]
    form = LocationForm
    
admin.site.register(Location, LocationAdmin)

