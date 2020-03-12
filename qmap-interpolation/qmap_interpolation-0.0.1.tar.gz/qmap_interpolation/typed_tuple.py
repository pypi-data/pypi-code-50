class TypedTuple(object):
    """
    Simple analog of NamedTuple with type checking. It raises TypeError if attribute types are wrong,
    allows setting new attributes and supports rewriting the __init__ method.
    However, it does not support any fancy types from typing module (e.g., List[int]).

    Examples:

    >>> class MyStructure(TypedTuple):
    ...    a: int
    ...    b: float
    ...    c: str = None
    ...
    >>> s = MyStructure(1, 1.2)
    >>> s.a
    1
    >>> s.b
    1.2
    >>> s.c is None
    True
    >>> s = MyStructure(1, 1.2, 1)
    Traceback (most recent call last):
     ...
    TypeError: Argument c has a wrong type: expected str, provided int instead.
    >>> s = MyStructure(1, 1, 'a')
    >>> s.c
    'a'
    >>> s.c = 'b'
    Traceback (most recent call last):
     ...
    AttributeError: Attempt to overwrite an existing attribute c.
    >>> s.d = 1
    >>> s.d
    1
    >>> s.asdict()
    {'a': 1, 'b': 1, 'c': 'a'}
    >>> s.update(a=2)
    MyStructure(a=2, b=1, c='a')
    """

    def __new__(cls, *args, **kwargs):
        if args:
            if len(args) > len(cls.__annotations__):
                raise ValueError(f'Wrong number of positional arguments.'
                                 f' Expected {len(cls.__annotations__)}, provided {len(args)}')
            for attr_value, attr_name in zip(args, cls.__annotations__.keys()):
                if attr_name in kwargs:
                    raise ValueError(f'Argument {attr_name} provided twice.')
                kwargs[attr_name] = attr_value
        for attr_name, attr_type in cls.__annotations__.items():
            if attr_name in kwargs:
                if not isinstance(kwargs[attr_name], attr_type):
                    if not (attr_type is float and isinstance(kwargs[attr_name], int)):
                        raise TypeError(f'Argument {attr_name} has a wrong type: expected {attr_type.__name__}, '
                                        f'provided {type(kwargs[attr_name]).__name__} instead.')
            elif attr_name in cls.__dict__:
                kwargs[attr_name] = getattr(cls, attr_name)
            else:
                raise ValueError(f'Missing non-default argument {attr_name}.')

        instance = super().__new__(cls)
        for attr_name, attr_value in kwargs.items():
            setattr(instance, attr_name, attr_value)
        return instance

    def __setattr__(self, key, value):
        if key in self.__annotations__ and key in self.__dict__:
            raise AttributeError(f'Attempt to overwrite an existing attribute {key}.')
        super().__setattr__(key, value)

    def asdict(self):
        return {k: getattr(self, k) for k in self.__annotations__.keys()}

    def update(self, **kwargs):
        params = self.asdict()
        params.update(kwargs)
        return self.__class__(**params)

    def __repr__(self):
        attr_line = ", ".join([f"{k}={v}" if not isinstance(v, str) else f"{k}='{v}'"
                              for k, v in self.asdict().items()])
        return f'{self.__class__.__name__}({attr_line})'


if __name__ == '__main__':
    import doctest
