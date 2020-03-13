from django.contrib import admin
from django.contrib.admin.options import csrf_protect_m


class DjangoWithExtraContextAdmin(admin.ModelAdmin):
    
    add_django_with_extra_context_admin_view_name = True

    def get_extra_context(self, request, **kwargs):
        return {}

    @csrf_protect_m
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if self.add_django_with_extra_context_admin_view_name and not "django_with_extra_context_admin_view_name" in extra_context:
            extra_context["django_with_extra_context_admin_view_name"] = "changeform_view"
        extra_context.update(self.get_extra_context(request, object_id=object_id, form_url=form_url, extra_context=extra_context))
        return super().changeform_view(request, object_id, form_url, extra_context)

    @csrf_protect_m
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        if self.add_django_with_extra_context_admin_view_name and not "django_with_extra_context_admin_view_name" in extra_context:
            extra_context["django_with_extra_context_admin_view_name"] = "changelist_view"
        extra_context.update(self.get_extra_context(request, extra_context=extra_context))
        return super().changelist_view(request, extra_context)

    @csrf_protect_m
    def delete_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        if self.add_django_with_extra_context_admin_view_name and not "django_with_extra_context_admin_view_name" in extra_context:
            extra_context["django_with_extra_context_admin_view_name"] = "delete_view"
        extra_context.update(self.get_extra_context(request, object_id=object_id, extra_context=extra_context))
        return super().delete_view(request, object_id, extra_context)

    def history_view(self, request, object_id, extra_context=None):
        extra_context = extra_context or {}
        if self.add_django_with_extra_context_admin_view_name and not "django_with_extra_context_admin_view_name" in extra_context:
            extra_context["django_with_extra_context_admin_view_name"] = "history_view"
        extra_context.update(self.get_extra_context(request, object_id=object_id, extra_context=extra_context))
        return super().history_view(request, object_id, extra_context)

    def add_view(self, request, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if self.add_django_with_extra_context_admin_view_name and not "django_with_extra_context_admin_view_name" in extra_context:
            extra_context["django_with_extra_context_admin_view_name"] = "add_view"
        extra_context.update(self.get_extra_context(request, form_url=form_url, extra_context=extra_context))
        return super().add_view(request, form_url, extra_context)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if self.add_django_with_extra_context_admin_view_name and not "django_with_extra_context_admin_view_name" in extra_context:
            extra_context["django_with_extra_context_admin_view_name"] = "change_view"
        extra_context.update(self.get_extra_context(request, object_id=object_id, form_url=form_url, extra_context=extra_context))
        return super().change_view(request, object_id, form_url, extra_context)
