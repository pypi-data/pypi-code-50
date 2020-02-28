
from django.utils.translation import ugettext_lazy as _

from cap.decorators import short_description
from exchange.utils import update_prices


@short_description(_('Recalculate prices'))
def recalculate_prices(modeladmin, request, queryset):
    update_prices(queryset)
