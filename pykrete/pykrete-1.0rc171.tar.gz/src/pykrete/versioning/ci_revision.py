"""
CI environment-based revision information manager
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from .revision_type import RevisionType


class CiRevision:
    """Handle revision in CI environment
    Revision is:
        Release - in master branch
        RC - in non-WIP merge request
        Beta - in merge request with 'WIP' in the title
        Alpha - none of the above
    """
    @property
    def revision_type(self):
        """
        :return: Revision type of the version
        """
        return self._revision_type

    def __init__(self, ci_io):
        """Initializes this instance from CI environment

        :param ci_io: CI IO for 'branch name', 'merge request title'
        """
        self.__ci_io = ci_io
        self._revision_type = self.__get_revision_type()

    def __get_revision_type(self):
        if self.__is_master():
            return RevisionType.Release

        revision = self.__revision_from_merge_request()
        return revision if revision else RevisionType.Alpha

    def __is_master(self):
        branch_name = self.__ci_io.read_env('branch name')
        return branch_name == 'master'

    def __revision_from_merge_request(self):
        merge_request_title = self.__ci_io.read_env('merge request title', True)
        if merge_request_title:
            return RevisionType.Beta if 'WIP' in merge_request_title else RevisionType.RC
        return None
