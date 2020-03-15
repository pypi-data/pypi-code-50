"""
Pykrete versioning.ci_version tests
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

import unittest
from pykrete.versioning import CiVersion, RevisionType
from .versioning import PykreteVersioningTestCase


class PykreteVersioningCiVersionTestCase(PykreteVersioningTestCase):
    """Unit tests for pykrete's versioning module's CiVersion class
    """
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

    def _assert_ci_version_local(self, spec, expected_revision_type, expected_revision):
        target = CiVersion(self._echo, spec)
        self._assert_version_pattern(target)
        self._assert_spec(spec, target)
        self.assertEqual(expected_revision_type, target.revision_type, "Wrong revision type")
        self.assertEqual(expected_revision, target.revision, "Wrong revision")

    def _assert_spec(self, spec, target):
        self.assertEqual(spec['major version'], target.major, "Wrong major version")
        self.assertEqual(spec['minor version'], target.minor, "Wrong minor version")
        self.assertEqual(spec['build version'], target.build, "Wrong build version")


if __name__ == '__main__':
    unittest.main()
