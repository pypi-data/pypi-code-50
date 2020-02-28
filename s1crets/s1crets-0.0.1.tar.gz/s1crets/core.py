from __future__ import absolute_import
import importlib


DOCSTRINGS = {
    'provider': 'provider (str): Secret provider (aws.sm|aws.ps)',
    'path': 'path (str): path for the given secret',
    'keypath': 'keypath (list): the key path for looking into a JSON secret'}


class DictQuery(dict):
    def get(self, keys, default=None):
        val = None

        for key in keys:
            if val:
                if isinstance(val, list):
                    val = [v.get(key, default) if v else None for v in val]
                else:
                    try:
                        val = val.get(key, default)
                    except AttributeError:
                        return default
            else:
                val = dict.get(self, key, default)

            if val == default:
                break
        return val


def _get_provider(provider, **params):
    m = importlib.import_module(name='.{}'.format(provider),
                                package='s1crets.providers')
    return m.SecretProvider(**params)


def docstring_parameter(sub):
    def dec(obj):
        obj.__doc__ = obj.__doc__.format(**sub)
        return obj
    return dec


@docstring_parameter(DOCSTRINGS)
def get(provider='aws.sm', path=None, keypath=None):
    """Get a secret from the given `provider`

    Args:
        {provider}
        {path}
        {keypath}

    Returns:
        secret: The returned secret, can be string, bytes or in case of JSON, a dictionary
    """
    p = _get_provider(provider)
    return p.get(path, keypath=keypath)


@docstring_parameter(DOCSTRINGS)
def path_exists(provider='aws.sm', path=None, keypath=None):
    """Check whether the path exists in the secrets provider

    Args:
        {provider}
        {path}
        {keypath}

    Returns:
        secret: The returned secret, can be string, bytes or in case of JSON, a dictionary
    """
    p = _get_provider(provider)
    return p.path_exists(path, keypath=keypath)


@docstring_parameter(DOCSTRINGS)
def get_by_path(provider='aws.sm', path=None):
    """Returns all secrets beneath a path (if the provider supports it)

    Args:
        {provider}
        {path}

    Returns:
        secrets (list): List of returned secrets
    """
    p = _get_provider(provider)
    return p.get_by_path(path)


@docstring_parameter(DOCSTRINGS)
def update(provider='aws.sm', path=None, value=None):
    """Updates secret with given value

    Args:
        {provider}
        {path}
        value (string, bytes): the value to be stored

    Returns:
        None
    """

    p = _get_provider(provider)
    return p.update(path, value)
