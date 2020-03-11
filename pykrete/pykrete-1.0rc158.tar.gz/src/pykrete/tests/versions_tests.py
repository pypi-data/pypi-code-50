"""
Pykrete versions tests
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

import unittest
import re
import os
from pykrete.versioning import CiVersion, RevisionType, Version, VersionPyVersion


def _echo(what, who):
    print(f'CiVersion is reading \'{who}\' and will get \'{what}\'')
    return None if what == 'None' else what


def _get_full_path(project):
    return os.path.join('pykrete', 'tests', 'src', project)


class PykreteVersionsTestCase(unittest.TestCase):
    """Unit tests for pykrete's versions module
    """
    version_patten = re.compile(r'(\d+\.){3}\d+ (Alpha|Beta|RC|Release)')

    def test_version_from_tuple(self):
        """Verifies creation of version from tuple"""
        target = Version((1, 2, 3, 4, RevisionType.Alpha))
        self._assert_version(target, (1, 2, 3, 4, RevisionType.Alpha))

    def test_version_from_args(self):
        """Verifies creation of version from arguments"""
        target = Version(12, 23, 34, 45, RevisionType.Beta)
        self._assert_version(target, (12, 23, 34, 45, RevisionType.Beta))

    def test_version_from_version(self):
        """Verifies creation of version from another version object"""
        source = Version(111, 222, 333, 444, RevisionType.RC)
        target = Version(source)
        self._assert_version(target, (111, 222, 333, 444, RevisionType.RC))
        self.assertEqual(source, target, "Version objects aren't equal")

    def test_version_from_kwargs(self):
        """Verifies creation of version from named arguments"""
        target = Version(major=21, minor=32, revision=43, revision_type=RevisionType.Release,
                         build=54)
        self._assert_version(target, (21, 32, 43, 54, RevisionType.Release))

    def test_version_ordering(self):
        """Verifies ordering of version objects"""
        source = [Version(1, 2, 3, 4, RevisionType.Release),
                  Version(1, 2, 3, 1, RevisionType.Release),
                  Version(1, 2, 3, 4, RevisionType.Release),
                  Version(1, 2, 1, 3, RevisionType.Release),
                  Version(1, 0, 2, 3, RevisionType.Release),
                  Version(0, 1, 2, 3, RevisionType.Release),
                  Version(11, 22, 33, 44, RevisionType.Release)]
        target = sorted(source)
        print('\n'.join(str(version) for version in target))
        expected = [Version(0, 1, 2, 3, RevisionType.Release),
                    Version(1, 0, 2, 3, RevisionType.Release),
                    Version(1, 2, 1, 3, RevisionType.Release),
                    Version(1, 2, 3, 1, RevisionType.Release),
                    Version(1, 2, 3, 4, RevisionType.Release),
                    Version(1, 2, 3, 4, RevisionType.Release),
                    Version(11, 22, 33, 44, RevisionType.Release)]
        for comparison in zip(expected, target):
            self.assertEqual(comparison[0], comparison[1], "Wrong ordering")

    def test_ci_version_server(self):
        """Verifies handling of CI-environment version
        NOTE: THIS TEST WILL FAIL LOCALLY, SAFE TO IGNORE
        """
        print('NOTE: THIS TEST WILL FAIL LOCALLY, SAFE TO IGNORE')
        self._assert_version_pattern(CiVersion())

    def test_ci_version_local_release(self):
        """Verifies handling of simulated CI-environment's release version"""
        self._assert_ci_version_local(
            spec={'major version': '1',
                  'minor version': '2',
                  'build version': '3',
                  'branch name': 'master',
                  'merge request title': 'None'},
            expected_revision_type=RevisionType.Release,
            expected_revision=4)

    def test_ci_version_local_rc(self):
        """Verifies handling of simulated CI-environment's release-candidate version"""
        self._assert_ci_version_local(
            spec={'major version': '11',
                  'minor version': '22',
                  'build version': '33',
                  'branch name': 'custom',
                  'merge request title': 'title'},
            expected_revision_type=RevisionType.RC, expected_revision=3)

    def test_ci_version_local_beta(self):
        """Verifies handling of simulated CI-environment's beta version"""
        self._assert_ci_version_local(
            spec={'major version': '111',
                  'minor version': '222',
                  'build version': '333',
                  'branch name': 'custom',
                  'merge request title': 'WIP: title'},
            expected_revision_type=RevisionType.Beta, expected_revision=2)

    def test_ci_version_local_alpha(self):
        """Verifies handling of simulated CI-environment's alpha version"""
        self._assert_ci_version_local(
            spec={'major version': '123',
                  'minor version': '456',
                  'build version': '789',
                  'branch name': 'custom',
                  'merge request title': 'None'},
            expected_revision_type=RevisionType.Alpha,
            expected_revision=1)

    def test_version_py_release_version_good(self):
        """Verifies reading of a release package's version
        """
        self._assert_good_package('african_swallow', '12.34.4.56 Release')

    def test_version_py_rc_version_good(self):
        """Verifies reading of a release-candidate package's version
        """
        self._assert_good_package('european_swallow', '12.34.3.56 RC')

    def test_version_py_missing_version_in_file(self):
        """Verifies handling of a bad version file
        """
        with self.assertRaises(IOError):
            print(str(VersionPyVersion(_get_full_path('a_duck'))))

    def test_version_py_missing_version_file(self):
        """Verifies handling of a missing version file
        """
        with self.assertRaises(FileNotFoundError):
            print(str(VersionPyVersion(_get_full_path('a_witch'))))

    def _assert_good_package(self, project, expected_version):
        """Assert version as expected"""
        target = VersionPyVersion(_get_full_path(project))
        self.assertEqual(expected_version, str(target), 'Wrong version read')

    def _assert_ci_version_local(self, spec, expected_revision_type, expected_revision):
        target = CiVersion(_echo, spec)
        self._assert_version_pattern(target)
        self._assert_spec(spec, target)
        self.assertEqual(expected_revision_type, target.revision_type, "Wrong revision type")
        self.assertEqual(expected_revision, target.revision, "Wrong revision")

    def _assert_spec(self, spec, target):
        self.assertEqual(spec['major version'], target.major, "Wrong major version")
        self.assertEqual(spec['minor version'], target.minor, "Wrong minor version")
        self.assertEqual(spec['build version'], target.build, "Wrong build version")

    def _assert_version_pattern(self, target):
        print(target)
        self.assertTrue(self.version_patten.match(str(target)), 'Wrong version format')

    def _assert_version(self, target, expected):
        (major, minor, revision, build, revision_type) = expected
        print(target)
        self._assert_version_pattern(target)
        self.assertEqual(major, target.major, "Wrong major version")
        self.assertEqual(minor, target.minor, "Wrong minor version")
        self.assertEqual(revision, target.revision, "Wrong revision")
        self.assertEqual(build, target.build, "Wrong build number")
        self.assertEqual(revision_type, target.revision_type, "Wrong revision type")


if __name__ == '__main__':
    unittest.main()
