try:
    from decimal import Decimal
except:
    from django.utils._decimal import Decimal


class BaseProcessor(object):
    """
    Base Tax Processor

    Individual tax processors are descendants of this class.

    The most important attributes implemented by every tax processor are:
        method       name of the subdirectory in tax/models, where the tax processor is
        by_price     get tax for the given taxclass and price
        process      get tax for the given order

    Tax processor is created new for every order/user and get details about them, when initialized. 
    """

    method = None   # string: Should be the name of subdirectory in tax/models, where processor is.
    
    def __init__(self, order=None, user=None, **kwargs):
        """
        Tax processor instance is usually created by methods, which have information about request context
        (consequently user and/or order)

        Any preprocessing steps should go here
        For instance, copying the shipping and billing areas
        Usually is the tax area/country recognized from order.billaddress or user.contact or default
        """
        self.order = order
        self.user = user
        
    def by_price(self, taxclass, price):
        """
        Tax calculated by tax class, price and information stored in taxprocessor instance.

        The most common basic method used for other methods, which should be defined by usual processors
        and is used by other methods.
        """
        # Descentant should implement it
        # If is implemented by_product_and_price,
        # this can be     return self.by_product_and_price(taxclass, price)
        raise NotImplementedError()

    def by_product_and_price(self, taxclass, price, product=None):
        """
        Tax calculated by a generalized method
        This must be for tax processors where tax depends on any product attribute
        (e.g. product area/country for tourism etc.)
        Used by 
        """
        return self.by_price(taxclass, price)
        
    def get_rate(self, taxclass=None, *args, **kwargs):
        """
        Tax / price
        Postional parameters should be added in this order, if implemented:
            taxclass=None, area=None, country=None, get_object=False, **kwargs
        Recommendation: Shold be called only with tax_class shold be used as 
        """
        return self.by_price(taxclass, Decimal('1.00')) / Decimal('1.00')

    def get_percent(self, *args, **kwargs):
        "Tax / price * 100"
        return 100 * self.get_rate(*args, **kwargs)
        
    def by_product(self, product, quantity=Decimal('1')):
        """
        Tax for the discounted price of a given product
        deprecated
        """
        raise NotImplementedError() 
        
    def by_orderitem(self, orderitem):
        """
        Tax for the given order item
        """
        if orderitem.product.taxable:
            price = orderitem.sub_total
            taxclass = orderitem.product.taxClass
            return self.by_price(taxclass, price)
        else:
            return Decimal("0.00")

    def shipping(self, subtotal=None):
        """
        Shipping Tax for the order
        deprecated: probably not used in standard Satchmo, replaced by shop.models.Order.shipping_tax
        """
        raise NotImplementedError() 

    def process(self, order=None):
        """
        Get tax subtotal and overview of taxes by taxclass
        example:
            (Decimal('30.00'), {'10%': Decimal('20.00'), 'Shipping': Decimal('10.00')})
            Is used by "Order.force_recalculate_total(..)" and many times in "payment".
        """
        raise NotImplementedError()
