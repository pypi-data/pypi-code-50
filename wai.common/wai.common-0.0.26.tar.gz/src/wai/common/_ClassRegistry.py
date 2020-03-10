from typing import Dict, Set, Type, Optional

from .meta import fully_qualified_name


class ClassRegistry:
    """
    A registry of classes that can be looked up by name.

    # TODO: Alias conflicts with name/qualname
    """
    def __init__(self):
        self._name_lookup: Dict[str, Set[str]] = {}
        self._qualname_lookup: Dict[str, Type] = {}
        self._aliases: Dict[str, Type] = {}

    def register(self, cls: Type):
        """
        Registers a class with the registry.

        :param cls:     The class to register.
        """
        # Get the short and qualified names of the class
        name: str = cls.__name__
        qualname: str = fully_qualified_name(cls)

        # Abort if already registered
        if qualname in self._qualname_lookup:
            return

        # Initialise the short-name list of necessary
        if name not in self._name_lookup:
            self._name_lookup[name] = set()

        # Add the qualified name to the lookup
        self._name_lookup[name].add(qualname)

        # Add the type to the qualified lookup
        self._qualname_lookup[qualname] = cls

    def alias(self, cls: Type, alias: str):
        """
        Creates an alias for a class. Automatically registers
        the class if it's not already.

        :param cls:         The class to alias.
        :param alias:       The alias to use.
        :raises NameError:  If the alias is already in use, or is empty.
        """
        # Make sure the alias isn't the empty string
        if alias == "":
            raise NameError("Aliases can't be empty")

        # Make sure the alias isn't already in use
        if alias in self._aliases:
            raise NameError(f"Alias '{alias}' already in use")

        # If it's not already registered, do so now
        self.register(cls)

        # Save the alias
        self._aliases[alias] = cls

    def find(self, name: str, *,
             attempt_class_import: bool = False) -> Optional[Type]:
        """
        Tries to find the registered class with the given name.

        :param name:                    The name to find (short or qualified).
        :param attempt_class_import:    Whether to attempt to import the class
                                        if it's not registered.
        :return:                        The class with the given name, or None
                                        if not found.
        :raises NameError:              If the name is an ambiguous short-name.
        """
        # If the name is qualified, return the class
        if name in self._qualname_lookup:
            return self._qualname_lookup[name]

        # If the name is an alias, return the aliased class
        if name in self._aliases:
            return self._aliases[name]

        # If the name is a short name, try to resolve it
        if name in self._name_lookup:
            # Get the potential qualified names
            qualnames = self._name_lookup[name]

            # If there's more than one, it's ambiguous
            if len(qualnames) > 1:
                raise NameError(f"Class name '{name}' is ambiguous: {', '.join(qualnames)}")

            for qualname in qualnames:  # Dummy loop to get first (only) item from set
                return self.find(qualname)

        # Attempt to import the class if selected
        if attempt_class_import:
            return self.attempt_class_import(name)

        # Class not found
        return None

    def attempt_class_import(self, name: str) -> Optional[Type]:
        """
        Attempts to import the class by name.

        :param name:    The fully-qualified name of the class.
        :return:        The class, or None if it could not
                        be imported.
        """
        # TODO: Implementation
        raise NotImplementedError(ClassRegistry.attempt_class_import.__qualname__)
