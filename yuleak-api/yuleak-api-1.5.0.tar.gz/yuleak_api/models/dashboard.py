from yuleak_api.client import YuleakClient

from .marker import Marker
from .node import Node
from .event import Event
from .server import Server
from .resource import Resource
from .filter import Filter
from .dnsentry import DNSEntry


class Dashboard:
    """Dashboard model"""
    BASE_STATS = {'server': 0,
                  'domain': 0,
                  'service': 0,
                  'alert': 0,
                  'hacked': 0,
                  'vulnerability': 0,
                  'leakcreds': 0,
                  'leak': 0,
                  'filedisclosure': 0,
                  'weakservice': 0,
                  'proxy': 0,
                  'tornode': 0,
                  'onion': 0,
                  'blacklist': 0,
                  'phishingurl': 0,
                  'ssl': 0,
                  'paste': 0,
                  'warez': 0,
                  'repository': 0,
                  'social_networks': 0,
                  'ids': 0,
                  'domain_expiration': 0,
                  'cryptowallet': 0}

    def __init__(self, id_, name):
        self.id = id_
        self.name = name

    def stats(self):
        """Get the current dashboard statistics (similar to dahboard view in WebUI).

        See https://app.yuleak.com/apidoc#get-dashboard for endpoint details.

        Returns:
            dict containing statistics
        """
        stats = self.BASE_STATS.copy()
        data = YuleakClient.get_request('dashboard/{0}'.format(self.id))
        if len(data) == 0:
            return stats
        for k, v in data[0].items():
            stats[k] = v
        return stats

    def statsdns(self):
        """Get the current dashboard DNS (Typosquatting) stats (similare to dns view in WebUI).

        See https://app.yuleak.com/apidoc#get-statsdns for endpoint details.

        Returns:
            dict containing statistics
        """
        data = YuleakClient.get_request('dashboard/{0}/statsdns'.format(self.id))
        if len(data) == 0:
            return []
        return data[0]

    def map(self):
        """Get the current dashboard map markers (similar to map widget in WebUI).

        See https://app.yuleak.com/apidoc#get-map for endpoint details.

        Returns:
            list of Marker items
        """
        results = []
        for d in YuleakClient.get_request('dashboard/{0}/map'.format(self.id)):
            results.append(Marker.from_json(d))
        return results

    def graph(self):
        """Get the current dashboard graph (similar to graph view in WebUI).

        See https://app.yuleak.com/apidoc#get-graph for endpoint details.

        Returns:
            list of Node items
        """
        results = {}
        data = YuleakClient.get_request('dashboard/{0}/graph'.format(self.id))
        if len(data) == 0:
            return []
        # Nodes
        for n in data[0].get('nodes', []):
            results[n.get('id')] = Node.from_json(n)
        # Edges
        for e in data[0].get('edges', []):
            parent_node = results.get(e[0])
            child_node = results.get(e[1])
            if parent_node is None or child_node is None:
                continue
            parent_node.connect(child_node)
        return list(results.values())

    def timeline(self):
        """Get the current dashboard timeline (similar to timeline widget in WebUI).

        See https://app.yuleak.com/apidoc#get-timeline for endpoint details.

        Returns:
            list of Event items
        """
        results = []
        for d in YuleakClient.get_request('dashboard/{0}/timeline'.format(self.id)):
            results.append(Event.from_json(d))
        return results

    def details(self):
        """Get the current dashboard servers (similar to details view in WebUI).

        See https://app.yuleak.com/apidoc#get-details for endpoint details.

        Returns:
            list of Server items
        """
        results = []
        for d in YuleakClient.get_request('dashboard/{0}/details'.format(self.id)):
            results.append(Server.from_json(d, self))
        return results

    def dns(self):
        """Get the current dashboard typosquatting dns entries (similar to dns view in WebUI).

        See https://app.yuleak.com/apidoc#get-dns for endpoint details.

        Returns:
            list of DNSEntry items
        """
        results = []
        for d in YuleakClient.get_request('dashboard/{0}/dns'.format(self.id)):
            results.append(DNSEntry.from_json(d))
        return results

    def resources(self):
        """Get the current dashboard resources (similar to resources list widget in WebUI).

        See https://app.yuleak.com/apidoc#get-resources for endpoint details.

        Returns:
            list of Resource items
        """
        results = []
        for d in YuleakClient.get_request('dashboard/{0}/resources'.format(self.id)):
            results.append(Resource.from_json(d, self))
        return results

    def renew_cost(self):
        """Get the cost to renew all resources

        See https://app.yuleak.com/apidoc#get-renewall for endpoint details.

        Returns:
            (int) Amount of credits
        """
        data = YuleakClient.get_request('dashboard/{0}/renewall'.format(self.id))
        if len(data) == 0:
            return 0
        return data[0].get('credits', 0)

    def renew_all(self):
        """Re-launch all resources of the current dashboard.

        See https://app.yuleak.com/apidoc#post-renewall for endpoint details.

        Returns:
            (bool) True if the search has been launched
        """
        return YuleakClient.post_request('dashboard/{0}/renewall'.format(self.id))

    def filters(self):
        """Get the current dashboard active filters (similar to filters list widget in WebUI).

        See https://app.yuleak.com/apidoc#get-filters for endpoint details.

        Returns:
            list of Filter items
        """
        results = []
        for d in YuleakClient.get_request('dashboard/{0}/filters'.format(self.id)):
            results.append(Filter.from_json(d, self))
        return results

    def add_filter(self, category, value, type_='required'):
        """Add a filter to the current dashboard.

        See https://app.yuleak.com/apidoc#post-filters for endpoint details.

        Args:
            category (str): Filter category (server, domain, alert, date)
            value (str): Filter value (all, blacklist, cloudflare ...)
            type_ (str): Filter type: required (by default) or ignored

        Returns:
            True if the filter has been added
        """
        return YuleakClient.post_request('dashboard/{0}/filters'.format(self.id),
                                         data={'category': category,
                                               'value': value,
                                               'type': type_})

    def search(self, search):
        """Launch a new search (credits will be used) in the current dashboard.

        See https://app.yuleak.com/apidoc#post-search for endpoint details.

        Args:
            search (str): Expression to search

        Returns:
            (bool) True if the search has been launched
        """
        return YuleakClient.post_request('dashboard/{0}/search'.format(self.id), data={'value': search})

    def list_new_servers(self):
        """Get list of servers not in resources.

        See https://app.yuleak.com/apidoc#get-searchall for endpoint details.

        Returns:
            list of ip (string)
        """
        return YuleakClient.get_request('dashboard/{0}/searchall'.format(self.id))

    def searchall(self):
        """Search all servers not listed in resources (credits will be used).

        See https://app.yuleak.com/apidoc#post-searchall for endpoint details.

        Returns:
            (bool) True if the search has been launched
        """
        return YuleakClient.post_request('dashboard/{0}/searchall'.format(self.id))

    def delete(self):
        """Delete the current dashboard and all its data.

        See https://app.yuleak.com/apidoc#post-delete for endpoint details.

        Returns:
            (bool) True if the dashboard has been deleted
        """
        return YuleakClient.delete_request('dashboard/{0}'.format(self.id))

    def __repr__(self):
        return '<Dashboard {0}> {1}'.format(self.id, self.name)
