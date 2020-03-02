# pylint: skip-file
import unittest

from ..config import load


class DatabaseConnectionLoaderTestCase(unittest.TestCase):

    def test_load_raises_notimplementederror_with_config_file(self):
        with self.assertRaises(NotImplementedError):
            load(config_dir='foo')

    def test_default_connection_is_self(self):
        connections = load({
            'DB_ENGINE': 'sqlite',
            'DB_NAME': ':mem:'
        })
        self.assertIn('self', connections)
        self.assertEqual(len(connections.keys()), 1)
