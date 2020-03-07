import time
import logging
import etools.consts


logger = logging.getLogger(etools.consts.LOGGER_NAME)
print(etools.consts.LOGGER_NAME)


def clear_none_in_dict(d, recursive=True):
    clear_keys = []
    for k, v in d.items():
        if v is None:
            clear_keys.append(k)
        if isinstance(v, dict) and recursive:
            clear_none_in_dict(v, True)
    for k in clear_keys:
        del d[k]
    return d


def bound(val, min_val, max_val):
    return min(max(val, min_val), max_val)


def log_run_time(action):
    def decorator(func):
        def inner_func(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            logger.info("action [%s] cost [%f]", action, time.time() - start)
            return result
        return inner_func
    return decorator
