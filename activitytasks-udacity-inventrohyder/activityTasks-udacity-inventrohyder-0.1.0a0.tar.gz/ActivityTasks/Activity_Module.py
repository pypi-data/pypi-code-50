from typing import List

from .Task_Module import Task


class Activity:
    """
    A class representing an activity that contains tasks
    """

    def __init__(self, name: str, *tasks: Task) -> None:
        self.__name: str = name
        self.__tasks: dict = {}
        if not len(tasks) == 0:
            self.add_tasks(*tasks)

    @property
    def name(self) -> str:
        """The name of the activity"""
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def tasks(self) -> List[Task]:
        """The tasks that are associated with the current activity"""
        return list(self.__tasks.values())

    @tasks.setter
    def tasks(self, value):
        raise TypeError("'tasks' cannot be updated directly")

    def add_tasks(self, *tasks) -> None:
        """
        Adds tasks to the activity

        :param tasks: Task
            The task(s) to add
        """
        for task in tasks:
            if task.id not in self.__tasks:
                self.__tasks[task.id] = task
                if task.activity != self: task.activity = self

    def remove_tasks(self, *tasks) -> None:
        """
        Removes tasks already in the current activity
        :param tasks:
            The tasks to remove the association with the current activity
        """
        for task in tasks:
            if task.id in self.__tasks:
                self.__tasks.pop(task.id)
                task.reset_activity()
