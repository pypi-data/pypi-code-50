class VersionException(Exception):
    """ Custom Version Exception for logging exception
    """
    pass


class Version(object):
    """ Version class for maintaining the versions

        Example:
            version = Version(10.10.1-beta.2)
            print(version.major)
            >> 10
            print(version.preRelease)
            >> 2
            print(version)
            >> 10.10.1-beta.2
    """
    def __init__(self, version=None):
        """ Version initializer

            KwArgs:
                version (str): Version string to parse.(Default: "1.0.0")
        """
        self.version = version or "1.0.0"
        self.major = self.minor = self.patch = self.preRelName = self.preRelease = None
        self._acceptedPreRelNames = ['alpha', 'beta', 'rc']

        self._parse_version()

    def __str__(self):
        """ Override function to return the version string object
        """
        if self.is_pre_version and self.preRelName and self.preRelease:
            return "{major}.{minor}.{patch}-{preRelN}.{preRel}" .format(
                major=self.major,
                minor=self.minor,
                patch=self.patch,
                preRelN=self.preRelName,
                preRel=self.preRelease,
            )
        else:
            return "{major}.{minor}.{patch}" .format(
                major=self.major,
                minor=self.minor,
                patch=self.patch,
            )

    @property
    def is_pre_version(self):
        """ Definition to check if the version is pre release or not

            :returns
                result (bool): Returns boolean value if the version is a pre release
        """
        result = False
        if '-' in self.version:
            result = True
        return result

    def _parse_version(self):
        """ Parse the version to specified types like major, minor, patch etc.,

            :raises VersionException if version syntax is wrong
        """
        if self.is_pre_version:
            pre_release_split = self.version.split('-')[-1].split('.')
            if not len(pre_release_split) == 2:
                raise VersionException(
                    "Pre release syntax must be <preReleaseName>.<preReleaseVersion>"
                )
            if not pre_release_split[0] in self._acceptedPreRelNames:
                raise VersionException(
                    "Pre release name must be of %s" % ", ".join(
                        self._acceptedPreRelNames
                    )
                )
            self.preRelName = pre_release_split[0]
            self.preRelease = self._get_int_value(pre_release_split[1], ver_type="pre")
        release_split = self.version.split('-')[0].split('.')
        if not len(release_split) == 3:
            raise VersionException(
                "Release syntax must be <major>.<minor>.<patch>"
            )
        self.major = self._get_int_value(release_split[0])
        self.minor = self._get_int_value(release_split[1])
        self.patch = self._get_int_value(release_split[2])

    @staticmethod
    def _get_int_value(version, ver_type=None):
        """ convert the string version to integer

            :raises VersionException if given version is a string
        """
        try:
            result = int(version)
        except ValueError:
            if ver_type:
                raise VersionException(
                    "Pre release version must be of type integer, not string"
                )
            else:
                raise VersionException(
                    "Release version must be of type integer, not string"
                )
        return result


if __name__ == '__main__':
    version = Version("1.0.1-beta.1")
    print(version.major)
    print(version.preRelease)
    print(version)
