# -*- coding: utf-8 -*-
from mongoengine import *
from spaceone.core.model.mongo_model import MongoModel

from spaceone.inventory.model.region_model import Region
from spaceone.inventory.model.zone_model import Zone
from spaceone.inventory.model.pool_model import Pool
from spaceone.inventory.model.collection_info_model import CollectionInfo


class CloudService(MongoModel):
    cloud_service_id = StringField(max_length=40, generate_id='cloud-svc', unique=True)
    cloud_service_type = StringField(max_length=255, default='')
    provider = StringField(max_length=255, default='')
    cloud_service_group = StringField(max_length=255, default=None, null=True)
    data = DictField()
    metadata = DictField()
    tags = DictField()
    pool = ReferenceField('Pool', default=None, null=True)
    zone = ReferenceField('Zone', default=None, null=True)
    region = ReferenceField('Region', default=None, null=True)
    project_id = StringField(max_length=255, default=None, null=True)
    domain_id = StringField(max_length=40)
    collection_info = EmbeddedDocumentField(CollectionInfo, default=CollectionInfo)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    meta = {
        'updatable_fields': [
            'data',
            'metadata',
            'tags',
            'region',
            'zone',
            'pool',
            'project_id',
            'collection_info'
        ],
        'exact_fields': [
            'cloud_service_id',
            'project_id',
            'domain_id',
            'collection_info.state'
        ],
        'minimal_fields': [
            'cloud_service_id',
            'provider',
            'cloud_service_group',
            'cloud_service_type',
            'collection_info.state'
        ],
        'change_query_keys': {
            'pool_id': 'pool.pool_id',
            'zone_id': 'zone.zone_id',
            'region_id': 'region.region_id'
        },
        'reference_query_keys': {
            'pool': Pool,
            'zone': Zone,
            'region': Region
        },
        'ordering': [
            'name'
        ],
        'indexes': [
            'cloud_service_id',
            'provider',
            'cloud_service_group',
            'cloud_service_type',
            'pool',
            'zone',
            'region',
            'domain_id',
            'collection_info.state'
        ]
    }
