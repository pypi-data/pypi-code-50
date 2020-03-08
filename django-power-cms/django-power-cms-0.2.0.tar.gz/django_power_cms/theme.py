from django.utils import timezone
from .models import Theme
from .models import ThemeCss
from .models import ThemeJs

def register_theme(name, code, css_files, js_files):
    theme_object = Theme()
    theme_object.name = name
    theme_object.code = code
    theme_object.published = True
    theme_object.published_time = timezone.now()
    theme_object.save()

    order = 0
    for css_file in css_files:
        order += 1000
        css_object = ThemeCss()
        css_object.theme = theme_object
        css_object.css = css_file
        css_object.order = order
        css_object.save()
    
    order = 0
    for js_file in js_files:
        order += 1000
        js_object = ThemeCss()
        js_object.theme = theme_object
        js_object.css = js_file
        js_object.order = order
        js_object.save()
