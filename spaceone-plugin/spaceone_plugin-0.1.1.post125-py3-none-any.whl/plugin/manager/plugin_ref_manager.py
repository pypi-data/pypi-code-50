# -*- coding: utf-8 -*-

import logging

from spaceone.core.manager import BaseManager
from spaceone.plugin.model import InstalledPluginRef, InstalledPlugin

__all__ = ['PluginRefManager']

_LOGGER = logging.getLogger(__name__)


class PluginRefManager(BaseManager):

    def __init__(self, transaction):
        super().__init__(transaction)
        self._installed_pluginref_model: InstalledPluginRef = self.locator.get_model('InstalledPluginRef')
        self._installed_plugin_model: InstalledPlugin = self.locator.get_model('InstalledPlugin')
        #self._domain_id = self.transaction.meta['domain_id']

    def create(self, params):
        """ 
        Args:
            params:
              - domain_id: my domain_id
              - plugin_id
              - version
              - supervisor_ref
        """
        def _rollback(vo):
            vo.delete()

        if 'supervisor_id' not in params:
            supervisor = params['supervisor']
            params['supervisor_id'] = supervisor.supervisor_id
        _LOGGER.debug(f'[create] params: {params}')
        plugin_ref = self._installed_pluginref_model.create(params)

        self.transaction.add_rollback(_rollback, plugin_ref)
        return plugin_ref

    def get(self, supervisor_id, domain_id, plugin_id, version):
        """ Based on installed_plugin_ref, get real installed_plugin
        """
        params = {
            'supervisor_id': supervisor_id,
            'domain_id': domain_id,
            'plugin_id': plugin_id,
            'version': version
            }
        plugin_ref = self._installed_pluginref_model.get(supervisor_id = supervisor_id,
                                                        domain_id = domain_id,
                                                        plugin_id = plugin_id,
                                                        version = version)
        parent_domain_id = plugin_ref.supervisor.supervisor.domain_id
        plugin = self._installed_plugin_model.get(supervisor_id = supervisor_id,
                                                        domain_id = parent_domain_id,
                                                        plugin_id = plugin_id,
                                                        version = version)

        return plugin

    def delete(self, supervisor_id, domain_id, plugin_id, version):
        _LOGGER.debug(f'[delete] supervisor_id: {supervisor_id} at {domain_id}')
        plugin_ref = self.get(supervisor_id, domain_id, plugin_id, version)
        if plugin_ref:
            plugin_ref.delete()

#    def list_supervisor(self, query):
#        return self._installed_pluginref_model.query(**query)
#

#    def create_or_update_supervisor_ref(self, supervisor: Supervisor, plugin: InstalledPlugin):
#        # TODO: rollback
#        try:
#            supervisor_ref: SupervisorRef = self._get_plugin_ref_by_domain(supervisor.supervisor_id)
#        except ERROR_NOT_FOUND:
#            supervisor_ref = None
#
#        if supervisor_ref is None:
#            params = {
#                'supervisor_id': supervisor.supervisor_id,
#                'name': supervisor.name,
#                'supervisor': supervisor,
#                'domain_id': self._domain_id,
#                'plugins': [{
#                    'name': plugin.name,
#                    'plugin_id': plugin.plugin_id
#                }]
#            }
#            supervisor_ref = self.create(params)
#        else:
#            params = supervisor_ref.to_dict()
#            installed_plugin_ref = {
#                'name': plugin.name,
#                'plugin_id': plugin.plugin_id
#            }
#            params['plugins'].append(installed_plugin_ref)
#            self.update(params)
#
#        return supervisor_ref
#
#    def _get_plugin_ref_by_domain(self, supervisor_id):
#        return self._installed_pluginref_model.get(supervisor_id=supervisor_id, domain_id=self._domain_id)
#
#    def _get_plugin_ref_by_ref_id(self, reference_id):
#        return self._installed_pluginref_model.get(reference_id=reference_id)
#
    # def get(self, supervisor_id):
    #     return self._installed_pluginref_model.get(supervisor_id=supervisor_id)

#    def update(self, params):
#        plugin_ref = self._get_plugin_ref_by_ref_id(params['reference_id'])
#        # TODO: rollback
#        return plugin_ref.update(params)

    # def get_all_supervisor_refs(self, domain_id):
    #     return self.list_supervisor(_query_domain_id(domain_id))

    # def get_matched_supervisor_refs(self, domain_id, labels):
    #     """
    #     Get label matched supervisor_reference in domain_id.
    #     :param domain_id: domain_id for matching supervisor_refs
    #     :param labels: labels to match
    #     :return: Return a SupervisorRef. If multiple SupervisorRef exists, returns random one.<br>
    #      None, if no matches.
    #     """
    #     plugin_references, total_count = self.list_supervisor(_query_domain_id(domain_id))
    #     matched_plugin_ref = _get_matched_supervisor_ref(plugin_references, labels)
    #     _LOGGER.debug(f'[get_matched_supervisor_refs] matched_plugin_ref: {matched_plugin_ref}')
    #     return matched_plugin_ref


# def _get_matched_supervisor_ref(plugin_refs, labels):
#     matched_plugin_ref = list(map(
#         lambda plugin_ref: plugin_ref if set(plugin_ref.supervisor.labels).issuperset(labels) else None,
#         plugin_refs
#     ))
#     if matched_plugin_ref and len(matched_plugin_ref) > 0:
#         return random.choice(matched_plugin_ref)
#     return None


def _query_domain_id(domain_id):
    return {
        'filter': [
            {
                'k': 'domain_id',
                'v': domain_id,
                'o': 'eq'
            }
        ]
    }
