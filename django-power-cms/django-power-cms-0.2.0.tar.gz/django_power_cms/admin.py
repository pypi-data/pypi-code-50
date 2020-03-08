from django.contrib import admin
from django.forms import ModelForm
from django.urls import reverse
from mptt.admin import DraggableMPTTAdmin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from django_readedit_switch_admin.admin import DjangoReadEditSwitchAdmin
from django_changelist_toolbar_admin.admin import DjangoChangelistToolbarAdminMixin
from django_cards_admin.admin import DjangoCardsAdminMixin
from django_msms_admin.admin import DjangoMsmsAdmin
from django_msms_admin.admin import DjangoSubclassAdmin
from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget
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




class PageWidgetInline(DjangoReadEditSwitchAdmin, admin.TabularInline):
    model = PageWidget

class PageAdmin(DjangoReadEditSwitchAdmin, DjangoChangelistToolbarAdminMixin, DraggableMPTTAdmin):
    list_display = ["tree_actions", "display_title", "display_page_url", "preview_link"]
    list_display_links = ["display_title"]
    inlines = [
        PageWidgetInline,
    ]
    changelist_toolbar_buttons = [
        "display_return_to_site",
    ]

    def display_return_to_site(self, request):
        return {
            "icon": "fas fa-undo-alt",
            "title": _("Return to site info page"),
            "href": reverse("admin:django_power_cms_site_change", kwargs={"object_id": 1}),
        }

    def display_title(self, obj):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            obj._mpttfield('level') * self.mptt_level_indent,
            obj.name,
        )
    display_title.short_description = _('Title')

    def display_page_url(self, obj):
        return "page:{0}:{1}".format(obj.site.code, obj.code)
    display_page_url.short_description = _("Display Page URL") 

    def preview_link(self, obj):
        return format_html(
            """<a href="{0}" target="_blank">{1}</a>""",
            obj.get_absolute_url(),
            _("Preview"),
        )
    preview_link.short_description = _("Preview")

class SiteForm(ModelForm):
    class Meta:
        model = Site
        exclude = []
        widgets = {
            "published": DjangoToggleSwitchWidget(klass="django-toggle-switch-primary"),
        }

class SiteAdmin(DjangoReadEditSwitchAdmin, DjangoCardsAdminMixin, admin.ModelAdmin):
    form = SiteForm
    list_display = ["name", "code", "published", "published_time", "preview_link"]
    list_filter = ["published"]
    search_fields = ["name", "code"]
    readonly_fields = ["published_time"]
    result_card_body_height = 200
    fieldsets = [
        (_("Basic Info"), {
            "fields": ["name", "code", "theme", "index_page_code"],
        }),
        (_("Publish State"), {
            "fields": ["published", "published_time"],
        })
    ]

    def preview_link(self, obj):
        return format_html(
            """<a href="{0}" target="_blank">{1}</a>""",
            obj.get_absolute_url(),
            _("Preview"),
        )

    preview_link.short_description = _("Preview")

    class Media:
        css = {
            "all": [
                "fontawesome/css/all.min.css",
            ]
        }

class ThemeCssInline(DjangoReadEditSwitchAdmin, admin.TabularInline):
    model = ThemeCss
    extra = 0

class ThemeJsInline(DjangoReadEditSwitchAdmin, admin.TabularInline):
    model = ThemeJs
    extra = 0

class ThemeAdmin(DjangoReadEditSwitchAdmin, admin.ModelAdmin):
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

class TopbarWidgetAdmin(DjangoSubclassAdmin, DjangoChangelistToolbarAdminMixin, admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        WidgetLinkInline,
        TopbarBrandInline,
    ]


class ArticleContentImageInline(admin.TabularInline):
    model = ArticleContentImage
    extra = 0

class ArticleAdmin(DjangoReadEditSwitchAdmin, DraggableMPTTAdmin, DjangoChangelistToolbarAdminMixin, admin.ModelAdmin):
    list_display = ["tree_actions", "display_title", "published", "published_time"]
    list_display_links = ["display_title"]
    inlines = [
        ArticleContentImageInline
    ]
    changelist_toolbar_buttons = [
        "display_return_to_site",
    ]

    def display_return_to_site(self, request):
        return {
            "icon": "fas fa-undo-alt",
            "title": _("Return to site info page"),
            "href": reverse("admin:django_power_cms_site_change", kwargs={"object_id": 1}),
        }

    def display_title(self, instance):
        return format_html(
            '<div style="text-indent:{}px">{}</div>',
            instance._mpttfield('level') * self.mptt_level_indent,
            instance.title,
        )
    display_title.short_description = _('Title')

class WidgetAdmin(DjangoMsmsAdmin, DjangoChangelistToolbarAdminMixin, admin.ModelAdmin):
    list_display = ["name", "type_name"]
    list_filter = ["type_name"]
    search_fields = ["name"]
    changelist_toolbar_buttons = [
        "display_return_to_site",
    ]

    def display_return_to_site(self, request):
        return {
            "icon": "fas fa-undo-alt",
            "title": _("Return to site info page"),
            "href": reverse("admin:django_power_cms_site_change", kwargs={"object_id": 1}),
        }
    
class ArticleListWidgetAdmin(DjangoSubclassAdmin, admin.ModelAdmin):
    list_display = ["name"]
    inlines = [
        WidgetLinkInline,
    ]

class TemplateSlotInline(DjangoReadEditSwitchAdmin, admin.TabularInline):
    model = TemplateSlot
    extra = 0

class TemplateAdmin(DjangoReadEditSwitchAdmin, admin.ModelAdmin):
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