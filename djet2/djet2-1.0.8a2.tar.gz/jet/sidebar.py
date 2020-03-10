import itertools
from typing import List

from django.dispatch import Signal
from django.template import loader
from django.utils.functional import cached_property
from django.utils.safestring import mark_safe


class Section:
    # position in the sidebar
    order = 0
    # menu title
    title = None
    # template used to render section
    template_name = ''

    def get_context_data(self, request, context):
        return {
            'self': self,
            'request': request,
            **context.flatten(),
        }

    def render(self, request, context):
        context = self.get_context_data(request, context)
        if context is None:
            return ''
        return mark_safe(
            loader.get_template(self.template_name).render(context)
        )

    def popups(self) -> List['Section']:
        """Submenus."""
        return []

    def __lt__(self, other: 'Section'):
        return self.order < other.order


class Sidebar(Section):
    signal = Signal(['request', 'context', 'sections'])
    # request being processed
    request = None
    # context of the page that being rendered
    context = None
    # Always rendered sections
    static_sections = []

    template_name = 'jet/sidebar/sidebar.html'

    def __init__(self, request, context):
        self.request = request
        self.context = context

    @classmethod
    def connect(cls, *args, **kwargs):
        cls.signal.connect(*args, **kwargs)

    @classmethod
    def disconnect(cls, *args, **kwargs):
        cls.signal.disconnect(*args, **kwargs)

    @classmethod
    def add(cls, section):
        """
        Add a section to the static sections
        """
        cls.static_sections.append(section)
        cls.static_sections.sort()

    @classmethod
    def remove(cls, section):
        """
        Remove a section from static sections
        """
        cls.static_sections.remove(section)

    @cached_property
    def sections(self):
        """
        Gather items by triggering signal, and return them sorted by priority.
        """
        sections = []
        results = (
            v for r, v in
            self.signal.send(
                sender=self,
                request=self.request,
                context=self.context,
                sections=sections,
            )
            if isinstance(v, Section)
        )
        return sorted(itertools.chain(
            self.static_sections, sections, results
        ))

    def get_context_data(self, request, context):
        context = super(Sidebar, self).get_context_data(request, context)
        return context

    def render(self, request=None, context=None):
        request = request or self.request
        context = context or self.context
        return super(Sidebar, self).render(request, context)

    def popups(self):
        return itertools.chain.from_iterable(
            item.popups() for item in self.sections
        )

    def render_sections(self):
        return [
            section.render(self.request, self.context)
            for section in self.sections
        ]

    def render_popups(self):
        return [
            section.render(self.request, self.context)
            for section in self.popups()
        ]


class NavSection(Section):
    template_name = 'jet/sidebar/section_nav.html'
    order = 1000


class AppPopup(Section):
    template_name = 'jet/sidebar/popup_app.html'
    app = None

    def __init__(self, app):
        self.app = app

    def get_context_data(self, request, context):
        context = super(AppPopup, self).get_context_data(request, context)
        context['app'] = self.app
        return context


class AppsSection(Section):
    template_name = 'jet/sidebar/section_apps.html'
    order = 2000

    def __init__(self):
        self._apps = []

    def get_context_data(self, request, context):
        from jet.utils import get_menu_items
        self._apps = [
            app for app in get_menu_items(context)
            if app.get('has_perms')
        ]
        context = super(AppsSection, self).get_context_data(request, context)
        context['app_list'] = self._apps
        return context

    def popups(self):
        return [AppPopup(app) for app in self._apps]


class BookmarkSection(Section):
    template_name = 'jet/sidebar/section_bookmarks.html'
    order = 3000


# default sections to render in sidebar
Sidebar.static_sections.extend([
    NavSection(),
    AppsSection(),
    BookmarkSection(),
])
