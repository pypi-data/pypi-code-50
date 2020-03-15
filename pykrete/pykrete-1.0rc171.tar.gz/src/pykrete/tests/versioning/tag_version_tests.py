"""
Pykrete versioning.tag_version tests
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

import unittest
from pykrete.versioning import TagVersion, RevisionType, Version, Bumper
from .versioning import PykreteVersioningTestCase


class PykreteVersioningTagVersionTestCase(PykreteVersioningTestCase):
    """Unit tests for pykrete's versioning module's TagVersion class
    """
    __tags = []

    def test_tag_version_server(self):
        """Verifies handling of CI-environment version
        NOTE: THIS TEST WILL FAIL LOCALLY, SAFE TO IGNORE
        """
        print('NOTE: THIS TEST WILL FAIL LOCALLY, SAFE TO IGNORE')
        self._assert_version_pattern(TagVersion())

    def test_tag_version_local_alpha_no_tags(self):
        """Verifies handling of no simulated tags present"""
        self._assert_ci_version_local(
            spec={'build version': '3',
                  'branch name': 'custom',
                  'merge request title': 'None'}, tags=[None],
            expected_version=Version((0, 0, 1, 3, RevisionType.Alpha)))

    def test_tag_version_local_alpha_first_minor_bump(self):
        """Verifies handling of simulated minor bump without a previous release"""
        self._assert_ci_version_local(
            spec={'build version': '4',
                  'branch name': 'custom',
                  'merge request title': 'None'},
            tags=[None, ('bump_minor', None)],
            expected_version=Version((0, 1, 1, 0, RevisionType.Alpha)))

    def test_tag_version_local_beta_major_bump(self):
        """Verifies handling of simulated major bump after a previous release"""
        self._assert_ci_version_local(
            spec={'build version': '111',
                  'branch name': 'custom',
                  'merge request title': 'WIP: something'},
            tags=[('0.7.56', 'ci_base_build 106'), ('bump_major', None)],
            expected_version=Version((1, 0, 2, 0, RevisionType.Beta)))

    def test_tag_version_local_rc_disabled_bump(self):
        """Verifies handling of simulated minor after major bump after a previous release
        where only the major bump should be used
        """
        self._assert_ci_version_local(
            spec={'build version': '1234',
                  'branch name': 'custom',
                  'merge request title': 'something'},
            tags=[('1.2.34', 'ci_base_build 1198'), ('bump_major', None), ('bump_minor', None)],
            expected_version=Version((1, 2, 3, 36, RevisionType.RC)),
            bump=False)

    def test_tag_version_local_rc_two_minor_bumps(self):
        """Verifies handling of simulated two minor bumps after a previous release
        where only one minor bump should be used
        """
        self._assert_ci_version_local(
            spec={'build version': '12345',
                  'branch name': 'custom',
                  'merge request title': 'something'},
            tags=[('11.22.341', 'ci_base_build 12338'), ('bump_minor', None), ('bump_minor', None)],
            expected_version=Version((11, 23, 3, 0, RevisionType.RC)))

    def test_tag_version_local_release_two_major_bumps(self):
        """Verifies handling of simulated two major bumps after a previous release
        where only one major bump should be used
        """
        self._assert_ci_version_local(
            spec={'build version': '88888',
                  'branch name': 'master',
                  'merge request title': 'blaster'},
            tags=[('7.7.77', 'ci_base_build 88880'), ('bump_major', None), ('bump_major', None)],
            expected_version=Version((8, 0, 4, 0, RevisionType.Release)))

    def _assert_ci_version_local(self, spec, tags, expected_version, bump=True):
        self.__tags = tags
        target = TagVersion(self._reader, Bumper.major_minor_tag if bump else Bumper.disabled,
                            self._echo, spec)
        print(target)
        self._assert_version_pattern(target)
        self.assertEqual(expected_version, target,
                         f'version not as expected: should be {expected_version}')

    def _reader(self, pattern, is_must):
        if is_must:
            raise AssertionError('tags are fetched with is_must=True')
        if not pattern:
            raise AssertionError('no pattern was provider for fetching tags')
        return self.__tags


if __name__ == '__main__':
    unittest.main()
