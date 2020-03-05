import allure
from ptst_swagger.config_host import ConfigHost as config
from ptst_swagger.client import SwaggerClient as client

@allure.title(" Тестируем ")
def test_t1():
    r = config.get_swagger_json(url='http://test.rais.d-net.pro:8080/bin/swagger/openapi.json')
    print('r=', r.json())
    r_path = client.get_paths_sw()
    print('r_path=', r_path)

@allure.title(" Тестируем ")
def test_t2():
    r = config.get_swagger_json(url='https://petstore.swagger.io/v2/swagger.json')
    print('r=', r.json())