class DeClass(object):
    """
    Class used for __repr__ of schema
    """
    def __init__(self, _name=None, _resp=("", ""), **kwargs):
        self._resp = _resp
        self._name = _name
        for a in kwargs:
            setattr(self, a, kwargs[a])

    def __repr__(self):
        f = getattr(self, self._resp[0])
        s = getattr(self, self._resp[1])
        return '<{} {} {}>'.format(self._name, f, s)
