# -*- coding: utf-8 -*-

import logging

from spaceone.core.error import *
from spaceone.core.service import *

from spaceone.repository.error import *
from spaceone.repository.manager.plugin_manager import PluginManager
from spaceone.repository.manager.plugin_manager.local_plugin_manager import LocalPluginManager
from spaceone.repository.manager.plugin_manager.remote_plugin_manager import RemotePluginManager
from spaceone.repository.manager.repository_manager import RepositoryManager

_LOGGER = logging.getLogger(__name__)


@authentication_handler(exclude=['get', 'get_versions'])
@authorization_handler
@event_handler
class PluginService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)
        # self.plugin_mgr: PluginManager = self.locator.get_manager('PluginManager')

    @transaction
    @check_required(['name', 'service_type', 'image', 'domain_id'])
    def register(self, params):
        """Register Plugin (local repo only)

        Args:
            params:
                - name
                - service_type
                - project_id
                - image
                - tags
                - template
                - labels
                - domain_id
        """
        # Pre-condition Check
        plugin_mgr = self.locator.get_manager('LocalPluginManager')
        plugin_mgr.check_project_id(params.get('project_id', None))
        plugin_mgr.check_service_type(params.get('service_type', None))

        # Only LOCAL repository can be registered
        repo_mgr = self.locator.get_manager('RepositoryManager')
        params['repository'] = repo_mgr.get_local_repository()

        return plugin_mgr.register_plugin(params)

    @transaction
    @check_required(['plugin_id', 'domain_id'])
    def update(self, params):
        """Update Plugin. (local repo only)

        Args:
            params:
              - plugin_id (pk)
              - name
              - tags
              - templates
              - domain_id
        """
        # Pre-condition Check
        plugin_mgr = self.locator.get_manager('LocalPluginManager')
        plugin_mgr.check_project_id(params.get('project_id', None))
        plugin_mgr.check_service_type(params.get('service_type', None))

        return plugin_mgr.update_plugin(params)

    @transaction
    @check_required(['plugin_id', 'domain_id'])
    def deregister(self, params):
        """Deregister Plugin (local repo only)

        Args:
            params:
                - plugin_id
                - domain_id
        """
        plugin_id = params['plugin_id']
        domain_id = params['domain_id']

        #########################################################################
        # Warning 
        #
        # To degister plugin, plugin has to verify there is no installed plugins
        # If there was installed plugin, other micro service can query endpoint
        # But plugin can not reply endpoint
        ##########################################################################
        # TODO: check plugin is not used

        plugin_mgr = self.locator.get_manager('LocalPluginManager')
        return plugin_mgr.delete_plugin(plugin_id, domain_id)

    @transaction
    @check_required(['plugin_id', 'domain_id'])
    def enable(self, params):
        """ Enable plugin (local repo only)
        """
        plugin_mgr = self.locator.get_manager('LocalPluginManager')
        return plugin_mgr.enable_plugin(params['plugin_id'], params['domain_id'])

    @transaction
    @check_required(['plugin_id', 'domain_id'])
    def disable(self, params):
        """ Disable Plugin (local repo only)
        """
        plugin_mgr = self.locator.get_manager('LocalPluginManager')
        return plugin_mgr.disable_plugin(params['plugin_id'], params['domain_id'])

    @transaction
    @check_required(['plugin_id', 'domain_id'])
    def get_versions(self, params):
        """ Get Plugin version (local & remote)
        """

        plugin_id = params['plugin_id']
        domain_id = params['domain_id']
        repo_mgr = self.locator.get_manager('RepositoryManager')
        query = {}
        repo_id = params.get('repository_id', None)
        if repo_id:
            query.update({'repository_id': repo_id})

        repo_vos, count = repo_mgr.list_repositories(query)
        if count == 0:
            raise ERROR_NO_REPOSITORY()

        for repo_vo in repo_vos:
            plugin_mgr = self._get_plugin_manager_by_repo(repo_vo)
            # plugin_manager may emit Error, if it is not found
            # skip error
            try:
                plugin_ver = plugin_mgr.get_plugin_versions(plugin_id, domain_id)
            except Exception as e:
                plugin_ver = None

            if plugin_ver:
                _LOGGER.debug(f'[get_versions] found at repo={repo_vo.name}')
                return plugin_ver
            _LOGGER.debug(f'[get_versions] not_fount at repo={repo_vo.name}')

        raise ERROR_NO_PLUGIN(plugin_id=plugin_id)

    @transaction
    @check_required(['plugin_id', 'domain_id'])
    def get(self, params):
        """ Get Plugin (local & remote)
        """
        plugin_id = params['plugin_id']
        domain_id = params['domain_id']

        repo_mgr = self.locator.get_manager('RepositoryManager')
        query = {}
        repo_id = params.get('repository_id', None)
        if repo_id:
            query.update({'repository_id': repo_id})

        repo_vos, count = repo_mgr.list_repositories(query)
        _LOGGER.debug(f'[get] number_of_repo: {count}')
        if count == 0:
            raise ERROR_NO_REPOSITORY()

        for repo_vo in repo_vos:
            _LOGGER.debug(f'[get] find at name: {repo_vo.name} repo_type: {repo_vo.repository_type}')
            plugin_mgr = self._get_plugin_manager_by_repo(repo_vo)
            try:
                plugin_vo = plugin_mgr.get_plugin(plugin_id, domain_id)
            except Exception as e:
                # No problem, search next
                plugin_vo = None

            if plugin_vo:
                return plugin_vo

        raise ERROR_NO_PLUGIN(plugin_id=plugin_id)

    @transaction
    @check_required(['repository_id', 'domain_id'])
    @append_query_filter(['repository_id', 'domain_id', 'plugin_id', 'name', 'state', 'service_type'])
    def list(self, params):
        """ List plugins (local & repo)
        if exists at both local and repo, merge result
        """

        repo_mgr = self.locator.get_manager('RepositoryManager')
        repository_id = params['repository_id']
        repo_vo = repo_mgr.get_repository(repository_id)

        plugin_mgr = self._get_plugin_manager_by_repo(repo_vo)
        query = params.get('query', {})
        _LOGGER.debug(f'[list] query: {query}')
        return plugin_mgr.list_plugins(query, params['domain_id'])

    def _get_plugin_manager_by_repo(self, repo):
        if repo.repository_type == 'local':
            return self.locator.get_manager('LocalPluginManager', repository=repo)
        return self.locator.get_manager('RemotePluginManager', repository=repo)
