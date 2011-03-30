from django.forms import models, ValidationError
from django.utils.translation import get_language, ugettext_lazy as _

class LocationForm(models.ModelForm):
    def clean(self):
        state_province = self.cleaned_data['state_province']
        country = self.cleaned_data['country']
        if state_province and not country or not state_province and country:
            return super(LocationForm, self).clean()
        else:
            raise ValidationError(_("You must choose a zone or a country."))