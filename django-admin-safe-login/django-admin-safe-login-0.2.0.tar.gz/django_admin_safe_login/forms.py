from django.contrib.admin.forms import AdminAuthenticationForm
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField
from django_secure_password_input.fields import DjangoSecurePasswordInput

class AdminSafeAuthenticationForm(AdminAuthenticationForm):
    password = DjangoSecurePasswordInput()
    captcha = CaptchaField()
