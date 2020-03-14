import os

from unittest import TestCase

from credentials_manager import CredentialsManager


class TestCredentialsManager(TestCase):

    def test_file_path(self):
        fn = 'test.ini'
        creds = CredentialsManager(filename=fn)
        self.assertEqual(
            creds._file_path,
            os.path.join(os.path.expanduser('~/'), fn),
        )

    def test_keyring_name(self):
        fn = 'test.ini'
        creds = CredentialsManager(filename=fn)
        bits = creds.keyring_name_bits[:]
        bits.append(fn.split('.')[0])
        self.assertEqual(
            creds._keyring_name,
            '.'.join(bits),
        )