from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django_readedit_switch_admin.admin import DjangoReadEditSwitchAdminMixin
from django_force_disable_permissions_admin.admin import DjagnoForceDisablePermissionsAdminMixin
from django_msms_admin.admin import DjangoMsmsAdmin
from django_msms_admin.admin import DjangoSubclassAdmin
from .models import Template
from .models import TemplateSlot
from .models import Site
from .models import Page
from .models import PageWidget
from .models import Widget
from .models import StaticHtmlWidget
from .models import CarouselWidget
from .models import CarouselWidgetImage
from .models import Theme
from .models import ThemeCss
from .models import ThemeJs
from .models import WidgetLink
from .models import StaticListWidget
from .models import StaticListItem
from .models import TopbarWidget
from .models import TopbarBrand
from .models import Article
from .models import ArticleContentImage
from .models import ArticleListWidget

class PageWidgetInline(admin.TabularInline):
    model = PageWidget

class PageAdmin(DraggableMPTTAdmin):
    list_display = ["tree_actions", "display_title", "code"]
    list_display_links = ["display_title"]
    inlines = [
        PageWidgetInline,
    ]

    def display_title(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.name,
        )
    display_title.short_description = _('Title')


class SiteAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "published", "published_time", "preview_link"]
    list_filter = ["published"]
    search_fields = ["name", "code"]

    def preview_link(self, obj):
        return format_html(
            """<a href="{0}" target="_blank">{1}</a>""",
            obj.get_absolute_url(),
            _("Preview"),
        )

    preview_link.short_description = _("Preview")


class ThemeCssInline(admin.TabularInline):
    model = ThemeCss

class ThemeJsInline(admin.TabularInline):
    model = ThemeJs

class ThemeAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "is_default"]
    list_filter = ["is_default"]
    search_fields = ["name", "description"]
    inlines = [
        ThemeCssInline,
        ThemeJsInline,
    ]


class WidgetLinkInline(admin.TabularInline):
    model = WidgetLink
    extra = 0

class StaticHtmlWidgetAdmin(DjangoSubclassAdmin, admin.ModelAdmin):
    list_dipslay = ["name"]
    inlines = [
        WidgetLinkInline,
    ]

class CarouselWidgetImageInline(admin.TabularInline):
    model = CarouselWidgetImage
    extra = 0

class CarouselWidgetAdmin(DjangoSubclassAdmin, admin.ModelAdmin):
    list_dipslay = ["name"]
    inlines = [
        WidgetLinkInline,
        CarouselWidgetImageInline,
    ]

class StaticListItemInline(admin.StackedInline):
    model = StaticListItem
    extra = 0
    fieldsets = [
        [None, {
            "fields": [
                ("title", "url"),
                ("target", "order"),
                ("label", "label_class"),
            ]
        }]
    ]


class StaticListWidgetAdmin(DjangoSubclassAdmin, admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        WidgetLinkInline,
        StaticListItemInline,
    ]

class TopbarBrandInline(admin.TabularInline):
    model = TopbarBrand
    extra = 0

class TopbarWidgetAdmin(DjangoSubclassAdmin, admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        WidgetLinkInline,
        TopbarBrandInline,
    ]


class ArticleContentImageInline(admin.TabularInline):
    model = ArticleContentImage
    extra = 0

class ArticleAdmin(DjangoReadEditSwitchAdminMixin, DraggableMPTTAdmin, admin.ModelAdmin):
    list_display = ["tree_actions", "display_title", "published", "published_time"]
    list_display_links = ["display_title"]
    inlines = [
        ArticleContentImageInline
    ]

    def display_title(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.title,
        )
    display_title.short_description = _('Title')

class WidgetAdmin(DjangoMsmsAdmin, admin.ModelAdmin):
    list_display = ["name", "type_name"]
    list_filter = ["type_name"]
    search_fields = ["name"]


class ArticleListWidgetAdmin(DjangoSubclassAdmin, admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        WidgetLinkInline,
    ]

class TemplateSlotInline(admin.TabularInline):
    model = TemplateSlot
    extra = 0

class TemplateAdmin(admin.ModelAdmin):
    list_display = ["name", "app_label", "template", "preview_image"]
    list_filter = ["app_label"]
    search_fields = ["name", "description", "template"]
    inlines = [
        TemplateSlotInline,
    ]

admin.site.register(Template, TemplateAdmin)
admin.site.register(Site, SiteAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Widget, WidgetAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(CarouselWidget, CarouselWidgetAdmin)
admin.site.register(StaticHtmlWidget, StaticHtmlWidgetAdmin)
admin.site.register(StaticListWidget, StaticListWidgetAdmin)
admin.site.register(TopbarWidget, TopbarWidgetAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleListWidget, ArticleListWidgetAdmin)