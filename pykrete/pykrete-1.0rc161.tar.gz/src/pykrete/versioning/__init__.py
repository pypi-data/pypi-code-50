"""
Version information managers
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from .ci_version import CiVersion
from .revision_type import RevisionType
from .version import Version
from .version_py_version import VersionPyVersion

__all__ = ['CiVersion', 'RevisionType', 'Version', 'VersionPyVersion']
