"""
Pykrete versioning tests base
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

import unittest
import re
import os


def _echo(what, who):
    print(f'CiVersion is reading \'{who}\' and will get \'{what}\'')
    return None if what == 'None' else what


def _get_full_path(project):
    return os.path.join('pykrete', 'tests', 'src', project)


class PykreteVersioningTestCase(unittest.TestCase):
    """Unit tests base for pykrete's versions module
    """
    version_patten = re.compile(r'(\d+\.){3}\d+ (Alpha|Beta|RC|Release)')

    def _assert_version_pattern(self, target):
        print(target)
        self.assertTrue(self.version_patten.match(str(target)), 'Wrong version format')

    @staticmethod
    def _echo(what, who):
        print(f'CiVersion is reading \'{who}\' and will get \'{what}\'')
        return None if what == 'None' else what
