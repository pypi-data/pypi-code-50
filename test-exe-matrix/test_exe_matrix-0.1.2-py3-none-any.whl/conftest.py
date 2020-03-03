"""pytest magic (hooks)
"""

import os

import yaml

from test_exe_matrix.test_data import ExeTestData
from test_exe_matrix.test_data import ExeTestConfig


def pytest_addoption(parser):
    parser.addoption(
        "--testsuite",
        help="testsuite.yaml file, see example matrix.yaml",
        default="matrix.yaml",
    )


def pytest_report_header(config):
    filename = os.path.abspath(config.option.testsuite)
    config.option.testsuite = filename
    return f"Tests from {filename}"


def pytest_generate_tests(metafunc):
    filename = metafunc.config.option.testsuite
    if "exetest" not in metafunc.fixturenames:
        return

    with open(filename, "rb") as yamlfd:
        testsuite = yaml.load(yamlfd, Loader=yaml.Loader)

    suite_config = ExeTestConfig(metafunc, testsuite.get("config", {}))

    alltests = [ExeTestData(suite_config, data) for data in testsuite["tests"]]

    metafunc.parametrize("exetest", [exetest.pytest_obj for exetest in alltests])
