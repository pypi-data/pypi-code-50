"""meta-class for table class
parse fields 
and generate realted information
"""

from typing import Any, List, Tuple
import bisect

from .parameter import Parameter
from .utils import get_name

class TableMeta(type):
    """[summary]
    :py:class:`fusionflow.uploads.Field`
    :param type: [description]
    :type type: [type]
    :return: [description]
    :rtype: [type]
    """
    def __new__(mcs, name, base, attrs, **kwargs) -> Any:
        cls = super().__new__(mcs, name, base, attrs)
        
        # class private attribute, not override by subclass
        cls.__parameters : List[Tuple[bool, int, str, Parameter]]= []
        cls._table_name = name.lower()
        cls.__names = set()

        cls.__validators = {'row':[], 'field': {}}

        # travel through all base class
        for c in cls.__mro__:
            for name, param in filter(lambda pair: isinstance(pair[1], Parameter), vars(c).items()):
                # overrided by subclass and is not :class:`Paramete`_
                if name in attrs and not isinstance(attrs[name], Parameter):
                    continue

                if not param.name:
                    param.name = name
                
                if not name in cls.__names:
                    cls.__names.add(name)
                    # positional parameter first
                    bisect.insort(cls.__parameters, (not param.positional, param._create_counter, name, param))
                    
        # validators
        for name in attrs:
            # filed validator
            if name.startswith("validate_"):
                cls.__validators['field'].setdefault(name[len('validate_'):], []).append(name)
            # row validator
            elif name.startswith("validate"):
                cls.__validators['row'].append(name)


        # docstring
        param_docs = []
        for  is_positional, counter, name, param in cls.__parameters:
            if param.type_:
                name = get_name(param.type_) + " " + name

            prefix = ":param {}: ".format(name)
            for lineno, line in enumerate((param.__doc__ or "").split("\n")):
                param_docs.append((" " * len(prefix) if lineno else prefix) + line)

        cls.__doc__ = "\n".join(map(str.strip, 
            filter(None, (cls.__doc__, "\n".join(param_docs)))))

        return cls

    @property
    def __parameters__(cls):
        return [(name, parameter) for _, _, name, parameter in cls.__parameters]

    
    @property
    def __validators__(cls):
        return cls.__validators

