from django.utils import timezone
from .models import Template

def register_template(name, code, template, slots):
    pass
    try:
        template_object = Template.objects.get(code=code)
        changed_flag = False
        if name != template_object.name:
            template_object.name = name
            changed_flag = True
        if template != template_object.template:
            template_object.template = template
            changed_flag = True
        if slots != template_object.slots:
            template_object.slots = slots
            changed_flag = True
        if changed_flag:
            template_object.save()
    except Template.DoesNotExist:
        template_object = Template()
        template_object.name = name
        template_object.code = code
        template_object.template = template
        template_object.published = True
        template_object.published_time = timezone.now()
        template_object.save()
