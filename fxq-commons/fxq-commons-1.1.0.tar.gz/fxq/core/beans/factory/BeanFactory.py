import logging


class BeanFactory:
    LOGGER = logging.getLogger("BeanFactory")

    def __init__(self):
        self._beans = {}
        BeanFactory.LOGGER.info("Bean Factory Initialized")

    def register_bean(self, name, bean):
        BeanFactory.LOGGER.debug("Registering Bean for type %s with name %s" % (bean.__class__.__name__, name))
        self._beans[name] = bean

    def get_bean(self, name: str = None, required_type: type = None):
        if name and required_type is None:
            assert isinstance(name, str), "Expected bean name to be of type str, got \"%s\"" % name.__class__
            bean = self._get_bean_by_name(name)
            BeanFactory.LOGGER.debug(
                "Found instance of type %s for requested bean %s" % (bean.__class__.__name__, name))
            return bean
        elif required_type and name is None:
            return self._get_bean_by_type(required_type)
        elif name and required_type:
            return self._get_bean_by_name_and_validate_type(name, required_type)
        else:
            raise BeanFactoryException("get_bean requires at least name or required type")

    def _get_bean_by_name(self, name):
        try:
            return self._beans[name]
        except KeyError as e:
            BeanFactory.LOGGER.error("Failed to find Bean %s" % name, e)
            raise BeanFactoryException("BeanFactory contains no bean of name:%s" % name)

    def _get_bean_by_type(self, type):
        candidate_beans = []
        for bean_name, bean_instance in self._beans.items():
            if isinstance(bean_instance, type):
                BeanFactory.LOGGER.debug("Matched %s to be of class type %s" % (bean_name, type.__name__))
                candidate_beans.append(bean_instance)

        if len(candidate_beans) == 1:
            return candidate_beans[0]
        elif len(candidate_beans) > 1:
            raise BeanFactoryException("More than one bean for type %s was found" % type.__name__)
        elif len(candidate_beans) < 1:
            raise BeanFactoryException("No bean for type %s was found" % type.__name__)

    def _get_bean_by_name_and_validate_type(self, name, type):
        try:
            instance = self._beans[name]
            if isinstance(instance, type):
                BeanFactory.LOGGER.debug("Validated Bean %s to be of type %s" % (name, type.__name__))
                return self._beans[name]
            else:
                raise BeanFactoryException(
                    "Bean %s is of type %s expected %s" % (name, instance.__class__.__name__, type.__name__))
        except KeyError as e:
            BeanFactory.LOGGER.error("Failed to find Bean %s" % name)
            raise BeanFactoryException("Injection for Bean %s failed" % name)


class BeanFactoryException(Exception):
    pass
