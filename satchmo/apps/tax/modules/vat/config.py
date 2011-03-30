from django.utils.translation import ugettext_lazy as _
from livesettings import *
from tax.config import TAX_MODULE

TAX_MODULE.add_choice(('tax.modules.vat', _('Value Added Tax')))  # VAT Europe
TAX_GROUP = config_get_group('TAX')

config_register(
    DecimalValue(TAX_GROUP,
        'PERCENT',
        description=_("Value Added Tax percent"),          # Normal tax
        requires=TAX_MODULE,
        requiresvalue='tax.modules.vat')
)

config_register(
    DecimalValue(TAX_GROUP,
        'REDUCEDVAT',
        description=_("Reduced Value Added Tax percent"),  # Basic food
        requires=TAX_MODULE,
        requiresvalue='tax.modules.vat')
)

config_register(
    BooleanValue(TAX_GROUP,
        'TAX_SHIPPING',
        description=_("Tax Shipping?"),
        requires=TAX_MODULE,
        requiresvalue='tax.modules.vat',
        default=False)
)

config_register(
     StringValue(TAX_GROUP,
         'TAX_CLASS',
         description=_("TaxClass for shipping"),
         help_text=_("Select a TaxClass that should be applied for shipments."),
         #TODO: [BJK] make this dynamic - doesn't work to have it be preloaded.
         default='Shipping'
     )
)

