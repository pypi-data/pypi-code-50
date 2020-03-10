# -*- coding: utf-8 -*-

from .Map import Map
from .User import User

class TestResult(Map):
    def __init__(self, q, test_cycle, body):
        self.q = q
        self.test_cycle = test_cycle
        for key in body:
            if key == 'user':
                self[key] = User(q, body[key])
            elif key == 'created_at' or key == 'updated_at' or key == 'executed_at':
                self[key] = q.to_date(body[key])
            else:
                self[key] = body[key]