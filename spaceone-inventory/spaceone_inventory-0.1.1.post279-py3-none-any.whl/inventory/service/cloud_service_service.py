# -*- coding: utf-8 -*-
from spaceone.core.service import *
from spaceone.inventory.manager.cloud_service_manager import CloudServiceManager
from spaceone.inventory.manager.region_manager import RegionManager
from spaceone.inventory.manager.zone_manager import ZoneManager
from spaceone.inventory.manager.pool_manager import PoolManager
from spaceone.inventory.manager.identity_manager import IdentityManager
from spaceone.inventory.manager.collection_data_manager import CollectionDataManager


@authentication_handler
@authorization_handler
@event_handler
class CloudServiceService(BaseService):

    def __init__(self, metadata):
        super().__init__(metadata)
        self.cloud_svc_mgr: CloudServiceManager = self.locator.get_manager('CloudServiceManager')

    @transaction
    @check_required(['data', 'provider', 'domain_id'])
    def create(self, params):
        """
        Args:
            params (dict): {
                    'cloud_service_type': 'str',
                    'provider': 'str',
                    'data': 'dict',
                    'cloud_service_group': 'str',
                    'tags': 'dict',
                    'region_id': 'str',
                    'zone_id': 'str',
                    'pool_id': 'str',
                    'project_id': 'str',
                    'domain_id': 'str'
                }

        Returns:
            cloud_service_vo (object)

        """

        collection_data_mgr: CollectionDataManager = self.locator.get_manager('CollectionDataManager')

        domain_id = params['domain_id']

        collector_id = self.transaction.get_meta('collector_id')
        job_id = self.transaction.get_meta('job_id')

        params['collection_info'] = collection_data_mgr.create_new_history(params,
                                                                           domain_id,
                                                                           collector_id,
                                                                           exclude_keys=['domain_id'])

        if 'region_id' in params:
            region_mgr: RegionManager = self.locator.get_manager('RegionManager')
            params['region'] = region_mgr.get_region(params['region_id'], domain_id)
            del params['region_id']

        if 'zone_id' in params:
            zone_mgr: ZoneManager = self.locator.get_manager('ZoneManager')
            zone_vo = zone_mgr.get_zone(params['zone_id'], domain_id)
            params['zone'] = zone_vo
            params['region'] = zone_vo.region
            del params['zone_id']

        if 'pool_id' in params:
            pool_mgr: PoolManager = self.locator.get_manager('PoolManager')
            pool_vo = pool_mgr.get_pool(params['pool_id'], domain_id)
            params['pool'] = pool_vo
            params['zone'] = pool_vo.zone
            params['region'] = pool_vo.region
            del params['pool_id']

        if 'project_id' in params:
            identity_mgr: IdentityManager = self.locator.get_manager('IdentityManager')
            identity_mgr.get_project(params['project_id'], domain_id)

        return self.cloud_svc_mgr.create_cloud_service(params)

    @transaction
    @check_required(['cloud_service_id', 'domain_id'])
    def update(self, params):
        """
        Args:
            params (dict): {
                    'cloud_service_id': 'str',
                    'data': 'dict',
                    'tags': 'dict',
                    'region_id': 'str',
                    'zone_id': 'str',
                    'pool_id': 'str',
                    'project_id': 'str',
                    'domain_id': 'str'
                }

        Returns:
            cloud_service_vo (object)

        """

        collection_data_mgr: CollectionDataManager = self.locator.get_manager('CollectionDataManager')

        domain_id = params['domain_id']

        collector_id = self.transaction.get_meta('collector_id')
        job_id = self.transaction.get_meta('job_id')

        cloud_svc_vo = self.cloud_svc_mgr.get_cloud_service(params['cloud_service_id'], domain_id)

        params = collection_data_mgr.exclude_data_by_pinned_keys(params, cloud_svc_vo.collection_info)
        params = collection_data_mgr.exclude_data_by_history(params,
                                                             domain_id,
                                                             cloud_svc_vo.collection_info,
                                                             collector_id,
                                                             exclude_keys=['cloud_service_id', 'domain_id'])

        if 'data' in params:
            params['data'] = collection_data_mgr.merge_data(cloud_svc_vo.data, params['data'])

        if 'metadata' in params:
            params['metadata'] = collection_data_mgr.merge_metadata(cloud_svc_vo.metadata, params['metadata'])

        if 'release_region' in params:
            params.update({
                'region': None,
                'zone': None,
                'pool': None
            })
        else:
            if 'region_id' in params:
                region_mgr: RegionManager = self.locator.get_manager('RegionManager')

                params.update({
                    'region': region_mgr.get_region(params['region_id'], domain_id),
                    'zone': None,
                    'pool': None
                })

                del params['region_id']

            if 'zone_id' in params:
                zone_mgr: ZoneManager = self.locator.get_manager('ZoneManager')
                zone_vo = zone_mgr.get_zone(params['zone_id'], domain_id)

                params.update({
                    'region': zone_vo.region,
                    'zone': zone_vo,
                    'pool': None
                })

                del params['zone_id']

            if 'pool_id' in params:
                pool_mgr: PoolManager = self.locator.get_manager('PoolManager')
                pool_vo = pool_mgr.get_pool(params['pool_id'], domain_id)

                params.update({
                    'region': pool_vo.region,
                    'zone': pool_vo.zone,
                    'pool': pool_vo
                })

                del params['pool_id']

        if 'release_project' in params:
            params['project_id'] = None
        elif 'project_id' in params:
            identity_mgr: IdentityManager = self.locator.get_manager('IdentityManager')
            identity_mgr.get_project(params['project_id'], domain_id)

        return self.cloud_svc_mgr.update_cloud_service_by_vo(params, cloud_svc_vo)

    @transaction
    @check_required(['cloud_service_id', 'keys', 'domain_id'])
    def pin_data(self, params):
        """
        Args:
            params (dict): {
                    'cloud_service_id': 'str',
                    'keys': 'list',
                    'domain_id': 'str'
                }

        Returns:
            cloud_service_vo (object)

        """

        collection_data_mgr: CollectionDataManager = self.locator.get_manager('CollectionDataManager')

        cloud_svc_vo = self.cloud_svc_mgr.get_cloud_service(params['cloud_service_id'], params['domain_id'])

        params['collection_info'] = collection_data_mgr.update_pinned_keys(params['keys'],
                                                                           cloud_svc_vo.collection_info)

        return self.cloud_svc_mgr.update_cloud_service_by_vo(params, cloud_svc_vo)

    @transaction
    @check_required(['cloud_service_id', 'domain_id'])
    def delete(self, params):
        """
        Args:
            params (dict): {
                    'cloud_service_id': 'str',
                    'domain_id': 'str'
                }

        Returns:
            None

        """

        cloud_svc_vo = self.cloud_svc_mgr.get_cloud_service(params['cloud_service_id'],
                                                            params['domain_id'])

        self.cloud_svc_mgr.delete_cloud_service_by_vo(cloud_svc_vo)

    @transaction
    @check_required(['cloud_service_id', 'domain_id'])
    def get(self, params):
        """
        Args:
            params (dict): {
                    'cloud_service_id': 'str',
                    'domain_id': 'str'
                }

        Returns:
            server_vo (object)

        """

        return self.cloud_svc_mgr.get_cloud_service(params['cloud_service_id'], params['domain_id'])

    @transaction
    @check_required(['domain_id'])
    @append_query_filter(['cloud_service_id', 'cloud_service_type', 'provider', 'cloud_service_group',
                          'region_id', 'zone_id', 'pool_id', 'project_id', 'domain_id'])
    def list(self, params):
        """
        Args:
            params (dict): {
                    'cloud_service_id': 'str',
                    'cloud_service_type': 'str',
                    'provider': 'str',
                    'cloud_service_group': 'str',
                    'region_id': 'str',
                    'zone_id': 'str',
                    'pool_id': 'str',
                    'project_id': 'str',
                    'domain_id': 'str',
                    'query': 'dict'
                }

        Returns:
            results (list)
            total_count (int)

        """

        return self.cloud_svc_mgr.list_cloud_services(params.get('query', {}))
