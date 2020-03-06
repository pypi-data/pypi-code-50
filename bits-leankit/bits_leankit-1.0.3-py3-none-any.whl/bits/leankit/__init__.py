# -*- coding: utf-8 -*-
"""Initialize the bits/leankit module."""

import requests


class Leankit(object):
    """Example class."""

    def __init__(self, host, username, password, verbose=False):
        """Initialize an Leankit class instance."""
        self.host = host
        self.username = username
        self.password = password
        self.verbose = verbose

        self.base_url = 'https://{}/io/scim/v1'.format(self.host)
        self.auth = (self.username, self.password)
        self.token = self._get_token()

        self.headers = {
            'Authorization': 'Bearer {}'.format(self.token),
            'Content-Type': 'application/json',
        }

    #
    # Sub-Classes
    #
    def client(self, auth):
        """Return an instance of the client class."""
        from .client import Client
        return Client(auth, self)

    #
    # Private methods
    #
    def _get_list(self, url, params=None):
        """Return a paginated list of items."""
        if not params:
            params = {}

        data = requests.get(url, headers=self.headers, params=params).json()

        resources = data.get('Resources', [])
        items_per_page = data.get('itemsPerPage', 0)
        start_index = data.get('startIndex', 0)
        total_results = data.get('totalResults', 0)

        while len(resources) < total_results:
            print('Get another page...')
            params['startIndex'] = start_index + items_per_page
            data = requests.get(url, headers=self.headers, params=params).json()

            resources.extend(data.get('Resources', []))
            items_per_page = data.get('itemsPerPage', 0)
            start_index = data.get('startIndex', 0)

        return resources

    def _get_token(self):
        """Return an auth token."""
        url = 'https://{}/io/auth/token'.format(self.host)
        body = {
            'description': 'bits-leankit python package',
        }
        return requests.post(url, data=body, auth=self.auth).json().get('token')

    #
    # Endpoints
    #
    def create_user(self, user):
        """Create a user in Leankit."""
        url = '{}/Users'.format(self.base_url)
        return requests.post(url, json=user, headers=self.headers).json()

    def delete_user(self, user_id):
        """Delete a user in Leankit."""
        url = '{}/Users/{}'.format(self.base_url, user_id)
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
        return True

    def disable_user(self, user_id):
        """Delete a user in Leankit."""
        user = self.get_user(user_id)
        user['active'] = False
        return self.update_user(user['id'], user)

    def get_user(self, user_id):
        """Return a user in Leankit."""
        url = '{}/Users/{}'.format(self.base_url, user_id)
        return requests.get(url, headers=self.headers).json()

    def get_users(self, searchfilter=None):
        """Return a list of users in Leankit."""
        url = '{}/Users'.format(self.base_url)
        params = {
            'count': 200,
            'filter': searchfilter,
        }
        return self._get_list(url, params=params)

    def update_user(self, user_id, user):
        """Update a user in Leankit."""
        url = '{}/Users/{}'.format(self.base_url, user_id)
        return requests.put(url, json=user, headers=self.headers).json()

    #
    # Helpers
    #
    def prepare_user(self, first_name, last_name, email, external_id=None):
        """Prepare a user for Leankit."""
        user = {
            'active': True,
            'externalId': external_id,
            # 'id': None,
            # 'meta': None,
            'name': {
                'familyName': last_name,
                'givenName': first_name,
                'formatted': '{} {}'.format(first_name, last_name),
            },
            'timezone': 'America/New_York',
            'userName': email,
            'urn:scim:schemas:extension:leankit:user:1.0': {
                'licenseType': 'full',
                # 'lastAccess': '2019-11-15T20:04:32Z',
                'administrator': False,
                'boardCreator': False,
                'dateFormat': 'mm/dd/yyyy'
            }
        }
        return user
