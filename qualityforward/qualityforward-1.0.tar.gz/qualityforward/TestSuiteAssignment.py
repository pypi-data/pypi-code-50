# -*- coding: utf-8 -*-

from .Map import Map
from .TestCycle import TestCycle

class TestSuiteAssignment(Map):
    def __init__(self, q, test_phase, body):
        self.q = q
        self.test_phase = test_phase
        for key in body:
            if key == 'created_at' or key == 'updated_at':
                self[key] = q.to_date(body[key])
            else:
                self[key] = body[key]
    def get_cycles(self):
        url = f'{self.q.url}/api/v2/test_phases/{self.test_phase.id}/test_suite_assignments/{self.id}/test_cycles.json?api_key={self.q.api_key}'
        body = self.q.get_json(url)
        test_cycles = []
        for test_cycle in body['test_cycles']:
            test_cycles.append(TestCycle(self.q, self, test_cycle))
        return test_cycles
