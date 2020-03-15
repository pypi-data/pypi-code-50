import os
import unittest
import subprocess

from python_extrac import extrac


class TestExtrac(unittest.TestCase):

    # tmp = sys.stdout
    file_path = "test/data/linux-amd64-1.1.0.tar.gz"

    def test_extrac_command_output(self):
        os.chdir(os.path.abspath("test/data/"))
        p = subprocess.Popen(
            "tar -zxvf data/linux-amd64-1.1.0.tar.gz",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        file = "linux-amd64-1.1.0"
        subprocess.Popen(f'if [ -d "{file}" ]; then rm -rf {file}; fi', shell=True)
        # current_output = p.stdout.read().decode("utf-8")
        current_output, err = p.communicate()
        print("current output is ::", current_output)
        print("err is ::", err)
        # extrac.cli(self.file_path, 0)
        test_p = subprocess.Popen(
            f"python3 ../python_extrac/extrac.py {file}",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
        )
        cli_out, cli_err = test_p.communicate()
        print(f"cli_out is {cli_out}")
        print(f"cli_err is {cli_err}")
        self.assertEqual(current_output, cli_out)
