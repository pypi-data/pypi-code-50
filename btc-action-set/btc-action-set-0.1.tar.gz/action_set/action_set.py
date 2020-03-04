from copy import deepcopy
from typing import Any, TypeVar, List, Optional

from dev_tools.meta.metaclasses import DeclarativeAttributesBaseMetaclass
from dev_tools.template.mixins import TemplateObjectMixin, HttpRequestType

from action_set.components import BaseAction, ActionType
from action_set.types import ActionSetDict


class ActionsDeclarativeMetaclass(DeclarativeAttributesBaseMetaclass):
    """
    Metaclass for collecting actions for action_set.
    """

    _attribute_base_class = BaseAction

    @classmethod
    def _contribute_to_class(mcs, class_obj: Any, declared_attributes: dict) -> None:
        class_obj.declared_actions = declared_attributes
        class_obj.base_actions = declared_attributes


class BaseActionSet(TemplateObjectMixin, metaclass=ActionsDeclarativeMetaclass):
    """
    Base raw class for creating custom Action Sets.
    """

    context_object_name = 'action_set'

    def __init__(self):
        self.actions = deepcopy(self.base_actions)

    def __getitem__(self, name):
        return self.actions[name]

    def __iter__(self):
        for _, action in self.actions.items():
            yield action


class ActionSet(BaseActionSet):
    """
    Main class for grouping actions with custom template support.
    """

    def __init__(self, request: HttpRequestType, action_set_group: Optional['ActionSetGroupType'] = None):
        super().__init__()
        self.request = request
        self.action_set_group = action_set_group

    def _get_request(self) -> Optional[HttpRequestType]:
        return self.request


class GroupedActionSet:
    """
    Mixin for adding Action Set grouper variable.
    """

    def __init__(self, action_set_group: 'ActionSetGroupType'):
        self.action_set_group = action_set_group
        request = action_set_group.request
        super().__init__(request)


ActionSetType = TypeVar('ActionSetType', bound=ActionSet)


class ActionSetDeclarativeMetaclass(DeclarativeAttributesBaseMetaclass):
    """
    Metaclass for collecting action_sets for action group.
    """

    _attribute_base_class = BaseActionSet.__class__

    @classmethod
    def _contribute_to_class(mcs, class_obj: Any, declared_attributes: dict) -> None:
        class_obj.declared_action_sets = declared_attributes
        class_obj.base_action_sets = declared_attributes


class BaseActionSetGroup(metaclass=ActionSetDeclarativeMetaclass):
    """
    Base raw class for creating custom Action Sets Groups.
    """

    def __init__(self):
        self.action_sets = ActionSetDict(deepcopy(self.base_action_sets))

    def __getitem__(self, name):
        return self.action_sets[name]

    def __iter__(self):
        for _, action_set in self.action_sets.items():
            yield action_set


class ActionSetGroup(BaseActionSetGroup):
    """
    Main class for grouping actions and use in views.
    """

    def __init__(self, request: HttpRequestType):
        self.request = request
        super().__init__()
        self.instantiate_action_sets()

    def instantiate_action_sets(self) -> None:
        for name, action_set in self.action_sets.items():
            self.action_sets.instantiate(name, request=self.request, action_set_group=self)


ActionSetGroupType = TypeVar('ActionSetGroupType', bound=ActionSetGroup)


class ActionSetWithPermissionCheck(ActionSet):
    """
    An example class of the action_set with permission protect.
    Uses HTML-element cleanup to prevent it's signature change in browser console.
    """

    elements_permissions: dict = {}  # {'object_name': [perm_1, perm_2,...]}
    protect_css_class: str = ''
    ignore_html_params: List[str] = ['type']

    def protect_element(self, element: ActionType) -> None:
        self.clean_css_classes(element)
        self.clean_html_params(element)

    def clean_html_params(self, element: ActionType) -> None:
        # clean html attributes.
        element.html_params = {
            name: value for name, value in element.html_params.items() if name in self.ignore_html_params
        }

    def clean_css_classes(self, element: ActionType) -> None:
        # clean js-* classes.
        element.css_classes = \
            [css_class for css_class in element.css_classes if not css_class.startswith('js')] + \
            [self.protect_css_class]

    def get_user_permissions(self) -> list:
        return []

    def get_element_permissions(self, element_name: str) -> list:
        return self.elements_permissions.get(element_name, [])

    def check_permissions(self) -> None:
        user_permissions = self.get_user_permissions()
        if user_permissions:
            for element_name, element in self.actions.items():
                element_permissions = self.get_element_permissions(element_name)
                if not all(permission in user_permissions for permission in element_permissions):
                    self.protect_element(element)

    def render(self) -> str:
        # verification of permissions before rendering.
        self.check_permissions()
        return super().render()
