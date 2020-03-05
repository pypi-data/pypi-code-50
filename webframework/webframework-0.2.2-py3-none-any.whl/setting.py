import os

URL = os.environ.get('URL')
WEB_BROWSER = os.getenv("WEB_BROWSER")
DRIVER_PATH = os.getenv("DRIVER_PATH")

if not URL or not WEB_BROWSER or not DRIVER_PATH:
    raise ValueError("You need setting all environment variables. "
                     "Please see the sample.env file")
