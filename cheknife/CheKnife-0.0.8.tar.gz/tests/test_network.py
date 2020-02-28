# nosetests --with-coverage --cover-inclusive --cover-package=CheKnife --cover-html tests/test_network.py
from unittest import TestCase
from CheKnife.network import is_ip_in_network


class TestNetwork(TestCase):
    def test_is_ip_in_network(self):
        self.assertTrue(is_ip_in_network('15.17.160.1', '15.17.160.0/24'))
        self.assertTrue(is_ip_in_network('15.17.160.1', '15.17.160.0/20'))
        self.assertTrue(is_ip_in_network('15.17.172.1', '15.17.160.0/20'))
        self.assertTrue(is_ip_in_network('15.17.175.255', '15.17.160.0/20'))

        self.assertFalse(is_ip_in_network('15.17.161.1', '15.17.160.0/24'))
        self.assertFalse(is_ip_in_network('15.17.176.1', '15.17.160.0/20'))

