try:
    from decimal import Decimal
except:
    from django.utils._decimal import Decimal

from django.core.exceptions import ObjectDoesNotExist
from tax.modules.area.processor import Processor as AreaProcessor
from livesettings import config_value

import logging

log = logging.getLogger('tax.local_product')

class Processor(AreaProcessor):
	
	method = "local_product"

	def by_product_and_price(self, taxclass, price, product=None):
		location = None
		if product:
			try:
				local_product = product.get_subtype_with_attr('location')
				if local_product:
					location = local_product.location
			except ObjectDoesNotExist:
				pass
			else:
				if location: 
					return price * self.get_rate(taxclass=taxclass, area=location.area, country=location.country)
		return self.by_price(taxclass, price)
		
	def by_orderitem(self, orderitem):
		if orderitem.product.taxable:
			price = orderitem.sub_total
			taxclass = orderitem.product.taxClass
			return self.by_product_and_price(taxclass, price, product=orderitem.product)
		else:
			return Decimal("0.00")

	def process(self, order=None):
		if order:
			self.order = order
		else:
			order = self.order		
		sub_total = Decimal('0.00')
		taxes = {}		
		rates = {}		
		# Calculate tax total
		for item in order.orderitem_set.filter(product__taxable=True):				
			price = item.sub_total
			t = self.by_orderitem(item)
			sub_total += t		
		# If appropriate, tax the shipping too
		if config_value('TAX','TAX_SHIPPING'):
			shipping = order.shipping_sub_total
			ship_tax = self.shipping(shipping)
			sub_total += ship_tax
			taxrates['Shipping'] = ship_tax		
		return sub_total, taxes
