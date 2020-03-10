import sys
import io
import os
import unittest
import subprocess
import extrac


class ExtracTest(unittest.TestCase):

    tmp = sys.stdout
    file_path = f'{os.getcwd()}/test/data/linux-amd64-1.1.0.tar.gz'

    def make_command(self, file_path):
        command = f'tar -xzvf {file_path}'
        print('right command is aaaaaaaaaaaaaaaaaaaa')
        print(command)

    def test_extrac_command_output(self):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(os.getcwd())
        p = subprocess.Popen(self.make_command(
            self.file_path), stdout=subprocess.PIPE, shell=True)
        current_output = p.stdout.read().decode('utf-8')
        out_put = io.StringIO()
        sys.stdout = out_put
        extrac.cli(self.file_path, 0)
        sys.stdout = self.tmp
        self.assertEqual(current_output, out_put)
