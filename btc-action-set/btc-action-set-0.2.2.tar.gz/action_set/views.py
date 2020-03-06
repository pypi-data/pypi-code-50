from typing import Type, List

from action_set.action_set import ActionSetType, ActionSetGroupType, BreadcrumbsSetType


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
                self.action_set_context_name: self.get_action_set_object()
            })
        return context

    def get_action_set_object(self) -> ActionSetType:
        return self.action_set_class(**self.get_action_set_kwargs())


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
                self.action_set_group_context_name: self.get_action_sets_group_object()
            })
        return context

    def get_action_sets_group_object(self) -> ActionSetGroupType:
        return self.action_set_group_class(**self.get_action_set_group_kwargs())


class BreadcrumbsMixinView:
    """
    Mixin for adding breadcrumbs to views.
    """

    breadcrumbs_set_class: Type[BreadcrumbsSetType] = None
    breadcrumbs_set_context_name: str = 'breadcrumbs'
    breadcrumbs_set: List[str] = []

    def get_breadcrumbs_set_kwargs(self, **kwargs) -> dict:
        return dict(request=self.request, crumbs_set=self.breadcrumbs_set, view_kwargs=self.kwargs, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.breadcrumbs_set_class:
            context.update({
                self.breadcrumbs_set_context_name: self.get_breadcrumbs_set_object()
            })
        return context

    def get_breadcrumbs_set_object(self) -> ActionSetType:
        return self.breadcrumbs_set_class(**self.get_breadcrumbs_set_kwargs())
