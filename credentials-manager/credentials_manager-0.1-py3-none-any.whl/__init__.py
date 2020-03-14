import os
import getpass
import configparser
import keyring


class CredentialsManager(object):
    _cred_section = 'credentials'
    username = None
    password = None
    keyring_name_bits = ['python', 'script']

    def __init__(self, filename=None):
        if filename is None:
            import __main__
            self.filename = '.%s.ini' % __main__.__file__.split('/')[-1]
        else:
            self.filename = filename

    @property
    def _file_path(self):
        return os.path.abspath(os.path.expanduser('~/%s' % self.filename))

    @property
    def _keyring_name(self):
        bits = self.keyring_name_bits[:]
        fn = self.filename.replace('.ini', '').replace('.py', '')
        bits.append(fn.strip('.'))
        return '.'.join(bits)

    def load(self):
        # Open the file to get the username
        try:
            fp = open(self._file_path, 'r')
        except IOError:
            print("Config '{}' file does not exist, creating..".format(self.filename))
            return self.create()
        else:
            fp.close()

        cp = configparser.ConfigParser()
        loaded = cp.read(self._file_path)
        if not loaded:
            print("Problem loading config file")
        else:
            self.username = cp.get(self._cred_section, 'username')
            # Get the password from the keychain
            self.password = keyring.get_password(
                self._keyring_name, self.username)
            if self.password is None:
                return self.create()

    def create(self):
        self.username = input("Please enter a username: ")
        self.password = getpass.getpass("Please enter a password: ")
        cp = configparser.ConfigParser()
        cp.add_section(self._cred_section)
        cp.set(self._cred_section, 'username', self.username)
        keyring.set_password(self._keyring_name, self.username, self.password)
        cp.write(open(self._file_path, 'w'))

    def save(self):
        pass

    def purge(self):
        if os.path.exists(self._file_path):
            print("Purging old config file: {}".format(self._file_path))
            os.remove(self._file_path)
