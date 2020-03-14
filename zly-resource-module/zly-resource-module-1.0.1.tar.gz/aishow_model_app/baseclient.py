# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import inspect
import json
import logging
import requests
import six
from six.moves.urllib.parse import urljoin

"""
    # >>>from urllib.parse import urljoin
    # >>> urljoin("http://www.chachabei.com/folder/currentpage.html", "anotherpage.html")
    # 'http://www.chachabei.com/folder/anotherpage.html'
    # >>> urljoin("http://www.chachabei.com/folder/currentpage.html", "/anotherpage.html")
    # 'http://www.chachabei.com/anotherpage.html'
    # >>> urljoin("http://www.chachabei.com/folder/currentpage.html", "folder2/anotherpage.html")
    # 'http://www.chachabei.com/folder/folder2/anotherpage.html'
    # >>> urljoin("http://www.chachabei.com/folder/currentpage.html", "/folder2/anotherpage.html")
    # 'http://www.chachabei.com/folder2/anotherpage.html'
    # >>> urljoin("http://www.chachabei.com/abc/folder/currentpage.html", "/folder2/anotherpage.html")
    # 'http://www.chachabei.com/folder2/anotherpage.html'
    # >>> urljoin("http://www.chachabei.com/abc/folder/currentpage.html", "../anotherpage.html")
    # 'http://www.chachabei.com/abc/anotherpage.html'
"""

from aishow_model_app.apis.base import BaseAPI
from aishow_model_app.core.exceptions import DingTalkClientException
from aishow_model_app.core.utils import json_loads
from aishow_model_app.storage.memorystorage import MemoryStorage



logger = logging.getLogger(__name__)

#判断是否是DingTalkBaseAPI的实列对象
def _is_api_endpoint(obj):
    return isinstance(obj, BaseAPI)


