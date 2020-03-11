"""Implementation of a finite state machine for studies"""
import logging

from study_state_machine.errors import StateNotFoundException

logger = logging.getLogger(__name__)


class Context:
    """
    Only if an initial state is passed to the constructor, the context of the current state is set. Otherwise, call
    :func:`~study_state_machine.context.Context.transition_to` or
    :func:`~study_state_machine.context.Context.load_state` with a State or a name of a State, respectively,
    before delegating behavior.
    """

    def __init__(self, initial_state=None):
        self._current_state = initial_state

        if self.current_state:
            self._current_state.context = self

        # Prevent circular import
        from study_state_machine.study_states import available_states
        self._available_states = available_states

    def __repr__(self):
        return f"<{self.__class__.__name__}" \
               f"(current state: {self._current_state})>"

    def transition_to(self, state):
        """ Set state as the new current state and set its context

        :param state: new current state
        """
        self._current_state = state
        self._current_state.context = self

    def load_state(self, name, *args, **kwargs):
        """Load state with given name

        :param name: Name of the state
        :param args: Passed to state initialization
        :param kwargs: Passed to state initialization
        :raise StateNotFoundException: If the state is not found
        """
        if name not in self._available_states.keys():
            error_msg = f"Fail to find state (name: {name})"
            logger.error(error_msg)
            raise StateNotFoundException(error_msg)

        self.transition_to(self._available_states[name](*args, **kwargs))

    @property
    def current_state(self):
        return self._current_state

    @current_state.setter
    def current_state(self, state):
        self.transition_to(state)

    @property
    def available_states(self):
        return self._available_states.keys(), self._available_states.values()


    """
    Context delegates behavior to current state
    """

    def create_study(self, *args, **kwargs):
        self.current_state.create_study(*args, **kwargs)

    def add_sample(self, *args, **kwargs):
        self.current_state.add_sample(*args, **kwargs)

    def change_state(self, *args, **kwargs):
        self.current_state.change_state(*args, **kwargs)
