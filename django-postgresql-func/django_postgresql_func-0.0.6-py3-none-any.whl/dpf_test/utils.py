import functools
import logging
import random
from string import ascii_letters, digits, punctuation
import environ

from django.utils import timezone


secret_array = ascii_letters + digits + punctuation


def regenerate_secret_key():
    return ''.join(random.SystemRandom().choice(secret_array) for i
                   in range(64))


def get_root():
    return environ.Path(__file__) - 2


def get_env():
    root = get_root()
    env = environ.Env()
    env_file = str(root.path('.env'))
    env.read_env(env_file)
    return env


def log(name=None):
    def wrapper(func):
        @functools.wraps(func)
        def decorator(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logging.getLogger("error_logger").error(f'{name} {repr(e)}')

        return decorator

    return wrapper