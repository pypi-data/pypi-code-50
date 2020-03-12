# -*- coding: utf-8 -*-

from .Map import Map
from .TestSuiteVersion import TestSuiteVersion

class TestSuite(Map):
    def __init__(self, q, body = {}):
        self.q = q
        self.sets(body)
    def sets(self, body = {}):
        if body is None:
            return
        for key in body:
            self.set(key, body[key])
    def set(self, key, value):
        if key == 'created_at' or key == 'updated_at':
            self[key] = self.q.to_date(value)
        else:
            self[key] = value
    def get_versions(self):
        url = f'{self.q.url}/api/v2/test_suites/{self.id}/test_suite_versions.json?api_key={self.q.api_key}'
        body = self.q.get_json(url)
        test_suite_versions = []
        for test_suite_version in body['test_suite_versions']:
            test_suite_versions.append(TestSuiteVersion(self.q, self, test_suite_version))
        return test_suite_versions
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
                json['test_suite_versions'] = list(map(lambda t: t.to_json(False), self[key]))
                continue
            if key != 'q':
                json[key] = self[key]
        return self.q.to_json({'test_suite': json})
    def version(self):
        ts = self.q.TestSuiteVersion()
        ts.test_suite = self
        return ts
    def set_version(self, tsv):
        if (self.test_suite_versions is None):
            self.test_suite_versions = []
        self.test_suite_versions.append(tsv)
    def destroy(self):
        url = f'{self.q.url}api/v2/test_suites/{self.id}.json?api_key={self.q.api_key}'
        json = self.q.delete_json(url)
    def create(self):
        if (self.test_suite_versions is None or len(self.test_suite_versions) == 0):
            raise Exception('TestSuite have to have at least one test_suite_versions.')
        url = f'{self.q.url}api/v2/test_suites.json?api_key={self.q.api_key}'
        json = self.q.post_json(url, self.to_json())
        self.sets(json)
        for ts in self.test_suite_versions:
            ts.test_suite = self
            ts.save()
        True