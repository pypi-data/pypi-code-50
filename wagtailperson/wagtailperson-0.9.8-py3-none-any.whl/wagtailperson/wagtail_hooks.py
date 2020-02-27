from django.utils.translation import gettext as _
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)

from .models import (
    Person,
)


class PersonModelAdmin(ModelAdmin):
    """Define the person model integration to the admin ui"""
    model = Person
    menu_label = _('Persons or authors')
    menu_icon = 'user'
    menu_order = 200
    list_display = ('name',)
    list_filter = ('tags',)
    search_field = ('name',)


modeladmin_register(PersonModelAdmin)
