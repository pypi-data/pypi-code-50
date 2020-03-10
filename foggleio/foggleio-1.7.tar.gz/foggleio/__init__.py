import requests

def enabled(tenantId, key, environment, consumer):
    try:
        return requests.get(f'https://api.foggle.io/api/{tenantId}/feature-toggle/{key}/enabled/{environment}/{consumer}').json()
    except:
        return False