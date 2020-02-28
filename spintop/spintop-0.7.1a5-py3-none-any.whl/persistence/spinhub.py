from datetime import datetime

from .base import PersistenceFacade

from ..models import Query, get_json_serializer, SpintopTestRecord

class SpinHubPersistenceFacade(PersistenceFacade):
    def __init__(self, spinhub):
        self.spinhub = spinhub

    @property
    def session(self):
        return self.spinhub.session

    @property
    def tests_endpoint(self):
        return '/tests/{}'.format(self.spinhub.default_org)

    def create(self, records):
        serialize = get_json_serializer().serialize
        records = [serialize(tr) for tr in list(records)]
        return self.session.post(self.tests_endpoint, json=dict(tests=records))
        
    def retrieve(self, query=Query()):
        query_dict = query.as_dict()
        resp = self.session.get(self.tests_endpoint, params=query_dict)
        tests = resp.json()['tests']
        for test in tests:
            yield get_json_serializer().deserialize(SpintopTestRecord, test)
        
    def update(self, records):
        raise NotImplementedError()
    
    def delete(self, query=Query()):
        query_dict = query.as_dict()
        return self.session.delete(self.tests_endpoint, params=query_dict)