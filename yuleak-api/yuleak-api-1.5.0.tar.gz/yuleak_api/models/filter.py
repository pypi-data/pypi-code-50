from yuleak_api.client import YuleakClient


class Filter:
    """Filter model."""
    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.value = None
        self.type = None
        self.category = None

    @classmethod
    def from_json(cls, filter_json, dashboard):
        filter_ = cls(dashboard)
        filter_.value = filter_json.get('value')
        filter_.type = filter_json.get('type', 'required')
        filter_.category = filter_json.get('category')
        return filter_

    def delete(self):
        """Delete the current filter

        See https://app.yuleak.com/apidoc#delete-filters for endpoint details.

        Returns:
            (bool) True if the filter has been deleted
        """
        return YuleakClient.delete_request('dashboard/{0}/filters'.format(self.dashboard.id),
                                           params={'value': self.value,
                                                   'category': self.category})

    def __repr__(self):
        return '<Filter> {0}:{1}'.format(self.category, self.value)
