__version__ = "0.1.2"
import time


def interval(time_interval, alternative_func=None):
    def decorator(function):
        function.__last_run = 0

        def guard(*args, **kwargs):
            now = time.time()
            if now - function.__last_run >= time_interval:
                function.__last_run = now
                return function(*args, **kwargs)
            else:
                if alternative_func is not None:
                    return alternative_func(*args, **kwargs)

        return guard

    return decorator


def interval_or_return_first_value(time_interval):
    def decorator(function):
        function.__last_run = 0

        def guard(*args, **kwargs):
            now = time.time()
            if now - function.__last_run >= time_interval:
                function.__last_run = now
                return function(*args, **kwargs)
            else:
                return args[0]

        return guard

    return decorator
