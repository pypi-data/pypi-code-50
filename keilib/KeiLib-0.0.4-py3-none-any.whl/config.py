from decouple import config

APP_UID = config('APP_UID', cast=str, default=None)
APP_SECRET = config('APP_SECRET', cast=str, default=None)
TOKEN_FILE = config('TOKEN_FILE', cast=str, default=None)
REDIRECT_URI = config('REDIRECT_URI', cast=str, default=None)
SCOPE = config('SCOPE', cast=str, default=None)
STATE = config('STATE', cast=str, default=None)
HOOK = config('HOOK', cast=str, default=None)