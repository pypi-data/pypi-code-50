
class LinkedNode:
    def __init__(self, value, prev=None):
        self.value = value
        self.prev = prev
        self.len = 1 if prev is None else prev.len + 1

    def __getitem__(self, key):
        try:
            length = len(self)
            n = self
            num_back = length - 1 - key
            if num_back < 0:
                raise IndexError()
            for _ in range(num_back):
                n = n.prev
            return n.value
        except ReferenceError:
            raise IndexError()

    def __str__(self):
        return "["+",".join(map(lambda n: str(n), self))+"]"

    def __len__(self):
        return self.len

    def __iter__(self):
        if self.prev is not None:
            for v in self.prev:
                yield v
        yield self.value

    def __eq__(self, other):
        if self.len != other.len:
            return False
        sn = self
        on = other
        while sn is not None and on is not None:
            if sn.value != on.value:
                return False
            sn = sn.prev
            on = on.prev
        return sn is None and on is None

    def __hash__(self):
        if self.prev is None:
            return hash(self.value)
        else:
            return hash(self.prev) * 31 + hash(self.value)
