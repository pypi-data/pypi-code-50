"""meta-class for table class
parse fields
and generate realted information
"""
import sys
from functools import partial
from typing import Type, Tuple, Dict, Any, cast, List
import bisect

from .parameter import Parameter
from .utils import get_name, get_module_configs


class TableMeta(type):
    """[summary]
    :py:class:`fusionflow.uploads.Field`
    :param type: [description]
    :type type: [type]
    :return: [description]
    :rtype: [type]
    """

    def __new__(mcs: Type["TableMeta"], name: str, base: Tuple[Type, ...],
                attrs: Dict[str, Any], **kwargs: Any) -> "TableMeta":
        cls = super().__new__(mcs, name, base, attrs)
        cls = cast("TableMeta", cls)
        #
        configs = get_module_configs(sys.modules[cls.__module__])
        # TODO: parse module setting
        # both subclass and instance
        # class private attribute, not override by subclass
        cls.__parameters = []
        cls._table_name = name.lower()
        cls.__names = set()

        cls.__validators = {'row': [], 'field': {}}

        # travel through all base class
        for c in cls.__mro__:
            for name, param in filter(
                lambda pair: isinstance(pair[1], Parameter), vars(c).items()
            ):
                # overrided by subclass and is not :class:`Paramete`_
                if name in attrs and not isinstance(attrs[name], Parameter):
                    continue

                if not param.name:
                    param.name = name

                if name not in cls.__names:
                    # setting through configs
                    if name in configs:
                        print('set configs')
                        setattr(cls, name, configs[name])
                        continue

                    cls.__names.add(name)
                    # positional parameter first
                    bisect.insort(
                        cls.__parameters, (
                            not param.positional, param._create_counter,
                            name, param
                        )
                    )

        # validators
        for name in attrs:
            # filed validator
            if name.startswith("validate_"):
                cls.__validators['field'].setdefault(
                    name[len('validate_'):], []
                ).append(name)
            # row validator
            elif name.startswith("validate"):
                cls.__validators['row'].append(name)

        # docstring
        param_docs: List[str] = []
        for is_positional, counter, name, param in cls.__parameters:
            if param.type_:
                name = get_name(param.type_) + " " + name

            prefix = ":param {}: ".format(name)
            for lineno, line in enumerate((param.__doc__ or "").split("\n")):
                param_docs.append(
                    (" " * len(prefix) if lineno else prefix) + line
                )

        filtered = filter(None, ("\n".join(param_docs), cls.__doc__))
        cls.__doc__ = "\n".join(
            map(str.strip, filtered)  # type: ignore
        )

        return cls

    @property
    def __parameters__(cls):
        return [
            (name, parameter)
            for _, _, name, parameter in cls.__parameters
        ]

    @property
    def __parameters_dict__(cls):
        return dict(cls.__parameters__)

    @property
    def __validators__(cls):
        return cls.__validators

    def __setattr__(self, name: str, value: Any) -> Any:
        """for typing check """
        super().__setattr__(name, value)

    def __getattr__(self, name: str) -> Any:
        """for typing check"""
        raise AttributeError


class PartialTable(partial):
    @property
    def missing(self):
        """missing parameters used in instantiate class object

        """
        return self.missing_

    def __new__(cls, *args, missing_=None, **kwargs):
        print(missing_, kwargs)
        obj = super().__new__(cls, *args, **kwargs)
        obj.missing_ = missing_

        return obj

    def __getattr__(self, item):
        params = self.func.__parameters_dict__
        kwargs = self.keywords
        # in passed kwargs
        if item in kwargs:
            return kwargs[item]
        # in parameters, return Default value
        if item in params:
            return params[item].__get__(self, self.func)

        cls_attr = getattr(self.func, item)
        # throw error when use object's bound methods
        if callable(cls_attr) or isinstance(cls_attr, property):
            raise ValueError("""table[{}] not fully instantiation because of missing parameters:\n\t{}
                    """. format(self.table_name, ", ".join(self.missing))
                             )
        return cls_attr

    @property
    def _parameter_values(self):
        """simulate parameter values for partially configuared object
        """
        try:
            return self.__parameter_values
        except AttributeError:
            self.__parameter_values = {**self.keywords}

            position = 0

            for name, option in self.func.__parameters__:
                if not option.positional:
                    break  # no positional left
                if name in self.keywords:
                    continue  # already fulfilled

                self.__parameter_values[name] = self.args[position] \
                    if len(self.args) >= position + 1\
                    else None

                position += 1

            return self.__parameter_values
