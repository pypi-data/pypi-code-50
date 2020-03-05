import json
from fastutils import listutils
from django.db import models
from django.template.loader import render_to_string
from django.apps import apps
from django.utils.html import mark_safe
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django_ckeditor_5.fields import CKEditor5Field
from django_msms_admin.models import DjangoMsmsModelAbstractBase


class Theme(models.Model):
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    is_default = models.BooleanField(default=False, verbose_name=_("Is default theme"))

    class Meta:
        verbose_name = _("Theme")
        verbose_name_plural = _("Themes")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)
        if self.is_default:
            for theme in Theme.objects.filter(is_default=True).exclude(pk=self.pk):
                theme.is_default = False
        return result

    @property
    def css(self):
        return [x.css for x in self.css_files.all()]

    @property
    def js(self):
        return [x.js for x in self.js_files.all()]

    @classmethod
    def get_default_theme(cls):
        return cls.objects.filter(is_default=True).all()[0]

class ThemeCss(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="css_files", verbose_name=_("Theme"))
    css = models.CharField(max_length=128, verbose_name=_("CSS File"))
    order = models.IntegerField(verbose_name=_("Order"))

    class Meta:
        verbose_name = _("Theme CSS")
        verbose_name_plural = _("Theme CSSes")
        ordering = ["order"]

class ThemeJs(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE, related_name="js_files", verbose_name=_("Theme"))
    js = models.CharField(max_length=128, verbose_name=_("JS File"))
    order = models.IntegerField(verbose_name=_("Order"))

    class Meta:
        verbose_name = _("Theme JS")
        verbose_name_plural = _("Theme JSes")
        ordering = ["order"]

