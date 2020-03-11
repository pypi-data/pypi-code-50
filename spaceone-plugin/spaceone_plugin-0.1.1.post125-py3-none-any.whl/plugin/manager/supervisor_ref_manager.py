# -*- coding: utf-8 -*-

import logging

from spaceone.core.manager import BaseManager
from spaceone.plugin.model import SupervisorRef

__all__ = ['SupervisorRefManager']

_LOGGER = logging.getLogger(__name__)


class SupervisorRefManager(BaseManager):

    def __init__(self, transaction):
        super().__init__(transaction)
        self._supervisor_ref_model: SupervisorRef = self.locator.get_model('SupervisorRef')
        #self._domain_id = self.transaction.meta['domain_id']

    def create(self, params):
        """ 
        Args:
            params:
              - supervisor_id: parent supervisor_id
              - domain_id: my domain_id
        """
        def _rollback(vo):
            vo.delete()

        _LOGGER.debug(f'[create] params: {params}')
        supvr_ref = self._supervisor_ref_model.create(params)

        self.transaction.add_rollback(_rollback, supvr_ref)
        return supvr_ref

    def get(self, supervisor_id, domain_id):
        return self._supervisor_ref_model.get(supervisor_id=supervisor_id, domain_id=domain_id)

    def delete(self, supervisor_id, domain_id):
        _LOGGER.debug(f'[delete] supervisor_id: {supervisor_id} at {domain_id}')
        supvr_ref = self.get(supervisor_id, domain_id)
        if supvr_ref:
            supvr_ref.delete()

    def list_supervisor(self, query):
        return self._supervisor_ref_model.query(**query)


#    def create_or_update_supervisor_ref(self, supervisor: Supervisor, plugin: InstalledPlugin):
#        # TODO: rollback
#        try:
#            supervisor_ref: SupervisorRef = self._get_supvr_ref_by_domain(supervisor.supervisor_id)
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
#    def _get_supvr_ref_by_domain(self, supervisor_id):
#        return self._supervisor_ref_model.get(supervisor_id=supervisor_id, domain_id=self._domain_id)
#
#    def _get_supvr_ref_by_ref_id(self, reference_id):
#        return self._supervisor_ref_model.get(reference_id=reference_id)
#
    # def get(self, supervisor_id):
    #     return self._supervisor_ref_model.get(supervisor_id=supervisor_id)

    def update(self, params):
        supvr_ref = self._get_supvr_ref_by_ref_id(params['reference_id'])
        # TODO: rollback
        return supvr_ref.update(params)

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
    #     supvr_references, total_count = self.list_supervisor(_query_domain_id(domain_id))
    #     matched_supvr_ref = _get_matched_supervisor_ref(supvr_references, labels)
    #     _LOGGER.debug(f'[get_matched_supervisor_refs] matched_supvr_ref: {matched_supvr_ref}')
    #     return matched_supvr_ref


# def _get_matched_supervisor_ref(supvr_refs, labels):
#     matched_supvr_ref = list(map(
#         lambda supvr_ref: supvr_ref if set(supvr_ref.supervisor.labels).issuperset(labels) else None,
#         supvr_refs
#     ))
#     if matched_supvr_ref and len(matched_supvr_ref) > 0:
#         return random.choice(matched_supvr_ref)
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
