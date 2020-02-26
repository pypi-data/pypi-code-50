#  Copyright (c) 2020. Brendan Johnson. All Rights Reserved.

from os.path import expanduser
import configparser
from DeepSecurity import config

class Session():
    def __init__(self):
        self._config = configparser.ConfigParser()
        self._creds = configparser.ConfigParser()
        self._config.read('/Users/brendan/.cloudone/config')
        self._creds.read('/Users/brendan/.cloudone/credentials')

    def BuildDSMConfig(self, profile):
        self._configuration = config.Config()
        self._configuration.host = self._config[profile]['DSMhost']
        self._configuration.api_key = self._creds[profile]['DSMapikey']
        if self._config[profile]['DSMverifyssl'].lower() == "false":
            self._configuration.verify_ssl = False
        return self._configuration
    def BuildSCConfig(self, profile):
        self._configuration = config.Config()
        self._configuration.host = self._config[profile]['SChost']
        self._configuration.username = self._creds[profile]['SCUser']
        self._configuration.password = self._creds[profile]['SCPassword']
        if self._config[profile]['SCverifyssl'].lower() == "false":
            self._configuration.verify_ssl = False
        return self._configuration


