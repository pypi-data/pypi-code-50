"""
GIT tag-based version information manager
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""


class Bumper:
    """Bumpers static class"""

    @staticmethod
    def major_minor_tag(version, tags):
        """Locates 'bump' tags (tag name is either 'bump_minor' or 'bump_major') then increments the
         relevant version part.
        One bump at most is performed, with bump_major overriding bump_minor.
        :param version: original version
        :param tags: tags read after original version
        :return: (version, was_bumped) the calculated versions, and a bool flag indicating if
         bumping occurred
        """
        bumps = [tag[0].split('_')[1] for tag in tags if tag and tag[0].startswith('bump_')]
        if 'major' in bumps:
            return [version[0] + 1, 0, 0], True
        if 'minor' in bumps:
            return [version[0], version[1] + 1, 0], True
        return version, False

    @staticmethod
    def disabled(version, tags):    # pylint: disable=unused-argument
        """Keep version as-is regardless of tags"""
        return version, False
