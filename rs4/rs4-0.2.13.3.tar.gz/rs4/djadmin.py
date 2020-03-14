from django.contrib import admin
from django.utils.safestring import mark_safe
from django.forms import Widget

def set_title (title):
    admin.site.site_title = title
    admin.site.site_header = "{}".format (title)
    admin.site.index_title = "{} Management Console".format (title)

def ImageWidget (width = 360):
    class _ImageWidget(Widget):
        def render(self, name, value, **noneed):
            return value and mark_safe ('<img src="{}" width="{}">'.format (value, width)) or 'No Image'
    return _ImageWidget

class LinkWidget(Widget):
    def render(self, name, value, **noneed):
        return value and mark_safe ('<a href="{}">{}</a> [<a href="{}" target="_blank">새창</a>]'.format (value, value, value)) or 'No Image'

class ModelAdmin (admin.ModelAdmin):
    image_width = 360
    def formfield_for_dbfield (self, db_field, request, **kwargs):
        if db_field.name.endswith ('image'):
            kwargs ['widget'] = ImageWidget (self.image_width)
            return db_field.formfield(**kwargs)
        elif db_field.name.endswith ('url'):
            kwargs ['widget'] = LinkWidget
            return db_field.formfield(**kwargs)
        return super ().formfield_for_dbfield (db_field, request, **kwargs)