import dateutil.parser

from yuleak_api.client import YuleakClient


class Resource:
    """Resource model."""
    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.value = None
        self.type = None
        self.date = None
        self.status = None

    @classmethod
    def from_json(cls, src_json, dashboard):
        src = cls(dashboard)
        src.value = src_json.get('value')
        src.type = src_json.get('type')
        src.date = dateutil.parser.parse(src_json.get('date'))
        src.status = src_json.get('status')
        return src

    def renew(self):
        """Launch a new search for the current resource (credits will be consumed)

        See https://app.yuleak.com/apidoc#post-renew for endpoint details.

        Returns:
            (bool) True if the search has been launched
        """
        return YuleakClient.post_request('dashboard/{0}/renew'.format(self.dashboard.id), data={'value': self.value})

    def delete(self):
        """Delete the current resource and all data linked

        See https://app.yuleak.com/apidoc#delete-resources for endpoint details.

        Returns:
            (bool) True if the search has been launched
        """
        return YuleakClient.delete_request('dashboard/{0}/resources'.format(self.dashboard.id), params={'value': self.value})

    def __repr__(self):
        return '<Resource> {0} - {1}'.format(self.type, self.value)
