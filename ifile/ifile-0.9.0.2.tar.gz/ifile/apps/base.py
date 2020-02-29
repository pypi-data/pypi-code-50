
class BaseService(object):
    def __init__(self, name):
        self.name = name
        self._state = None

    def run(self):
        pass

    def stop(self):
        pass

    @property
    def state(self):
        return self._state
