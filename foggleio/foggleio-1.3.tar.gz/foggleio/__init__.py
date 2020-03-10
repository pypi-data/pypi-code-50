import requests

def enabled(tenantId, key, environment, consumer):
    return requests.get('https://api.github.com/repos/psf/requests')