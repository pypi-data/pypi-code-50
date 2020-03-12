# -*- coding: utf-8 -*-

from .Map import Map
from .User import User

class TestSuiteVersion(Map):
    def __init__(self, q, test_suite = None, body = {}):
        self.q = q
        self.test_suite = test_suite
        for key in body:
            sef(key, body[key])
    
    def sets(self, body = {}):
        if body is None:
            return
        for key in body:
            self.set(key, body[key])
    def set(self, key, value):
        if key == 'user':
            self[key] = User(q, value)
        elif key == 'created_at' or key == 'updated_at':
            self[key] = self.q.to_date(value)
        else:
            self[key] = value
    def to_json(self, encode = True):
        json = {}
        for key in self:
            if key == 'test_suite':
                if self[key] is not None and self[key].id is not None:
                    json['test_suite_id'] = self[key].id
                continue
            if key != 'q' and self[key] is not None:
                json[key] = self[key]
        return self.q.to_json(json) if encode else json
    def save(self):
        url = f'{self.q.url}api/v2/test_suites/{self.test_suite.id}/test_suite_versions.json?api_key={self.q.api_key}'
        json = self.q.post_json(url, self.to_json())
        self.sets(json)
