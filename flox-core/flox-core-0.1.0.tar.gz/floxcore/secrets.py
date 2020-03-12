import platform
from functools import wraps
from os.path import isfile

from click import ClickException
from keyring import get_password, set_password

from floxcore import KEYCHAIN_PATH
from floxcore.console import info
from floxcore.exceptions import MissingConfigurationValue


def ensure_keychain():
    try:
        if isfile(KEYCHAIN_PATH):
            return

        info("Looks like flox is trying to access keychain for the first time. \n"
             "Please select keychain password.")

        from plumbum.cmd import security
        security["create-keychain", "-P", KEYCHAIN_PATH]()
    except Exception as e:
        raise ClickException(f"Unable to initialise keychain.")


def with_keychain(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if platform.system() == 'Darwin':
            ensure_keychain()

        return f(*args, **kwargs)

    return wrapper


class Manager:
    def get(self, name, required=False):
        val = self[name]

        if not val and required:
            raise MissingConfigurationValue(name)

        return val

    def put(self, name, value):
        self[name] = value

    @with_keychain
    def __getitem__(self, item):
        return get_password(item, item)

    @with_keychain
    def __setitem__(self, key, value):
        set_password(key, key, value)