class BaseClient(object):

    _http = requests.Session()

    API_BASE_URL = 'http://192.168.0.58:8001/'

    def __new__(cls, *args, **kwargs):
        self = super(BaseClient, cls).__new__(cls)
        api_endpoints = inspect.getmembers(self, _is_api_endpoint)
        for name, api in api_endpoints:
            api_cls = type(api)
            api = api_cls(self)
            setattr(self, name, api)
        return self

    def __init__(self, storage=None, timeout=None, auto_retry=True):
        self.storage = storage or MemoryStorage()
        self.timeout = timeout
        self.auto_retry = auto_retry  #自动重播


    #对request进行封装
    def _request(self, method, url_or_endpoint, **kwargs):
        # 将基础路径和试图函数拼接成完整的访问路劲
        if not url_or_endpoint.startswith(('http://', 'https://')):
            api_base_url = kwargs.pop('api_base_url', self.API_BASE_URL)
            url = urljoin(api_base_url, url_or_endpoint)
        else:
            url = url_or_endpoint

        #判断是否有params参数，
        if 'params' not in kwargs:
            kwargs['params'] = {}
        # 判断是否有data参数，
        if isinstance(kwargs.get('data', ''), dict):
            body = json.dumps(kwargs['data'], ensure_ascii=False)
            body = body.encode('utf-8')
            kwargs['data'] = body
            # 判断是否有headers参数，
            if 'headers' not in kwargs:
                kwargs['headers'] = {}
            kwargs['headers']['Content-Type'] = 'application/json'

        kwargs['timeout'] = kwargs.get('timeout', self.timeout)
        result_processor = kwargs.pop('result_processor', None)    #processor:处理器 ???????????
        top_response_key = kwargs.pop('top_response_key', None)     # ?????????
        #发送requests.Session()的request()请求
        res = self._http.request(
            method=method,
            url=url,
            **kwargs
        )
        #异常处理返回的数剧是否正常
        try:
            res.raise_for_status()
        except requests.RequestException as reqe:
            logger.error("\n【请求地址】: %s\n【请求参数】：%s \n%s\n【异常信息】：%s",
                         url, kwargs.get('params', ''), kwargs.get('data', ''), reqe)

            #返回自定义的DingTalkClientException异常处理类
            raise DingTalkClientException(
                errcode=None,
                errmsg=None,
                client=self,
                request=reqe.request,
                response=reqe.response
            )

        #处理返回的结果
        result = self._handle_result(
            res, method, url, result_processor, top_response_key, **kwargs
        )

        logger.debug("\n【请求地址】: %s\n【请求参数】：%s \n%s\n【响应数据】：%s",
                     url, kwargs.get('params', ''), kwargs.get('data', ''), result)
        return result

    def _decode_result(self, res):
        try:
            result = json_loads(res.content.decode('utf-8', 'ignore'), strict=False)
            # 1、ValueError: Invalid control characterat: line 1 column 8363(char8362)使用json.loads(json_data)时，出现：
            #     ValueError: Invalid control character at: line 1column 8363(char8362)
            # 出现错误的原因是字符串中包含了回车符（\r）或者换行符（\n）
            #     解决方法：
            #     (1)对这些字符转义：json_data = json_data.replace('\r', '\\r').replace('\n', '\\n')
            #     (2)使用关键字strict:json.loads(json_data, strict=False)strict默认是True, 它将严格控制内部字符串，将其设置为False, 便可以允许你\n \r

        except (TypeError, ValueError):
            # Return origin response object if we can not decode it as JSON
            logger.debug('Can not decode response as JSON', exc_info=True)
                # logger.debug('Can not decode response as JSON', exc_info=True)
                # exc_info： 其值为布尔值，如果该参数的值设置为True，则会将异常异常信息添加到日志消息中。如果没有异常信息则添加None到日志信息中。
                # stack_info： 其值也为布尔值，默认值为False。如果该参数的值设置为True，栈信息将会被添加到日志信息中。
                # extra： 这是一个字典（dict）参数，它可以用来自定义消息格式中所包含的字段，但是它的key不能与logging模块定义的字段冲突。
            return res
        return result

    def _handle_result(self, res, method=None, url=None, result_processor=None, top_response_key=None, **kwargs):
        """
       :param res:
       :param method:
       :param url:
       :param result_processor:  结果处理;
       :param top_response_key:
       :param kwargs:
       :return:
       """
        if not isinstance(res, dict):
            # Dirty hack around asyncio based AsyncWeChatClient
            result = self._decode_result(res)
        else:
            result = res

        if not isinstance(result, dict):
            return result

        if top_response_key:
            if 'error_response' in result:
                error_response = result['error_response']
                logger.error("\n【请求地址】: %s\n【请求参数】：%s \n%s\n【错误信息】：%s",
                             url, kwargs.get('params', ''), kwargs.get('data', ''), result)
                raise DingTalkClientException(
                    error_response.get('code', -1),
                    error_response.get('sub_msg', error_response.get('msg', '')),
                    client=self,
                    request=res.request,
                    response=res
                )
            top_result = result
            if top_response_key in top_result:
                top_result = result[top_response_key]
                if 'result' in top_result:
                    top_result = top_result['result']
                    if isinstance(top_result, six.string_types):
                        try:
                            top_result = json_loads(top_result)
                        except Exception:
                            pass
            if isinstance(top_result, dict):
                if ('success' in top_result and not top_result['success']) or (
                        'is_success' in top_result and not top_result['is_success']):
                    logger.error("\n【请求地址】: %s\n【请求参数】：%s \n%s\n【错误信息】：%s",
                                 url, kwargs.get('params', ''), kwargs.get('data', ''), result)
                    raise DingTalkClientException(
                        top_result.get('ding_open_errcode', -1),
                        top_result.get('error_msg', ''),
                        client=self,
                        request=res.request,
                        response=res
                    )
            result = top_result
        if not isinstance(result, dict):
            return result
        if 'errcode' in result:
            result['errcode'] = int(result['errcode'])

        if 'errcode' in result and result['errcode'] != 0:
            errcode = result['errcode']
            errmsg = result.get('errmsg', errcode)

            logger.error("\n【请求地址】: %s\n【请求参数】：%s \n%s\n【错误信息】：%s",
                         url, kwargs.get('params', ''), kwargs.get('data', ''), result)
            raise DingTalkClientException(
                errcode,
                errmsg,
                client=self,
                request=res.request,
                response=res
            )

        return result if not result_processor else result_processor(result)

    def _handle_pre_request(self, method, uri, kwargs):
        return method, uri, kwargs

    def _handle_pre_top_request(self, params, uri):
        if not uri.startswith(('http://', 'https://')):
            uri = urljoin('https://eco.taobao.com', uri)
        return params, uri

    def _handle_request_except(self, e, func, *args, **kwargs):
        raise e

    def request(self, method, uri, **kwargs):
        method, uri_with_access_token, kwargs = self._handle_pre_request(method, uri, kwargs)
        try:
            return self._request(method, uri_with_access_token, **kwargs)
        except DingTalkClientException as e:
            return self._handle_request_except(e, self.request, method, uri, **kwargs)

    def top_request(self, method, params=None, format_='json', v='2.0',
                    simplify='false', partner_id=None, url=None, **kwargs):
        """
        top 接口请求

        :param method: API接口名称。
        :param params: 请求参数 （dict 格式）
        :param format_: 响应格式（默认json，如果使用xml，需要自己对返回结果解析）
        :param v: API协议版本，可选值：2.0。
        :param simplify: 是否采用精简JSON返回格式
        :param partner_id: 合作伙伴身份标识。
        :param url: 请求url，默认为 https://eco.taobao.com/router/rest
        """
        from datetime import datetime

        reqparams = {}
        if params is not None:
            for key, value in params.items():
                reqparams[key] = value if not isinstance(value, (dict, list, tuple)) else json.dumps(value)
        reqparams['method'] = method
        reqparams['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        reqparams['format'] = format_
        reqparams['v'] = v

        if format_ == 'json':
            reqparams['simplify'] = simplify
        if partner_id:
            reqparams['partner_id'] = partner_id
        base_url = url or '/router/rest'

        reqparams, base_url = self._handle_pre_top_request(reqparams, base_url)

        if not base_url.startswith(('http://', 'https://')):
            base_url = urljoin(self.API_BASE_URL, base_url)
        response_key = method.replace('.', '_') + "_response"
        try:
            return self._request('POST', base_url, params=reqparams, top_response_key=response_key, **kwargs)
        except DingTalkClientException as e:
            return self._handle_request_except(e, self.request,
                                               method, format_, v, simplify, partner_id, url, params, **kwargs)

    def get(self, uri, params=None, **kwargs):
        """
        get 接口请求

        :param uri: 请求url
        :param params: get 参数（dict 格式）
        """
        if params is not None:
            kwargs['params'] = params
        # return self._client.get(url=none, kwargs['params']={'select_type':select_type,'page':page,'limit':limit})
        return self.request('GET', uri, **kwargs)

    def post(self, uri, data=None, params=None, **kwargs):
        """
        post 接口请求

        :param uri: 请求url
        :param data: post 数据（dict 格式会自动转换为json）
        :param params: post接口中url问号后参数（dict 格式）
        """
        if data is not None:
            kwargs['data'] = data
        if params is not None:
            kwargs['params'] = params
        return self.request('POST', uri, **kwargs)
