# -*- coding: utf-8 -*-

import functools
from spaceone.api.repository.v1 import plugin_pb2
from spaceone.core.pygrpc.message_type import *
from spaceone.repository.model.plugin_model import Plugin
from spaceone.repository.info.repository_info import RepositoryInfo

__all__ = ['PluginInfo', 'PluginsInfo', 'VersionsInfo']

def PluginInfo(plugin_vo, minimal=False):
    info = {
        'domain_id': plugin_vo.domain_id,
        'plugin_id': plugin_vo.plugin_id,
        'name': plugin_vo.name,
        'image': plugin_vo.image,
        'service_type': plugin_vo.service_type,
        'state': plugin_vo.state
    }
    if not minimal:
        info.update({
            'registry_url': plugin_vo.registry_url,
            'project_id': plugin_vo.project_id,
            'tags': change_struct_type(plugin_vo.tags),
            'template': change_struct_type(plugin_vo.template),
            'labels': change_list_value_type(plugin_vo.labels), 
            'created_at': change_timestamp_type(plugin_vo.created_at)
            })
        # WARNING
        # Based on local_plugin or remote_plugin
        # vo has different repository or repository_info field
        if hasattr(plugin_vo, 'repository'):
            info.update({
                'repository_info': RepositoryInfo(plugin_vo.repository, minimal=True)})
        if hasattr(plugin_vo, 'repository_info'):
            info.update({
                'repository_info': RepositoryInfo(plugin_vo.repository_info, minimal=True)})

    return plugin_pb2.PluginInfo(**info)

def PluginsInfo(plugin_vos, total_count):
    results = list(map(functools.partial(PluginInfo), plugin_vos))
    return plugin_pb2.PluginsInfo(results=results, total_count=total_count)

def VersionsInfo(version_list):
    return plugin_pb2.VersionsInfo(version=version_list, total_count=len(version_list))

