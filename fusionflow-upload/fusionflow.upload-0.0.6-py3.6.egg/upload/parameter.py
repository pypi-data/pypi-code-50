import textwrap
import warnings
from collections.abc import MutableSequence, MutableMapping, MutableSet

class Parameter:
    """parameter is just a data descriptor for subclass configurable parameters

    :param type_: 
        parameter type, use for format value, use this callable, otherwise return
        directly
    :param required: ``bool`` 
        must provide this parameter, otherwise default value must set 
    :param default:
        default value for no required parameter, call be callable, like :method:`datetime.now`_
    :param positional: default False
        pass in dunder init as positional arguemnt or keyword only
    :param help: doc string 
    """
    
    _create_counter = 0

    def __init__(self, type_=None, *, required=True, default=None, positional=False, help=None):

        if isinstance(default, (MutableMapping, MutableSequence, MutableSet)):
            warnings.warn("""{} is mutable contain, subclass which inheriate this paramater will shared this parameter 
            both manipulate it will lead unexpected result, use `lambda : {}()` instead""".format(default, type(default)))
        # assign later
        self.name = None
        
        self.type_ = type_
        self.required = required if default is None else False
        self.positional = positional
        self.default = default

        self.__doc__ = help or None
        if self.__doc__:
            self.__doc__ = textwrap.dedent(self.__doc__.strip("\n")).strip()
            if self.default:
                self.__doc__ += "\nDefault: %s" % default

        self._create_counter = Parameter._create_counter
        Parameter._create_counter += 1


    def __get__(self, instance, cls):
        if not instance:
            return cls.__dict__.get(self.name, self)

        # cache in instance _parameter_values attribute
        if not self.name in instance._parameter_values:
            instance._parameter_values[self.name] = self.get_default()
        
        return instance._parameter_values[self.name]

    
    def __set__(self, instance, value):
        instance._parameter_values[self.name] = self.format_value(value)

    def format_value(self, value):
        """format value depend on type_
        """
        return self.type_(value) if self.type_ else value


    def get_default(self):
        return self.default() if callable(self.default) else self.default

    
    def __repr__(self):
        return """{parametertype} {type}{name}({default}) {required}
        """.format(parametertype=type(self).__name__, type=self.type_, name=self.name,
                    required="requried" if self.required else "",
                    default=self.default
        )