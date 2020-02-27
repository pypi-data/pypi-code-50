# Copyright 2015 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import ddt
from tempest.common import utils
from tempest.lib import decorators
from tempest.lib import exceptions as lib_exc

from neutron_tempest_plugin.api import base

FAKE_IP = '10.0.0.1'
FAKE_MAC = '00:25:64:e8:19:dd'


@ddt.ddt
class PortSecTest(base.BaseNetworkTest):

    @decorators.idempotent_id('7c338ddf-e64e-4118-bd33-e49a1f2f1495')
    @utils.requires_ext(extension='port-security', service='network')
    def test_port_sec_default_value(self):
        # Default port-sec value is True, and the attr of the port will inherit
        # from the port-sec of the network when it not be specified in API
        network = self.create_network()
        self.assertTrue(network['port_security_enabled'])
        self.create_subnet(network)
        port = self.create_port(network)
        self.assertTrue(port['port_security_enabled'])

    @decorators.idempotent_id('e60eafd2-31de-4c38-8106-55447d033b57')
    @utils.requires_ext(extension='port-security', service='network')
    @ddt.unpack
    @ddt.data({'port_sec_net': False, 'port_sec_port': True, 'expected': True},
              {'port_sec_net': True, 'port_sec_port': False,
               'expected': False})
    def test_port_sec_specific_value(self, port_sec_net, port_sec_port,
                                     expected):
        network = self.create_network(port_security_enabled=port_sec_net)
        self.create_subnet(network)
        port = self.create_port(network, port_security_enabled=port_sec_port)
        self.assertEqual(network['port_security_enabled'], port_sec_net)
        self.assertEqual(port['port_security_enabled'], expected)

    @decorators.idempotent_id('fe7c27b9-f320-4daf-b977-b1547c43daf6')
    @utils.requires_ext(extension='port-security', service='network')
    def test_create_port_sec_with_security_group(self):
        network = self.create_network(port_security_enabled=True)
        self.create_subnet(network)

        port = self.create_port(network, security_groups=[])
        self.assertTrue(port['port_security_enabled'])
        self.client.delete_port(port['id'])

        port = self.create_port(network, security_groups=[],
                                port_security_enabled=False)
        self.assertFalse(port['port_security_enabled'])
        self.assertEmpty(port['security_groups'])

    @decorators.attr(type='negative')
    @decorators.idempotent_id('ff11226c-a5ff-4ad4-8480-0840e36e47a9')
    @utils.requires_ext(extension='port-security', service='network')
    def test_port_sec_update_port_failed(self):
        network = self.create_network()
        self.create_subnet(network)

        security_group = self.create_security_group()
        port = self.create_port(network)

        # Exception when set port-sec to False with sec-group defined
        self.assertRaises(lib_exc.Conflict, self.update_port, port,
                          port_security_enabled=False)

        port = self.update_port(port, security_groups=[],
                                port_security_enabled=False)
        self.assertEmpty(port['security_groups'])
        self.assertFalse(port['port_security_enabled'])
        port = self.update_port(
            port, security_groups=[security_group['id']],
            port_security_enabled=True)

        self.assertNotEmpty(port['security_groups'])
        self.assertTrue(port['port_security_enabled'])

        # Remove security group from port before deletion on resource_cleanup
        self.update_port(port, security_groups=[])

    @decorators.idempotent_id('05642059-1bfc-4581-9bc9-aaa5db08dd60')
    @utils.requires_ext(extension='port-security', service='network')
    def test_port_sec_update_pass(self):
        network = self.create_network()
        self.create_subnet(network)
        security_group = self.create_security_group()

        port = self.create_port(network,
                                security_groups=[security_group['id']],
                                port_security_enabled=True)
        self.assertNotEmpty(port['security_groups'])
        self.assertTrue(port['port_security_enabled'])

        port = self.update_port(port, security_groups=[])
        self.assertEmpty(port['security_groups'])
        self.assertTrue(port['port_security_enabled'])

        port = self.update_port(port, security_groups=[security_group['id']])
        self.assertNotEmpty(port['security_groups'])
        port = self.update_port(port, security_groups=[],
                                port_security_enabled=False)
        self.assertEmpty(port['security_groups'])
        self.assertFalse(port['port_security_enabled'])

    @decorators.idempotent_id('2df6114b-b8c3-48a1-96e8-47f08159d35c')
    @utils.requires_ext(extension='port-security', service='network')
    def test_delete_with_port_sec(self):
        network = self.create_network(port_security_enabled=True)
        port = self.create_port(network=network,
                                port_security_enabled=True)
        self.client.delete_port(port['id'])
        self.assertTrue(self.client.is_resource_deleted('port', port['id']))
        self.client.delete_network(network['id'])
        self.assertTrue(
            self.client.is_resource_deleted('network', network['id']))

    @decorators.attr(type='negative')
    @decorators.idempotent_id('ed93e453-3f8d-495e-8e7e-b0e268c2ebd9')
    @utils.requires_ext(extension='port-security', service='network')
    @utils.requires_ext(extension='allowed-address-pairs', service='network')
    def test_allowed_address_pairs(self):
        network = self.create_network()
        self.create_subnet(network)
        port = self.create_port(network=network, port_security_enabled=False)
        allowed_address_pairs = [{'ip_address': FAKE_IP,
                                  'mac_address': FAKE_MAC}]

        # Exception when set address-pairs with port-sec is False
        self.assertRaises(lib_exc.Conflict,
                          self.update_port, port,
                          allowed_address_pairs=allowed_address_pairs)
