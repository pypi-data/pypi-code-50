import importlib


class Provider:
    def __init__(self):
        self._profiles = None

    @property
    def profiles(self):
        return self._profiles

    @profiles.setter
    def profiles(self, profiles):
        self._profiles = profiles

    def scrape(self, resource):
        module = importlib.import_module(f'aws.{resource}')
        module_class = getattr(module, 'Resource')
        instance = module_class(profiles=self.profiles, regions=self.regions)
        return instance.scrape()
