from django.contrib import admin
from django.urls import path
from django.urls import reverse
from django.http import HttpResponse
from django import forms
from django_with_extra_context_admin.admin import DjangoWithExtraContextAdmin

class DjangoDynamicResourceAdmin(DjangoWithExtraContextAdmin):

    def get_css(self, request, **kwargs):
        # MUST reimplemented by sub classes
        return []
    
    def get_js(self, request, **kwargs):
        # MUST reimplemented by sub classes
        return []

    def get_extra_context(self, request, **kwargs):
        app_label = self.model._meta.app_label
        model_name = self.model._meta.model_name
        extra_context = super().get_extra_context(request, **kwargs)
        extra_context.update({
            "django_dynamic_resource_admin_css_codes": self.get_css(request, **kwargs),
            "django_dynamic_resource_admin_js_codes": self.get_js(request, **kwargs),
        })
        return extra_context
