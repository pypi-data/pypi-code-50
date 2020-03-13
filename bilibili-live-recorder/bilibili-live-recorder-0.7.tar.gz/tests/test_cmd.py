import pytest

from live.param import Fpath
from live.args import Cmd


def test_cmd(mocker):
    mocker.patch('sys.argv')
    my_path = Cmd()

    assert my_path.config_file == Fpath.config_file
    assert my_path.save_dir == Fpath.save_dir
