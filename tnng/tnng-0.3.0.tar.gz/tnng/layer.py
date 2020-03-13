import typing


class DummyConcat:
    def __init__(self, dummy_args):
        self.dummy_args = dummy_args
    def __call__(self, x):
        return x


class BaseLayer:
    def __init__(self,
                 parent: typing.List['Layer'] = None,
                 child=None):
        self.layers = None
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
        return f"{self.__class__.__name__}({self.layers}) parent:{self._parent}, child:{self.child}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.layers})"


class Layer(BaseLayer):
    def __init__(self,
                 layers: typing.List[typing.Callable] = None,
                 parent: typing.List['Layer'] = None,
                 child=None):
        super(Layer, self).__init__(parent, child)
        if layers is not None:
            layers[0] # check index access
            len(layers) # check length access
        assert isinstance(parent, list) or parent is None
        self.layers = layers


class LazyLayer(BaseLayer):
    def __init__(self,
                 klass=None,
                 kwargs_list: list=None,
                 parent: typing.List['Layer'] = None,
                 child=None):
        super(LazyLayer, self).__init__(parent, child)
        if kwargs_list is not None:
            kwargs_list[0] # check index access
            len(kwargs_list) # check length access
            assert isinstance(kwargs_list[0], dict)
        self.klass = klass
        self.kwargs_list = kwargs_list
        self.layers = kwargs_list #


class MultiHeadLinkedListLayer:
    def __init__(self, head=None, depth: int = 0):
        if head is None:
            self.head = Layer()
        else:
            self.head = head
        assert isinstance(self.head, (Layer, LazyLayer))
        self.tail = self.head
        self._immutable = False
        self.depth = depth
        self.klass_set = set()

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

    def append_lazy(self, klass, layers: typing.List['kwargs']) -> 'MultiHeadLinkedListLayer':
        if self._immutable:
            print("can't append Lazy Layer")
            return self
        self.klass_set.add(klass)
        self.depth += 1
        new = LazyLayer(klass, layers)
        self.tail.child = new
        new.parent = [self.tail,]
        self.tail = new
        return self

    def __add__(self, other: 'MultiHeadLinkedListLayer') -> 'MultiHeadLinkedListLayer':
        concat_layer = LazyLayer(DummyConcat, [dict(dummy_args=True),])
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
