class DynamoDataAttribute(object):
    def __init__(self, datatype, value=None, initialized=True):
        self.datatype = datatype
        self.value = self.datatype.build(value)
        self.initialized = initialized
        self._changed = False

    def get(self):
        return self.value

    def set(self, newvalue):
        self._changed = True
        self.value = self.datatype.build(newvalue)

    def as_dict(self):
        if self.value is not None:
            return self.datatype.as_dict(self.value)
        return None


