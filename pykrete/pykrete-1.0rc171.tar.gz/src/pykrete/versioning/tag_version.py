"""
GIT tag-based version information manager
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
import re
from pykrete.args import environ
from pykrete.repo import Git
from .version import Version
from .ci_io import CiIo
from .ci_revision import CiRevision
from .bumper import Bumper


class TagVersion(Version):
    """Handle version in CI environment
    A version is constructed from the last version tag (tag name format '<major>.<minor>.<build>'
     indicating a release version, with a message format of 'ci_base_build <build>' indicating the
     CI build number for the first release with this major-minor combo).
    Build is calculated as the current CI project-build# variable, minus the build specified in the
     last version tag's message (unless bumper was activated, in which case it'll be 0).
    Revision is read from the CI environment variables (see CiRevision).
    """
    def __init__(self, tag_reader=None, bumper=Bumper.disabled, ci_reader=environ, ci_spec=None):
        """Initializes this instance from CI environment

        :param tag_reader: (pattern, is_must)=>tag list
         [see pykrete.repo.git.get_tags_from behavior]
        :param bumper: (version, tags)=>version, was_bumped
         [see pykrete.versioning.Bumper.major_minor_tag behavior]
        :param ci_reader: (ci_variable, role)=>value function
         [see pykrete.args.environ behavior]
        :param ci_spec: dictionary of part to CI variable
         (parts are: 'major version', 'minor version', 'build version', 'branch name',
          'merge request title')
        """
        self.__ci_io = CiIo(ci_reader, ci_spec)
        self.__tag_reader = tag_reader if tag_reader else Git().get_tags_from
        self.__bumper = bumper
        revision_type = CiRevision(self.__ci_io).revision_type
        (major, minor, build) = self._read_version_from_tags()
        super().__init__(major=major,
                         minor=minor,
                         revision=revision_type.value,
                         build=build,
                         revision_type=revision_type)

    def _read_version_from_tags(self):
        tags = self.__tag_reader(pattern=r'(\d+\.){2}\d+', is_must=False)
        last_version_tag = tags[0] if tags else None
        version, base_build = self.__get_version_and_base_build_from(last_version_tag)
        version, was_bumped = self.__bumper(version, tags)
        if not was_bumped:
            version = self.__bump_relative_build(version, base_build)
        return tuple(version)

    def __bump_relative_build(self, version, base_build):
        ci_build = int(self.__ci_io.read_env('build version'))
        version[2] = ci_build - base_build
        return version

    @staticmethod
    def __get_version_and_base_build_from(tag):
        if not tag:
            return [0, 0, 0], 0
        version = [int(part) for part in tag[0].split('.')]
        message_build = re.findall(r'ci_base_build (\d+)', tag[1]) if tag[1] else None
        base_build = int(message_build[0]) if message_build else 0
        return version, base_build
