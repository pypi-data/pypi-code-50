
from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from cap.decorators import short_description

from history.models import HistoryRecord, HistoryGroup


@admin.register(HistoryGroup)
class HistoryGroupAdmin(admin.ModelAdmin):

    list_display = ['name', 'code']

    fields = ['name']

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HistoryRecord)
class HistoryRecordAdmin(admin.ModelAdmin):

    list_display = [
        'user', 'text_tag', 'group', 'created'
    ]

    list_display_links = None

    list_pre_page = 100

    list_filter = ['created', 'group', 'user']

    search_fields = ['text']

    @short_description(_('Text'))
    def text_tag(self, obj):
        return mark_safe(obj.text)

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def change_view(self, request, object_id, form_url='', extra_context=None):
        raise PermissionDenied()


class LogHistoryAdmin(admin.ModelAdmin):

    history_group = None

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        if not change:
            return

        HistoryRecord.log_action(
            action=HistoryRecord.ACTION_CHANGE,
            group=self.history_group,
            user=request.user,
            obj=obj,
            fields=form.changed_data)

    def log_addition(self, request, object, message):
        HistoryRecord.log_action(
            action=HistoryRecord.ACTION_CREATE,
            group=self.history_group,
            user=request.user,
            obj=object)

    def log_deletion(self, request, object, object_repr):
        HistoryRecord.log_action(
            action=HistoryRecord.ACTION_DELETE,
            group=self.history_group,
            user=request.user,
            obj=object)
