__author__ = 'v.denisov'

import requests
import allure


class RegustsHelper:

    def __init__(self):
        pass

    @allure.step('Execute "GET" request ')
    def get(url, data=None, params=None, headers=None, cookies=None):
        response = None
        try:
            response = requests.request(
                "GET", url, data=data, headers=headers, params=params,
                cookies=cookies, timeout=20,  verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response

    @allure.step('Execute "POST" request ')
    def post(url, data=None, params=None, headers=None, cookies=None, files=None):
        response = None
        try:
            response = requests.request(
                "POST", url, data=data, headers=headers, params=params,
                cookies=cookies, files=files, timeout=20,  verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response

    @allure.step('Execute "DELETE" request ')
    def delete(url, data=None, params=None, headers=None, cookies=None, files=None):
        response = None
        try:
            response = requests.request(
                "DELETE", url, data=data, headers=headers, params=params,
                cookies=cookies, files=files, timeout=20, verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response

    @allure.step('Execute "OPTIONS" request ')
    def options(url, data=None, params=None, headers=None, cookies=None, files=None):
        response = None
        try:
            response = requests.request(
                "OPTIONS", url, data=data, headers=headers, params=params,
                cookies=cookies, files=files, timeout=20, verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response

    @allure.step('Execute "HEAD" request ')
    def head(url, data=None, params=None, headers=None, cookies=None, files=None):
        response = None
        try:
            response = requests.request(
                "HEAD", url, data=data, headers=headers, params=params,
                cookies=cookies, files=files, timeout=20, verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response

    @allure.step('Execute "PUT" request ')
    def put(url, data=None, params=None, headers=None, cookies=None, files=None):
        response = None
        try:
            response = requests.request(
                "PUT", url, data=data, headers=headers, params=params,
                cookies=cookies, files=files, timeout=20, verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response

    @allure.step('Execute "PATCH" request ')
    def patch(url, data=None, params=None, headers=None, cookies=None, files=None):
        response = None
        try:
            response = requests.request(
                "PATCH", url, data=data, headers=headers, params=params,
                cookies=cookies, files=files, timeout=20, verify=False)
        except requests.exceptions.ConnectTimeout:
            print('Oops. Connection timeout occured!')
        except requests.exceptions.ReadTimeout:
            print('Oops. Read timeout occured')
        except requests.exceptions.ConnectionError:
            print('Seems like dns lookup failed..')
        except requests.exceptions.HTTPError as err:
            print('Oops. HTTP Error occured')
            print('Response is: {content}'.format(content=err.response.content))
        else:
            print('Success!')
        return response





