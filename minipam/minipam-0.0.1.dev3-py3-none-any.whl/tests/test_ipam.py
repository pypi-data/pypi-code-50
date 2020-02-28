import pytest
from minipam import MinIpam


class TestMinIpam:
    def test_functionality(self):
        ipam = MinIpam()
        print(ipam)

        ipam.add_network(network='192.168.0.0/24')
        ipam.add_network(network='192.168.0.0/24', notes='Home network')
        print(ipam.get_network('192.168.0.0/24'))

        ipam.add_network(network='2001:db8:abc:1400::/64')

        ipam.add_host(ip='192.168.0.1')
        ipam.add_host(ip='192.168.0.1', hostname='server')
        ipam.add_alias('server', 'homeserver')
        ipam.get_host_by_ip('192.168.0.1').add_hostname('sshserver', 'sshome')
        print(ipam.get_host_by_ip('192.168.0.1'))

        ipam.add_host(ip='192.168.1.1', hostname={'strayserver': []})

        ipam.get_host_by_ip('::1')

        ipam.add_alias('remoteserver', 'externalserver')
        ipam.add_alias('remoteserver', 'notmyserver')

    def test_errors(self):
        ipam = MinIpam()
        with pytest.raises(TypeError):
            ipam.add_network()
        with pytest.raises(TypeError):
            ipam.add_host()
        with pytest.raises(TypeError):
            ipam.add_host(ip='172.0.0.1', hostname=['localhost'])

    def test_load_save(self):
        ipam = MinIpam()
        ipam.load_yaml('tests/test.yaml')
        ipam.save_yaml('tests/test.yaml')
