from collections import namedtuple
from typing import List

Status = namedtuple('status', ('NOT_YET_STARTED', 'IN_PROGRESS', 'COMPLETED'))
status = Status(-1, 0, 1)


class Task:
    """
    A class used to represent a task

    Attributes:
        description:
            The description of the task

    Methods:
        is_complete:
            Checks if the task is completed
        is_in_progress:
            Checks if the task is still in progress
    """

    __id_generator = (x for x in range(1, 99999999, 1))
    """It produces a new id for each instantiation of the Task class"""

    __tasks = []
    """A list that contains all the tasks instantiated by the class"""

    def __init__(self, minutes: float, description: str, activity=None, *dependencies) -> None:
        self.__id: int = Task.__id_generator.__next__()
        self.description: str = description
        self.__activity = None
        # Initialise activity as None
        # then update it
        self.activity = activity  # :type Activity
        self.__original_duration: float = minutes
        self.__duration: float = minutes
        self.__dependencies: dict = {}
        if not len(dependencies) == 0:
            self.add_dependency(*dependencies)
        self.__dependants: dict = {}
        Task.__tasks.append(self)

    @property
    def id(self) -> int:
        """The unique identifier of the given task"""
        return self.__id

    @id.setter
    def id(self, new_id: int) -> None:
        raise TypeError("'id' does not support assignment")

    @property
    def activity(self):
        """The activity associated with the current task"""
        return self.__activity

    @activity.setter
    def activity(self, activity):
        if self.__activity:
            self.__activity.remove_tasks(self)
        self.__activity = activity
        if activity:
            activity.add_tasks(self)

    @property
    def original_duration(self) -> float:
        """The original duration set for the given task"""
        return self.__original_duration

    @original_duration.setter
    def original_duration(self, new_duration: float) -> None:
        raise TypeError("'original_duration' does not support assignment")

    @property
    def duration(self) -> float:
        """The remaining amount of time to complete the given task"""
        return self.__duration

    @duration.setter
    def duration(self, value: float) -> None:
        raise TypeError("'duration' cannot be updated directly")

    @property
    def status(self) -> int:
        """The status of the task if it has not yet started, is in progress or is completed"""
        self.__update_status()
        return self.__status

    @status.setter
    def status(self, value) -> None:
        raise TypeError("'status' does not support assignment")

    @property
    def dependencies(self) -> List:
        """The tasks that the current task depends on"""
        return list(self.__dependencies.values())

    @dependencies.setter
    def dependencies(self, value) -> None:
        raise TypeError("'dependencies' cannot be updated directly")

    @property
    def dependants(self) -> List:
        """The tasks that depend on the current task"""
        return list(self.__dependants.values())

    @dependants.setter
    def dependants(self, value) -> None:
        raise TypeError("'dependants' cannot be updated directly")

    def add_dependency(self, *tasks) -> None:
        """
        Add task(s) that the current task depends on

        :param tasks:
            The task(s) to add as dependencies
        """
        for task in tasks:
            if not task.is_complete():
                self.__dependencies[task.id] = task
                task.__add_dependant(self)

    def remove_dependency(self, *tasks) -> None:
        """
        Removes task(s) that the current task depends on

        :param tasks:
            The task(s) to remove as dependencies
        """

        for task in tasks:
            self.__dependencies.pop(task.id)
            task.__remove_dependant(self)

    def __add_dependant(self, *tasks) -> None:
        """
        Adds task(s) that depends on the current task

        :param tasks:
            The task(s) that will have the current task as a dependency
        """
        for task in tasks:
            self.__dependants[task.id] = task

    def __remove_dependant(self, *tasks) -> None:
        """
        Removes task(s) that depend on the current task

        :param tasks:
            The task(s) that already have the current task as a dependency
        """
        for task in tasks:
            self.__dependants.pop(task.id)

    def complete(self, minutes: float) -> None:
        """
        Reduces the remaining duration

        :param minutes:
            The number of minutes to complete within the task
        """
        self.__duration -= minutes
        self.__update_status()

    def is_complete(self) -> bool:
        return self.status == status.COMPLETED

    def is_in_progress(self) -> bool:
        return self.status == status.IN_PROGRESS

    def __update_status(self) -> None:
        """Updates the status of the given task based on the duration remaining"""
        if self.__duration <= 0:
            self.__status = status.COMPLETED
            self.__duration = 0
            self.__clear_dependants()
        elif self.duration == self.original_duration:
            self.__status = status.NOT_YET_STARTED
        else:
            self.__status = status.IN_PROGRESS

    def __clear_dependants(self) -> None:
        """Removes the current task as a dependency in all the tasks that depend on it"""
        for task in self.__dependants.copy().values():
            if task.id in self.__dependants:
                task.remove_dependency(self)

    def reset_activity(self):
        """Resets the activity associated with the task"""
        self.__activity = None

    @classmethod
    def all_tasks(cls) -> List:
        """
        Produces all the objects instantiated by the class
        :return:
            All the tasks
        """
        return cls.__tasks

    @classmethod
    def reset(cls) -> None:
        """Deletes all the tasks that have ever been instantiated"""
        for task in cls.all_tasks():
            del task
        cls.__tasks = []
        cls.__id_generator = (x for x in range(1, 99999999, 1))

    def __str__(self) -> str:
        return f"Task: {self.id} - {self.description}, remaining time: {self.duration} minutes"

    def __gt__(self, other) -> bool:
        if isinstance(other, Task):
            return self.duration > other.duration
        return self.duration > other

    def __ge__(self, other) -> bool:
        if isinstance(other, Task):
            return self.duration >= other.duration
        return self.duration >= other

    def __lt__(self, other) -> bool:
        if isinstance(other, Task):
            return self.duration < other.duration
        return self.duration < other

    def __le__(self, other) -> bool:
        if isinstance(other, Task):
            return self.duration <= other.duration
        return self.duration <= other
