# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from collective.expandcollapse.tile.testing import COLLECTIVE_EXPANDCOLLAPSE_TILE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.expandcollapse.tile is properly installed."""

    layer = COLLECTIVE_EXPANDCOLLAPSE_TILE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.expandcollapse.tile is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.expandcollapse.tile'))

    def test_browserlayer(self):
        """Test that ICollectiveExpandcollapseTileLayer is registered."""
        from collective.expandcollapse.tile.interfaces import (
            ICollectiveExpandcollapseTileLayer)
        from plone.browserlayer import utils
        self.assertIn(
            ICollectiveExpandcollapseTileLayer,
            utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_EXPANDCOLLAPSE_TILE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer.uninstallProducts(['collective.expandcollapse.tile'])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if collective.expandcollapse.tile is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.expandcollapse.tile'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveExpandcollapseTileLayer is removed."""
        from collective.expandcollapse.tile.interfaces import \
            ICollectiveExpandcollapseTileLayer
        from plone.browserlayer import utils
        self.assertNotIn(
            ICollectiveExpandcollapseTileLayer,
            utils.registered_layers())
