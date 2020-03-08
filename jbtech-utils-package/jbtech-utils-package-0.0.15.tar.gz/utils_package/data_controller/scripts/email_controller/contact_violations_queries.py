""" Queries for writing to and getting information from the ContactViolations table in the coreapp schema """
from utils_package.data_controller.pg_util import PGUtil
from utils_package.data_controller import query_tools


class ViolationsWriter(object):
    """ Queries for writing to the contact violations table """

    def __init__(self):
        """ Initialize class variables """
        self.violation_pg = PGUtil(user='app_writer', database='catan_local')

    def insert_new_record(self, rel_dict):
        """
        Inserts a new record to coreapp.contactviolations
        :param rel_dict: Dictionary of all relavent information
        :return: Row count and SQL response
        """
        columns, values = query_tools.insert_string_from_dict(rel_dict)
        sql = """
        INSERT INTO coreapp.contactviolations
                    (%s)
        VALUES      (%s)
        """ % (columns, values)
        response = self.violation_pg.execute_query(sql)
        assert response[0] == 1
        assert response[1] is None
        return response
