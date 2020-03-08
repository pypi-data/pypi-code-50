''' A ScheduleProvider Service Provider '''
from masonite.provider import ServiceProvider

from ..commands.CreateTaskCommand import CreateTaskCommand
from ..commands.ScheduleRunCommand import ScheduleRunCommand
from ..CommandTask import CommandTask
from ..CanSchedule import CanSchedule


class ScheduleProvider(ServiceProvider, CanSchedule):

    def register(self):
        self.app.bind('ScheduleCommand', ScheduleRunCommand())
        self.app.bind('CreateTaskCommand', CreateTaskCommand())

    def boot(self):
        pass
