"""Console commands for the scheduler."""
from __future__ import print_function
from .config import task_file_path
from .task_parser import TaskParser
from .scheduler import schedule_tasks


def run():
    """Run the scheduler.

    This command is exported as the script for the package.
    """
    tasks = TaskParser().get_tasks(task_file_path)
    schedule_tasks(tasks)
