"""
CI environment-based version information manager
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""
from pykrete.args import environ
from pykrete.repo import Git
from .version import Version
from .ci_io import CiIo
from .ci_revision import CiRevision


class TagVersion(Version):
    """Handle version in CI environment
    A version is constructed from the last version tag (tag name format '<major>.<minor>.<build>',
    with a message format of 'ci_build <build>') and any following 'bump' tags (tag name is either
    'bump_minor' or 'bump_major', which increment the relevant version part).
    One bump at most is performed, with bump_major overriding bump_minor.
    Build is calculated as the current CI project-build# variable, minus the build specified in the
    last version tag's message.
    Revision is read from the CI environment variables (see CiRevision).
    """
    def __init__(self, tag_reader=None, ci_reader=environ, ci_spec=None):
        """Initializes this instance from CI environment

        :param tag_reader: (pattern, is_must)=>tag list
         [see pykrete.repo.git.get_tags_from behavior]
        :param ci_reader: (ci_variable, role)=>value function
         [see pykrete.args.environ behavior]
        :param ci_spec: dictionary of part to CI variable
         (parts are: 'major version', 'minor version', 'build version', 'branch name',
          'merge request title')
        """
        self.__ci_io = CiIo(ci_reader, ci_spec)
        revision_type = CiRevision(self.__ci_io).revision_type
        (major, minor, build) = self._read_tag(tag_reader if tag_reader else Git().get_tags_from)
        super().__init__(major=major,
                         minor=minor,
                         revision=revision_type.value,
                         build=build,
                         revision_type=revision_type)

    def _read_tag(self, tag_reader):
        tags = tag_reader(pattern=r'(\d+\.){2}\d+', is_must=False)
        last_version_tag = tags[0] if tags else None
        version, build = self.__get_last_version_and_build_from(last_version_tag)
        version = self.__bump_version_from_tags(version, tags)
        build = self.__get_relative_build(build)
        return version[0], version[1], build

    def __get_relative_build(self, build):
        ci_build = int(self.__ci_io.read_env('build version'))
        return ci_build - build

    @staticmethod
    def __get_last_version_and_build_from(tag):
        version = [int(part) for part in (tag[0] if tag else '0.0.0').split('.')]
        build = int(tag[1].split(' ')[1] if tag else '0')
        return version, build

    @staticmethod
    def __bump_version_from_tags(version, tags):
        bumps = [tag[0].split('_')[1] for tag in tags if tag and tag[0].startswith('bump_')]
        if 'major' in bumps:
            version[0] += 1
            version[1] = 0
        elif 'minor' in bumps:
            version[1] += 1
        return version
