"""
CI environment-based version information manager
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from pykrete.args import environ
from pykrete.versioning.revision_type import RevisionType


class CiVersion:
    """Handle version in CI environment
    Revision is:
        Release - in master branch
        RC - in non-WIP merge request
        Beta - in merge request with 'WIP' in the title
        Alpha - none of the above
    """

    @property
    def major(self):
        """
        :return: Major part of the version
        """
        return self._major

    @property
    def minor(self):
        """
        :return: Minor part of the version
        """
        return self._minor

    @property
    def revision(self):
        """
        :return: Revision part of the version
        """
        return self._revision_type.value

    @property
    def build(self):
        """
        :return: Build part of the version
        """
        return self._build

    @property
    def revision_type(self):
        """
        :return: Revision type of the version
        """
        return self._revision_type

    def __init__(self, ci_reader=environ, ci_spec=None):
        """Initializes this instance from CI environment

        :param ci_reader: (ci_variable, role)=>value function [see pykrete.args.environ behavior]
        :param ci_spec: dictionary of part to CI variable
         (parts are: 'major version', 'minor version', 'build version', 'branch name',
          'merge request title')
        """
        self.__ci_reader = ci_reader
        self.__ci_spec = ci_spec if ci_spec else self.__get_default_ci_spec()
        self._major = self.__read_env('major version')
        self._minor = self.__read_env('minor version')
        self._revision_type = self.__get_revision_type()
        self._build = self.__read_env('build version')

    def __str__(self):
        return f'{self.major}.{self.minor}.{self.revision}.{self.build} {self.revision_type.name}'

    def __get_revision_type(self):
        if self.__is_master():
            return RevisionType.Release

        revision = self.__revision_from_merge_request()
        return revision if revision else RevisionType.Alpha

    def __read_env(self, part, is_no_role=False):
        return self.__ci_reader(self.__ci_spec[part],
                                None if is_no_role else f'CI''s \'{part}\' value')

    def __is_master(self):
        branch_name = self.__read_env('branch name')
        return branch_name == 'master'

    def __revision_from_merge_request(self):
        merge_request_title = self.__read_env('merge request title', True)
        if merge_request_title:
            return RevisionType.Beta if 'WIP' in merge_request_title else RevisionType.RC
        return None

    @staticmethod
    def __get_default_ci_spec():
        return {'major version': 'CI_VERSION_MAJOR',
                'minor version': 'CI_VERSION_MINOR',
                'build version': 'CI_PIPELINE_IID',
                'branch name': 'CI_COMMIT_REF_NAME',
                'merge request title': 'CI_MERGE_REQUEST_TITLE'}
