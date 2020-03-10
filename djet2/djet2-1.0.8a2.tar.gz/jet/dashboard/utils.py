import logging
from importlib import import_module
from jet.dashboard import settings


logger = logging.getLogger(__name__)


def import_value(path: str):
    module, name = path.rsplit('.', 1)
    try:
        module = import_module(module)
        value = getattr(module, name)
    except (ImportError, AttributeError) as e:
        raise ImportError(e)
    return value


def get_current_dashboard(location):
    if location == 'index':
        path = settings.JET_INDEX_DASHBOARD
    elif location == 'app_index':
        path = settings.JET_APP_INDEX_DASHBOARD
    else:
        raise ValueError('Unknown dashboard location: %s' % location)
    dashboard_cls = import_value(path)
    return dashboard_cls
