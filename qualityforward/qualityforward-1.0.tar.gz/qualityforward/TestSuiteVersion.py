# -*- coding: utf-8 -*-

from .Map import Map
from .User import User

class TestSuiteVersion(Map):
    def __init__(self, q, test_suite = None, body = {}):
        self.q = q
        self.test_suite = test_suite
        for key in body:
            sef(key, body[key])
    
    def set(self, key, value):
        if key == 'user':
            self[key] = User(q, value)
        elif key == 'created_at' or key == 'updated_at':
            self[key] = q.to_date(value)
        else:
            self[key] = value
