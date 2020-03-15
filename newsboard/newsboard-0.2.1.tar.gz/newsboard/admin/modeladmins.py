from django.contrib import admin
from django.urls import reverse, reverse_lazy
from django.utils.translation import ugettext_lazy as _

from dj_web_rich_object.admin.modeladmins import WebRichObjectAdmin
from dj_web_rich_object.admin.modeladmins import TagAdmin as BaseTagAdmin

from newsboard import tasks
from newsboard.admin import forms


class StreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'remote_id', 'last_updated', 'auto_enabled', 'auto_frequency')
    list_filter = ('type', 'auto_enabled')
    actions = ('update', 'enable_auto', 'disable_auto')
    prepopulated_fields = {'slug': ('name', )}

    def update(self, request, queryset):
        stream_ids = list(queryset.values_list('id', flat=True))
        tasks.update_streams.delay(stream_ids)
    update.short_description = _("Update selected streams")

    def enable_auto(self, request, queryset):
        queryset.update(auto_enabled=True)
    enable_auto.short_description = _("Enable automatic updating")

    def disable_auto(self, request, queryset):
        queryset.update(auto_enabled=False)
    disable_auto.short_description = _("Disable automatic updating")


class PostAdmin(WebRichObjectAdmin):
    actions = WebRichObjectAdmin.actions + ('remove_posts', 'unremove_posts')
    list_display = WebRichObjectAdmin.list_display + ('is_removed',)
    list_filter = WebRichObjectAdmin.list_filter + ('streams', 'is_removed')

    add_form = forms.PostAdminAddForm
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'url',
                'streams',
            )
        }),
    )

    list_url = reverse_lazy("admin:newsboard_post")
    detail_url_name = "admin:newsboard_post_change"

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is not None and ('streams', 'is_removed') not in fieldsets[0][1]['fields']:
            fieldset = (('streams', 'is_removed'),) + tuple(fieldsets[0][1]['fields'])
            fieldsets[0][1]['fields'] = fieldset
        return fieldsets

    def remove_posts(self, request, queryset):
        queryset.update(is_removed=True)
    remove_posts.short_description = _("Remove selected posts")

    def unremove_posts(self, request, queryset):
        queryset.update(is_removed=False)
    unremove_posts.short_description = _("Display selected posts")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)


class TagAdmin(BaseTagAdmin):
    list_display = ('name', 'slug', 'parent', 'is_hidden')
    list_filter = ('is_hidden',)
    actions = ('hide', 'unhide', 'set_parent')

    def hide(self, request, queryset):
        queryset.update(is_hidden=True)
    hide.short_description = _("Hide selected tag(s)")

    def unhide(self, request, queryset):
        queryset.update(is_hidden=False)
    unhide.short_description = _("Unhide selected tag(s)")

    def set_parent(self, request, queryset):
        form = forms.TagParentAdminForm(request.POST)
        if not '_continue' in request.POST:
            form.fields['_selected_action'].queryset = queryset
            admin_form = admin.helpers.AdminForm(
                form,
                fieldsets=(
                    (None, {
                        'classes': ('wide',),
                        'fields': (
                            'action',
                            'parent',
                            'index',
                            'select_across',
                            '_selected_action',
                            'post',
                        )
                    }),
                ),
                # Clear prepopulated fields on a view-only form to avoid a crash.
                prepopulated_fields={},
                readonly_fields=[],
                model_admin=self
            )
            context = {
                'inline_admin_formsets': [],
                'adminform': admin_form,
                'is_popup': False,
                'show_save': False,
                'show_save_and_continue': True,
                'show_save_and_add_another': False,
                'show_close': False,
                'change': True,
            }
            return self.render_change_form(
                request=request,
                context=context,
                change=True,
            )
        else:
            queryset.update(parent=request.POST.get('parent'))
    set_parent.short_description = _("Set parent of selected tag(s)")
