# import
## batteries
import os
import sys
import pytest
import logging
from pkg_resources import resource_filename
## application
from traitar import get_external_data

# tests
def test_pfam(tmpdir):
    tmp_dir = str(tmpdir.mkdir('pfam'))
    args = Args(tmp_dir, False)
    get_external_data.download(args)
    assert os.path.exists(os.path.join(tmp_dir, 'Pfam-A.hmm'))
    
