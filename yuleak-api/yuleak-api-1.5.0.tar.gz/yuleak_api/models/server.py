import requests
import dateutil.parser

from yuleak_api.client import YuleakClient
from yuleak_api.logs import logger

# Python2 support
try:
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError


class Geo:
    def __init__(self):
        self.country_code = None
        self.country_name = None
        self.city = None
        self.latitude = None
        self.longitude = None


class Whois:
    def __init__(self):
        self.range = None
        self.name = None
        self.organisation = None
        self.asn = None


class Domain:
    def __init__(self):
        self.id = None
        self.parent = None
        self.value = None
        self.in_src = False
        self.tags = []
        self.risk = 0
        self.screenshot= None

    @classmethod
    def from_json(cls, domain_json, parent=None):
        domain = cls()
        domain.id = domain_json.get('id')
        domain.parent = parent
        domain.value = domain_json.get('value')
        domain.in_src = domain_json.get('in_src', False)
        domain.tags = domain_json.get('tags', [])
        domain.risk = domain_json.get('risk', 0)
        screenshot_url = domain_json.get('screenshot', None)
        if screenshot_url is not None:
            domain.screenshot = ScreenShot(screenshot_url)
        return domain

    def __repr__(self):
        return '<Domain {0}> {1}'.format(self.id, self.value)


class ScreenShot:
    def __init__(self, url):
        self.url = url

    def download(self, filepath, timeout=30):
        try:
            req = requests.get(self.url, timeout=timeout)
            with open(filepath, 'wb') as fc:
                fc.write(req.content)
            return True
        except requests.exceptions.RequestException as e:
            logger.error(e)
            return False
        except FileNotFoundError as e:
            logger.error(e)
            return False

class Service:
    def __init__(self):
        self.id = None
        self.parent = None
        self.port = 0
        self.date = None
        self.first_seend = None
        self.risk = 0
        self.weak = False
        self.protocol = 'tcp'
        self.name = None
        self.version = None

    @classmethod
    def from_json(cls, service_json, parent=None):
        service = cls()
        service.id = service_json.get('id')
        service.parent = parent
        service.port = service_json.get('port',0)
        service.date = dateutil.parser.parse(service_json.get('date'))
        service.first_seend = dateutil.parser.parse(service_json.get('first_seen'))
        service.risk = service_json.get('risk', 0)
        service.weak = service_json.get('weak', False)
        service.protocol = service_json.get('protocol', 'tcp')
        service.name = service_json.get('name')
        service.version = service_json.get('version')
        return service

    def __repr__(self):
        return '<Service {0}> {1} {2} - {3}'.format(self.id, self.protocol, self.port, self.name)


class Alert:
    def __init__(self):
        self.id = None
        self.parent = None
        self.date = None
        self.first_seen = None
        self.type = None
        self.value = None
        self.risk = 0
        self.link = None

    @classmethod
    def from_json(cls, alert_json, parent=None):
        alert = cls()
        alert.id = alert_json.get('id')
        alert.parent = parent
        alert.date = dateutil.parser.parse(alert_json.get('date'))
        alert.first_seen = dateutil.parser.parse(alert_json.get('first_seen'))
        alert.type = alert_json.get('type')
        alert.value = alert_json.get('value')
        alert.risk = alert_json.get('risk', 0)
        alert.link = alert_json.get('link')
        return alert

    def __repr__(self):
        return '<Alert {0}> {1} - {2}'.format(self.id, self.type, self.value)


class Leak:
    def __init__(self):
        self.id = None
        self.parent = None
        self.date = None
        self.first_seen = None
        self.risk = 0
        self.email = None
        self.password = None

    @classmethod
    def from_json(cls, leak_json, parent=None):
        leak = cls()
        leak.id = leak_json.get('id')
        leak.parent = parent
        leak.date = dateutil.parser.parse(leak_json.get('date'))
        leak.first_seen = dateutil.parser.parse(leak_json.get('first_seen'))
        leak.risk = leak_json.get('risk', 0)
        leak.email = leak_json.get('email')
        leak.password = leak_json.get('password')
        return leak

    def __repr__(self):
        return '<Leak {0}> {1}'.format(self.id, self.email)


class SocialNetwork:
    def __init__(self):
        self.id = None
        self.parent = None
        self.date = None
        self.first_seen = None
        self.platform = None
        self.login = None
        self.link = None
        self.icon = None
        self.risk = 0

    @classmethod
    def from_json(cls, sn_json, parent=None):
        sn = cls()
        sn.id = sn_json.get('id')
        sn.parent = parent
        sn.date = dateutil.parser.parse(sn_json.get('date'))
        sn.first_seen = dateutil.parser.parse(sn_json.get('first_seen'))
        sn.risk = sn_json.get('risk', 0)
        sn.platform = sn_json.get('platform')
        sn.login = sn_json.get('login')
        sn.link = sn_json.get('link')
        sn.icon = sn_json.get('icon')
        return sn

    def __repr__(self):
        return '<SocialNetwork {0}> {1} - {2}'.format(self.id, self.platform, self.login)


