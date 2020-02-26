from pathlib import Path

from pythonanywhereapiclient.utils import getenv


# General paths
PACKAGE_ROOT = Path(__file__).parent

# API client configuration
API_HOST = getenv('HOST')
API_TOKEN = getenv('TOKEN')
API_USER = getenv('USER')
