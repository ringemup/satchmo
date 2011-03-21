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
        """
        Return the tax rate as a percent value (a Decimal between 0 and 100)
        """
        return 100*self.get_rate(*args, **kwargs)
        
    def get_rate(self, *args, **kwargs):
        """
        Return the tax rate as a rate value (a Decimal between 0 and 1)
        """
        raise NotImplementedError() 

    def by_price(self, taxclass, price):
        """
        Calculate tax given a price and tax class
        """
        raise NotImplementedError() 

    def by_product(self, product, quantity=Decimal('1')):
        """
        Calculate tax given a product and quantity
        """
        raise NotImplementedError() 
        
    def by_product_and_price(self, taxclass, price, product=None):
        """
        Calculate tax given a price, tax class, and possibly product.
        """
        return self.by_price(taxclass, price)
        
    def by_orderitem(self, orderitem):
        """
        Calculate tax given a line item from an order
        """
        raise NotImplementedError() 

    def shipping(self, *args, **kwargs):
        """
        Calculate the tax on shipping
        """
        raise NotImplementedError() 

    def process(self, order=None):
        """
        Calculate the tax for an entire order
        """
        raise NotImplementedError() 
