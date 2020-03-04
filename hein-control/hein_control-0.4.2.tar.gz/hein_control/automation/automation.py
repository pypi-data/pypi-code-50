import logging
from hein_control.automation.step import Step
from hein_control.scheduler.action import TrackedAction

logger = logging.getLogger(__name__)


class Automation(TrackedAction):
    """
    An Automation is used to run a sequence of Steps. For an Automation, you need to specify what the first step to
    run is.

    An Automation instance is callable. When called, it will run the first Step, get the next_step from
    that first step, and loop through running and retrieving the next Step to run, until there are no more Steps to run.

    The IfStep enables decision making in an Automation

    The Automation class is also important, because all the arguments for all the Steps must be passed into the
    Automation on instantiation, and these arguments may potentially be updated by the Steps. All these arguments for
    the CustomSteps must be passed into an Automation sequence as a dictionary, where the keys are the argument names
    and the values are the initial values for these arguments. These arguments get stored as self.kwargs in the
    Automation instance, and self.kwargs gets used as the arguments to run the CustomSteps. If the CustomStep run
    function has a return value, it MUST be a dictionary, where the keys are argument names (that must correspond to
    a key in the self.kwargs dictionary of the Automation instance), and the values are the new values for the
    arguments; and in this way the arguments for the Automation instance can be updated.

    In short for using the Automation and Steps classes:
    * An Automation instantiation MUST include a dictionary of arguments and initial values to be used by the Steps
        in the Automation, unless no variables need to be passed between/used by multiple Steps
    * The parameter names for all the functions of CustomSteps must be identical to the keys in the kwargs
        dictionary that get passed into an Automation instance on instantiation
    * The return value of any CustomStep must be a dictionary, with the keys being identical to the keys in the
        kwargs dictionary of the Automation instance, and the values are the updated values
    * All these functions for the CustomSteps must also have a **kwargs parameter, to catch arguments that get passed
        through that are not actually required by the functions.
    * An Automation instance must know what the first step to run is
    * Steps need to be 'chained' to each other

    """
    def __init__(self,
                 first_step: Step,
                 **kwargs):
        """

        :param Step, first_step: first step in the automation to run
        :param dict, kwargs: all the entry keys need to be identical to the parameter names for the callable actions
            for all the Steps in the automation
        """
        if isinstance(first_step, Step) is False:
            raise TypeError('first_step must be of type Step')

        self._first_step: Step = first_step
        self._next_step = None
        self.kwargs = kwargs

        super().__init__(action=self.run_automation,
                         **kwargs,
                         )

        self.logger = logger.getChild(f'{self.__class__.__name__} {self.name}')

    def __call__(self, **kwargs):
        """
        Run the first step in the automation, and get the next step that results from it. then loop, running the next
        step after that and so on, until the end of the automation has been reached.

        :param dict, kwargs: dictionary of arguments to run the Steps in the automation. Nothing should need to be
            passed in here for this because the kwargs should have been passed in when the Automation instance was
            instantiated, but if they were not or need to be updated, they can be passed here
        :return:
        """
        self.logger.debug(f'run automation')
        self.run_automation(**kwargs)

    @property
    def first_step(self) -> Step:
        """The first step in the Automation run"""
        return self._first_step

    @first_step.setter
    def first_step(self,
                   value: Step,
                   ):
        if isinstance(value, Step) is False:
            raise TypeError('value must be of type Step')

        self._first_step = value

    @first_step.deleter
    def first_step(self):
        self._first_step = None

    @property
    def next_step(self) -> Step:
        """The next step in the Automation run"""
        return self._next_step

    @next_step.setter
    def next_step(self,
                  value: Step
                  ):
        if isinstance(value, Step) is False:
            raise TypeError('value must be of type Step')

        self._next_step = value

    @next_step.deleter
    def next_step(self,
                  ):
        self._next_step = None

    def run_step_and_return_next_step(self,
                                      step: Step,
                                      **kwargs,
                                      ) -> Step:
        """
        Run a Step, and get the next_step from the Step that was run and return it. If the Step is a CustomStep,
        a dictionary will be returned when the step is run. The dictionary will have identical keys to the kwargs for
        the Automation instance. If a dictionary is returned, then update self.kwargs for the Automation instance
        with the return from the Step

        :param Step, step: a Step to run
        :param dict, kwargs: if the Step callable (action) requires arguments, they must be passed in through this
            kwargs dictionary
        :return: Step, self._next_step: the next Step that should be run
        """
        kwargs_from_step_that_was_run = step(**kwargs)  # note that the next step may be set within the run function
        #  in some of the subclasses or depending on what the run function is

        if type(kwargs_from_step_that_was_run) == dict:
            # if the return type of the run function is a dictionary, then update self.kwargs of the automation object
            self.kwargs.update(kwargs_from_step_that_was_run)

        self._next_step = step.next_step
        return self._next_step

    def run_automation(self,
                       **kwargs,
                       ):
        """
        Run the first step in the automation, and get the next step that results from it. then loop, running the next
        step after that and so on, until the end of the automation has been reached. Will get called when an
        Automation instance is called.

        :param dict, kwargs: dictionary of arguments to run the Steps in the automation. Nothing should need to be
            passed in here for this because the kwargs should have been passed in when the Automation instance was
            instantiated, but if they were not or need to be updated, they can be passed here
        :return:
        """
        self.kwargs.update(kwargs)
        self._next_step = self._first_step
        while self._next_step is not None:
            self.logger.debug(f'next step: {self._next_step}')
            self._next_step = self.run_step_and_return_next_step(step=self._next_step, **self.kwargs)
        self.logger.debug('automation ended')

