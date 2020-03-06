import re
from urllib import parse as urlparse


def normalise_url(url, prefix):
    """Convert URL to lower case, remove trailing slash and add prefix."""
    url = url.lower().rstrip('/')
    return f'{prefix}{url}'


def convert_url(url):
    if url.startswith("http"):
        url = urlparse.urlparse(url).path

    return re.sub(r'^//', '/', re.sub(r'([^:])/+', r'\1/', url))


def sanitise_url(url, regexes):
    """Convert URL to expected format, based on regex(es) provided, if possible.

    Args:
        url (str): URL to sanitise.
        regexes (list): Regular expressions to match the URL against.

    Returns:
        str: URL match for one of the regular expressions or the original URL.
    """
    for regex in regexes:
        matched = re.search(regex, url)
        if matched is not None:
            return matched.group()

    return url


def prepare_url(path, prefix, regexes):
    """Convert, normalise and sanitise a path from a GA report.

    Args:
        path (str): Site path  from a GA report.
        prefix (str): prefix that precedes a path in the URL matched.
        regexes (list): Regular expressions to match the URL against.

    Returns:
        str: URL of a hit from a GA report.
    """
    return sanitise_url(
        normalise_url(
            convert_url(path),
            prefix),
        regexes
    )


def standardise_row(row):
    """Adds path value '/' to GA report row if it is missing.

    Args:
        row (list): Values from a row in the GA report.

    Returns:
        list: Values from a row in the GA report.
    """
    if len(row) == 2:
        row = ['/'] + row
    return row
