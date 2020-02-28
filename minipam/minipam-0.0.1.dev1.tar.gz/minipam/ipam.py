"""Mini IPAM using flat YAML file for data storage"""
from collections import OrderedDict
import ipaddress
import logging
import pkg_resources
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper

logging.getLogger('minipam').addHandler(logging.NullHandler())


class MinIpam():
    """Main MiniIpam object"""
    def __init__(self):
        self.version = pkg_resources.get_distribution('minipam').version
        self.networks = self.V4V6()
        self.hosts = dict()
        self.stray_hosts = self.V4V6()
        self.stray_aliases = dict()
        self.logger = logging.getLogger('minipam')

    def __repr__(self):
        return "MinIpam(networks: {}, stray_hosts: {}, stray_aliases: {})". \
            format(len(self.networks.joined()),
                   len(self.stray_hosts.joined()),
                   len(self.stray_aliases))

    def __ordered_items__(self):
        orddict = OrderedDict()
        self.networks.sort('ipnetwork')
        orddict['networks'] = self.networks.joined()
        self.stray_hosts.sort('ipaddress')
        orddict['stray_hosts'] = self.stray_hosts.joined()
        orddict['stray_aliases'] = self.stray_aliases
        return orddict.items()

    def add_network(self, *args, **kwargs):
        """Add and return a network to the MinIpam object
        with given network peramiters"""
        newnetwork = Network(*args, **kwargs)
        tempnetwork = self.get_network(str(newnetwork.ipnetwork))
        if tempnetwork:
            tempnetwork.update(*args, **kwargs)
            return tempnetwork
        if isinstance(newnetwork.ipnetwork, ipaddress.IPv4Network):
            self.networks.ipv4.append(newnetwork)
        elif isinstance(newnetwork.ipnetwork, ipaddress.IPv6Network):
            self.networks.ipv6.append(newnetwork)
        return newnetwork

    def add_host(self, *args, **kwargs):
        """Add and return a host to the appropriate network,
        if it exists, or to the orphaned_hosts list"""
        newhost = Host(*args, **kwargs)
        if newhost.ipaddress in self.hosts.keys():
            self.hosts[newhost.ipaddress].update(*args, **kwargs)
            return self.hosts[newhost.ipaddress]
        self.hosts[newhost.ipaddress] = newhost
        for network in self.networks.joined():
            if newhost.ipaddress in network.ipnetwork:
                network.hosts.append(newhost)
                return newhost
        self.logger.warning('No network found for %s', str(newhost.ipaddress))
        if isinstance(newhost.ipaddress, ipaddress.IPv4Address):
            self.stray_hosts.ipv4.append(newhost)
        elif isinstance(newhost.ipaddress, ipaddress.IPv6Address):
            self.stray_hosts.ipv6.append(newhost)
        return newhost

    def get_network(self, networkstring):
        """Return Network object defined by network string,
        if it exists in the MinIpam object"""
        tempnetwork = Network(network=networkstring)
        for network in self.networks.joined():
            if tempnetwork.ipnetwork == network.ipnetwork:
                return network
        return None

    def get_host_by_ip(self, ipstring):
        """Return Host object defined by the ipstring
        Create a new one if it does not exits in the MinIpam object"""
        temphost = Host(ip=ipstring)
        if temphost.ipaddress in self.hosts.keys():
            return self.hosts[temphost.ipaddress]
        return self.add_host(ip=ipstring)

    def get_host_by_name(self, hostname):
        """Return Host object with the given hostname,
        if it exits in the MinIpam object"""
        for host in self.hosts.values():
            if hostname in host.hostname:
                return host
        self.logger.warning('No host found with hostname %s', hostname)
        return None

    def add_alias(self, hostname, alias):
        """Add alias record to the host with the given hostname,
        else add it to the stray_aliases"""
        temphost = self.get_host_by_name(hostname)
        if temphost:
            temphost.hostname[hostname].append(alias)
        elif hostname in self.stray_aliases.keys():
            self.stray_aliases[hostname].append(alias)
        else:
            self.stray_aliases[hostname] = list([alias])

    def load_yaml(self, yamlfile):
        """Populate MinIpam ojectct with values from given YAML file"""
        networkfile = open(yamlfile, 'r')
        yamldict = yaml.load(networkfile.read(), Loader=Loader)
        networkfile.close()
        for yamlnetwork in yamldict['networks']:
            self.add_network(yamlnetwork)
            for yamlhost in yamlnetwork['hosts']:
                self.add_host(yamlhost)
        for yamlhost in yamldict['stray_hosts']:
            self.add_host(yamlhost)
        for yamlhostname in yamldict['stray_aliases'].keys():
            for yamlalias in yamldict['stray_aliases'][yamlhostname]:
                self.add_alias(yamlhostname, yamlalias)

    def save_yaml(self, yamlfile):
        """Save MinIpam object to YAML file"""

        def net_host_representer(self, data):
            """YAML representer used for Network and Host objects"""
            return self.represent_mapping('tag:yaml.org,2002:map',
                                          data.__ordered_items__())

        yaml.add_representer(MinIpam, net_host_representer, Dumper=Dumper)
        yaml.add_representer(Network, net_host_representer, Dumper=Dumper)
        yaml.add_representer(Host, net_host_representer, Dumper=Dumper)

        for network in self.networks.joined():
            network.hosts.sort(key=lambda x: x.ipaddress)
        networkfile = open(yamlfile, 'w')
        networkfile.write(yaml.dump(self, Dumper=Dumper))
        networkfile.close()

    class V4V6():
        """Seperate IPv4 and IPv6 objects"""
        def __init__(self):
            self.ipv4 = list()
            self.ipv6 = list()

        def sort(self, attribute):
            """sort ipv4 and ipv6 lists by given attribute"""
            self.ipv4.sort(key=lambda x: getattr(x, attribute))
            self.ipv6.sort(key=lambda x: getattr(x, attribute))

        def joined(self):
            """return list ipv4 + ipv6"""
            return self.ipv4 + self.ipv6


