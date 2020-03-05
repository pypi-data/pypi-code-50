"""Quick setup for my local/tower develop environment
"""
import sys
import json
from pathlib import Path
from .log import logging
import os


def on(project):
    dev_mode = DevMode()
    dev_mode.on(project)


def off(project):
    dev_mode = DevMode()
    dev_mode.off(project)


class DevMode:
    """Control package path in the development environment for projects, include pythonpath and ENV variables

    Can load and save info from
        ``~/.yutil.config``, with format
        {project: {pkg_path: [], env_var: {name: value}}
    """

    def __repr__(self):

        def proj_formatter(proj):
            f = proj + ':\n'
            f += '  Package:\n    '
            f += '\n    '.join(self.config[proj]['pkg_path'])
            f += '\n  ENV variable:\n    '
            f += '\n    '.join([f'{env}: {var}' for env, var in self.config[proj]['env_var'].items()])
            return f
        return '\n'.join([proj_formatter(proj) for proj in self.config.keys()])

    def __init__(self, project=None, auto_on=True):
        """Initialize a DevMode controller"""

        _HOME = os.getenv('HOME', '~')
        if Path(_HOME + '/.yutil.config').exists():
            with open(_HOME + '/.yutil.config', 'r') as handle:
                self.config = json.load(handle)
        else:
            self.config = dict()

        self.current_on = None

        if auto_on and project is not None:
            self.on(project)

    def add_project(self, project):
        """Add a project, if not exist"""
        if project not in self.config.keys():
            self.config[project] = dict(pkg_path=[], env_var={})
        else:
            logging.error(f"Project '{project}' exists", error_type=ValueError)

    def add_pkg_path(self, path, project=None):
        """Add pkg path under a project name"""

        if Path(path).exists():
            if project is None:
                if self.config == {}:
                    logging.error('Configuration seems empty, please add project first', error_type=ValueError)
                else:
                    for p in self.config.values():
                        if path not in p['pkg_path']:
                            p['pkg_path'].append(path)
            else:
                if project not in self.config.keys():
                    self.add_project(project=project)
                if path not in self.config[project]['pkg_path']:
                    self.config[project]['pkg_path'].append(path)
        else:
            logging.error(f'{path} does not seem to be an existing directory', error_type=NotADirectoryError)

    def add_env_var(self, project=None, **kwargs):
        """Add environmental variables [to a project]
        Warning: old environmental variable could be overwrote
        """

        if project is None:
            if self.config == {}:
                logging.error('Configuration seems empty, please add project first', error_type=ValueError)
            else:
                for p in self.config.values():
                    p['env_var'].update(kwargs)
        else:
            if project not in self.config.keys():
                self.add_project(project=project)
            self.config[project]['env_var'].update(kwargs)

    def delete_project(self, project):
        _ = self.config.pop(project)

    def delete_pkg_path(self, path, project=None):
        """Delete path from given project"""
        if project is None:
            for pkg_list in self.config['pkg_path'].values():
                _ = pkg_list.pop(path)
        else:
            if project not in self.config['pkg_path'].keys():
                logging.error(f"'{project}' not found", error_type=ValueError)
            else:
                self.config[project]['pkg_path'].pop(path)

    def delete_env_var(self, env_var, project=None):
        """Delete env var from given project"""
        if project is None:
            for pkg_list in self.config['env_var'].values():
                _ = pkg_list.pop(env_var)
        else:
            if project not in self.config['pkg_path'].keys():
                logging.error(f"'{project}' not found", error_type=ValueError)
            else:
                _ = self.config[project]['pkg_path'].pop(env_var)

    def on(self, project):
        """Turn on the dev mode by prioritizing python PATHs and assigning env variable values"""

        if project not in self.config.keys():
            logging.error(f'{project} not found', error_type=ValueError)

        # prioritize the dev package location
        for p in self.config[project]['pkg_path'][::-1]:
            if p not in sys.path:
                sys.path.insert(0, p)
            elif sys.path.index(p) != 0:
                sys.path.remove(p)
                sys.path.insert(0, p)

        for env_var, value in self.config[project]['env_var'].items():
            os.environ[env_var] = value

        # redirect logging info to standard output
        logging.add_console_handler()
        self.current_on = project

    def off(self, project=None):
        if project is None:
            project = self.current_on
        if project is None:
            logging.error('DevMode is not on', error_type=ValueError)

        for p in self.config[project]['pkg_path']:
            if p in sys.path:
                sys.path.remove(p)

        for env in self.config[project]['env_var'].keys():
            del os.environ[env]

        self.current_on = None

    def save(self):
        _HOME = os.getenv('HOME', '~')
        with open(_HOME + '/.yutil.config', 'w') as handle:
            json.dump(obj=self.config, fp=handle)
