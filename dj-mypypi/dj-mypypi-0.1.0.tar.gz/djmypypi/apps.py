# -*- coding: utf-8
"Application config"

from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class DjMyPypiConfig(AppConfig):
    "Application config"
    name = 'djmypypi'
    
    verbose_name = _("Python package index")
