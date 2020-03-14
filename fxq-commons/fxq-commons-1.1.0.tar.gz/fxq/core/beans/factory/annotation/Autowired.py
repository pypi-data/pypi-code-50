import logging
from inspect import Parameter, signature

from fxq.core.beans.factory.BeanFactory import BeanFactoryException
from fxq.core.context.ApplicationContext import application_context

LOGGER = logging.getLogger("Autowired")


def Autowired(name: str = None, type: type = None, *args, **kwargs):
    '''
    Decorator which can either be called directly or added to a method to inject beans dynamically.
    Should be primarily used to decorate a contructor whereby the required parameters will be
    injected at instantiation time.
    :param name: Name of the Bean as defined in the name
    :param type: Class of the Bean to be retreived
    :return: Returns the requested instance from the Bean factory
    '''
    if isinstance(name, str):
        return _AutowiredField(name, type)
    elif name is None and type is not None:
        return _AutowiredField(name, type)
    elif hasattr(name, '__name__') and name.__name__ == '__init__':
        return _AutowiredConstructor(name)
    else:
        LOGGER.error("Unsupported use of the Autowired decorator, call from the constructor or directly")
        raise Exception("Unsupported use of Autowired decorator")


def _AutowiredField(name: str, type: type):
    return application_context.get_bean(name, type)


def _AutowiredConstructor(constructor):
    LOGGER.debug("Attempting to Autowire constructor fields")

    injectable_beans = {}

    for parameter in signature(constructor).parameters.values():
        p: Parameter = parameter
        try:
            if parameter.name != 'self':
                injectable_beans[p.name] = _AutowiredField(name=p.name, type=None)
        except BeanFactoryException as e:
            LOGGER.warning("Unable to inject bean of name %s" % p.name)

    def injecting_constructor(instance, *args, **kwargs):
        constructor(instance, *args, **injectable_beans, **kwargs)

    return injecting_constructor
