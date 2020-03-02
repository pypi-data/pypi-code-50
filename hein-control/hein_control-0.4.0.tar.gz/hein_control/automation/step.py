from typing import List
import logging
from hein_control.scheduler.action import TrackedAction


logger = logging.getLogger(__name__)


class Step(TrackedAction):
    def __init__(self,
                 action: callable,
                 next_step: 'Step' = None,
                 bypass_return=None,
                 **kwargs,
                 ):
        """
        A step in an automation sequence. An instance of a Step should not be created, instead one of the subclasses
        should be instantiated.

        A Step can be bypassed (skipped over).

        A `Step` will have a `next_step`, which is another `Step` or `None`; in this way,
        steps in an `Automation` can be linked, and different work flows can be created.

        A `Step` is also callable. The details of this will depend on the specific subclass.

        :param callable, action: a callable, most of the time it will be a function, that will be executed when the
            Step is called/run
        :param Step, next_step: the Step that should follow after this Step has been run
        :param bypass_return: for a CustomStep, there might be some return value. If a Step is bypassed but you need
            a value to be returned still, you can hardcode a value to be returned. For example, if the step is to
            take a measurement with an  instrument and update a value, you can set what the measurement value that
            gets returned should be here
        :param dict, kwargs: dictionary must contain entries with keys that are identical to all the parameters for
            the callable action
        """

        super().__init__(
            action=action,
            **kwargs,
        )

        self.logger = logger.getChild(f'{self.__class__.__name__} {self.name}')

        self._next_step: Step = next_step  # the step that follows from this step
        self._bypass_step: bool = False  # Bool, if set to True, don't run what the step should do aka bypass it
        self._bypass_return = bypass_return

    def __call__(self, **kwargs):
        """

        :param dict, kwargs: dictionary must contain entries with keys that are identical to all the parameters for
            the callable action, and the values are the actual values/items for the corresponding keys
        :return:
        """
        if self._bypass_step is True:
            self.logger.debug(f'bypass step')
            self._action_return = self._bypass_return
        else:
            super().__call__(**kwargs)

    @property
    def next_step(self) -> 'Step':
        """The step that follows this step"""
        return self._next_step

    @next_step.setter
    def next_step(self,
                  value: 'Step'
                  ):
        if isinstance(value, Step) is False:
            raise TypeError('value must be of type Step')

        self._next_step = value

    @next_step.deleter
    def next_step(self,
                  ):
        self._next_step = None

    @property
    def bypass_step(self) -> bool:
        """whether the step should be bypassed"""
        return self._bypass_step

    @bypass_step.setter
    def bypass_step(self,
                    value: bool
                    ):
        if type(value)is not bool:
            raise TypeError('value must be of type bool')
        self._bypass_step = value
        self.logger.debug(f'set bypass step to True')

    @bypass_step.deleter
    def bypass_step(self):
        self._bypass_step = False

    @property
    def bypass_return(self):
        """
        If a Step will be bypassed but normally the action that should be executed needs to return some
        value, then some default/hardcoded value can be set to be returned. The type of value will depending on
        the specific subclass of Step that is being bypassed
        """
        return self._bypass_return

    @bypass_return.setter
    def bypass_return(self,
                      value):
        self._bypass_return = value

    @bypass_return.deleter
    def bypass_return(self):
        self._bypass_return = None


class CustomStep(Step):
    def __init__(self,
                 action: callable,
                 next_step: Step = None,
                 **kwargs,
                 ):
        """
         A `Step` that could have a return value after the callable has been executed; the return type must be a
        dictionary where keys are argument names (identical to the arguments of the parameters of the callable and
        therefore also identical to the keys in the dictionary used when an `Automation` is instantiated),
        and the values are the new value they should take. See the `Automation` class as to why this is important.

        :param callable, action: a callable, most of the time it will be a function, that will be executed when the
            Step is called/run. It may return a dictionary.
        :param Step, next_step: the Step that should follow after this Step has been run
        :param bypass_return: there might be some return value. If a CustomStep is bypassed but you need
            a value to be returned still, you can hardcode a value to be returned. For example, if the step is to
            take a measurement with an  instrument and update a value, you can set what the measurement value that
            gets returned should be here
        :param dict, kwargs: dictionary must contain entries with keys that are identical to all the parameters for
            the callable action
        """
        super().__init__(
            action=action,
            next_step=next_step,
            **kwargs,
        )

    def __call__(self, **kwargs) -> dict:
        """

        :param dict, kwargs: dictionary must contain entries with keys that are identical to all the parameters for
            the callable action, and the values are the actual values/items for the corresponding keys
        :return: dict, a dictionary of where entries are keys that are identical to all the parameters for
            the callable action, and the values are the updated value of the corresponding keys
        """
        super().__call__(**kwargs)
        return self._action_return


