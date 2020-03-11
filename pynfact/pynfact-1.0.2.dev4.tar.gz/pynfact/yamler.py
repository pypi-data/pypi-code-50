# vim: set ft=python fileencoding=utf-8 tw=72 fdm=indent nowrap:
"""
    pynfact.yamler
    ~~~~~~~~~~~~~~

    Handles a YAML file by setting a default value when variable
    is not set.

    :copyright: (c) 2012-2020, J. A. Corbal
    :license: MIT
"""
import sys
import yaml


class Yamler:
    """Handles a YAML file."""

    def __init__(self, filename):
        """Initializer.

        :param filename: YAML filename where to look for the config.
        :type filename: str
        """
        self.filename = filename
        self.fd = None
        try:
            with open(self.filename, 'r') as self.fd:
                self.config = yaml.load(self.fd)
        except IOError:
            sys.exit("pynfact.Yamler: cannot read configuration file")


    def __del__(self):
        """Destructor."""
        if (self.fd):
            self.fd.close()


    def __getitem__(self, key):
        try:
            value = self.config[key]
        except KeyError:
            sys.exit("pynfact.Yamler: key not found")
        else:
            return value


    def retrieve(self, key, default_value=None):
        """Gets a value from a key or sets a default value."""
#        try:
#            value = self.config[key]
#        except KeyError:
#            value = default_value
#        else:
#            return value
        if key in self.config:
            value = self.config[key]
        else:
            value = default_value
        return value

