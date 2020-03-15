"""
Pykrete repo tests
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

import unittest
from pykrete.repo import Git
from .helpers import get_full_path


class PythonRepoTestCase(unittest.TestCase):
    """Unit tests for pykrete's repo module
    """
    def test_get_all_tags(self):
        """Verifies getting all tags from repo
        """
        self._assert_get_tags(lambda git: git.get_all_tags(),
                              ('1.0.0', None), ('1.0.1', 'bug fix'))

    def test_get_tags_from_existing(self):
        """Verifies getting all tags from repo starting from a specific tag
        """
        self._assert_get_tags(lambda git: git.get_tags_from(r'.*?0\.1', True),
                              ('1.0.1', 'bug fix'))

    def test_get_tags_from_must_but_non_existing(self):
        """Verifies getting all tags from repo
        """
        with self.assertRaises(KeyError):
            self._assert_get_tags(lambda git: git.get_tags_from(r'no such tag', True))

    def test_get_tags_from_non_must_non_existing(self):
        """Verifies getting all tags from repo
        """
        self._assert_get_tags(lambda git: git.get_tags_from(r'no such tag', False),
                              None, ('1.0.0', None), ('1.0.1', 'bug fix'))

    def _assert_get_tags(self, getter, *expected):
        """Verifies tags from repo

        :param getter: tag getter (lambda on Git object)
        :param expected: expected returned tags
        :return:
        """
        test_repo_path = get_full_path('git-tag-example', True)
        target = Git(test_repo_path)
        tags = getter(target)
        print(tags)
        self.assertTrue(tags, 'Got empty tags')
        self.assertTrue(len(tags) >= len(expected), 'too few tags returned')
        for test in zip(expected, tags):
            self.assertEqual(test[0], test[1], 'wrong tag returned')


if __name__ == '__main__':
    unittest.main()
