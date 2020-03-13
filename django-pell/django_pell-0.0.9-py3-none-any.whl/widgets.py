"""
django_pell.widgets
~~~~~~~~~~~~~~~~~~~

Implements a the django PellWidget.
"""

from typing import List, Dict
from django.forms import widgets

import enum


class PellAction(enum.Enum):
    """Enum for pell menu actions."""

    bold = "bold"
    italic = "italic"
    underline = "underline"
    strikethrough = "strikethrough"
    heading1 = "heading1"
    heading2 = "heading2"
    paragraph = "paragraph"
    quote = "quote"
    olist = "olist"
    ulist = "ulist"
    code = "code"
    line = "line"
    link = "link"
    image = "image"

    @classmethod
    def get_action_list(cls) -> List:
        """Return the full list of actions, this is the default editor config."""

        return [action.value for action in cls]


class PellWidget(widgets.Widget):
    """Pell WYSIWYG widget.

    Pell is a WYSIWYG editor creatd by Jared Reich (https://jaredreich.com/pell/).

    Thanks Jared for the awesome editor.
    """

    template_name = "django_pell/pell.html"

    class Media:
        css = {"all": ("django_pell/css/pell.min.css",)}
        js = ("django_pell/js/pell.min.js",)

    def __init__(self, *args: List, **kwargs: Dict) -> None:
        """Set the custom widget attributes."""

        self.default_paragraph_separator = kwargs.pop(
            "default_paragraph_separator", "div"
        )
        self.style_with_css = kwargs.pop("style_with_css", False)
        self.actions = kwargs.pop("actions", PellAction.get_action_list())

        super().__init__(*args, **kwargs)

    def get_context(self, *args: List, **kwargs: Dict) -> Dict:
        """Add the custom attributes to the widget context."""

        context = super().get_context(*args, **kwargs)
        context["widget"][
            "default_paragraph_separator"
        ] = self.default_paragraph_separator
        context["widget"]["style_with_css"] = self.style_with_css
        context["widget"]["actions"] = self.actions
        return context
