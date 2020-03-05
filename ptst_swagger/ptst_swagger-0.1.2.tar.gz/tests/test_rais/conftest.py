__author__ = 'v.denisov'

import pytest
from ptst_swagger.config_host import ConfigHost as config
from ptst_swagger.client import SwaggerClient as client
from tests.test_rais.conftest2 import conftest2

@pytest.fixture()
def rais():
    config.get_swagger_json(url='http://test.rais.d-net.pro:8080/bin/swagger/openapi.json')
    config.url_host = "http://rais.dev.d-net.pro"
    conftest2()
    client.inn_record_test()
    return client