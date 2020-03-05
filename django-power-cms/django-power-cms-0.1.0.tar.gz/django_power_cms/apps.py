from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class DjangoPowerCmsConfig(AppConfig):
    name = 'django_power_cms'
    verbose_name = _("Django Power CMS")

    def ready(self):
        from django.conf import settings
        if hasattr(settings, "ADMIN_REORDER"):
            for app_index in range(len(settings.ADMIN_REORDER)):
                app_setting = settings.ADMIN_REORDER[app_index]
                if isinstance(app_setting, str):
                    if app_setting != "django_power_cms":
                        continue
                    else:
                        app_setting = {"app": "django_power_cms"}
                        settings.ADMIN_REORDER[app_index] = app_setting
                else:
                    if app_setting["app"] != "django_power_cms":
                        continue
                app_setting["models"] =  [
                    {"model":  'django_power_cms.Site', "label": _("Site Manager")},
                    {"model": 'django_power_cms.Page', "label": _("Page Manager")},
                    {"model": 'django_power_cms.Widget', "label": _("Widget Manager")},
                    {"model": 'django_power_cms.Article', "label": _("Article Manager")},
                    {"model": 'django_power_cms.Template', "label": _("Template Manager")},
                    {"model": 'django_power_cms.Theme', "label": _("Theme Manager")},
                ]
