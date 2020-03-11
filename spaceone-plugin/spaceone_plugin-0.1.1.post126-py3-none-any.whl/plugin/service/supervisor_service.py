# -*- coding: utf-8 -*-

import logging

from spaceone.core.error import *
from spaceone.core.service import *
from spaceone.plugin.manager import PluginManager
from spaceone.plugin.manager.supervisor_manager.__init__ import SupervisorManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@event_handler
class SupervisorService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)
        self._supervisor_mgr: SupervisorManager = self.locator.get_manager('SupervisorManager')

    @transaction
    @check_required(['name', 'hostname', 'domain_id'])
    def publish(self, params):
        _LOGGER.debug(f'[publish] params: {params}')
        plugin_mgr: PluginManager = self.locator.get_manager('PluginManager')

        domain_id = params['domain_id']
        # get supervisor
        if 'user_id' in params:
            del params['user_id']

        try:
            # unique: hostname + name
            supervisor = self._supervisor_mgr.get_by_hostname(params['hostname'], domain_id)
        except ERROR_NOT_FOUND:
            # create new supervisor
            supervisor = self._supervisor_mgr.create(params)
            ###############################
            # East EGG for Automatic Test
            ###############################
            if params['name'] == 'root':
                self._supervisor_mgr.update({'supervisor_id': supervisor.supervisor_id, 'is_public': True, 'domain_id': domain_id})

        if supervisor:
            plugins_info = params.get('plugin_info', [])
            print(f'[publish] plugin_info: {plugins_info}')
            for plugin in plugins_info:
                # Update State (XXXX -> ACTIVE)
                # Update endpoint (grpc://xxxx)
                # There may be no plugin at DB (maybe deleted, or supervisor's garbage)
                #self._plugin_mgr.update_plugin(plugin)
                _LOGGER.debug(f'[publish] plugin={plugin}')
                try:
                    plugin_mgr.update_plugin_state(plugin['plugin_id'],
                                                   plugin['version'],
                                                   plugin['state'],
                                                   plugin['endpoint'],
                                                   supervisor.supervisor_id)
                except Exception as e:
                    _LOGGER.error(f'[publish] e={e}')
                    _LOGGER.warning(f'[publish] Failed update plugin.state:{plugin["state"]}')
        else:
            # There is no plugin_info
            supervisor = self._supervisor_mgr.create(params)


        return supervisor

    @transaction
    @check_required(['supervisor_id', 'domain_id'])
    def register(self, params):
        domain_id = params['domain_id']
        _LOGGER.debug(f'[register] params: {params}')

        # TODO: Should I validate supervisor_id?
        return self._supervisor_mgr.register(params['supervisor_id'], domain_id)

    @transaction
    @check_required(['supervisor_id', 'domain_id'])
    def update(self, params):
        domain_id = params['domain_id']
        _LOGGER.debug(f'[update] params: {params}')

        if 'user_id' in params:
            del params['user_id']


        # TODO: Should I validate supervisor_id?
        return self._supervisor_mgr.update(params)


    @transaction
    @check_required(['supervisor_id', 'domain_id'])
    def deregister(self, params):
        domain_id = params['domain_id']
        _LOGGER.debug(f'[deregister] supervisor_id: {params["supervisor_id"]}')
        self._supervisor_mgr.delete(params['supervisor_id'], domain_id)

    @transaction
    @check_required(['supervisor_id', 'domain_id'])
    def enable(self, params):
        domain_id = params['domain_id']
        _LOGGER.debug(f'[enable] supervisor_id: {params["supervisor_id"]}')
        return self._supervisor_mgr.enable(params['supervisor_id'], domain_id)

    @transaction
    @check_required(['supervisor_id', 'domain_id'])
    def disable(self, params):
        domain_id = params['domain_id']
        _LOGGER.debug(f'[disable] supervisor_id: {params["supervisor_id"]}')
        return self._supervisor_mgr.disable(params['supervisor_id'], domain_id)

    @transaction
    @check_required(['supervisor_id', 'plugin_id', 'version', 'domain_id'])
    def recover_plugin(self, params):
        """ Recover plugin if exist
        """
        supervisor = self._get_supervisor_by_id(params['supervisor_id'], params['domain_id'])
        # Get plugin_info
        plugin_mgr: PluginManager = self.locator.get_manager('PluginManager')
        
        supervisor_id = params['supervisor_id']
        domain_id = params['domain_id']
        plugin_id = params['plugin_id']
        version = params['version']

        plugin_vo = plugin_mgr.get(supervisor_id, domain_id, plugin_id, version)

        # Get endpoint
        endpoint = plugin_vo.endpoint
        plugin_vo = plugin_mgr.update_plugin_state(plugin_id, version, 'RE-PROVISIONING', endpoint, supervisor_id)
        return plugin_vo


    @transaction
    @check_required(['supervisor_id', 'domain_id'])
    def get(self, params):
        """ Get PluginManager

        Args:
            params:
                - plugin_manager_id
                - domain_id (from metadata)
        Returns:
            PluginManagerData
        """
        domain_id = params['domain_id']
        _LOGGER.debug(f'[get] supervisor_id: {params["supervisor_id"]}')

        return self._supervisor_mgr.get_by_id(params['supervisor_id'], domain_id)

    @transaction
    @check_required(['domain_id'])
    @append_query_filter(filter_keys=['supervisor_id', 'name'])
    def list_supervisors(self, params):
        query = params.get('query', {})
        return self._supervisor_mgr.list_supervisors(query)

    @transaction
    @check_required(['domain_id'])
    @append_query_filter(filter_keys=['supervisor_id', 'hostname', 'plugin_id', 'version', 'state', 'endpoint'])
    def list_plugins(self, params):
        """ Only real supervisor can do list_plugins
        """
        query = params.get('query', {})
        # if hostname exist, change to Ref.
        _LOGGER.debug(f'[list_plugins] Before Query: {query}')
        query_new = []
        host_ref = False
        domain_id = params['domain_id']
        for q in query['filter']:
            # {'k': 'hostname', 'v': 'dev-docker.pyengine.net', 'o': 'eq'}
            _LOGGER.debug(f'[list_plugins] q={q}')
            if q['k'] == 'hostname':
                supervisor = self._supervisor_mgr.get_by_hostname(q['v'], domain_id)
                host_ref = True
            else:
                query_new.append(q)
        _LOGGER.debug(f'[list_plugins] After Query: {query_new}')
        if host_ref:
            return self._supervisor_mgr.list_plugins({'supervisor': supervisor, 'filter': query_new})
        return self._supervisor_mgr.list_plugins(query)


    def _get_supervisor_by_id(self, supervisor_id):
        """ Find Supervisor from supervisor_id
        Return may be Supervisor or Supervisor_ref
        """
        supervisor = self._supervisor_mgr.get_by_id(supervisor_id, domain_id)
        return supervisor

