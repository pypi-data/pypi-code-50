from abc import ABC, abstractmethod


def resolvers():
    """Return all supported resolvers, ordered by precedence"""
    from . import gradle, cbng_web
    return [cbng_web.CbngWebResolver, gradle.GradleResolver]


class Resolver(ABC):
    """
    An abstract base class for a dependency resolver.

    Known implementations include
    :class:`cmmnbuild_dep_manager.resolver.cbng_web.CbngWebResolver`
    and
    :class:`cmmnbuild_dep_manager.resolver.gradle.GradleResolver`

    """
    #: The name of the variable that must be available on a module which wishes
    #: to be able to have its dependencies resolved by this resolver (str).
    dependency_variable = '__the_name_of_the_module_attribute_for_deps__'

    #: A short description of the resolver, for logging/info purposes
    #: only (str).
    description = 'The description of the resolver.'

    @classmethod
    @abstractmethod
    def is_available(cls):
        pass

    @abstractmethod
    def __init__(self, dependencies):
        pass

    @abstractmethod
    def save_jars(self, dir):
        pass

    @classmethod
    @abstractmethod
    def get_help(cls, classnames, class_info):
        pass
