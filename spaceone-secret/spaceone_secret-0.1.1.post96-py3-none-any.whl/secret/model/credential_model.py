# -*- coding: utf-8 -*-

from mongoengine import *
from spaceone.core.model.mongo_model import MongoModel


class Credential(MongoModel):
    credential_id = StringField(max_length=40, generate_id='cred', unique=True)
    name = StringField(max_length=255, unique_with='domain_id')
    issue_type = StringField(max_length=20, default='credential')
    project_id = StringField(max_length=40, null=True, default=None)
    # plugin_info
    domain_id = StringField(max_length=255)
    tags = DictField()
    created_at = DateTimeField(auto_now_add=True)

    meta = {
        'db_alias': 'default',
        'updatable_fields': [
            'name',
            'tags'
        ],
        'exact_fields': [
            'credential_id',
            'issue_type',
            'project_id'
        ],
        'minimal_fields': [
            'credential_id',
            'name'
        ],
        'ordering': [
            'name'
        ],
        'indexes': [
            'credential_id'
        ]
    }
