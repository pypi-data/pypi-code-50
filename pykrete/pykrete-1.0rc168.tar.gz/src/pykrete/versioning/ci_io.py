"""
CI information manager
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from pykrete.args import environ


class CiIo:
    """Handle CI environment IO
    """
    def __init__(self, ci_reader=environ, ci_spec=None):
        """Initializes this instance from CI environment

        :param ci_reader: (ci_variable, role)=>value function [see pykrete.args.environ behavior]
        :param ci_spec: dictionary of part to CI variable
         (parts are: 'major version', 'minor version', 'build version', 'branch name',
          'merge request title')
        """
        self.__ci_reader = ci_reader
        self.__ci_spec = ci_spec if ci_spec else self.__get_default_ci_spec()

    def read_env(self, part, is_no_role=False):
        """Read a spec-part from the CI environment

        :param part: part name
        :param is_no_role: should there be an exception if not found
        :return: Read value, or None if not found
        :exception: The part's variable is not defined in the environment and it should be
        """
        return self.__ci_reader(self.__ci_spec[part],
                                None if is_no_role else f'CI\'s \'{part}\' value')

    @staticmethod
    def __get_default_ci_spec():
        return {'major version': 'CI_VERSION_MAJOR',
                'minor version': 'CI_VERSION_MINOR',
                'build version': 'CI_PIPELINE_IID',
                'branch name': 'CI_COMMIT_REF_NAME',
                'merge request title': 'CI_MERGE_REQUEST_TITLE'}
