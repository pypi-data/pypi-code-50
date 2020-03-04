from functools import total_ordering
import re as _re

from semi_semantic.version_segment import VersionSegment
from semi_semantic.parse_error import ParseError


_SEMI_SEMVER_REGEX = r"^(?P<release>[\dA-za-z_\.]+)(\-(?P<pre_release>[\dA-Za-z_\-\.]+))?(\+(?P<post_release>[\dA-Za-z_\-\.]+))?$"


@total_ordering
class Version:
    def __init__(self, release, pre_release=None, post_release=None):
        self.release = release
        self.pre_release = pre_release
        self.post_release = post_release

        self.segments = [release]
        if pre_release:
            self.segments.append(pre_release)
        if post_release:
            self.segments.append(post_release)

    @classmethod
    def parse(cls, version_string):
        if version_string is None:
            raise ValueError("Invalid Version String: none")
        if version_string == "":
            raise ValueError("Invalid Version String: ''")
        matches = _re.match(_SEMI_SEMVER_REGEX, version_string)
        if matches is None:
            raise ParseError(f"Invalid Version Format: '{version_string}'")

        release = VersionSegment.parse(matches["release"])
        pre_release = None
        if matches["pre_release"]:
            pre_release = VersionSegment.parse(matches["pre_release"])
        post_release = None
        if matches["post_release"]:
            post_release = VersionSegment.parse(matches["post_release"])

        return Version(release, pre_release, post_release)

    def __str__(self):
        version_str = str(self.release)
        if self.pre_release:
            version_str += f"-{self.pre_release}"
        if self.post_release:
            version_str += f"+{self.post_release}"

        return version_str

    def __hash__(self):
        return hash(self.__str__())

    # rich comparisons
    def __eq__(self, other):
        if self.release != other.release:
            return False
        if self.pre_release != other.pre_release:
            return False
        if self.post_release != other.post_release:
            return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if self.release != other.release:
            return self.release < other.release

        if self.pre_release is not None and other.pre_release is None:
            return True
        elif self.pre_release is None and other.pre_release is not None:
            return False
        elif self.pre_release != other.pre_release:
            return self.pre_release < other.pre_release

        if self.post_release is not None and other.post_release is None:
            return False
        elif self.post_release is None and other.post_release is not None:
            return True
        else:
            return self.post_release < other.post_release
