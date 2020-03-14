import pytest
import os
import delegator
import shutil
import tempfile
import importlib
from pathlib import Path

def test_init(pytestconfig,request,data_path):
    import ryo_iso.cli
    importlib.reload(ryo_iso.cli)
    ryo_iso.cli.cli(['_hash_version'])

    with (data_path/'iso.yml').open('w') as f:
        f.write("""# test config file
image: ubuntu/16.04.6
arch: amd64
variant: desktop
apt:
  install:
    - git
    - python3-pip

pip:
  install:
    - doit
""")

    with (data_path/'.release_version').open('r') as f:
        image_version = f.read()
    assert(image_version == '16.04.6')

    with (data_path/'.hash').open('r') as f:
        image_hash = f.read()
    assert(image_hash == 'e27d13d089a027601099b050fd6080785aae99c1a8eb7848774b8d44f1f679b9')
