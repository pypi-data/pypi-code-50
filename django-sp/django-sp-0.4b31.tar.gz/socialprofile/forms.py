"""Django forms for the socialprofile application"""
from django import forms
from django.utils.html import strip_tags
from .models import SocialProfile
import logging

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# from django.conf import settings
# from django.core.exceptions import ObjectDoesNotExist
# from django.utils.translation import ugettext_lazy as _
# from widgets import H5EmailInput
# from image_cropping import ImageCropWidget


# pylint: disable=E1120,W0212

LOGGER = logging.getLogger(name='socialprofile.forms')


class SocialProfileForm(forms.ModelForm):
    """Master form for editing the user's profile"""

    # user = forms.IntegerField(widget=forms.HiddenInput, required=True)
    returnTo = forms.CharField(widget=forms.HiddenInput, required=False, initial='/')  # URI to Return to after save
    manually_edited = forms.BooleanField(widget=forms.HiddenInput, required=False, initial=True)

    class Meta(object):
        """Configuration for the ModelForm"""
        model = SocialProfile
        fields = ['username',
                  'first_name', 'last_name', 'email', 'gender',
                  'url', 'image_url', 'description',
                  'cropping', 'cropping_free',
                  'country', 'city', 'address', 'postalcode',
                  'company', 'visible', 'sort', 'title', 'role',
                  'function_01', 'function_02', 'function_03', 'function_04', 'function_05', 'function_06',
                  'function_07', 'function_08', 'function_09', 'function_10']

    # Don't let through for security reasons, user should be based on logged in user only
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('gender', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('url', css_class='form-group col-md-6 mb-0'),
                Column('image_url', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('address', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('country', css_class='form-group col-md-6 mb-0'),
                Column('city', css_class='form-group col-md-4 mb-0'),
                Column('postalcode', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )

    def clean_description(self):
        """Automatically called by Django, this method 'cleans' the description, e.g. stripping HTML out of desc"""

        LOGGER.debug("socialprofile.forms.SocialProfileForm.clean_description")

        return strip_tags(self.cleaned_data['description'])

    def clean(self):
        """Automatically called by Django, this method 'cleans' the whole form"""

        LOGGER.debug("socialprofile.forms.SocialProfileForm.clean")

        if self.changed_data:
            self.cleaned_data['manually_edited'] = True
