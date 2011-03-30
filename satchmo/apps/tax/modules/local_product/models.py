from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _
from product.models import Product
from l10n.models import AdminArea, Country

class Location(models.Model):
    name = models.CharField(max_length=50)
    admin_area = models.ForeignKey(AdminArea, blank=True, null=True)
    country = models.ForeignKey(Country, blank=True, null=True)
    
    @property
    def area(self):
        if self.admin_area:
            return self.admin_area
        return self.country
    
    def __unicode__(self):
        return self.name
    
    
class LocalProduct(Product):
    location = models.ForeignKey(Location)
    
    
import config