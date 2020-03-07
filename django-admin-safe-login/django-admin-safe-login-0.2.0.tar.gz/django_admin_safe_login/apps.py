from django.apps import AppConfig


class DjangoAdminSafeLoginConfig(AppConfig):
    name = 'django_admin_safe_login'

    def ready(self):
        self.replace_admin_login_form()
        self.reset_captcha_image_size()

    def reset_captcha_image_size(self):
        from django.conf import settings
        settings.CAPTCHA_IMAGE_SIZE = (100, 30)
    
    def replace_admin_login_form(self):
        from django.contrib import admin
        from django.conf import settings
        from .forms import AdminSafeAuthenticationForm

        ENABLE_LOGIN_CAPTCHA = getattr(settings, "ENABLE_LOGIN_CAPTCHA", None)
        if ENABLE_LOGIN_CAPTCHA is True or ENABLE_LOGIN_CAPTCHA is None:
            admin.site.login_form = AdminSafeAuthenticationForm
            admin.site.login_template = "django-admin-safe-login/login.html"
