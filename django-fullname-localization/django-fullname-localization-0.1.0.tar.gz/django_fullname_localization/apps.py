from django.apps import AppConfig


class DjangoFullnameLocalizationConfig(AppConfig):
    name = 'django_fullname_localization'

    def ready(self):
        from django.contrib.auth.models import AbstractUser

        def get_full_name(self):
            """
            Add localization support for user's fullname.
            """
            from django.conf import settings
            full_name_template = getattr(settings, "FULL_NAME_TEMPLATE", "{user.last_name}{user.first_name}")
            full_name = full_name_template.format(user=self, first_name=self.first_name, last_name=self.last_name)
            return full_name.strip()
        
        AbstractUser.get_full_name = get_full_name
