# -*- coding: utf-8 -*-
import logging
import copy
from mongoengine import *
from spaceone.core.model.mongo_model import MongoModel
from spaceone.secret.model.credential_model import Credential

_LOGGER = logging.getLogger(__name__)


class CredentialGroup(MongoModel):
    credential_group_id = StringField(max_length=40, generate_id='cred-grp', unique=True)
    name = StringField(max_length=255, unique_with='domain_id')
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
            'credential_group_id',
        ],
        'minimal_fields': [
            'credential_group_id',
            'name'
        ],
        'change_query_keys': {},
        'reference_query_keys': {},
        'ordering': [
            'name'
        ],
        'indexes': [
            'credential_group_id'
        ]
    }

    @classmethod
    def create(cls, data):
        credentials = data.get('credentials', [])

        cred_grp_vo = super().create(data)

        cred_maps = list(map(lambda cred_vo: {'credential_group': cred_grp_vo, 'credential': cred_vo}, credentials))
        list(map(lambda cred_map: CredentialGroupMap.create(cred_map), cred_maps))

        return cred_grp_vo

    def append(self, key, data):
        if key == 'credentials':
            CredentialGroupMap.create({'credential_group': self, 'credential': data})
        else:
            super().append(key, data)

        return self

    def remove(self, key, data):
        if key == 'credentials':
            query = {
                'filter': [{
                    'k': 'credential_group_id',
                    'v': self.credential_group_id,
                    'o': 'eq'
                }, {
                    'k': 'credential_id',
                    'v': data.credential_id,
                    'o': 'eq'
                }]
            }

            credential_group_map_vos, map_count = CredentialGroupMap.query(**query)
            credential_group_map_vos.delete()
        else:
            super().remove(key, data)

        return self


class CredentialGroupMap(MongoModel):
    credential_group = ReferenceField('CredentialGroup', reverse_delete_rule=CASCADE)
    credential = ReferenceField('Credential', reverse_delete_rule=CASCADE)

    meta = {
        'reference_query_keys': {
            'credential_group': CredentialGroup,
            'credential': Credential
        },
        'change_query_keys': {
            'credential_group_id': 'credential_group.credential_group_id',
            'credential_id': 'credential.credential_id'
        },
        'indexes': [
            'credential_group',
            'credential'
        ]
    }