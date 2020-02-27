# Copyright 2019 Okera Inc. All Rights Reserved.
#
# Integration authorization tests
#
# pylint: disable=consider-using-enumerate
# pylint: disable=too-many-locals

import random
import time
import unittest

from okera import context
from okera._thrift_api import TRecordServiceException
from okera._thrift_api import TTypeId

TEST_DB = 'auth_test_db'
TEST_ROLE = 'auth_test_role'
TEST_USER = 'auth_test_user'

class AuthorizationTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """ Initializes one time state that is shared across test cases. This is used
            to speed up the tests. State that can be shared across (but still stable)
            should be here instead of __cleanup()."""
        super(AuthorizationTest, cls).setUpClass()

    # Runs a SQL statement and log it
    @staticmethod
    def __ddl(conn, sql):
        print(sql)
        conn.execute_ddl(sql)

    def __cleanup(self, conn):
        """ Cleanups all the test state used in this test to "reset" the catalog.
            dbs can be specified to do the initialize over multiple databases.
            This can be used for tests that use multiple dbs (but makes the test
            take longer). By default, only load TEST_DB.
        """
        self.__ddl(conn, "DROP ROLE IF EXISTS %s" % TEST_ROLE)
        self.__ddl(conn, "CREATE ROLE %s" % TEST_ROLE)
        self.__ddl(conn, "GRANT ROLE %s to GROUP %s" % (TEST_ROLE, TEST_USER))

    @staticmethod
    def __top_level_columns(schema):
        cols = schema.nested_cols
        if not cols:
            cols = schema.cols
        to_skip = 0
        result = []
        types = []
        for c in cols:
            if to_skip == 0:
                result.append(c.name)
                types.append(c.type)
            else:
                to_skip -= 1
            if c.type.num_children:
                to_skip += c.type.num_children
        return result, types

    @staticmethod
    def __collect_grant_objects(conn):
        grants = conn.execute_ddl('SHOW GRANT ROLE %s' % (TEST_ROLE))
        result = []
        for grant in grants:
            path = ''
            if grant[1]:
                path = grant[1]
                if grant[2]:
                    path += '.' + grant[2]
                    if grant[3]:
                        path += '.' + grant[3]
                else:
                    path += '.*'
            else:
                path = '*'
            result.append(path)
        return result

    # Tests that revokes to a db does not cascade to the table or columns
    def test_revoke_db_no_cascade(self):
        ctx = context()
        with ctx.connect() as conn:
            self.__cleanup(conn)

            # Grant on db, table and column
            conn.execute_ddl(
                'GRANT SELECT ON DATABASE okera_sample TO ROLE %s' % (TEST_ROLE))
            conn.execute_ddl(
                'GRANT SELECT ON TABLE okera_sample.sample TO ROLE %s' % (TEST_ROLE))
            conn.execute_ddl(
                'GRANT SELECT(record) ON TABLE okera_sample.sample TO ROLE %s' %\
                (TEST_ROLE))

            objs = self.__collect_grant_objects(conn)
            print(objs)
            self.assertTrue('okera_sample.*' in objs)
            self.assertTrue('okera_sample.sample' in objs)
            self.assertTrue('okera_sample.sample.record' in objs)
            self.assertTrue(len(objs) == 3)

            # Revoke on db, should not cascade, this cascade can take a while so sleep
            # first. In the test setup, the refresh is 5 seconds.
            conn.execute_ddl(
                'REVOKE SELECT ON DATABASE okera_sample FROM ROLE %s' % (TEST_ROLE))
            time.sleep(7)
            objs = self.__collect_grant_objects(conn)
            print(objs)
            self.assertTrue('okera_sample.sample' in objs)
            self.assertTrue('okera_sample.sample.record' in objs)
            self.assertTrue(len(objs) == 2)

            # Revoke on table, should not cascade.
            conn.execute_ddl(
                'REVOKE SELECT ON TABLE okera_sample.sample FROM ROLE %s' % (TEST_ROLE))
            time.sleep(7)
            objs = self.__collect_grant_objects(conn)
            print(objs)
            self.assertTrue('okera_sample.sample.record' in objs)
            self.assertTrue(len(objs) == 1)

            # Revoke on column.
            conn.execute_ddl(
                'REVOKE SELECT(record) ON TABLE okera_sample.sample FROM ROLE %s' %\
                (TEST_ROLE))
            objs = self.__collect_grant_objects(conn)
            self.assertTrue(len(objs) == 0)

    # Runs ACL tests against db.ds
    def __test_dataset(self, ctx, conn, db, ds):
        ctx.disable_auth()
        schema = conn.plan('select * from %s.%s' % (db, ds)).schema
        cols, types = self.__top_level_columns(schema)
        self.__cleanup(conn)

        # Columns the test user can access. This is appended to below.
        visible_cols = []

        print("Testing dataset: %s.%s..." % (db, ds))

        # Randomize order of columns. We tend to put the types in the same order
        # across tables
        order = list(range(0, len(cols)))
        random.shuffle(order)

        for idx in range(0, len(cols)):
            c = cols[order[idx]]
            print("    granting to col: %s" % c)

            ctx.disable_auth()
            self.__ddl(conn, 'GRANT SELECT(%s) ON TABLE %s.%s TO ROLE %s' %\
                  (c, db, ds, TEST_ROLE))
            visible_cols.append(c)

            # Admin user should always see all columns
            schema = conn.plan('select * from %s.%s' % (db, ds)).schema
            result_cols, _ = self.__top_level_columns(schema)
            self.assertEqual(len(cols), len(result_cols))

            # Try select * as testuser
            ctx.enable_token_auth(token_str=TEST_USER)
            schema = conn.plan('select * from %s.%s' % (db, ds)).schema
            result_cols, _ = self.__top_level_columns(schema)
            self.assertEqual(len(visible_cols), len(result_cols))

            # Wrap this inside an inline view
            sql = "SELECT * FROM (SELECT * FROM %s.%s)v" % (db, ds)
            schema = conn.plan(sql).schema
            result_cols, _ = self.__top_level_columns(schema)
            self.assertEqual(len(visible_cols), len(result_cols))

            # Try selecting from visible cols, should work
            schema = conn.plan('select %s from %s.%s' % \
                (','.join(visible_cols), db, ds)).schema
            result_cols, _ = self.__top_level_columns(schema)
            self.assertEqual(len(visible_cols), len(result_cols))

            # Wrap this inside an inline view
            sql = "SELECT * FROM (SELECT %s FROM %s.%s)v" % \
                (','.join(visible_cols), db, ds)
            schema = conn.plan(sql).schema
            result_cols, _ = self.__top_level_columns(schema)
            self.assertEqual(len(visible_cols), len(result_cols))

            # Wrap this inside a different inline view
            sql = "SELECT %s FROM (SELECT %s FROM %s.%s)v" % \
                (','.join(visible_cols), ','.join(visible_cols), db, ds)
            schema = conn.plan(sql).schema
            result_cols, _ = self.__top_level_columns(schema)
            self.assertEqual(len(visible_cols), len(result_cols))

            # Test column only in WHERE clause, not select list
            if types[order[idx]].type_id == TTypeId.RECORD \
                    or types[order[idx]].type_id == TTypeId.ARRAY \
                    or types[order[idx]].type_id == TTypeId.MAP:
                # We don't support IS NULL on complex types, but it should get past
                # authorization
                with self.assertRaises(TRecordServiceException) as ex_ctx:
                    conn.plan("SELECT %s FROM %s.%s WHERE %s IS NOT NULL" % \
                        (visible_cols[0], db, ds, c))
                self.assertTrue('does not support complex types' in str(ex_ctx.exception))
            else:
                schema = conn.plan(
                    "SELECT %s FROM %s.%s WHERE %s IS NOT NULL" % \
                    (visible_cols[0], db, ds, c)).schema
                result_cols, _ = self.__top_level_columns(schema)
                self.assertEqual(1, len(result_cols))

            # Try selecting from columns past the columns we've granted, these
            # should fail
            for i in range(idx + 1, len(cols)):
                with self.assertRaises(TRecordServiceException) as ex_ctx:
                    conn.plan('select %s from %s.%s' % (cols[order[i]], db, ds))
                self.assertTrue('not have privilege' in str(ex_ctx.exception))

                # Test with a where clause on inaccessible column
                with self.assertRaises(TRecordServiceException) as ex_ctx:
                    conn.plan('select %s from %s.%s WHERE %s IS NOT NULL' %\
                              (','.join(visible_cols), db, ds, cols[order[i]]))
                self.assertTrue('not have privilege' in str(ex_ctx.exception))

                # Add this inaccessible column to the accessible ones, should fail
                # Try a few permutations
                select_list = visible_cols.copy()
                select_list.append(cols[order[i]])
                for _ in range(0, 3):
                    random.shuffle(select_list)
                    with self.assertRaises(TRecordServiceException) as ex_ctx:
                        conn.plan('select %s from %s.%s' % \
                            (','.join(select_list), db, ds))
                    self.assertTrue('not have privilege' in str(ex_ctx.exception))

                if types[i].type_id == TTypeId.RECORD:
                    # Test with a where clause on inaccessible column.
                    # TODO: We hardcode looking for 'f1' as the field inside the
                    # struct. This is true for many structs we use for testing.
                    with self.assertRaises(TRecordServiceException) as ex_ctx:
                        conn.plan('select %s from %s.%s WHERE %s.f1 IS NOT NULL' %\
                                  (','.join(visible_cols), db, ds, cols[order[i]]))
                    self.assertTrue('not have privilege' in str(ex_ctx.exception) or \
                        'Could not resolve' in str(ex_ctx.exception))

        # Grant to entire table
        print("Entire table: " + ds)
        ctx.disable_auth()
        conn.execute_ddl('GRANT SELECT ON TABLE %s.%s TO ROLE %s' %\
              (db, ds, TEST_ROLE))

        # Try select * as testuser, should see everything
        self.assertTrue(len(visible_cols), len(cols))
        ctx.enable_token_auth(token_str=TEST_USER)
        schema = conn.plan('select * from %s.%s' % (db, ds)).schema
        result_cols, _ = self.__top_level_columns(schema)
        self.assertEqual(len(cols), len(result_cols))

        # Try selecting from visible cols, should work
        schema = conn.plan('select %s from %s.%s' % \
            (','.join(visible_cols), db, ds)).schema
        result_cols, _ = self.__top_level_columns(schema)
        self.assertEqual(len(cols), len(result_cols))

    # Tests that verify grants to complex types works. This programmatically gets
    # columns to the table/view and increasingly grants more access to it.
    # TODO: find a library to compute powerset of columns.
    def test_complex_types(self):
        # FIXME: These are not working.
        not_working = ['struct_nested_s1_s2']
        print("THESE ARE NOT WORKING: " + str(not_working))

        # These tests are N^2 with the number of columns so don't run these by default
        slow = ['test_bucketing_tbl', 'zd1216', 'zd1216_with_subscriptionlimit']
        print("THESE ARE SLOW: " + str(slow))

        ctx = context()
        with ctx.connect() as conn:
            for ds in ['struct_t', 'struct_t2', 'struct_t3', 'struct_nested',
                       'struct_array_struct', 'struct_t_id', 'struct_nested_s1_f1',
                       'struct_view', 'struct_t_view', 'struct_t_view2',
                       'struct_t_s1', 'struct_nested_view', 'struct_nested_s1',
                       'rs_complex_array_map_t', 'strarray_t', 'strarray_t_view',
                       'array_struct_array', 'array_struct_t', 'array_t', 'avrotbl',
                       'map_t', 'market_v20_single', 'market_v30_single',
                       'multiple_structs_nested', 'users', 'user_phone_numbers',
                       'user_phone_numbers_map', 'view_over_multiple_structs']:
                self.__test_dataset(ctx, conn, 'rs_complex', ds)

if __name__ == "__main__":
    unittest.main()
