from sqlalchemy import or_, and_

from spintop.models import TestRecordSummary

class PostgreSQLQuery(object):
    def __init__(self, query):
        self.orig_query = query
    
    def build_data_query(self, test_record_table):
        """Only support test_uuids for now"""
        test_uuids = []

        for key, value in self.orig_query.value_equals.items():
            if key == TestRecordSummary.test_id.test_uuid.name_:
                test_uuids.append(value)
            else:
                raise NotImplementedError('PostgreSQL QuerySet only supports querying of the test_uuid field.')
        
        for key, value in self.orig_query.list_contains.items():
            raise NotImplementedError()

        for key, list_of_values in self.orig_query.value_equals_one_of.items():
            if key == TestRecordSummary.test_id.test_uuid.name_:
                test_uuids += list_of_values
            else:
                raise NotImplementedError('PostgreSQL QuerySet only supports querying of the test_uuid field.')
        
        if test_uuids:
            return [test_record_table.test_uuid.in_(test_uuids)]
        else:
            return []