import typing

class Layer:
    def __init__(self,
                 layers: typing.List[typing.Callable] = None,
                 parent: typing.List['Layer'] = None,
                 child=None):
        self.layers = layers
        self._parent = parent
        self.child = child

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    @parent.getter
    def parent(self):
        return self._parent

    def __str__(self):
        return f"Layer({self.layers}) parent:{self._parent}, child:{self.child}"

    def __repr__(self):
        return f"Layer({self.layers})"


class MultiHeadLinkedListLayer:
    def __init__(self, head=None, depth: int = 0):
        if head is None:
            self.head = Layer()
        else:
            self.head = head
        self.tail = self.head
        self._immutable = False
        self.depth = depth

    def _set_immutable(self):
        self._immutable = True

    def append(self, layers: typing.List[typing.Callable]) -> 'MultiHeadLinkedListLayer':
        if self._immutable:
            print("can't append layer")
            return self
        self.depth += 1
        new = Layer(layers)
        self.tail.child = new
        new.parent = [self.tail,]
        self.tail = new
        return self

    def __add__(self, other: 'MultiHeadLinkedListLayer') -> 'MultiHeadLinkedListLayer':
        concat_layer = Layer()
        self.tail.child = concat_layer
        other.tail.child = concat_layer
        concat_layer.parent = [self.tail, other.tail]
        self._set_immutable()
        other._set_immutable()
        if self.depth > other.depth:
            _depth = self.depth
        else:
            _depth = other.depth
        _depth += 1 # for concat layer

        return MultiHeadLinkedListLayer(concat_layer, _depth)

    def __str__(self):
        out = ""
        cur = [self.tail,]
        for _ in range(self.depth):
            parents = []
            out += f"{cur}\n"
            for c in cur:
                if c is None or c.parent is None:
                    parents.append(None)
                    continue
                for p in c.parent:
                    parents.append(p)
            cur = parents
        return out

    def __rper__(self):
        return f"MultiHeadLinkedListLayer({self.depth})"

    def __len__(self):
        return self.depth
