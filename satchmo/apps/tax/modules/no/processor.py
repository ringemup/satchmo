from decimal import Decimal
from tax.modules.processor import BaseProcessor

class Processor(BaseProcessor):
    
    method="no"
    
    def by_product(self, product, quantity=Decimal('1')):
        return Decimal("0.0")
        
    def by_orderitem(self, orderitem):
        return Decimal("0.0")
                
    def by_price(self, taxclass, price):
        return Decimal("0.0")                
                
    def shipping(self, product, user):
        return Decimal("0.0")                
                
    def process(self, order=None):
        return Decimal("0.0"), {}

    def get_rate(self, *args, **kwargs):
        return Decimal("0")
        
