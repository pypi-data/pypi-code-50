from collections import OrderedDict


class ActionSetDict(OrderedDict):
    """
    Custom dict type for instantiating item classes.
    """

    def instantiate(self, name: str, *args, **kwargs) -> None:
        self[name] = self[name](*args, **kwargs)
