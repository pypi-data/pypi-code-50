from .config import Config
from .context import Context
from .log import set_job_id as set_logging_job_id, set_task_name as set_logging_task_name

__all__ = ['Context', 'Config', 'set_logging_task_name', 'set_logging_job_id']

# Version of cinnamon-task-base
__version__ = '0.8.2'
