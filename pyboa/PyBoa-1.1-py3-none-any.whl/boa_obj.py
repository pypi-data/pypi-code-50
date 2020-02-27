import random
import functools


class Dict(dict):
    def __init__(self, d):
        for k, v in d.items():
            d[k] = boa(v)
        super().__init__(d)

    def __getattribute__(self, name):
        """get, if exist, ``dict`` data then ``dict`` attribut"""
        if name in dict.keys(self):
            return dict.get(self, name)
        return super(Dict, self).__getattribute__(name)

    def __setattr__(self, name, value):
        dict.update(self, {name: boa(value)})

    def __setitem__(self, key, value):
        dict.update(self, {key: boa(value)})

    def toPython(self):
        return to_py(self)


class List(list):
    def __init__(self, li):
        super().__init__(map(boa_if_not_already, li))

    def map(self, fun):
        return List(map(fun, self))

    def reduce(self, fun):
        return functools.reduce(fun, self)

    def filter(self, fun):
        return List(filter(fun, self))

    def index(self, elem, *args, raise_exception=True):
        try:
            return super().index(elem, *args)
        except ValueError as e:
            if raise_exception:
                raise e
            return None

    def reverse(self, side_effect=False):
        if side_effect:
            return list.reverse(self)
        return List(self[::-1])

    def shuffle(self):
        li = self[:]
        random.shuffle(li)
        return li

    def randomChoice(self):
        return random.choice(self)

    def copy(self):
        return List(self[:])

    def append(self, el):
        list.append(self, boa(el))

    def toPython(self):
        return to_py(self)


def boa(data, raise_exception=True):
    """
        transforme recursively a Python ``dict``, ``list`` into a Boa
        :param data: insert any Python data
        :return: the corresponding Boa data
    """
    if isinstance(data, List) or isinstance(data, Dict):
        if raise_exception:
            raise ValueError("the data given is already Boa data\n" +
                             "if you don't want to raise an exception, pass raise_exception=False")
        else:
            return data

    if isinstance(data, list) or isinstance(data, tuple):
        return List(data)
    elif isinstance(data, dict):
        return Dict(data)
    else:
        return data


def boa_if_not_already(data):
    return boa(data, raise_exception=False)


def to_py(data):
    if isinstance(data, List):
        return list(map(to_py, data))
    elif isinstance(data, Dict):
        return {k: to_py(v) for k, v in data.items()}
    else:
        return data
