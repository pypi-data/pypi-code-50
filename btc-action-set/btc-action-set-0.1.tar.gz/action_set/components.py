from typing import TypeVar

from dev_tools.meta.metaclasses import MethodCheckMetaclass
from dev_tools.template.components import BaseHTMLElement, BaseButton


class AbstractActionMetaclass(MethodCheckMetaclass):
    """
    Metaclass for verifying the existence of the render method in the class.
    """

    base_class_name = 'BaseAction'
    method_name = 'render'


class BaseAction(metaclass=AbstractActionMetaclass):
    """
    Base class for defining objects as actions. Any object may be an action if it has a render method.
    """

    def __str__(self):
        return self.render()


ActionType = TypeVar('ActionType', bound=BaseAction)


class SimpleActionElement(BaseHTMLElement, BaseAction):
    """
    Base class for simple actions presented as HTML-element.
    """

    pass


class ActionButton(BaseButton, BaseAction):
    """
    Base class for action button.
    """

    pass
