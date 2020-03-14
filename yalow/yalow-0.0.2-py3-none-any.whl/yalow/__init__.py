import os
import logging


class Yalow:
    """Yet Another LOgging Wrapper

    Wraps Python's logging module functionality for the
    generic use case of generating and writing to a shared project
    log file in the 'root_path/log' directory.

    Parameters
    ----------
    root_path : pathlib.Path
        Root path of project.
    project_name : str
        Name of project (The default is 'yalow', I know, very imaginative).
    log_dir_name : str
        Name of the log directory created in project root (The default is 'log', because as we've already established
        my imagination is a veritable cornucopia of originality).
    level : logging.Logger.level
        Default logging level for events added to log (The default is logging.DEBUG).
    file_write_mode : str
        Mode for writing log file, 'w' for overwrite, 'a' for append (The default behavior is 'w' for overwrite).

    Attributes
    ----------
    log_filepath : pathlib.Path
        Path for generated log file for project.
    logger : logging.Logger
        Project shared logger object.
    handler : logging.FileHandler
        Responsible for writing the project log to file.
    formatter : logging.Formatter
        Responsible for formatting project log file output.

    """
    def __init__(self, root_path, project_name='yalow', log_dir_name='log', level=logging.DEBUG, file_write_mode='w'):
        if not os.path.exists(root_path / log_dir_name):
            os.makedirs(root_path / log_dir_name)
        self.log_filepath = root_path/f'log/{project_name}.log'
        self.logger = logging.getLogger(project_name)
        self.handler = logging.FileHandler(root_path/self.log_filepath, mode=file_write_mode)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(level)
        self.logger.info(f'Logging initialized for project: {project_name}')