class ID:
    def __init__(self):
        self.id = None
        self.parent = None
        self.date = None
        self.first_seen = None
        self.risk = 0
        self.type = None
        self.value = None

    @classmethod
    def from_json(cls, id_json, parent=None):
        id_ = cls()
        id_.id = id_json.get('id')
        id_.parent = parent
        id_.date = dateutil.parser.parse(id_json.get('date'))
        id_.first_seen = dateutil.parser.parse(id_json.get('first_seen'))
        id_.risk = id_json.get('risk', 0)
        id_.type = id_json.get('type')
        id_.value = id_json.get('value')
        return id_

    def __repr__(self):
        return '<ID {0}> {1} - {2}'.format(self.id, self.type, self.value)


class Server:
    """Server model"""
    def __init__(self, dashboard):
        self.dashboard = dashboard
        self.id = None
        self.ip = None
        self.cloudflare = False
        self.in_src = False
        self.bookmark = None
        self.risk = None
        self.logo = None
        self.os = None
        self.equipment = None
        self.geo = Geo()
        self.whois = Whois()
        self.domains = []
        self.services = []
        self.alerts = []
        self.leaks = []
        self.social_networks = []
        self.ids = []

    def add_bookmark(self):
        """Add a bookmark to the current server.

        See https://app.yuleak.com/apidoc#post-bookmark for endpoint details.

        Returns:
            (bool) True if the bookmark have been added
        """
        if self.bookmark:
            logger.warning('The server is already bookmarked.')
        if YuleakClient.post_request('dashboard/{0}/server/{1}/bookmark'.format(self.dashboard.id, self.id)):
            self.bookmark = True
        return self.bookmark

    def del_bookmark(self):
        """Delete the bookmark of the current server.

        See https://app.yuleak.com/apidoc#delete-bookmark for endpoint details.

        Returns:
            (bool) True if the bookmark have been deleted
        """
        if not self.bookmark:
            logger.warning('The server is not bookmarked.')
        if YuleakClient.delete_request('dashboard/{0}/server/{1}/bookmark'.format(self.dashboard.id, self.id)):
            self.bookmark = False
            return True
        else:
            return False

    def _get_element_by_id(self, element_id):
        if element_id == self.id:
            return self
        for d in self.domains:
            if element_id == d.id:
                return d
        for s in self.services:
            if element_id == s.id:
                return s
        return None

    @classmethod
    def from_json(cls, server_json, dashboard):
        server = cls(dashboard)
        server.id = server_json.get('id')
        server.ip = server_json.get('ip')
        server.cloudflare = server_json.get('cloudflare', False)
        server.in_src = server_json.get('in_src', False)
        server.bookmark = server_json.get('bookmark')
        server.risk = server_json.get('risk', 0)
        server.logo = server_json.get('logo')
        server.os = server_json.get('os')
        server.equipment = server_json.get('equipment')

        server.geo.country_code = server_json.get('country_code')
        server.geo.country_name = server_json.get('country_name')
        server.geo.city = server_json.get('geo_city')
        server.geo.latitude = server_json.get('geo_lat')
        server.geo.longitude = server_json.get('geo_long')
        server.whois.name = server_json.get('whois_name')
        server.whois.organisation = server_json.get('whois_organisation')
        server.whois.range = server_json.get('whois_range')
        server.whois.asn = server_json.get('whois_as')

        for d in server_json.get('domains'):
            server.domains.append(Domain.from_json(d, server))
        for s in server_json.get('services'):
            server.services.append(Service.from_json(s, server))
        for a in server_json.get('alerts'):
            server.alerts.append(Alert.from_json(a, server._get_element_by_id(a.get('parent'))))
        for l in server_json.get('leaks'):
            server.leaks.append(Leak.from_json(l, server._get_element_by_id(l.get('parent'))))
        for s in server_json.get('social_networks'):
            server.social_networks.append(SocialNetwork.from_json(s, server._get_element_by_id(s.get('parent'))))
        for i in server_json.get('ids'):
            server.ids.append(SocialNetwork.from_json(i, server._get_element_by_id(i.get('parent'))))
        return server

    def __repr__(self):
        return '<Server {0}> {1}'.format(self.id, self.ip)
