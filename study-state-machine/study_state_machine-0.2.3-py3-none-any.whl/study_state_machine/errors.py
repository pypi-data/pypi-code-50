"""Collection of state machine related exceptions.

All exceptions inherit from :class:`~study_state_machine.errors.StateMachineException`
"""


class StateMachineException(Exception):
    """Generic state machine error"""
    pass


class BehaviorNotAllowedException(StateMachineException):
    """Exception if a state does not support a behavior"""
    pass


class StateNotFoundException(StateMachineException):
    """Exception if state is not found by its name"""
    pass

