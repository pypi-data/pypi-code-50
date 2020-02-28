# import
## batteries
import os
import sys
import pytest
from pkg_resources import resource_filename
## application
from traitar.Commands import phenotype as phenotype_cmd

# test/data dir
data_dir = resource_filename('traitar', 'data')



def test_help(tmpdir):
    args = ['-h']
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        args = phenotype_cmd.ParseArgs(args)
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0

def test_script_help(script_runner):
    ret = script_runner.run('traitar', 'phenotype', '-h')
    assert ret.success

@pytest.mark.script_launch_mode('subprocess')
def test_script_data1(tmpdir, script_runner):
    tmp_dir = str(tmpdir.mkdir('phenotype'))
    sample_data_dir = os.path.join(data_dir, 'sample_data')
    sample_data_file = os.path.join(sample_data_dir, 'samples.txt')
    ret = script_runner.run('traitar', 'phenotype', '--overwrite',
                            'db', sample_data_dir, sample_data_file,
                            'from_genes', tmp_dir)
    assert ret.success

