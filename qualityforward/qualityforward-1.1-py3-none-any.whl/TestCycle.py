# -*- coding: utf-8 -*-

from .Map import Map
from .TestResult import TestResult

class TestCycle(Map):
    def __init__(self, q, test_suite_assignment, body):
        self.q = q
        self.test_suite_assignment = test_suite_assignment
        for key in body:
            if key == 'created_at' or key == 'updated_at':
                self[key] = q.to_date(body[key])
            else:
                self[key] = body[key]
    def get_results(self):
        url = f'{self.q.url}/api/v2/test_phases/{self.test_suite_assignment.test_phase_id}/test_suite_assignments/{self.test_suite_assignment.id}/test_cycles/{self.id}/test_results.json?api_key={self.q.api_key}'
        body = self.q.get_json(url)
        test_results = []
        for test_result in body['test_results']:
            test_results.append(TestResult(self.q, self, test_result))
        return test_results
        