# -*- coding: utf-8 -*-

__all__ = ['Plugin']

from datetime import datetime

from mongoengine import *

from spaceone.core.error import *
from spaceone.core.model.mongo_model import MongoModel

from spaceone.repository.model.repository_model import Repository

"""
name is unique per domain
"""
class Plugin(MongoModel):
    plugin_id = StringField(max_length=40, generate_id='plugin', unique=True)
    name = StringField(max_length=255)
    state = StringField(max_length=40, default='ENABLED', choices=('ENABLED', 'DISABLED', 'DELETED'))
    image = StringField(max_length=255)
    registry_url = StringField(max_length=255)
    service_type = StringField(max_length=255)
    repository = ReferenceField('Repository')
    domain_id = StringField(max_length=255)
    project_id = StringField(max_length=255)
    tags = DictField()
    template = DictField()
    labels = ListField(StringField(max_length=255))
    created_at = DateTimeField(auto_now_add=True)
    deleted_at = DateTimeField(default=None, null=True)

    meta = {
        'db_alias': 'default',
        'updatable_fields': [
            'name',
            'tags',
            'template',
            'state',
            'labels',
            'deleted_at'
        ],
        'exact_fields': [
            'plugin_id',
            'domain_id',
            'name',
            'service_type'
        ],
        'minimal_fields': [
            'plugin_id',
            'domain_id',
            'name',
            'service_type',
        ],
        'change_query_keys': {
            'repository_id': 'repository.repository_id'
        },
        'reference_query_keys': {
            'repository': Repository 
        },
        'ordering': ['name'],
        'indexes': [
            'plugin_id',
            'domain_id',
            'service_type'
        ]
    }

    @queryset_manager
    def objects(doc_cls, queryset):
        return queryset.filter(state__ne='DELETED')

    @classmethod
    def create(cls, data):
        """ Unique per domain
        """
        plugin_vos = cls.filter(name=data['name'], domain_id=data['domain_id'])
        if plugin_vos.count() > 0:
            raise ERROR_NOT_UNIQUE(key='name', value=data['name'])

        return super().create(data)

    def update(self, data):
        """ Unique per domain
        """
        if 'name' in data:
            plugin_vos = self.filter(name=data['name'], domain_id=data['domain_id'], plugin_id__ne=self.plugin_id)
            if plugin_vos.count() > 0:
                raise ERROR_NOT_UNIQUE(key='name', value=data['name'])

        return super().update(data)

    def delete(self):
        self.update({
            'state': 'DELETED',
            'deleted_at': datetime.utcnow()
            })
