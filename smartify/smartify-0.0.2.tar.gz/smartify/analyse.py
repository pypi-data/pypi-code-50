from .arg import get_arg_dict
from .param import PDict


class Analyse:
    @staticmethod
    def p(*params, abundant=True):
        p = PDict().set_fields(*params)

        def decorator(func):
            def wrapper(*args, **kwargs):
                param_dict = get_arg_dict(func, *args, **kwargs)
                _, param_dict = p.run(param_dict, abundant=abundant)
                return func(**param_dict)
            return wrapper
        return decorator
