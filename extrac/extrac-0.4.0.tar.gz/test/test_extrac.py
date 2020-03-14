import sys
import io
import os
import unittest
import subprocess
from python_extrac import extrac


class TestExtrac(unittest.TestCase):

    # tmp = sys.stdout
    file_path = "linux-amd64-1.1.0.tar.gz"

    def make_command(self, file_path):
        return f"tar -zxvf {file_path}"

    def test_extrac_command_output(self):
        os.chdir(os.path.abspath("test/data/"))
        p = subprocess.Popen(
            "tar -zxvf linux-amd64-1.1.0.tar.gz",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        # current_output = p.stdout.read().decode("utf-8")
        current_output, err = p.communicate()
        print("current output is ::", current_output)
        print("err is ::", err)
        tmp = sys.stdout
        out_put = io.StringIO()
        sys.stdout = out_put
        extrac.cli(self.file_path, 0)
        # print(out_put)
        cli_out = out_put.read().decode("utf-8")
        print(cli_out)
        sys.stdout = tmp
        self.assertEqual(current_output, cli_out)
