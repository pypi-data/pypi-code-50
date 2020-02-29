from run_subprocess import run_list
import os
import unittest


class RunTest(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.dirname(os.path.dirname(__file__)))

    def test_simple(self):
        error, lines = run_list('ls')
        assert error == 0
        assert 'run_subprocess.py' in lines
        assert len(lines) >= 10

    def test_error(self):
        error, lines = run_list('ls foo setup.py bar')
        assert error == 1
        expected = [
            'setup.py',
            'ls: bar: No such file or directory',
            'ls: foo: No such file or directory',
        ]

        assert lines == expected
