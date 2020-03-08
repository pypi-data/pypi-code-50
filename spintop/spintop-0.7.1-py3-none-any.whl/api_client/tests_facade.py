from datetime import datetime

from spintop.persistence.base import PersistenceFacade

from ..models import Query, get_json_serializer, SpintopTestRecord

class SpintopAPIPersistenceFacade(PersistenceFacade):
    def __init__(self, spintop_api):
        self.spintop_api = spintop_api

    @property
    def session(self):
        return self.spintop_api.session

    def create(self, records):
        serialized = self._serialize_records(records)
        return self.session.post(self.spintop_api.get_link('tests.create'), json=serialized)
        
    def _serialize_records(self, records):
        serialize = get_json_serializer().serialize
        return {'tests': [serialize(tr) for tr in list(records)]}

    def retrieve(self, query=Query()):
        query_dict = query.as_dict()
        resp = self.session.get(self.spintop_api.get_link('tests.retrieve'), params=query_dict)
        tests = resp.json()['tests']
        for test in tests:
            yield get_json_serializer().deserialize(SpintopTestRecord, test)

    def retrieve_one(self, test_uuid):
        resp = self.session.get(self.spintop_api.get_link('tests.retrieve_one', test_uuid=test_uuid))
        test = resp.json()
        return get_json_serializer().deserialize(SpintopTestRecord, test)
        
    def update(self, records):
        serialized = self._serialize_records(records)
        return self.session.put(self.spintop_api.get_link('tests.update'), json=serialized)
    
    def delete(self, query=Query()):
        query_dict = query.as_dict()
        return self.session.delete(self.spintop_api.get_link('tests.delete'), params=query_dict)