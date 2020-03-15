class primary_key(object):
    def __init__(self, partition_key, sort_key=None):
        self.partition_key = partition_key
        self.sort_key = sort_key

    def __call__(self, cls):
        column = getattr(cls, self.partition_key)
        if self.sort_key:
            cls._primary_key = (column, getattr(cls, self.sort_key))
        else:
            cls._primary_key = (column,)
        return cls