class ConditionCheck(Step):
    def __init__(self,
                 condition: callable,
                 next_step: Step,
                 **kwargs,
                 ):
        """
        A `Step` that, when executed, returns a `bool`. It is used by the `IfStep` to know what the `next_step` in an
        `Automation` instance should be.

        :param callable, condition: a callable, most of the time it will be a function, that will be executed when the
            Check is called/run. it must return a bool
        :param Step, next_step: the Step that should follow after this Step has been run
        :param kwargs: dictionary must contain entries with keys that are identical to all the parameters for
            the callable action
        """

        super().__init__(
            action=condition,
            next_step=next_step,
            **kwargs,
        )

    def __call__(self, **kwargs) -> bool:
        """
        Run the callable action and return the return of that action; the action should return a bool

        :param dict, kwargs: dictionary must contain entries with keys that are identical to all the parameters for
            the callable action, and the values are the actual values/items for the corresponding keys
        :return: bool, value is based on the return of the callable action
        """
        super().__call__(**kwargs)
        return self._action_return


class IfStep(Step):
    def __init__(self,
                 condition_check_list: list = None,
                 **kwargs,
                 ):
        """
         A `Step` in an automation sequence that has multiple possible next steps, which is decided based on a list of
        `ConditionChecks`. If the return of the first `ConditionCheck` is `True`, then the next step of the `IfStep` is
        the `next_step` of the `ConditionCheck`. If the bool is `False`, then iterate through the list of
        `ConditionChecks` until a condition returns `True`. If none of them return `True`, then the last
        `ConditionCheck` in the list is assumed to be `True` (essentially it is like the `else` in an
        `if-elif-...-else` block).

        :param list, condition_check_list: a list of ConditionCheck instances
        :param kwargs: dictionary must contain entries with keys that are identical to all the parameters for
            the callable action
        """
        self._condition_check_list = condition_check_list

        super().__init__(
            action=self.run_conditions,
            next_step=None,
            **kwargs,
        )

    def __call__(self, **kwargs) -> None:
        """

        :param dict, kwargs: dictionary must contain entries with keys that are identical to all the parameters for
            the callable action, and the values are the actual values/items for the corresponding keys
        :return:
        """
        return super().__call__(**kwargs)

    @property
    def condition_check_list(self) -> List[Step]:
        """
        a list of ConditionChecks to iterate through to know what to put as the self.next_step
        when the IfStep instance is run
        """
        return self._condition_check_list

    @condition_check_list.setter
    def condition_check_list(self,
                             value: List[Step],
                             ):
        if isinstance(value, list) is False:
            raise TypeError('value should be of type list')
        elif any([isinstance(step, Step) is False for step in value]):
            raise TypeError('A list of Step instances must be provided')
        self._condition_check_list = value

    @condition_check_list.deleter
    def condition_check_list(self):
        self._condition_check_list = None

    def run_conditions(self,
                       **kwargs,
                       ) -> None:
        """
        Go through each ConditionCheck in the self._condition_check_list to find out what the next_step from this
        IfStep instance should be. If the Step has been set to be bypassed, then the next_step is based on the last
        ConditionCheck in the list

        :param dict, kwargs:  dictionary must contain entries with keys that are identical to all the parameters for
            all the ConditionChecks
        :return:
        """

        if self._bypass_step is False:
            for condition_check in self._condition_check_list:
                if condition_check(**kwargs):
                    resulting_step = condition_check.next_step
                    self.logger.debug(f'true condition is {condition_check}')
                    self._next_step = resulting_step
                    return

        # if None of the condition checks return true or bypass is true, then make the next step by default the
        # resulting step of the last condition step in the list
        last_condition_step = self._condition_check_list[-1]
        resulting_step = last_condition_step.next_step
        self._next_step = resulting_step
        self.logger.debug(f'no condition was true.')

