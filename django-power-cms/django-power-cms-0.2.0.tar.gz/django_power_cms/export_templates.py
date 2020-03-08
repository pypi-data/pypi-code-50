from django_power_cms.apps import DjangoPowerCmsConfig
from django.utils.translation import ugettext_lazy as _

templates = [{
    "code": "4ef1dbc1256149a09d6ea9b23b09a7a8",
    "name": _("Right Portlet Template"),
    "app_label": "django_power_cms",
    "app_verbose_name": DjangoPowerCmsConfig.verbose_name,
    "description": _("Right Portlet Template Description."),
    "preview_image": "django-power-cms/template-preview-image/right-portlet.png",
    "template": "django-power-cms/templates/right-portlet.html",
    "slots": [{
        "code": "topbars",
        "name": _("Slot Topbars"),
    },{
        "code": "headers",
        "name": _("Slot Headers"),
    },{
        "code": "mains",
        "name": _("Slot Mains"),
    },{
        "code": "right_portlets",
        "name": _("Right Slot Portlets"),
    },{
        "code": "footers",
        "name": _("Slot Footers"),
    }]
},{
    "code": "811ec1329c7f4d9b9d874090d6094cec",
    "name": _("Left Portlet Template"),
    "app_label": "django_power_cms",
    "app_verbose_name": DjangoPowerCmsConfig.verbose_name,
    "description": _("Left Portlet Template Description."),
    "preview_image": "django-power-cms/template-preview-image/left-portlet.png",
    "template": "django-power-cms/templates/left-portlet.html",
    "slots": [{
        "code": "topbars",
        "name": _("Slot Topbars"),
    },{
        "code": "headers",
        "name": _("Slot Headers"),
    },{
        "code": "mains",
        "name": _("Slot Mains"),
    },{
        "code": "left_portlets",
        "name": _("Left Slot Portlets"),
    },{
        "code": "footers",
        "name": _("Slot Footers"),
    }]
},{
    "code": "84121a8a2a77470bb958df38711a5ea2",
    "name": _("Both Portlet Template"),
    "app_label": "django_power_cms",
    "app_verbose_name": DjangoPowerCmsConfig.verbose_name,
    "description": _("Both Portlet Template Description."),
    "preview_image": "django-power-cms/template-preview-image/both-portlet.png",
    "template": "django-power-cms/templates/both-portlet.html",
    "slots": [{
        "code": "topbars",
        "name": _("Slot Topbars"),
    },{
        "code": "headers",
        "name": _("Slot Headers"),
    },{
        "code": "left_portlets",
        "name": _("Left Slot Portlets"),
    },{
        "code": "mains",
        "name": _("Slot Mains"),
    },{
        "code": "right_portlets",
        "name": _("Right Slot Portlets"),
    },{
        "code": "footers",
        "name": _("Slot Footers"),
    }]
}]
