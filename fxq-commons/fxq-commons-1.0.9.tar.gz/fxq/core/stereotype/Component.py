from stringcase import snakecase as beancase

from fxq.core.context.ApplicationContext import application_context


def Component(__component_class=None, name=None):
    '''
    Class Decorator to indicate that a bean of this class should be instantiated.
    Beans are created using the Class name by default and would be singletons.
    :param name: Optional Argument to define the explicit name of the bean
    :return: Returns the class after a bean has been instantiated and stored
    '''
    if __component_class:
        bean_id = beancase(__component_class.__name__)
        application_context.register_bean(bean_id, __component_class())
        return __component_class
    else:
        def wrapper(__component_class):
            application_context.register_bean(name if name else __component_class.__name__, __component_class())
            return __component_class

        return wrapper
