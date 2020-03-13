import os
from dataclasses import dataclass


class SpintopEnv(object):
    ENV_NAMES = [
        'SPINTOP_MONGO_URI',
        'SPINTOP_DATABASE_NAME',
        'SPINTOP_POSTGRES_URI',
        'SPINTOP_API_URL'
    ]

    def __init__(self, init_values=None):
        if init_values is None:
            init_values = {}
        self._values = init_values

    def __getitem__(self, key):
        if key not in self.ENV_NAMES:
            raise KeyError(key)
        
        try:
            return self._values[key]
        except KeyError:
            return os.environ[key]
    
    def __setitem__(self, key, value):
        self._values[key] = value

    def freeze(self):
        return {key: self[key] for key in self.ENV_NAMES}

    
