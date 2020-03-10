# -*- coding: utf-8 -*-

from .Map import Map
from .TestSuiteVersion import TestSuiteVersion

class TestSuite(Map):
    def __init__(self, q, body):
        self.q = q
        for key in body:
            if key == 'created_at' or key == 'updated_at':
                self[key] = q.to_date(body[key])
            else:
                self[key] = body[key]
    def get_versions(self):
        url = f'{self.q.url}/api/v2/test_suites/{self.id}/test_suite_versions.json?api_key={self.q.api_key}'
        body = self.q.get_json(url)
        test_suite_versions = []
        for test_suite_version in body['test_suite_versions']:
            test_suite_versions.append(TestSuiteVersion(self.q, self, test_suite_version))
        return test_suite_versions
