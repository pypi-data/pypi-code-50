import logging

from fxq.core.beans.factory import BeanFactory


class ApplicationContext(BeanFactory):
    LOGGER = logging.getLogger("ApplicationContext")

    def __init__(self):
        super(ApplicationContext, self).__init__()
        ApplicationContext.LOGGER.info("Application Context Initialized")


application_context = ApplicationContext()
