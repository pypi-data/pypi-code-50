"""
CI environment-based version information manager
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from pykrete.args import environ
from .version import Version
from .ci_io import CiIo
from .ci_revision import CiRevision


class CiVersion(Version):
    """Handle version in CI environment
    Version parts are read from CI variables

    """
    def __init__(self, ci_reader=environ, ci_spec=None):
        """Initializes this instance from CI environment

        :param ci_reader: (ci_variable, role)=>value function [see pykrete.args.environ behavior]
        :param ci_spec: dictionary of part to CI variable
         (parts are: 'major version', 'minor version', 'build version', 'branch name',
          'merge request title')
        """
        ci_io = CiIo(ci_reader, ci_spec)
        revision_type = CiRevision(ci_io).revision_type
        super().__init__(major=ci_io.read_env('major version'),
                         minor=ci_io.read_env('minor version'),
                         revision=revision_type.value,
                         build=ci_io.read_env('build version'),
                         revision_type=revision_type)
