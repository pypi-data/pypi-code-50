
from django import template


register = template.Library()


@register.inclusion_tag(
    'notify-js.html',
    takes_context=True,
    name='notify_js')
def render_notify_js(context):
    return context
