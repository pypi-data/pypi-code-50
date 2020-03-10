# -*- coding: utf-8 -*-

from mongoengine import *

from spaceone.core.model.mongo_model import MongoModel

__all__ = ['Supervisor']


#class InstalledPlugin(EmbeddedDocument):
#    name = StringField(max_length=255)
#    plugin_id = StringField(max_length=255)
#    image = StringField(max_length=255)
#    version = StringField(max_length=255)
#    state = StringField(max_length=40, default='ENABLED', choices=('ENABLED', 'DISABLED'))
#    endpoint = StringField(max_length=255)


class Supervisor(MongoModel):
    supervisor_id = StringField(max_length=40, generate_id='supervisor', unique=True)
    name = StringField(max_length=255)
    hostname = StringField()
    domain_id = StringField(max_length=64)
    state = StringField(max_length=40, default='ENABLED', choices=('ENABLED', 'DISABLED', 'PENDING'))
    is_public = BooleanField(default=False)
    labels = DictField()
    tags = DictField()
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(default=None, null=True)

    #installed_plugins = ListField(EmbeddedDocumentField(InstalledPlugin, default=None, null=True))

    meta = {
        'db_alias': 'default',
        'updatable_fields': [
            'name',
            'state',
            'updated_at',
            'plugins',
            'is_public',
            'hostname',
            'labels'
        ],
        'exact_fields': [
            'supervisor_id',
            'name',
            'state',
            'is_public'
        ],
        'minimal_fields': [
            'supervisor_id',
            'name',
            'state',
            'is_public',
            'labels'
        ],
        'ordering': ['name'],
        'indexes': [
            'supervisor_id',
            'name'
        ]
    }
