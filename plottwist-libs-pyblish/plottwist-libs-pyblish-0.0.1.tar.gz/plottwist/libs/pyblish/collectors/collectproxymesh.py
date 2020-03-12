import pyblish.api

import artellapipe


class CollectPlotTwistProxyMesh(pyblish.api.ContextPlugin):

    label = 'Collect Proxy Mesh'
    order = pyblish.api.CollectorOrder
    hosts = ['maya']

    def process(self, context):

        import maya.cmds as cmds

        project = None
        for name, value in artellapipe.__dict__.items():
            if name == 'project':
                project = value
                break

        assert project, 'Project not found'

        proxy_geo = artellapipe.NamesMgr().solve_name('proxy_geo')
        if proxy_geo and cmds.objExists(proxy_geo):
            node_name = proxy_geo.split('|')[-1].split(':')[-1]
            instance = context.create_instance(node_name, project=project)
            instance.data['icon'] = 'cube'
            instance.data['node'] = proxy_geo
            instance.data['family'] = 'proxy'
