# -*- coding: utf-8 -*-

from mongoengine import *

from spaceone.inventory.error import *


class UpdateHistory(EmbeddedDocument):
    key = StringField()
    updated_by = StringField(max_length=40)
    updated_at = IntField()


class CollectionInfo(EmbeddedDocument):
    state = StringField(max_length=20, default='MANUAL', choices=('MANUAL', 'ACTIVE', 'DISCONNECTED'))
    collectors = ListField(StringField(max_length=40))
    update_history = ListField(EmbeddedDocumentField(UpdateHistory))
    pinned_keys = ListField(StringField())