class Template(models.Model):
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    app_label= models.CharField(max_length=64, null=True, blank=True, verbose_name=_("App Label"))
    app_verbose_name = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("App Verbose Name"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    preview_image = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Preview Image"))
    template = models.CharField(max_length=128, verbose_name=_("Template File"))

    class Meta:
        verbose_name = _("Template")
        verbose_name_plural = _("Templates")

    def __str__(self):
        return self.name

class TemplateSlot(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE, related_name="slots", verbose_name=_("Template"))
    code = models.CharField(max_length=32, verbose_name=_("Code"))
    name = models.CharField(max_length=32, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Template Slot")
        verbose_name = _("Template Slots")
        unique_together = [
            ("template", "code"),
        ]

    def __str__(self):
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    code = models.CharField(max_length=64, unique=True, verbose_name=_("Code"))
    published = models.BooleanField(verbose_name=_("Published"))
    published_time = models.DateTimeField(null=True, blank=True, verbose_name=_("Published Time"))
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Theme"))
    index_page_code = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Index Page Code"))

    class Meta:
        verbose_name = _("Site")
        verbose_name_plural = _("Sites")


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.published and (not self.published_time):
            self.published_time = timezone.now()
        if not self.published:
            self.published_time = None
        return super().save(*args, **kwargs)

    @property
    def is_published(self):
        return self.published

    def get_theme(self):
        if self.theme:
            return self.theme
        else:
            return Theme.get_default_theme()

    def get_absolute_url(self):
        return reverse("django-power-cms.site", kwargs={"site_code": self.code})

class Page(MPTTModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name="pages", verbose_name=_("Site"))
    parent = TreeForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children", verbose_name=_("Parent Page"))
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    code = models.CharField(max_length=64, unique=True, verbose_name=("Code"))
    order = models.IntegerField(null=True, blank=True, verbose_name=_("Order"))
    published = models.NullBooleanField(verbose_name=_("Published"))
    published_time = models.DateTimeField(null=True, blank=True, verbose_name=_("Published Time"))
    template = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Template"))
    theme = models.ForeignKey(Theme, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Theme"))

    class Meta:
        verbose_name = _("Page")
        verbose_name_plural = _("Pages")
    
    class MPTTMeta:
        order_insertion_by = ['order']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.published and (not self.published_time):
            self.published_time = timezone.now()
        if not self.published:
            self.published_time = None
        return super().save(*args, **kwargs)

    @property
    def is_published(self):
        if self.published == True:
            return True
        if self.published == False:
            return False
        if self.parent:
            return self.parent.is_published
        else:
            return self.site.is_published

    def get_absolute_url(self):
        return reverse("django-power-cms.page", kwargs={"site_code": self.site.code, "page_code": self.code})

    def get_theme(self):
        if self.theme:
            return self.theme
        else:
            return self.site.get_theme()

    def render(self, request, global_context):
        css_links = []
        js_links = []
        # append theme resources
        theme = self.get_theme()
        for css in theme.css:
            listutils.append_new(css_links, css)
        for js in theme.js:
            listutils.append_new(js_links, js)
        # render widgets
        # and append widget resources
        widgets = {}
        for binding in self.widget_bindings.all():
            if not binding.slot.code in widgets:
                widgets[binding.slot.code] = []
            widgets[binding.slot.code].append(binding.widget.render(request, global_context))
            for css in binding.widget.get_real_model().css:
                listutils.append_new(css_links, css)
            for js in binding.widget.get_real_model().js:
                listutils.append_new(js_links, js)
        # make context
        context = {}
        context.update(global_context or {})
        context["widgets"] = widgets
        context["css_links"] = css_links
        context["js_links"] = js_links
        # render to string
        return render_to_string(self.template.template, context, request=request)

class PageWidget(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="widget_bindings", verbose_name=_("Page"))
    slot = models.ForeignKey(TemplateSlot, on_delete=models.CASCADE, related_name="+", verbose_name=_("Slot"))
    order = models.IntegerField(default=0, verbose_name=_("Order"))
    widget = models.ForeignKey("Widget", on_delete=models.CASCADE, related_name="+", verbose_name=_("Widget"))

    class Meta:
        verbose_name = _("Page Widget Binding")
        verbose_name_plural = _("Page Widget Bindings")
        ordering = ["slot", "order"]

    def __str__(self):
        return str(self.pk)

class Widget(DjangoMsmsModelAbstractBase, models.Model):
    name = models.CharField(max_length=64, verbose_name=_("Name"))
    # widget box settings
    title = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Title"))
    widget_with_border = models.BooleanField(default=False, verbose_name=_("Widget With border"))
    widget_body_padding = models.CharField(max_length=16, default="10px", null=True, blank=True, verbose_name=_("Widget Body Pading"))
    widget_style = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Widget Style"))
    widget_header_style = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Widget Header Style"))
    widget_body_style = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Widget Body Style"))
    widget_footer_style = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Widget Footer Style"))
    widget_class = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Widget Class"))
    widget_header_class = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Widget Header Class"))
    widget_body_class = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Widget Body Class"))
    widget_footer_class = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Widget Footer Class"))

    css = []
    js = []

    class Meta:
        verbose_name = _("Widget")
        verbose_name_plural = _("Widgets")

    def __str__(self):
        return self.name

    def render(self, request, global_context):
        context = {}
        context.update(global_context or {})
        header, footer = self.widget_header_and_footer_render(request, global_context)
        real_widget_model = self.get_real_model()
        if real_widget_model:
            body = real_widget_model.objects.get(pk=self.pk).render(request, global_context)
            context.update({
                "pk": self.pk,
                "widget_with_border": self.widget_with_border,
                "widget_body_padding": self.widget_body_padding or "",
                "widget_style": self.widget_style or "",
                "widget_header_style": self.widget_header_style or "",
                "widget_body_style": self.widget_body_style or "",
                "widget_footer_style": self.widget_footer_style or "",
                "widget_class": self.widget_class or "",
                "widget_header_class": self.widget_header_class or "",
                "widget_body_class": self.widget_body_class or "",
                "widget_footer_class": self.widget_footer_class or "",
                "header": header.strip(),
                "body": body.strip(),
                "footer": footer.strip(),
            })
            return render_to_string("django-power-cms/widgets/power-widget.html", context)
        else:
            return ""

    def widget_header_and_footer_render(self, request, global_context):
        top_left_links = []
        top_right_links = []
        bottom_left_links = []
        bottom_right_links = []
        links = self.links.all()
        for link in links:
            if link.role == WidgetLink.TOP_LEFT:
                top_left_links.append(link)
            elif link.role == WidgetLink.TOP_RIGHT:
                top_right_links.append(link)
            elif link.role == WidgetLink.BOTTOM_LEFT:
                bottom_left_links.append(link)
            elif link.role == WidgetLink.BOTTOM_RIGHT:
                bottom_right_links.append(link)
        header_context = {}
        footer_context = {}
        header_context.update(global_context or {})
        footer_context.update(global_context or {})
        header_context.update({
            "title": self.title,
            "top_left_links": top_left_links,
            "top_right_links": top_right_links,
        })
        footer_context.update({
            "bottom_left_links": bottom_left_links,
            "bottom_right_links": bottom_right_links,
        })
        header = render_to_string("django-power-cms/widgets/power-widget-header.html", header_context)
        footer = render_to_string("django-power-cms/widgets/power-widget-footer.html", footer_context)
        return header, footer


class WidgetLink(models.Model):
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGHT = 4
    ROLES = [
        (TOP_LEFT, _("Top Left")),
        (TOP_RIGHT, _("Top Right")),
        (BOTTOM_LEFT, _("Bottom Left")),
        (BOTTOM_RIGHT, _("Bottom Right")),
    ]

    Widget = models.ForeignKey(Widget, on_delete=models.CASCADE, related_name="links", verbose_name=_("Widget"))
    role = models.IntegerField(choices=ROLES, verbose_name=_("Widget Link Role"))
    title = models.CharField(max_length=32, verbose_name=_("Title"))
    url = models.CharField(max_length=128, verbose_name=_("Url"))
    icon = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Icon Class"))
    target = models.CharField(max_length=16, null=True, blank=True, verbose_name=_("Link Target"))

    class Meta:
        verbose_name = _("Widget Link")
        verbose_name_plural = _("Widget Links")

class StaticHtmlWidget(Widget):
    html = models.TextField(null=True, blank=True, verbose_name=_("HTML Code"))

    class Meta:
        verbose_name = _("Static HTML Widget")
        verbose_name_plural = _("Static HTML Widgets")

    def render(self, request, global_context):
        return self.html

class CarouselWidget(Widget):
    width = models.IntegerField(null=True, blank=True, verbose_name=_("Width"))
    height = models.IntegerField(null=True, blank=True, verbose_name=_("Height"))

    css = [
        "bootstrap/css/bootstrap.min.css",
    ]
    js = [
        "jquery3/jquery.js",
        "bootstrap/js/bootstrap.min.js",
    ]

    class Meta:
        verbose_name = _("Carousel Widget")
        verbose_name_plural = _("Carousel Widgets")

    def render(self, request, global_context):
        return render_to_string("django-power-cms/widgets/carousel.html", {
            "pk": self.pk,
            "images": self.images.all(),
            "width": self.width,
            "height": self.height,
        })

class CarouselWidgetImage(models.Model):
    carousel = models.ForeignKey(CarouselWidget, on_delete=models.CASCADE, related_name="images", verbose_name=_("Carousel"))
    image = models.ImageField(upload_to="carousel-images", verbose_name=_("Image"))
    url = models.CharField(max_length=512, null=True, blank=True, verbose_name=_("URL"))
    target = models.CharField(max_length=32, null=True, blank=True, verbose_name=_("URL Target"))
    order = models.IntegerField(default=0, verbose_name=_("Order"))

    class Meta:
        verbose_name = _("Carousel Widget Image")
        verbose_name_plural =  _("Carousel Widget Images")
        ordering = ["order"]

    def __str__(self):
        return str(self.pk)


class StaticListWidget(Widget):
    max_display_count = models.IntegerField(null=True, blank=True, verbose_name=_("Max Display Count"))
    empty_display_message = models.TextField(null=True, blank=True, verbose_name=_("Empty Display Message"))

    class Meta:
        verbose_name = _("Static List Widget")
        verbose_name_plural = _("Static List Widgets")

    def render(self, request, global_context):
        if self.max_display_count:
            lists = self.lists.filter(published=True).order_by("order").all()[:self.max_display_count]
        else:
            lists = self.lists.filter(published=True).order_by("order").all()
        return render_to_string("django-power-cms/widgets/static-list.html", {
            "lists": lists,
            "lists_length": len(lists),
            "empty_display_message": self.empty_display_message,
        })

class StaticListItem(models.Model):
    thelist = models.ForeignKey(StaticListWidget, on_delete=models.CASCADE, related_name="lists", verbose_name=_("The Static List Widget"))
    title = models.CharField(max_length=128, verbose_name=_("Title"))
    url = models.CharField(max_length=512, null=True, blank=True, verbose_name=_("URL"))
    target = models.CharField(max_length=32, null=True, blank=True, verbose_name=_("URL Target"))
    order = models.IntegerField(default=0, verbose_name=_("Order"))
    label = models.CharField(max_length=128, verbose_name=_("Label"))
    label_class = models.CharField(max_length=32, verbose_name=_("Label Class"))

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class TopbarWidget(Widget):
    brand_link = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Brand Link"))
    brand_link_target = models.CharField(max_length=32, null=True, blank=True, verbose_name=_("Brand Link Target"))
    welcome_message_for_login_user = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Welcome Message For Login User"))
    welcome_message_for_anonymous_user = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Welcome Message For Anonymous User"))
    fix_position = models.BooleanField(default=False, verbose_name=_("Fix Position"))
    show_login_or_logout_link = models.BooleanField(default=False, verbose_name=_("Show Login Or Logout Link"))
    login_link = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Login Link"))
    logout_link = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Logout Link"))
    show_change_password_link = models.BooleanField(default=False, verbose_name=_("Show Change Password Link"))
    change_password_link = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("Change Password Link"))

    class Meta:
        verbose_name = _("Topbar Widget")
        verbose_name_plural = _("Topbar Widgets")

    def render(self, request, global_context):
        context = {}
        context.update(global_context or {})
        brands = self.brands.all()
        context.update({
            "brand_link": self.brand_link,
            "brand_link_target": self.brand_link_target,
            "brands": brands,
            "welcome_message": self.get_welcome_message(request),
            "welcome_links": self.get_welcome_links(request),
        })
        return render_to_string("django-power-cms/widgets/topbar.html", context)

    def get_welcome_message(self, request):
        if request.user and request.user.pk:
            if not self.welcome_message_for_login_user:
                return ""
            else:
                return self.welcome_message_for_login_user.format(fullname=request.user.get_full_name())
        else:
            if not self.welcome_message_for_anonymous_user:
                return ""
            else:
                return self.welcome_message_for_anonymous_user
    
    def get_welcome_links(self, request):
        links = []
        change_password_link = self.get_change_password_link(request)
        if change_password_link:
            links.append(change_password_link)
        login_or_logout_link = self.get_login_or_logout_link(request)
        if login_or_logout_link:
            links.append(login_or_logout_link)
        links.reverse()
        return links

    def get_login_or_logout_link(self, request):
        if not self.show_login_or_logout_link:
            return None
        if request.user and request.user.pk:
            return {
                "class": "logout-link",
                "title": _("Logout"),
                "url": self.logout_link,
            }
        else:
            return {
                "class": "login-link",
                "title": _("Login"),
                "url": self.login_link,
            }

    def get_change_password_link(self, request):
        if not (self.show_change_password_link and request.user and request.user.pk):
            return None
        else:
            return {
                "class": "change-password-link",
                "title": _("Change password"),
                "url": self.change_password_link,
            }

class TopbarBrand(models.Model):
    topbar = models.ForeignKey(TopbarWidget, on_delete=models.CASCADE, related_name="brands", verbose_name=_("Topbar"))
    image = models.ImageField(upload_to="brand-images", null=True, blank=True, verbose_name=_("Image"))
    title = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Title"))
    url = models.CharField(max_length=128, null=True, blank=True, verbose_name=_("URL"))
    order = models.IntegerField(default=0, verbose_name=_("Order"))

    class Meta:
        ordering = ["order"]
        verbose_name = _("Topbar Brand")
        verbose_name_plural = _("Topbar Brands")


class Article(MPTTModel):
    TOP = _("Set Top")
    IMPORTANT = _("Important")
    GOOD_NEWS = _("Good News")
    WARNING = _("Warning")
    LABEL_CHOICES = [
        (TOP, TOP),
        (IMPORTANT, IMPORTANT),
        (GOOD_NEWS, GOOD_NEWS),
        (WARNING, WARNING),
    ]
    LABEL_CLASS_MAP = {
        str(TOP): "label label-primary",
        str(IMPORTANT): "label label-primary",
        str(GOOD_NEWS): "label label-success",
        str(WARNING): "label label-warning",
    }
    HIGH = 0
    NORAML = 99

    parent = TreeForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children", verbose_name=_("Article Parent"))
    title = models.CharField(max_length=64, verbose_name=_("Title"))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    content = CKEditor5Field(null=True, blank=True, verbose_name=_("Content"))
    published = models.BooleanField(verbose_name=_("Published"))
    published_time = models.DateTimeField(null=True, blank=True, verbose_name=_("Published Time"))
    preview_image = models.ImageField(upload_to="article-preview-images", null=True, blank=True, verbose_name=_("Preview Image"))
    show_preview_image = models.BooleanField(default=False, verbose_name=_("Show Preview Image"))
    order = models.IntegerField(null=True, blank=True, verbose_name=_("Order"))
    priority = models.IntegerField(default=99, verbose_name=_("Priority"))
    label = models.CharField(max_length=16, choices=LABEL_CHOICES, null=True, blank=True, verbose_name=_("Label"))

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    class MPTTMeta:
        order_insertion_by = ['order']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.label:
            self.priority = self.HIGH
        else:
            self.priority = self.NORAML
        return super().save(*args, **kwargs)

    @property
    def label_class(self):
        return self.LABEL_CLASS_MAP.get(self.label, "")

class ArticleContentImage(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="images", verbose_name=_("Article"))
    image = models.ImageField(upload_to="article-content-images", verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Article Content Image")
        verbose_name_plural = _("Article Content Images")

class ArticleListWidget(Widget):
    root = models.ForeignKey("Article", on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Root"))
    max_display_count = models.IntegerField(default=10, verbose_name=_("Max Display Count"))
    empty_display_message = models.TextField(null=True, blank=True, verbose_name=_("Empty Display Message"))

    class Meta:
        verbose_name = _("Article List Widget")
        verbose_name_plural = _("Article List Widgets")

    def render(self, request, global_context):
        lists = self.root.children.filter(published=True).order_by("priority").all()[:self.max_display_count]
        return render_to_string("django-power-cms/widgets/article-list.html", {
            "lists": lists,
            "lists_length": len(lists),
            "empty_display_message": self.empty_display_message,
        })
