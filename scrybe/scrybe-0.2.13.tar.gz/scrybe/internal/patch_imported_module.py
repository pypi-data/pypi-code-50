import sys
import functools
from scrybe.internal.tracker.save_and_load_tracker import save_func_after_decorator, deserialize_func_after_decorator


def get_wrapped_func(func_to_decorate, after_decorator):
    @functools.wraps(func_to_decorate)
    def wrapper_fn(*args, **kwargs):
        return_value = func_to_decorate(*args, **kwargs)
        try:
            after_decorator(return_value, *args, **kwargs)
        except Exception as e:
            pass
        return return_value
    return wrapper_fn


def patch(module_to_patch_str):
    if module_to_patch_str == 'pickle':
        module = sys.modules[module_to_patch_str]
        dump_func = getattr(module, 'dump', None)
        if dump_func is not None:
            dump_func = get_wrapped_func(dump_func, save_func_after_decorator)
            setattr(module, 'dump', dump_func)
        load_func = getattr(module, 'load', None)
        if load_func is not None:
            load_func = get_wrapped_func(load_func, deserialize_func_after_decorator)
            setattr(module, 'load', load_func)
