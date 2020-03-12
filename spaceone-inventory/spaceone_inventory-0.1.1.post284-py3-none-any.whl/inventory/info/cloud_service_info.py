# -*- coding: utf-8 -*-
import functools
from spaceone.api.inventory.v1 import cloud_service_pb2
from spaceone.core.pygrpc.message_type import *
from spaceone.inventory.model.cloud_service_model import CloudService
from spaceone.inventory.info.pool_info import PoolInfo
from spaceone.inventory.info.zone_info import ZoneInfo
from spaceone.inventory.info.region_info import RegionInfo
from spaceone.inventory.info.collection_info import CollectionInfo

__all__ = ['CloudServiceInfo', 'CloudServicesInfo']


def CloudServiceInfo(cloud_svc_vo: CloudService, minimal=False):
    info = {
        'cloud_service_id': cloud_svc_vo.cloud_service_id,
        'cloud_service_type': cloud_svc_vo.cloud_service_type,
        'provider': cloud_svc_vo.provider,
        'cloud_service_group': cloud_svc_vo.cloud_service_group
    }

    if not minimal:
        info.update({
            'data': change_struct_type(cloud_svc_vo.data),
            'metadata': change_struct_type(cloud_svc_vo.metadata),
            'pool_info': PoolInfo(cloud_svc_vo.pool, minimal=True) if cloud_svc_vo.pool else None,
            'zone_info': ZoneInfo(cloud_svc_vo.zone, minimal=True) if cloud_svc_vo.zone else None,
            'region_info': RegionInfo(cloud_svc_vo.region, minimal=True) if cloud_svc_vo.region else None,
            'project_id': cloud_svc_vo.project_id,
            'domain_id': cloud_svc_vo.domain_id,
            'tags': change_struct_type(cloud_svc_vo.tags),
            'collection_info': change_struct_type(CollectionInfo(cloud_svc_vo.collection_info)),
            'created_at': change_timestamp_type(cloud_svc_vo.created_at),
            'updated_at': change_timestamp_type(cloud_svc_vo.updated_at)
        })

    return cloud_service_pb2.CloudServiceInfo(**info)


def CloudServicesInfo(cloud_svc_vos, total_count, **kwargs):
    return cloud_service_pb2.CloudServicesInfo(results=list(map(functools.partial(CloudServiceInfo, **kwargs),
                                                                cloud_svc_vos)),
                                               total_count=total_count)
