from pythonanywhereapiclient.client import Client

base_endpoint = 'webapps/'
client = Client()


def create(domain_name, python_version):
    """Create a new webapp with manual configuration"""
    payload = {
        'domain_name': domain_name,
        'python_version': python_version
    }

    return client.post(base_endpoint, data=payload)


def create_static(domain_name, url, path):
    payload = {
        'url': url,
        'path': path
    }

    return client.post(
        f'{base_endpoint}{domain_name}/static_files/',
        data=payload
    )


def delete(domain_name):
    """Delete the webapp"""
    return client.delete(f'{base_endpoint}{domain_name}/')


def delete_ssl():
    """Delete TLS/HTTPS info"""
    raise NotImplementedError


def delete_static():
    """Remove a static files mapping"""
    raise NotImplementedError


def disable(domain_name):
    """Disable the webapp"""
    return client.post(f'{base_endpoint}{domain_name}/disable/')


def enable(domain_name):
    """Enable the webapp"""
    return client.post(f'{base_endpoint}{domain_name}/enable/')


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
    return client.get(base_endpoint)


def list_static():
    """Get URL and path of a particular mapping"""
    raise NotImplementedError


def modify(domain_name, python_version=None, source_directory=None,
           working_directory=None, virtualenv_path=None, force_https=None):
    """Modify configuration of a web app"""
    kwargs = locals()
    payload = {}

    del kwargs['domain_name']

    for key, value in kwargs.items():
        if value is not None:
            payload[key] = value

    return client.patch(f'{base_endpoint}{domain_name}/', data=payload)


def modify_ssl():
    """Set TLS/HTTPS info"""
    raise NotImplementedError


def modify_static():
    """Modify a static files mapping"""
    raise NotImplementedError


def reload(domain_name):
    """Reload the webapp to reflect changes to configuration and/or source code
     on disk"""
    return client.post(f'{base_endpoint}{domain_name}/reload/')
