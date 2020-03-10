import json

from django.template.loader import render_to_string

from jet.utils import LazyDateTimeEncoder, context_to_dict


class DashboardModule(object):
    """
    Base dashboard module class. All dashboard modules (widgets) should inherit it.
    """

    #: Path to widget's template. There is no need to extend such templates from any base templates.
    template = 'jet.dashboard/module.html'
    enabled = True

    #: Specify if module can be draggable or has static position.
    draggable = True

    #: Specify if module can be collapsed.
    collapsible = True

    #: Specify if module can be deleted.
    deletable = True
    show_title = True

    #: Default widget title that will be displayed for widget in the dashboard. User can change it later
    #: for every widget.
    title = ''

    #: Specify title url. ``None`` if title shouldn't be clickable.
    title_url = None
    css_classes = None

    #: HTML content that will be displayed before widget content.
    pre_content = None

    #: HTML content that will be displayed after widget content.
    post_content = None
    children = None

    #: A ``django.forms.Form`` class which may contain custom widget settings. Not required.
    settings_form = None

    #: A ``django.forms.Form`` class which may contain custom widget child settings, if it has any. Not required.
    child_form = None

    #: Child name that will be displayed when editing module contents. Required if ``child_form`` set.
    child_name = None

    #: Same as child name, but plural.
    child_name_plural = None
    settings = None
    column = None
    order = None

    #: A boolean field which specify if widget should be rendered on dashboard page load or fetched
    #: later via AJAX.
    ajax_load = False

    #: A boolean field which makes widget ui color contrast.
    contrast = False

    #: Optional style attributes which will be applied to widget content container.
    style = False

    class Media:
        css = ()
        js = ()

    def __init__(self, title=None, model=None, context=None, **kwargs):
        if title is not None:
            self.title = title
        self.model = model
        self.context = context or {}

        for key in kwargs:
            if hasattr(self.__class__, key):
                setattr(self, key, kwargs[key])

        self.children = self.children or []

        if self.model:
            self.load_from_model()

    def fullname(self):
        return self.__module__ + "." + self.__class__.__name__

    def load_settings(self, settings):
        """
        Should be implemented to restore saved in database settings. Required if you have custom settings.
        """
        pass

    def load_children(self, children):
        self.children = children

    def store_children(self):
        """
        Specify if children field should be saved to database.
        """
        return False

    def settings_dict(self):
        """
        Should be implemented to save settings to database. This method should return ``dict`` which will be serialized
        using ``json``. Required if you have custom settings.
        """
        pass

    def dump_settings(self, settings=None):
        settings = settings or self.settings_dict()
        if settings:
            return json.dumps(settings, cls=LazyDateTimeEncoder)
        else:
            return ''

    def dump_children(self):
        if self.store_children():
            return json.dumps(self.children, cls=LazyDateTimeEncoder)
        else:
            return ''

    def load_from_model(self):
        self.title = self.model.title

        if self.model.settings:
            try:
                self.settings = json.loads(self.model.settings)
                self.load_settings(self.settings)
            except ValueError:
                pass

        if self.store_children() and self.model.children:
            try:
                children = json.loads(self.model.children)
                self.load_children(children)
            except ValueError:
                pass

    def init_with_context(self, context):
        """
        Allows you to load data and initialize module's state.
        """
        pass

    def get_context_data(self):
        context = context_to_dict(self.context)
        context.update({
            'module': self
        })
        return context

    def render(self):
        self.init_with_context(self.context)
        return render_to_string(self.template, self.get_context_data())
