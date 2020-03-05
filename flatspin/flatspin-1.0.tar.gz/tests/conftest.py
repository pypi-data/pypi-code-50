import pytest

# ugh...
from os.path import abspath, join, dirname
import sys
package_path = abspath(dirname(dirname(__file__)))
sys.path.insert(0, package_path)

def pytest_addoption(parser):
    parser.addoption("--opencl-platform", type=int, default=0)
    parser.addoption("--opencl-device", type=int, default=0)

@pytest.fixture(params=[{'use_opencl': False}, {'use_opencl': True}], ids=['default', 'opencl'])
def opencl(request):
    args = request.param
    args['opencl_platform'] = request.config.getoption("--opencl-platform")
    args['opencl_device'] = request.config.getoption("--opencl-device")
    return args
