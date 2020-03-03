import datetime
import uuid
import threading
import logging
import time
from typing import Union, List, Dict
from .action import TrackedAction, SchedulerAction


logger = logging.getLogger(__name__)


class TimePoint(object):
    UUID_PREFIX = 'tp-'

    # timepoint instance tracking
    _instances: List["TimePoint"] = []

    def __init__(self,
                 time_delta: float,
                 name: str = None,
                 description: str = None,
                 parent_sequence_id: str = None,
                 ):
        """
        A class for describing and tracking an event time point

        :param time_delta: time delta for the time point (relative to some other time)
        :param name: convenience name for time point differentiation
        :param description: extended description for differentiation
        :param parent_sequence_id: uuid of parent SamplingScheduler (if applicable)
        """
        # time delta from trigger time
        self.time_delta: float = float(time_delta)
        # storage for start time
        self.sequence_time_started: float = None
        # name for convenience
        self.name: str = name
        # description
        self.description: str = description
        # parent uuid
        self.parent_sequence_id: str = parent_sequence_id

        self._uuid = str(uuid.uuid4())  # assign unique identifier
        TimePoint._instances.append(self)
        # todo add description attribute
        # todo create association between time point and parent scheduler
        # todo finish refactor
        #   - move as_dict, update as necessary

    def __str__(self):
        return (
            f'{self.__class__.__name__} {self.time_delta} s '
        )

    def __repr__(self):
        return self.__str__()

    @property
    def uuid(self) -> str:
        """uuid for the time point"""
        return self.UUID_PREFIX + self._uuid

    @property
    def basic_dict(self) -> dict:
        """basic dictionary for any TimePoint class or subclass"""
        return {
            'time_delta': self.time_delta,
            'uuid': self.uuid,
            'name': self.name,
            'class': self.__class__.__name__,
        }

    @classmethod
    def get_instance(cls, key: str) -> "TimePoint":
        """
        Retreives a timepoint instance by key. The key may be a uuid, or class-uuid

        :param key: key to search by
        :return: TimePoint (or subclass) instance
        """
        for instance in cls._instances:
            if any([
                # instance.name == key,  # todo consider reimplementing
                instance._uuid == key,
                instance.uuid == key,
            ]):
                return instance
        raise KeyError(f'the key "{key}" does not match an identifier for any {cls.__class__.__name__} instances')

    def as_dict(self) -> dict:
        """Returns a key: value representation of the instance"""
        return self.basic_dict

    def sample_time_from_reference(self, reference_time: float):
        """
        Returns the sample time for the time point from the reference time (in seconds)

        :param reference_time: reference time to calculate from
        :return: time to trigger (seconds)
        """
        return self.time_delta + reference_time

    def __lt__(self, other: Union[float, "TimePoint"]):
        if isinstance(other, TimePoint):
            other = other.time_delta
        return self.time_delta < other

    def __eq__(self, other: Union[float, "TimePoint"]):
        if isinstance(other, TimePoint):
            other = other.time_delta
        return self.time_delta == other

    def __gt__(self, other: Union[float, "TimePoint"]):
        if isinstance(other, TimePoint):
            other = other.time_delta
        return self.time_delta > other

    def __le__(self, other: Union[float, "TimePoint"]):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: Union[float, "TimePoint"]):
        return self.__gt__(other) or self.__eq__(other)


