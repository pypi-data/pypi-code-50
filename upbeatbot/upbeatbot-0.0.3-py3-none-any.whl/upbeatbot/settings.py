import os

from envparse import env

env.read_envfile('.env')

LOG_FILE = os.environ.get('LOG_FILE', 'dev.log')
DEBUG = env.bool('DEBUG', default=False)
SLEEP_TIMEOUT = env.int('SLEEP_TIMEOUT', default=300)

# Twitter API Credentials
CONSUMER_KEY = env.str('CONSUMER_KEY', default='__consumer_key_not_set__')
CONSUMER_SECRET = env.str('CONSUMER_SECRET', default='__consumer_secret_not_set__')
ACCESS_TOKEN = env.str('ACCESS_TOKEN', default='__access_token_not_set__')
ACCESS_TOKEN_SECRET = env.str('ACCESS_TOKEN_SECRET', default='__access_token_secret_not_set__')