class Network():
    """Simple Network object"""
    def __init__(self, *args, **kwargs):
        self.ipnetwork = None
        self.gateway = None
        self.vlan = None
        self.dhcp_range = None
        self.notes = None
        self.hosts = list()
        self.update(*args, **kwargs)
        if not self.ipnetwork:
            raise TypeError("missing required argument: 'network'")

    def __repr__(self):
        return "Network('{}, {}, {}, {}')". \
            format(str(self.ipnetwork),
                   str(self.ipnetwork.netmask),
                   self.gateway,
                   self.notes)

    def __setattr__(self, name, value):
        if name == 'network':
            self.ipnetwork = ipaddress.ip_network(value)
        elif name == 'hosts':
            if not hasattr(self, 'hosts'):
                object.__setattr__(self, 'hosts', list())
        elif name.lower() in ['vlan', 'dhcp_range']:
            object.__setattr__(self, name.lower(), value)
        else:
            object.__setattr__(self, name, value)

    def __ordered_items__(self):
        orddict = OrderedDict()
        orddict['network'] = str(self.ipnetwork)
        orddict['netmask'] = str(self.ipnetwork.netmask)
        orddict['gateway'] = self.gateway
        orddict['VLAN'] = self.vlan
        orddict['DHCP_range'] = self.dhcp_range
        orddict['notes'] = self.notes
        orddict['hosts'] = self.hosts
        return orddict.items()

    def update(self, *args, **kwargs):
        """Set attributes with given dict or keyword argumenst"""
        for key, value in dict(*args, **kwargs).items():
            self.__setattr__(key, value)


class Host():
    """Simple Host object"""
    def __init__(self, *args, **kwargs):
        self.ipaddress = None
        self.mac = None
        self.reserved = False
        self.hostname = dict()
        self.notes = None
        self.update(*args, **kwargs)
        if not self.ipaddress:
            raise TypeError("missing required argument: 'ip'")

    def __repr__(self):
        return "Host('{} {} {} #{}')". \
            format(str(self.ipaddress), self.hostname, self.mac, self.notes)

    def __setattr__(self, name, value):
        if name.lower() == 'ip':
            self.ipaddress = ipaddress.ip_address(value)
        elif name.lower() == 'mac':
            object.__setattr__(self, name.lower(), value)
        elif name == 'hostname':
            if not hasattr(self, 'hostname'):
                object.__setattr__(self, 'hostname', dict())
            if isinstance(value, dict):
                for hostname in value.keys():
                    self.add_hostname(hostname, *value[hostname])
            elif isinstance(value, str):
                self.add_hostname(value)
            else:
                raise TypeError("'hostname' must be type dict or str")
        else:
            object.__setattr__(self, name, value)

    def __ordered_items__(self):
        orddict = OrderedDict()
        orddict['IP'] = str(self.ipaddress)
        if self.mac:
            orddict['MAC'] = self.mac
        if self.reserved:
            orddict['reserved'] = self.reserved
        if len(self.hostname) > 0:
            orddict['hostname'] = self.hostname
        if self.notes:
            orddict['notes'] = self.notes
        return orddict.items()

    def update(self, *args, **kwargs):
        """Set attributes with given dict or keyword argumenst"""
        for key, value in dict(*args, **kwargs).items():
            self.__setattr__(key, value)

    def add_hostname(self, hostname, *args):
        """Add hostname to Host if it doesn't exist.
        Args will be added as aliases to the hostname"""
        if hostname not in self.hostname:
            self.hostname[hostname] = list()
        for arg in args:
            self.hostname[hostname].append(arg)
