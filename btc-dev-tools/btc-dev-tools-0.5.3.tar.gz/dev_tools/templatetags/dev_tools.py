from django import template

from dev_tools.template.components import HTMLElementType, BaseHTMLElement

register = template.Library()


@register.filter
def tweak_parameter(element: HTMLElementType, value: str):
    """
    Filter for tweaking HTMLElement (must be type of BaseHTMLElement class).
    element|tweak_parameter:'class:my-class my-class-2'
    element|tweak_parameter:'type:button'
    """

    data = value.split(':')
    if isinstance(element, BaseHTMLElement) and data:
        if data[0] == 'class':
            element.css_classes += data[1].strip().split(' ')
        else:
            element.html_params.update({data[0]: data[1]})

    return element
