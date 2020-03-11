import abc

from study_state_machine.context import Context
from study_state_machine.errors import BehaviorNotAllowedException


class IState(abc.ABC):
    """Base class for all states.

     The state has a reference to the context in order to change into the next state.
    """
    def __init__(self, context=None):
        self.context = context

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

    def __str__(self):
        return self.__class__.__name__

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.context == other.context
        return False

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context


class IStudyState(IState):
    """Base class for all study states"""

    def create_study(self, *args, **kwargs):
        raise BehaviorNotAllowedException(f"Not allowed to create study in state {self.__class__.__name__}")

    def add_sample(self, *args, **kwargs):
        raise BehaviorNotAllowedException(f"Not allowed to add sample in state {self.__class__.__name__}")

    def change_state(self, *args, **kwargs):
        raise BehaviorNotAllowedException(f"Not allowed to change to another state in state {self.__class__.__name__}")

