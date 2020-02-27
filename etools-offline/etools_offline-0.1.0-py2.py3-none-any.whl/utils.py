from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.encoding import smart_str


def get_task_app():
    try:
        dotted_path = settings.ETOOLS_OFFLINE_TASK_APP
        assert dotted_path is not None
        module, func_name = dotted_path.rsplit('.', 1)
        module, func = smart_str(module), smart_str(func_name)
        func = getattr(__import__(module, {}, {}, [func]), func)
        return func()
    except ImportError as e:
        raise ImproperlyConfigured(
            "Could not import ETOOLS_OFFLINE_TASK_APP {}: {}".format(
                settings.ETOOLS_OFFLINE_TASK_APP,
                e,
            )
        )
    except ValueError as e:
        raise ImproperlyConfigured(
            "ETOOLS_OFFLINE_TASK_APP {} appears invalid: {}".format(
                settings.ETOOLS_OFFLINE_TASK_APP,
                e,
            )
        )
