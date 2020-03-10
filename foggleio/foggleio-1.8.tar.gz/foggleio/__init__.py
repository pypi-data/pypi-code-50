import requests

def enabled(tenantId, environment, key, consumer):
    try:
        return requests.get(f'https://api.foggle.io/api/{tenantId}/feature-toggle/{key}/enabled/{environment}/{consumer}').json()
    except:
        return False