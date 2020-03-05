import allure
#from ptst_swagger.client import SwaggerClient

@allure.title(" Тестируем  test_t2")
# @SwaggerClient.record_test("GET", '/test', '1')
def test_t2(rais):
    rais.record_test("GET", '/system/health', 1)
    rais.record_test("POST", '/v1/file', 1)
    rais.record_test("POST", '/v1/file', '1')
    rais.record_test("GET", '/v1/file/{id}/permission', '1')
    r = rais.get_paths_sw()
    for rx in r:
        print('rx=', rx)
    print('r=', r)
    r2 = rais.get()
    print('r2=', r2.cookies)
    response_user = rais.get(paths='/interface/orange/user/get')
    print('response_user=', response_user.cookies, response_user.json())

    payload = {'login': 'test@id-network.ru',
               'password': 'TestPassword'}
    headers = {
        'x-project-name': 'rais_lkp'
    }
    url = 'https://lkp.hypergraph.dev.k8s.id-network.ru'
    paths = '/golkp/api/auth/login'
    response = rais.post(url=url, paths=paths, data=payload, headers=headers)
    print("login_cooke=", response.cookies, response.json())
