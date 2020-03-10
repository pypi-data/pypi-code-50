# -*- coding: utf-8 -*-

from .Map import Map
class User(Map):
    def __init__(self, q, body):
        self.q = q
        for key in body:
            if key == 'created_at' or key == 'updated_at':
                self[key] = q.to_date(body[key])
            else:
                self[key] = body[key]
