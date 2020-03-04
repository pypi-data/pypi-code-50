import logging
from hein_control.automation.automation import Automation
from hein_control.automation.step import CustomStep, ConditionCheck, IfStep

class AA():
    def __init__(self):
        self.logger = logger.getChild(f'{self.__class__.__name__}')

    def func_a(self):
        self.logger.debug('func_a')

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

aa = AA()

automation_kwargs = {
    'aa': aa,
    'a': 'a',
}

def action_1(aa, a, **kwargs):
    aa.func_a()
    return

def action_2(**kwargs):
    return

def condition_1(**kwargs):
    return True


step_a = CustomStep(action=action_1)
step_b = CustomStep(action=action_2)

cond_a = ConditionCheck(condition=condition_1, next_step=step_a)

if_check = IfStep(condition_check_list=[cond_a,
                                        ])

step_a.next_step = step_b
step_b.next_step = if_check

automation = Automation(first_step=step_a,
                        **automation_kwargs)

automation()