class ActionTimePoint(TimePoint):
    UUID_PREFIX = 'atp-'

    def __init__(self,
                 time_delta: float,
                 name: str = None,
                 actions: List[Union[callable, TrackedAction]] = [],
                 ):
        """
        A class for describing and tracking an event time point where actions (e.g. sampling) are to be triggered

        :param time_delta: time delta for the time point (relative to some other time)
        :param name: convenience name for time point differentiation
        :param actions: action methods to call. These methods will be called in the order provided
        """
        # todo create abstract class with context
        #   - individual methods for pre-step, main, and post-step (e.g. turn on pump, run experiment, process data)
        # todo associate timepoint with parent scheduler instance (by UUID)
        # todo create passthrough for sequence_time_started on init
        TimePoint.__init__(
            self,
            time_delta=time_delta,
            name=name,
        )
        # store actions for timepoint
        self._actions: List[TrackedAction] = [
            TrackedAction(action) for action in actions
        ]
        # internal storage attributes
        self._triggered = False
        self._thread: threading.Thread = None
        self._lock: threading.Lock = threading.Lock()
        # todo create attribute for retrieving action returns

    def __str__(self):
        # todo add attribute for retrieving formatted time (HH:MM:SS)
        out = f'{self.__class__.__name__} {self.string_time_delta}'
        if self.complete is True:
            out += ' COMPLETE'
        elif self.triggered is True:
            out += ' TRIGGERED'
        return out

    def __call__(self, **kwargs):
        self.trigger(**kwargs)

    @property
    def actions(self) -> List[TrackedAction]:
        """actions to be run when the timepoint is called"""
        return self._actions

    def add_action(self,
                   action: Union[str, callable, SchedulerAction],
                   location: int = None,
                   ):
        """
        Adds an action to the timepoint. Actions will be executed in the order they appear in the list of actions for
        the ActionTimePoint instance.

        :param action: action to perform. Actions may be added by providing a callable method or name of a predefined
            callable method
        :param location: index location to insert. If left as None the action will be appended
        """
        if location is None:
            location = len(self._actions)
        self._actions.insert(
            location,
            TrackedAction(action),
        )

    def remove_action(self,
                      action: Union[str, callable, SchedulerAction],
                      ):
        """
        Removes an action from the list of actions associated with a timepoint.

        :param action: action identifier
        :return:
        """
        raise NotImplementedError()
        # todo implement
        #   - determine identifier
        #   - remove from _actions list
        # todo implement ability to change action associated with time points
        #   - e.g. switch from no pump ON/OFF to method with pump on/off

    def _execute_actions(self, **kwargs):
        """
        Executes the actions defined in the instance.

        :param kwargs: keyword arguments for those action methods
        """
        execution_logger = logger.getChild(f'{self.__class__.__name__} {self.string_time_delta}')
        with self._lock:
            execution_logger.debug('initiating action sequence')
            # for each action, retrieve keyword arguments if specified then execute
            for action in self.actions:
                action_kwargs = {}
                if action.name in kwargs:
                    action_kwargs.update(kwargs[action.name])
                execution_logger.debug(f'executing {action.name}')
                action(**action_kwargs)
                execution_logger.debug(f'{action.name} complete')
            execution_logger.debug('action sequence complete')

    def trigger(self,
                wait: bool = None,
                **kwargs,
                ):
        """
        Triggers the actions of the ActionTimePoint. Keyword arguments will be passed through to their respective methods.

        e.g. if there is a method named "do_this_thing" which expects the keyword argument "value", the expected syntax
        of kwargs would be

            {
                "do_this_thing": {"value": 42},
            }

        :param kwargs: keyword arguments for the actions. Keyword arguments will be passed through to their respective
            methods.
        """
        if self.triggered is True:
            raise SystemError(f'Multiple executions of the same {self.__class__.__name__} are not supported')
        # todo catch multiple calls and raise
        self._triggered = True  # set flag as triggered
        # set up thread
        self._thread = threading.Thread(
            target=self._execute_actions,
            name=f'{str(self)} action thread',
            daemon=True,
            kwargs=kwargs,
        )
        self._thread.start()  # start thread
        if wait is True:  # wait if specified
            self.wait_for_completion()

    @property
    def string_time_delta(self) -> str:
        """formatted string version of time delta"""
        return str(
            datetime.timedelta(seconds=self.time_delta)
        )

    @property
    def triggered(self) -> bool:
        """whether the time point has been triggered"""
        return self._triggered

    @property
    def in_progress(self) -> bool:
        """
        whether the actions are in progress
        (time point is triggered and actions are in the process of being executed)
        """
        if self.triggered is True:
            return self._lock.locked()
        return False

    @property
    def complete(self) -> bool:
        """whether the actions have completed"""
        if self.triggered is True:  # if instance has been triggered, check lock state
            return not self._lock.locked()
        return False

    @property
    def action_start_times(self) -> dict:
        """times when the prescribed actions were started"""
        if self.triggered is True:
            return {
                action.name: action.time_started for action in self.actions
            }

    @property
    def action_completion_times(self) -> dict:
        """times when the prescribed actions were completed"""
        if self.triggered is True:
            return {
                action.name: action.time_completed for action in self.actions
            }

    @property
    def action_durations(self) -> dict:
        """execution durations for the prescribed actions"""
        if self.triggered is True:
            return {
                action.name: action.action_duration for action in self.actions
            }

    @property
    def started_timestamps(self) -> Dict[str, datetime.datetime]:
        """timestamps for when actions were started"""
        if self.triggered is True:
            return {
                action.name: action.started_timestamp for action in self.actions
            }

    @property
    def relative_start_times(self) -> dict:
        """relative start times for actions"""
        if self.triggered is False:
            raise ValueError(f'the {self.__class__.__name__} has not been triggered yet')
        if self.sequence_time_started is None:
            raise ValueError(f'sequence_start_time is not set for the {self.__class__.__name__} instance')
        return {
            action.name: action.time_started - self.sequence_time_started for action in self.actions
        }

    @property
    def action_returns(self) -> dict:
        """retrieves the returned values from the actions. Only actions which have completed will have return values"""
        return {
            action.name: action.method_return for action in self.actions
        }

    @property
    def actions_status(self) -> dict:
        """status of the actions of the instance"""
        return {action.name: action.status for action in self.actions}

    def wait_for_completion(self, cycle_time: float = 0.1):
        """
        Waits for the completion of the time point

        :param cycle_time: cycle check time
        """
        while self.in_progress is True:
            time.sleep(cycle_time)

    def as_dict(self) -> dict:
        """Returns a key: value representation of the instance"""
        out = self.basic_dict
        out['triggered'] = self.triggered
        out['actions'] = [
            action.as_dict() for action in self.actions
        ]
        # todo decide how to include relative start times
        return out

