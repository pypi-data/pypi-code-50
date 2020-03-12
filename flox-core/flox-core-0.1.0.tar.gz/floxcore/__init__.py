import os
from os.path import join

from floxcore.settings import CONFIG_DIRS

KEYCHAIN_PATH = join(CONFIG_DIRS.get("user"), "flox-secrets")
os.environ["KEYRING_PROPERTY_KEYCHAIN"] = KEYCHAIN_PATH
