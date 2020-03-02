"""
Python package
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from re import findall
from os import path
from pkg_resources import require


def make_python_root_version_file_path(project):
    """ Generate the version.py file from the project's name

    :param project: project name
    :return: src/<project>/version.py
    """
    return path.join('src', project, 'version.py')


class PythonPackage:
    """Python package"""

    @property
    def project(self):
        """
        :return: (string) name of project package under 'src'.
        """
        return self._project

    @property
    def version(self):
        """
        :return: (string) The project's version
        """
        return self._version

    def __init__(self, project, package_fallback=False):
        """Initializes this instance to analyze the specified project

        :param project: name of project package under 'src'
        """
        self._version_file = make_python_root_version_file_path(project)
        self._project = project
        self._package_fallback = package_fallback
        self._version = self._get_version()

    @staticmethod
    def get_long_description():
        """Gets the contents of the README.md file

        :return: Long description
        """
        with open('README.md', 'r') as readme:
            return readme.read()

    def _get_version(self):
        """Gets the package version

        :return: The version
        :exception IndexError: Version not found
        """
        try:
            return self._get_version_from_file()
        except IOError:
            if not self._package_fallback:
                raise
            version_from_current_package = require(self._project)[0].version
            return version_from_current_package

    def _get_version_from_file(self):
        """Gets the version from the version file

        :return: The version
        :exception IOError: Version file doesn't exist
        """
        try:
            with open(self._version_file, 'r') as file:
                return findall("__version__ = '([^']*)'", file.read())[0]
        except IndexError:
            raise IOError('Version not found in ' + self._version_file)

    def __str__(self):
        return f'{self._project} v{self._version}'
