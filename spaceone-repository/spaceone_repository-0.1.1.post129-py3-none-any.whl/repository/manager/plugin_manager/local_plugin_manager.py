# -*- coding: utf-8 -*-

__all__ = ['PluginManager']

import logging

from spaceone.core import config
from spaceone.core import pygrpc
from spaceone.core.error import *
from spaceone.core.manager import BaseManager
from spaceone.repository.model import *
from spaceone.repository.error.custom import *
from spaceone.repository.manager.plugin_manager import PluginManager

_LOGGER = logging.getLogger(__name__)

class LocalPluginManager(PluginManager):
    def __init__(self, transaction, **kwargs):
        super().__init__(transaction, **kwargs)
        self.plugin_model : Plugin = self.locator.get_model("Plugin")

    def register_plugin(self, params):
        def _rollback(plugin_vo):
            plugin_vo.delete()

       # Add registry_url
        try:
            con_config = config.get_global("CONNECTORS")
            # ex) 'https://registry.hub.docker.com'
            reg_con = con_config['RegistryConnector']['host']
            item = reg_con.split('://')
            reg_base = item[1]
        except:
            _LOGGER.error('No RegistryConnector.host:%s' % config.get_global())
            reg_base = ''
        params['registry_url'] = reg_base
        plugin_vo = self.plugin_model.create(params)
        self.transaction.add_rollback(_rollback, plugin_vo)

        return plugin_vo

    def update_plugin(self, params):
        def _rollback(old_data):
            plugin_vo.update(old_data)

        domain_id = params['domain_id']
        plugin_id = params['plugin_id']
        plugin_vo = self.plugin_model.get(plugin_id=plugin_id, domain_id=domain_id)

        self.transaction.add_rollback(_rollback, plugin_vo.to_dict())
        return plugin_vo.update(params)

    def enable_plugin(self, plugin_id, domain_id):
        plugin_vo = self.plugin_model.get(domain_id=domain_id, plugin_id=plugin_id)

        if plugin_vo.state == 'ENABLED':
            return plugin_vo
        return plugin_vo.update({'state': 'ENABLED'})

    def disable_plugin(self, plugin_id, domain_id):
        def _rollback(old_data):
            plugin_vo.update(old_data)
        plugin_vo = self.plugin_model.get(domain_id=domain_id, plugin_id=plugin_id)

        if plugin_vo.state == 'DISABLED':
            return plugin_vo

        return plugin_vo.update({'state': 'DISABLED'})

    def delete_plugin(self, plugin_id, domain_id):
        plugin_vo = self.plugin_model.get(domain_id=domain_id, plugin_id=plugin_id)
        plugin_vo.delete()

    def get_plugin(self, plugin_id, domain_id):
        plugin_vo = self.plugin_model.get(domain_id=domain_id, plugin_id=plugin_id)
        return plugin_vo

    def list_plugins(self, query, domain_id):
        return self.plugin_model.query(**query)

    def get_plugin_versions(self, plugin_id, domain_id):
        """ Get version of image

        version: tag list of docker image
        create RegistryConnector
        call get_tags()

        Returns:
            A list of docker tag
        """
        plugin = self.get_plugin(plugin_id, domain_id)

        connector = self.locator.get_connector("RegistryConnector")
        tags = connector.get_tags(plugin.image)
        return tags
        
