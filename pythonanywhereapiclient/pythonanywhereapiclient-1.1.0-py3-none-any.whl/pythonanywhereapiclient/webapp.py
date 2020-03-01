from requests import codes

from pythonanywhereapiclient.client import Client
from pythonanywhereapiclient.error import QuotaError, ResponseError
from pythonanywhereapiclient.utils import construct_request_payload

base_endpoint = 'webapps/'
client = Client()


def create(domain_name, python_version):
    """Create a new webapp with manual configuration"""
    response = client.post(
        base_endpoint,
        data=construct_request_payload(locals())
    )

    if response.status_code == codes.CREATED:
        return response.json()
    elif response.status_code == codes.BAD_REQUEST:
        raise QuotaError(response.json()['error_message'])
    else:
        raise ResponseError(response)


def create_static(domain_name, url, path):
    response = client.post(
        f'{base_endpoint}{domain_name}/static_files/',
        data=construct_request_payload(locals())
    )

    if response.status_code == codes.CREATED:
        return response.json()
    else:
        raise ResponseError(response)


def delete(domain_name):
    """Delete the webapp"""
    response = client.delete(f'{base_endpoint}{domain_name}/')

    if response.status_code == codes.NO_CONTENT:
        return
    else:
        raise ResponseError(response)


def delete_ssl():
    """Delete TLS/HTTPS info"""
    raise NotImplementedError


def delete_static():
    """Remove a static files mapping"""
    raise NotImplementedError


def disable(domain_name):
    """Disable the webapp"""
    response = client.post(f'{base_endpoint}{domain_name}/disable/')

    if response.status_code == codes.OK:
        return
    else:
        raise ResponseError(response)


def enable(domain_name):
    """Enable the webapp"""
    response = client.post(f'{base_endpoint}{domain_name}/enable/')

    if response.status_code == codes.OK:
        return
    else:
        raise ResponseError(response)


def get():
    """Return information about a web app's configuration"""
    raise NotImplementedError


def get_ssl():
    """Get TLS/HTTPS info"""
    raise NotImplementedError


def get_static():
    """Get TLS/HTTPS info"""
    raise NotImplementedError


def list():
    """List all webapps"""
    response = client.get(base_endpoint)

    if response.status_code == codes.OK:
        return response.json()
    else:
        raise ResponseError(response)


def list_static():
    """Get URL and path of a particular mapping"""
    raise NotImplementedError


def modify(domain_name, python_version=None, source_directory=None,
           working_directory=None, virtualenv_path=None, force_https=None):
    """Modify configuration of a web app"""
    response = client.patch(
        f'{base_endpoint}{domain_name}/',
        data=construct_request_payload(locals())
    )

    if response.status_code == codes.OK:
        return response.json()
    else:
        raise ResponseError(response)


def modify_ssl():
    """Set TLS/HTTPS info"""
    raise NotImplementedError


def modify_static():
    """Modify a static files mapping"""
    raise NotImplementedError


def reload(domain_name):
    """Reload the webapp to reflect changes to configuration and/or source code
     on disk"""
    response = client.post(f'{base_endpoint}{domain_name}/reload/')

    if response.status_code == codes.OK:
        return
    else:
        raise ResponseError(response)
