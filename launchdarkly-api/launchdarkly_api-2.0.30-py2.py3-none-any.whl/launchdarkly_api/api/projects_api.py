# coding: utf-8

"""
    LaunchDarkly REST API

    Build custom integrations with the LaunchDarkly REST API  # noqa: E501

    OpenAPI spec version: 2.0.30
    Contact: support@launchdarkly.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from launchdarkly_api.api_client import ApiClient


class ProjectsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_project(self, project_key, **kwargs):  # noqa: E501
        """Delete a project by key. Caution-- deleting a project will delete all associated environments and feature flags. You cannot delete the last project in an account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project(project_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_project_with_http_info(project_key, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_project_with_http_info(project_key, **kwargs)  # noqa: E501
            return data

    def delete_project_with_http_info(self, project_key, **kwargs):  # noqa: E501
        """Delete a project by key. Caution-- deleting a project will delete all associated environments and feature flags. You cannot delete the last project in an account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_project_with_http_info(project_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `delete_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectKey}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_project(self, project_key, **kwargs):  # noqa: E501
        """Fetch a single project by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project(project_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_project_with_http_info(project_key, **kwargs)  # noqa: E501
        else:
            (data) = self.get_project_with_http_info(project_key, **kwargs)  # noqa: E501
            return data

    def get_project_with_http_info(self, project_key, **kwargs):  # noqa: E501
        """Fetch a single project by key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_project_with_http_info(project_key, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `get_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectKey}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Project',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_projects(self, **kwargs):  # noqa: E501
        """Returns a list of all projects in the account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_projects(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Projects
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_projects_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_projects_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_projects_with_http_info(self, **kwargs):  # noqa: E501
        """Returns a list of all projects in the account.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_projects_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: Projects
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_projects" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Projects',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_project(self, project_key, patch_delta, **kwargs):  # noqa: E501
        """Modify a project by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_project(project_key, patch_delta, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.patch_project_with_http_info(project_key, patch_delta, **kwargs)  # noqa: E501
        else:
            (data) = self.patch_project_with_http_info(project_key, patch_delta, **kwargs)  # noqa: E501
            return data

    def patch_project_with_http_info(self, project_key, patch_delta, **kwargs):  # noqa: E501
        """Modify a project by ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_project_with_http_info(project_key, patch_delta, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str project_key: The project key, used to tie the flags together under one project so they can be managed together. (required)
        :param list[PatchOperation] patch_delta: Requires a JSON Patch representation of the desired changes to the project. 'http://jsonpatch.com/' (required)
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_key', 'patch_delta']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_key' is set
        if ('project_key' not in params or
                params['project_key'] is None):
            raise ValueError("Missing the required parameter `project_key` when calling `patch_project`")  # noqa: E501
        # verify the required parameter 'patch_delta' is set
        if ('patch_delta' not in params or
                params['patch_delta'] is None):
            raise ValueError("Missing the required parameter `patch_delta` when calling `patch_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'project_key' in params:
            path_params['projectKey'] = params['project_key']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'patch_delta' in params:
            body_params = params['patch_delta']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects/{projectKey}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Project',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_project(self, project_body, **kwargs):  # noqa: E501
        """Create a new project with the given key and name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_project(project_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectBody project_body: Project keys must be unique within an account. (required)
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_project_with_http_info(project_body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_project_with_http_info(project_body, **kwargs)  # noqa: E501
            return data

    def post_project_with_http_info(self, project_body, **kwargs):  # noqa: E501
        """Create a new project with the given key and name.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_project_with_http_info(project_body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ProjectBody project_body: Project keys must be unique within an account. (required)
        :return: Project
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['project_body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_project" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'project_body' is set
        if ('project_body' not in params or
                params['project_body'] is None):
            raise ValueError("Missing the required parameter `project_body` when calling `post_project`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'project_body' in params:
            body_params = params['project_body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Token']  # noqa: E501

        return self.api_client.call_api(
            '/projects', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Project',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
