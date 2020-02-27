from .Task_Module import Task


class MultiTask(Task):
    """
    Extends the Task class and adds a multitasking attribute
    """

    def __init__(self, minutes: float, description: str, multitasking: bool, activity=None, *dependencies) -> None:
        super().__init__(minutes, description, activity, *dependencies)
        self.__multitask = multitasking

    @property
    def can_multitask(self) -> bool:
        """The ability to multitask"""
        return self.__multitask

    @can_multitask.setter
    def can_multitask(self, value: bool) -> None:
        self.__multitask = value

    def __str__(self) -> str:
        return super().__str__() + '; Multitasking: ' + str(self.__multitask)





