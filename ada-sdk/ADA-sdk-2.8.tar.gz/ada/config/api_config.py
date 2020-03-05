import os


ADA_API_URL = os.getenv("ADA_API_URL", "http://10.128.220.229:86/api/")

DEFAULT_HEADERS = {
    'content-type': "application/json"
}
