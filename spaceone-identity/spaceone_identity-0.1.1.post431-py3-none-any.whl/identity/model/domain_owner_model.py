# -*- coding: utf-8 -*-

from mongoengine import *

from spaceone.core.error import *
from spaceone.core.model.mongo_model import MongoModel


class DomainOwner(MongoModel):
    owner_id = StringField(max_length=40, unique_with='domain_id', required=True)
    password = BinaryField()
    name = StringField(max_length=128)
    email = StringField(max_length=255)
    mobile = StringField(max_length=24)
    language = StringField(max_length=7, default='en')
    timezone = StringField(max_length=50, default='Etc/GMT')
    # roles = ListField(ReferenceField('Role'))
    last_accessed_at = DateTimeField(auto_now_add=True)
    created_at = DateTimeField(auto_now_add=True)
    domain_id = StringField(max_length=40)

    meta = {
        'updatable_fields': [
            'owner_id',
            'password',
            'name',
            'email',
            'mobile',
            'language',
            'timezone',
            'state',
            'roles'
        ],
        'exact_fields': [
            'owner_id',
            'domain_id'
        ],
        'minimal_fields': [
            'owner_id',
            'name',
            'state',
            'domain_id'
        ],
        'ordering': ['name'],
        'indexes': [
            'owner_id'
        ]
    }

    @classmethod
    def create(cls, data):
        user_vos = cls.filter(domain_id=data['domain_id'])
        if user_vos.count() > 0:
            raise ERROR_NOT_UNIQUE(key='owner_id', value=data['owner_id'])
        return super().create(data)

    def update(self, data):
        return super().update(data)
