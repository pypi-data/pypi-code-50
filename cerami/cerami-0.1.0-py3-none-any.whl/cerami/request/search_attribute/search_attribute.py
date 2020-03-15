class SearchAttribute(object):
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def add(self, value):
        self.value = value

    def build(self):
        return self.value
