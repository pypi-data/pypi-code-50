# -*- coding: utf-8 -*-

from .Map import Map
from .TestSuiteAssignment import TestSuiteAssignment
class TestPhase(Map):
    def __init__(self, q, body = {}):
        self.q = q
        self.sets(body)
    def sets(self, body):
        for key in body:
            self.set(key, body[key])
    def set(self, key, value):
        if key == 'test_suite_assignments':
            self[key] = []
            for t in value:
                self[key].append(TestSuiteAssignment(self.q, self, t))
        elif key in ['created_at', 'updated_at', 'start_on', 'end_on']:
            self[key] = self.q.to_date(value)
        else:
            self[key] = value
        return self
    def add_test_suite_version(self, ts):
        if 'test_suite_versions' not in self:
            self['test_suite_versions'] = []
        self['test_suite_versions'].append(ts)
    def save(self):
        if 'id' in self:
            self.update()
        else:
            self.create()
    def to_json(self):
        json = {}
        for key in self:
            if key in ['start_on', 'end_on']:
                json[key] = self[key].strftime('%Y-%m-%d')
                continue
            if key == 'test_suite_versions':
                json['test_suite_version_ids'] = []
                for test_suite_version in self[key]:
                    json['test_suite_version_ids'].append(test_suite_version.id)
                continue
            if key not in ['q']:
                json[key] = self[key]
        return self.q.to_json({'test_phase': json})
    def create(self):
        url = f'{self.q.url}api/v2/test_phases.json?api_key={self.q.api_key}'
        json = self.q.post_json(url, self.to_json())
        self.sets(json)
        