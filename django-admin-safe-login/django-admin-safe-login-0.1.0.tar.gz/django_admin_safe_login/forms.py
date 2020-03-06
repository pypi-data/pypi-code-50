from django.contrib.admin.forms import AdminAuthenticationForm
from django.utils.translation import ugettext_lazy as _
from captcha.fields import CaptchaField

class AdminSafeAuthenticationForm(AdminAuthenticationForm):
    captcha = CaptchaField()
