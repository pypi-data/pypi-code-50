import os
import sys


def test_files_there():
    filename = os.path.join(os.path.dirname(__file__), 'systemd')
    print(filename)
    print(os.listdir(filename))
    os.chdir(filename)
    print(f'CWD is: {os.getcwd()}')
    print(sys.prefix)
    filepath = sys.prefix + "/FHmonitor/systemd"
    print(filepath)
