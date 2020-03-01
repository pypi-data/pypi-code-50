""" Integration tests to test the capability of adding EVCs. """


import os
import pytest
from evc_manager import EvcManager
from ...libs.core.cli import CliOptions, create_parser
from ...libs.core.singleton import Singleton


FOLDER = './tests/test_integration/content_files/'
CORRECT_CLI = ['-u', 'admin',
               '-t', 'admin',
               '-p', 'sparc123',
               '-O', 'https://192.168.56.12/oess/',
               '-v', 'info',
               '-q']


def prepare_cli(option, source_file, nni_option, nni_name):
    """ Prepare CLI options adding action and source file """
    source_file = os.path.abspath(FOLDER + source_file)
    cli_options = CORRECT_CLI
    cli_options.append(option)
    cli_options.append('-f')
    cli_options.append(source_file)
    cli_options.append(nni_option)
    cli_options.append(nni_name)
    return cli_options


def start_cli(action, source_file, nni_option, nni_name):
    """ Prepare CLI """
    parser = create_parser()
    args = parser.parse_args(prepare_cli(action, source_file, nni_option, nni_name))
    return CliOptions(parser, args)


def instantiate_cli(filename, nni_option, nni_name):
    """ Instantiate CLI """
    return start_cli('-M', filename, nni_option, nni_name)


def evc_manager(filename, nni_option, nni_name):
    """ Instantiate EvcManager """
    return EvcManager(cli_option=instantiate_cli(filename, nni_option, nni_name))


@pytest.mark.skip
def test_move_out_evc_example01_with_success():
    """ Move out of NNI Ampath1-Ampath2 """
    Singleton._instances.clear()
    evc_mgr = evc_manager("move_out_evc_correct_request_example01.yaml",
                          "--move-from-nni",
                          "Ampath1-Ampath2")
    results = evc_mgr.move_evcs()
    print(results)

    # Result: No backup
    if 'attention_required' in results and results['attention_required']:
        if not results['results']['msgs'][0]['msg'].find("No changes made."):
            raise ValueError(results['results']['msgs'])
    assert 1


@pytest.mark.skip
def test_move_out_evc_example02_with_success():
    """ Move out of NNI Ampath1-Ampath3 """
    Singleton._instances.clear()
    evc_mgr = evc_manager("move_out_evc_correct_request_example02.yaml",
                          "--move-from-nni",
                          "Ampath1-Ampath3")
    results = evc_mgr.move_evcs()
    print(results)
    # Result: no change
    if 'attention_required' in results and results['attention_required']:
        if not results['results']['msgs'][0]['msg'].find("No available path."):
            raise ValueError(results['results']['msgs'])
    assert 1


@pytest.mark.skip
def test_move_out_evc_example03_with_success():
    """ Move out of NNI Ampath1-Sax """
    Singleton._instances.clear()
    evc_mgr = evc_manager("move_out_evc_correct_request_example03.yaml",
                          "--move-from-nni",
                          "Ampath1-Sax")
    results = evc_mgr.move_evcs()
    print(results)
    # Result: change primary, no backup
    if 'attention_required' in results and results['attention_required']:
        raise ValueError(results['results']['msgs'])
    assert 1


@pytest.mark.skip
def test_move_out_evc_example04_with_success():
    """ Move out of NNI Ampath1-Ampath2 """
    Singleton._instances.clear()
    evc_mgr = evc_manager("move_out_evc_correct_request_example04.yaml",
                          "--move-from-nni",
                          "Ampath1-Ampath2")
    results = evc_mgr.move_evcs()
    print(results)
    # Result: change primary and backup
    if 'attention_required' in results and results['attention_required']:
        raise ValueError(results['results']['msgs'])
    assert 1
