try:
    from decimal import Decimal
except:
    from django.utils._decimal import Decimal

class BaseProcessor(object):
    method = None
    
    def __init__(self, order=None, user=None):
        """
        Any preprocessing steps should go here
        For instance, copying the shipping and billing areas
        """
        self.order = order
        self.user = user
        
    def get_percent(self, *args, **kwargs):
        return 100*self.get_rate(*args, **kwargs)
        
    def get_rate(self, *args, **kwargs):
        raise NotImplementedError() 

    def by_price(self, taxclass, price):
        raise NotImplementedError() 

    def by_product(self, product, quantity=Decimal('1')):
        raise NotImplementedError() 
        
    def by_product_and_price(self, taxclass, price, product=None):
        return self.by_price(taxclass, price)
        
    def by_orderitem(self, orderitem):
        raise NotImplementedError() 

    def shipping(self, subtotal=None):
        raise NotImplementedError() 

    def process(self, order=None):
        raise NotImplementedError() 
