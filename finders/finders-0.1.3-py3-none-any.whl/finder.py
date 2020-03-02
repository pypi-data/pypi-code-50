import importlib


class Finder:
    def __init__(self):
        pass

    def init(self, provider):
        if hasattr(self, provider):
            print(f'{provider} provider already set')
            return
        module = importlib.import_module(provider)
        module_class = getattr(module, 'Provider')
        setattr(self, provider, module_class())
