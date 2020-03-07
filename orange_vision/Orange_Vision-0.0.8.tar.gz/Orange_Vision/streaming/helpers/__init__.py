import json
from datetime import datetime
from threading import Thread

from . import utils
from .warnings import *
from .utils import warn_with_ignore




def check_outdated(package, version):
    """
    Given the name of a package on PyPI and a version (both strings), checks
    if the given version is the latest version of the package available.

    Returns a 2-tuple (is_outdated, latest_version) where
    is_outdated is a boolean which is True if the given version is earlier
    than the latest version, which is the string latest_version.

    Attempts to cache on disk the HTTP call it makes for 24 hours. If this
    somehow fails the exception is converted to a warning (OutdatedCacheFailedWarning)
    and the function continues normally.
    """

    from pkg_resources import parse_version

    parsed_version = parse_version(version)
    latest = None

    # with utils.cache_file(package, 'r') as f:
    #     content = f.read()
    #     if content:  # in case cache_file fails and so f is a dummy file
    #         latest, cache_dt = json.loads(content)
    #         if not utils.cache_is_valid(cache_dt):
    #             latest = None

    def get_latest():
        url = 'https://pypi.python.org/pypi/%s/json' % package
        response = utils.get_url(url)
        return json.loads(response)['info']['version']

    if latest is None:
        latest = get_latest()

    parsed_latest = parse_version(latest)

    if parsed_version > parsed_latest:

        # Probably a stale cached value
        latest = get_latest()
        parsed_latest = parse_version(latest)

        if parsed_version > parsed_latest:
            print(f'you are ahead current{version}, latest on Pypi {latest}')
            oudated = False
            return oudated, latest
           
    is_latest = parsed_version == parsed_latest
    assert is_latest or parsed_version < parsed_latest
    with utils.cache_file(package, 'w') as f:
        data = [latest, utils.format_date(datetime.now())]
        json.dump(data, f)

    return not is_latest, latest

