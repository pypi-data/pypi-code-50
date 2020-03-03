# -*- coding: utf-8 -*-

import os

from .helper import BaseHelper
from migratron.command.initialize import CREATE_TABLE_SQL
from migratron.command.run_migration import RunMigrationCommand, ALL_MIGRATION_TYPES


class RunMigrationCommandTest(BaseHelper):
    def setUp(self):
        super(RunMigrationCommandTest, self).setUp()
        self.command = RunMigrationCommand(
            migration_type=ALL_MIGRATION_TYPES,
            just_list_files=False,
            psql_additional_options=None,
            **self.BASE_ARGS
        )
        with self.command.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(CREATE_TABLE_SQL)

    def test_no_migrations(self):
        self.command.run()
        self.assertEqual(self._get_executed_migrations(), [])

    def test_run_new_migrations(self):
        self._create_migration_files()
        self.command.run()
        self.assertEqual(self._get_executed_migrations(), self.valid_filenames)
        for table_name in ["t0", "t1"]:
            self.assertTrue(self._check_table_exist(table_name))

    def test_run_missing_migrations(self):
        self._create_migration_files()
        self._insert_migration_data(self.valid_filenames[0])
        self.command.run()
        self.assertEqual(self._get_executed_migrations(), self.valid_filenames)
        self.assertTrue(self._check_table_exist("t1"))
        self.assertFalse(self._check_table_exist("t0"))

    def test_run_failed_migration(self):
        self._create_migration_files()
        file_path = os.path.join(self.migrations_path, self.valid_filenames[0])
        with open(file_path, "w") as f:
            f.write("SELECT 1 / 0;")

        with self.assertRaises(Exception):
            self.command.run()

        executed_filenames = self._get_executed_migrations()
        self.assertEqual(executed_filenames, [self.valid_filenames[0]])

    def test_filter_migration_type(self):
        self._create_migration_files()
        self.command.migration_type = "pre"
        self.command.run()
        self.assertEqual(self._get_executed_migrations(), [self.valid_filenames[0]])
        self.assertFalse(self._check_table_exist("t1"))
        self.assertTrue(self._check_table_exist("t0"))
