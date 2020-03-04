from typing import Type

from action_set.action_set import ActionSetType, ActionSetGroupType


class ActionSetMixinView:
    """
    A view mixin for adding action_set to views.
    """

    action_set_class: Type[ActionSetType] = None
    action_set_context_name: str = 'action_set'

    def get_action_set_kwargs(self, **kwargs) -> dict:
        return dict(request=self.request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.action_set_class:
            context.update({
                self.action_set_context_name: self.action_set_class(**self.get_action_set_kwargs())
            })
        return context


class ActionSetGroupMixinView:
    """
    A view mixin for adding action_set_group to views.
    """

    action_set_group_class: Type[ActionSetGroupType] = None
    action_set_group_context_name: str = 'action_set_group'

    def get_action_set_group_kwargs(self, **kwargs) -> dict:
        return dict(request=self.request, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.action_set_group_class:
            context.update({
                self.action_set_group_context_name: self.action_set_group_class(**self.get_action_set_group_kwargs())
            })
        return context
