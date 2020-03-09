import logging

import keyring

from jsonnote import jsonnote

logger = logging.getLogger(__name__)

class safe:

    _srctype = None
    _service = None
    _alias = None
    _user = None
    _pwd = None
    _unsecure = jsonnote()
    _sepid = '_id_:'
    _seppwd = '_pwd_:'

    CREDS_TYPE_PLAIN = 'plain' # used for storing credentials as plain text in JSON format
    CREDS_TYPE_SECURE = 'keyring' # used for storing credentials securely using keyring package
    KWD_UID = 'uid'
    KWD_PWD = 'pwd'
    DEFAULT_FNAME_PLAIN = 'creds'

    def __init__(self, type=None):
        self._unsecure.filename = self.DEFAULT_FNAME_PLAIN
        self._unsecure.mustdelete = True
        self._unsecure.mustsave = True
        self.type = type
        if type == None:
            self.type = self.CREDS_TYPE_SECURE
        assert self.type == self.CREDS_TYPE_PLAIN or self.type == self.CREDS_TYPE_SECURE, 'Invalid credentials type value.'

    @property
    def type(self):
        return self._srctype

    @type.setter
    def type(self, val):
        self._srctype = val

    @property
    def service(self):
        if self.type != self.CREDS_TYPE_SECURE:
            raise AttributeError('Wrong value for credentials type: ' + self.type)
        return self._service

    @service.setter
    def service(self, val):
        if self.type != self.CREDS_TYPE_SECURE:
            raise AttributeError('Wrong value for credentials type: ' + self.type)
        self._service = val

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, val):
        self._alias = val

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, val):
        self._user = val

    @property
    def password(self):
        return self._pwd

    @password.setter
    def password(self, val):
        self._pwd = val

    @property
    def plain(self):
        if self.type != self.CREDS_TYPE_PLAIN:
            raise AttributeError('Wrong value for credentials type: ' + self.type)
        return self._unsecure

    def get(self):
        if self.type == self.CREDS_TYPE_SECURE:
            self.__get_secure__()
        elif self.type == self.CREDS_TYPE_PLAIN:
            self.__get_plain__()
        else:
            raise ValueError('Could not detemine credentials type.')

    def set(self):
        if self.type == self.CREDS_TYPE_SECURE:
            self.__set_secure__()
        elif self.type == self.CREDS_TYPE_PLAIN:
            self.__set_plain__()
        else:
            raise ValueError('Could not detemine credentials type.')

    def delete(self):
        if self.type == self.CREDS_TYPE_SECURE:
            self.__delete_secure__()
        elif self.type == self.CREDS_TYPE_PLAIN:
            self.__delete_plain__()
        else:
            raise ValueError('Could not detemine credentials type.')

    def __delete_secure__(self):
        keyring.delete_password(self.service, self.alias)

    def __delete_plain__(self):
        self.plain.destroy()

    def __set_plain__(self):
        self.plain.contents = { self.alias: { self.KWD_UID: self.user, self.KWD_PWD: self.password } }
        self.plain.save_to_file()

    def __get_plain__(self):
        self.plain.get_from_file()
        t = self.plain.contents[self.alias]
        self.user = t[self.KWD_UID]
        self.password = t[self.KWD_PWD]

    def __set_secure__(self):
        assert self.user is not None and self.password is not None
        actual = self._sepid + self.user + self._seppwd + self.password
        keyring.set_password(self.service, self.alias, actual)

    def __get_secure__(self):
        actual = keyring.get_password(self.service, self.alias)
        if actual is not None:
            self.user = (actual.split(self._sepid)[1]).split(self._seppwd)[0]
            self.password = actual.split(self._seppwd)[1]
