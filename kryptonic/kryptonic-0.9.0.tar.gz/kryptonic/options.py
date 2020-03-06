import logging as log

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=Singleton):

    DEFAULT_OPTIONS = {
        'url': 'http://localhost:5000',
        'headless': False,
        'cleanup': 'always',
        'cleanup_db_writes': 'always' #TODO: this is the mongo extension
    }

    def __init__(self, **kwargs):
        self.options = self.DEFAULT_OPTIONS
        options_names = self.DEFAULT_OPTIONS.keys()
        for key, value in kwargs.items():
            if key not in options_names:
                log.warning(f'kr WARN: option {key} is not a valid option. Skipping.')
                continue
            self.options[key] = value

    def overwrite_options(self, **kwargs):
        options_names = self.DEFAULT_OPTIONS.keys()
        for key, value in kwargs.items():
            if key not in options_names:
                log.warning(f'kr WARN: option {key} is not a valid option. Skipping.')
                continue
            log.debug(f'Overwriting config option {key} to be {value} (was {self.options[key]})')
            self.options[key] = value

