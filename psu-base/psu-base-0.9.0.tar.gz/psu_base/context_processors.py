from psu_base.services import auth_service, utility_service
from django.conf import settings
from django.urls import reverse


def auth(request):
    auth_object = auth_service.get_auth_object()
    logged_in = auth_service.is_logged_in()
    can_impersonate = auth_object.can_impersonate()
    can_proxy = auth_object.has_authority('proxy', True)
    is_impersonating = auth_object.is_impersonating()
    is_proxying = auth_object.is_proxying()
    # Cannot call a function from a template.  Pre-query for commonly-used roles
    is_developer = auth_service.has_authority('developer')
    is_sso_developer = auth_service.has_authority('developer', True)
    is_global_developer = auth_service.has_authority('developer', True, True)
    is_admin = auth_service.has_authority('admin')
    is_sso_admin = auth_service.has_authority('admin', True)
    is_global_admin = auth_service.has_authority('admin', True, True)
    return {
        'auth': auth_object,
        'logged_in': logged_in, 'not_logged_in': not logged_in,
        'can_impersonate': can_impersonate, 'can_not_impersonate': not can_impersonate,
        'can_proxy': can_proxy, 'can_not_proxy': not can_proxy,
        'is_impersonating': is_impersonating, 'is_not_impersonating': not is_impersonating,
        'is_proxying': is_proxying, 'is_not_proxying': not is_proxying,
        'is_developer': is_developer, 'is_sso_developer': is_sso_developer, 'is_global_developer': is_global_developer, 
        'is_admin': is_admin, 'is_sso_admin': is_sso_admin, 'is_global_admin': is_global_admin, 
    }


def util(request):
    model = {
        # The home URL (path) depends on existence of URL Context
        'home_url': f"/{settings.URL_CONTEXT}/" if settings.URL_CONTEXT else '/',

        # Prod vs Nonprod
        'is_production': utility_service.is_production(),
        'is_non_production': utility_service.is_non_production(),
        'is_development': utility_service.is_development(),

        # Does PSU Logo color need to be modified (i.e. heading color is non-white)
        'modify_logo': settings.PSU_LOGO_FILTER is not None,
        'modify_logo_filter': settings.PSU_LOGO_FILTER.replace('filter:', '').strip(' ;') if settings.PSU_LOGO_FILTER else None,
        'modify_logo_calculate': settings.PSU_LOGO_FILTER is None and settings.PRIMARY_FG_COLOR,
    }

    # If white (the default color) was unnecessarily specified, logo doesn't need to be modified
    if model['modify_logo_calculate']:
        if str(settings.PRIMARY_FG_COLOR).lower() in ['white', '#fff', '#ffffff']:
            model['modify_logo_calculate'] = False
        elif settings.PRIMARY_FG_COLOR == (255, 255, 255):
            model['modify_logo_calculate'] = False
        elif settings.PRIMARY_FG_COLOR == (255, 255, 255, 1):
            model['modify_logo_calculate'] = False
        # If filter needs to be calculated, it also needs to be applied
        model['modify_logo'] = model['modify_logo_calculate']

    return model
