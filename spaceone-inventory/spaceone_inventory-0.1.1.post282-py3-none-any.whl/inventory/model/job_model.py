# -*- coding: utf-8 -*-
import datetime
from mongoengine import *

from spaceone.core.model.mongo_model import MongoModel
from spaceone.inventory.model.collector_model import Collector


class Job(MongoModel):
    job_id = StringField(max_length=40, generate_id='job', unique=True)
    state = StringField(max_length=20, default='CREATED', 
                choices=('CREATED', 'PENDING', 'IN-PROGRESS', 'SUCESS', 'FAILURE', 'TIMEOUT', 'IDLE'))
    filters = DictField()
    results = DictField()
    collect_mode = StringField(max_length=20, default='ALL',
                choices=('ALL', 'CREATE', 'UPDATE'))
    created_count = IntField()
    updated_count = IntField()
    collected_resources = ListField()
    collector = ReferenceField('Collector')
    domain_id = StringField(max_length=255)
    created_at = DateTimeField(auto_now_add=True)
    finished_at = DateTimeField()

    meta = {
        'db_alias': 'default',
        'updatable_fields': [
            'state',
            'results',
            'created_count',
            'updated_count',
            'collected_resources',
            'finished_at'
        ],
        'exact_fields': [
            'job_id',
        ],
        'minimal_fields': [
            'job_id',
            'state'
        ],
        'change_query_keys': {
            'collector_id': 'collector.collector_id'
        },
        'reference_query_keys': {
            'collector': Collector
        },
        'ordering': [
            'domain_id'
        ],
        'indexes': [
            'job_id'
        ]
    }
 
    def update_collected_at(self, stat):
        stat.update({'finished_at': datetime.datetime.utcnow()})
        return self.update(stat)
