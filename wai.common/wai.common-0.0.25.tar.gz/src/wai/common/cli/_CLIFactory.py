from typing import Type, Union
from argparse import Namespace

from ..meta import instanceoptionalmethod, get_import_code
from ..meta.constants import TRIPLE_QUOTES
from ..meta.typing import VAR_ARGS_TYPE
from ._CLIInstantiable import CLIInstantiable
from ._OptionHandler import OptionHandler
from ._typing import OptionsList


class CLIFactory(OptionHandler):
    """
    Base class for factory classes which instantiate objects
    from command-line arguments.
    """
    @instanceoptionalmethod
    def production_class(self, namespace: Namespace) -> Type:
        """
        Gets the type of object to produce.

        :param namespace:   The namespace from parsing the command-line options.
        :return:            The produced object type.
        """
        raise NotImplementedError(CLIFactory.production_class.__qualname__)

    @instanceoptionalmethod
    def init_args(self, namespace: Namespace) -> VAR_ARGS_TYPE:
        """
        Translates the namespace created by the configured parser
        into arguments to the __init__ method of the production class.

        :param namespace:   The namespace from parsing the command-line options.
        :return:            The arguments to the class.
        """
        raise NotImplementedError(CLIFactory.init_args.__qualname__)

    @instanceoptionalmethod
    def instantiate(self, namespace: Union[Namespace, OptionsList, None] = None) -> CLIInstantiable:
        """
        Produces an instance of the production class from the given namespace.

        :return:    The instance.
        """
        # If values passes unparsed, parse them
        namespace = self._ensure_namespace(namespace)

        # Get the production class
        cls = self.production_class(namespace)

        # Get the init args
        args, kwargs = self.init_args(namespace)

        return cls(*args, **kwargs)

    @staticmethod
    def for_class(cls: Type[CLIInstantiable]) -> Type['CLIFactory']:
        """
        Creates a class which is a factory for the given CLI-instantiable type.

        :param cls:     Any CLI-instantiable type.
        :return:        The factory class.
        """
        # Get the factory class code
        code = CLIFactory.code_for_class(cls)

        # Create a scope dictionary
        scope = {}

        # Execute the class definition code
        exec(code, scope)

        # Return the defined class from the local scope
        return scope[f"{cls.__name__}CLIFactory"]

    @staticmethod
    def code_for_class(cls: Type[CLIInstantiable], *, include_imports: bool = True) -> str:
        """
        Gets the code to execute to produce a factory for the given
        type of instantiable.

        :param cls:                 The class to produce factory code for.
        :param include_imports:     Whether to include import code.
        :return:                    The factory class definition code.
        """
        # Create the required formatted strings
        cls_name: str = cls.__name__

        # Function for formatting the import code
        def import_code(klass: Type, indent: int = 0) -> str:
            return f"{get_import_code(klass, indent)}\n" if include_imports else ""

        # Get the import code for the types used by CLIFactory
        types_import_code: str = ""
        if include_imports:
            types_import_code = (
                f"from argparse import Namespace\n"
                f"from typing import Type\n"
                f"\n"
                f"from wai.common.cli import CLIFactory, CLIInstantiable\n"
                f"from wai.common.meta.typing import VAR_ARGS_TYPE\n"
                f"\n"
            )

        # Get the import code for the option types used by the class
        # (and any types those options depend on)
        option_types = set()
        for option in cls._get_all_options():
            option_types.add(type(option))
            option_types = option_types.union(option.get_repr_imports())
        option_types_import_code: str = "".join(import_code(option_type) for option_type in option_types)
        if include_imports:
            option_types_import_code += "\n\n"

        # Get the import code for the class itself
        # (this will be a local import, hence the indentation)
        cls_import_code: str = import_code(cls, 8)

        # Format the options
        option_definitions = "\n    ".join(f"{option.name} = {repr(option)}" for option in cls._get_all_options())
        if option_definitions == "":
            option_definitions = "# None"

        return (
            f"{types_import_code}"
            f"{option_types_import_code}"
            f"class {cls_name}CLIFactory(CLIFactory):\n"
            f"    {TRIPLE_QUOTES}\n"
            f"    Factory which instantiates the {cls_name} class.\n"
            f"    {TRIPLE_QUOTES}\n"
            f"    # Options\n"
            f"    {option_definitions}\n"
            f"\n"
            f"    @classmethod\n"
            f"    def production_class(self, namespace: Namespace) -> Type[CLIInstantiable]:\n"
            f"{cls_import_code}"
            f"        return {cls_name}\n"
            f"\n"
            f"    @classmethod\n"
            f"    def init_args(self, namespace: Namespace) -> VAR_ARGS_TYPE:\n"
            f"        return (namespace,), dict()\n"
        )
