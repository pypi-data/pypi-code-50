from requests import codes

from pythonanywhereapiclient.client import Client
from pythonanywhereapiclient.error import QuotaError, ResponseError
from pythonanywhereapiclient.utils import construct_request_payload

base_endpoint = 'schedule/'
client = Client()


def create(command, enabled=True, interval='daily', hour=0, minute=0):
    """Create a new scheduled task"""
    response = client.post(
        base_endpoint,
        data=construct_request_payload(locals())
    )

    if response.status_code == codes.CREATED:
        return response.json()
    elif response.status_code == codes.FORBIDDEN:
        raise QuotaError(response.json()['detail'])
    else:
        raise ResponseError(response)


def delete(id):
    """Delete an scheduled task"""
    response = client.delete(f'{base_endpoint}{id}/')

    if response.status_code == codes.NO_CONTENT:
        return
    else:
        raise ResponseError(response)


def get(id):
    """Return information about a scheduled task"""
    response = client.get(f'{base_endpoint}{id}/')

    if response.status_code == codes.OK:
        return response.json()
    else:
        raise ResponseError(response)


def list():
    """List all of your scheduled tasks"""
    response = client.get(base_endpoint)

    if response.status_code == codes.OK:
        return response.json()
    else:
        raise ResponseError(response)


def modify():
    """Modify a scheduled task"""
    raise NotImplementedError
