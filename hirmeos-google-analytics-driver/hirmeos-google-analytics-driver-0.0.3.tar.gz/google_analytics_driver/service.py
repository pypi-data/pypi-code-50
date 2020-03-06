"""Code for get_service and initialize_service originally obtained from the
Google Analytics API V3 quick-start examples (Apache License 2.0).

It has since been updated to use google-auth since oauth2client is depreciated,
based on:
https://google-auth.readthedocs.io/en/latest/reference/google.oauth2.service_account.html
"""

import json

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials


def get_service(
        api_name,
        api_version,
        scopes,
        key_file_location=None,
        key_file_content=None,
):
    """Get a service that communicates to a Google API.

    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list auth scopes to authorize for the application.
        key_file_location: The path to a valid service account JSON key file.
        key_file_content: Content of a valid service account JSON key file.

    Returns:
        A service that is connected to the specified API.
    """
    if not key_file_content:
        if not key_file_location:
            raise TypeError('Service account key file details are missing.')

        with open(key_file_location, 'r') as f:
            key_file_content = json.load(f)

    credentials = Credentials.from_service_account_info(
        key_file_content,
        scopes=scopes
    )
    service = build(api_name, api_version, credentials=credentials)

    return service


def initialize_service(key_file_location=None, key_file_content=None):
    """Authenticate and construct a GA service."""

    return get_service(
        api_name='analyticsreporting',
        api_version='v4',
        scopes=['https://www.googleapis.com/auth/analytics.readonly'],
        key_file_location=key_file_location,
        key_file_content=key_file_content,
    )
