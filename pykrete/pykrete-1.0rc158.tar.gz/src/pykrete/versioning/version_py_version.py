"""
version.py version information manager
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from re import findall
from pykrete.packages import make_python_root_version_file_path
from .version import Version
from .revision_type import RevisionType


class VersionPyVersion(Version):
    """Handle version in python.py"""
    revisions = {
        '.': RevisionType.Release,
        'rc': RevisionType.RC,
        'b': RevisionType.Beta,
        'a': RevisionType.Alpha}

    def __init__(self, project):
        """Initialize this instance from the specified project's version.py file

        :param project: Python project (under 'src')
        """
        version_py_path = make_python_root_version_file_path(project)
        version_match = self.__read_version_match(version_py_path)
        version_parts = self.__parse_version_parts(version_match)
        super().__init__(version_parts)

    @staticmethod
    def __read_version_match(version_py_path):
        try:
            with open(version_py_path, 'r') as file:
                separator_pattern = '|'.join(VersionPyVersion.revisions.keys()).replace('.', r'\.')
                return findall(f"__version__ = '(\\d+)\\.(\\d+)({separator_pattern})(\\d+)'",
                               file.read())[0]
        except IndexError:
            raise IOError("No version specification found in file")

    @staticmethod
    def __parse_version_parts(version_parts):
        if not version_parts or len(version_parts) != 4:
            raise IOError('Incompatible version')
        revision_marker = version_parts[2]
        revision_type = VersionPyVersion.revisions[revision_marker]
        return (version_parts[0], version_parts[1], revision_type.value, version_parts[3],
                revision_type)
