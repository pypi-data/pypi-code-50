# coding: utf-8

"""
    Pulp 3 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulpcore
from pulpcore.client.pulpcore.api.signing_services_api import SigningServicesApi  # noqa: E501
from pulpcore.client.pulpcore.rest import ApiException


class TestSigningServicesApi(unittest.TestCase):
    """SigningServicesApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulpcore.api.signing_services_api.SigningServicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_list(self):
        """Test case for list

        List signing services  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect a signing service  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
