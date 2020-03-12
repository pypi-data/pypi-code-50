#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains Plot Twist hierarchy validator implementation
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import pyblish.api

import tpDcc

import artellapipe


class SetupHierachy(pyblish.api.Action):
    label = 'Setup Hierarchy'
    on = 'failed'

    def process(self, context, plugin):
        if not tpDcc.is_maya():
            self.log.warning('Setup Hierarchy Action is only available in Maya!')
            return False

        from tpDcc.dccs.maya.core import scene

        # Make sure that root group exists
        root_group_name = artellapipe.NamesMgr().solve_name('root_group')
        create_root = context.data.get('create_root', False)
        if create_root:
            tpDcc.Dcc.create_empty_group(root_group_name)
        assert tpDcc.Dcc.object_exists(root_group_name), 'Root group node does not exists in current scene!'

        geo_group_name = artellapipe.NamesMgr().solve_name('geo_group')
        if not geo_group_name.startswith('|'):
            geo_group_name = '|{}'.format(geo_group_name)

        # Make sure that high group exists
        high_group_name = artellapipe.NamesMgr().solve_name('high_group')
        create_high = context.data.get('create_high', False)
        parent_high = context.data.get('parent_high', False)
        create_geo_high = context.data.get('create_high_geo')
        if create_high:
            tpDcc.Dcc.create_empty_group(high_group_name)
            parent_high = True
            create_geo_high = True
        assert tpDcc.Dcc.object_exists(high_group_name), 'High group node does not exists in current scene!'
        if parent_high:
            if create_geo_high:
                tpDcc.Dcc.create_empty_group(geo_group_name, parent=high_group_name)
            tpDcc.Dcc.set_parent(high_group_name, root_group_name)

        # Make sure that proxy group exists
        proxy_group_name = artellapipe.NamesMgr().solve_name('proxy_group')
        create_proxy = context.data.get('create_proxy', False)
        parent_proxy = context.data.get('parent_proxy', False)
        create_geo_proxy = context.data.get('create_proxy_geo')
        if create_proxy:
            tpDcc.Dcc.create_empty_group(proxy_group_name)
            parent_proxy = True
            create_geo_proxy = True
        assert tpDcc.Dcc.object_exists(proxy_group_name), 'Proxy group node does not exists in current scene!'
        if parent_proxy:
            if create_geo_proxy:
                tpDcc.Dcc.create_empty_group(geo_group_name, parent=proxy_group_name)
            tpDcc.Dcc.set_parent(proxy_group_name, root_group_name)

        # Make sure that proxy geometry is in the scene and parented properly
        check_proxy_geo = context.data.get('check_proxy_geo', False)
        if check_proxy_geo:
            proxy_geo_parent = '{}|{}|{}'.format(root_group_name, proxy_group_name, geo_group_name)
            proxy_geo = artellapipe.NamesMgr().solve_name('proxy_geo')
            assert proxy_geo and tpDcc.Dcc.object_exists(
                proxy_geo), 'Proxy geometry "{}" not found in scene!'.format(proxy_geo)
            assert tpDcc.Dcc.object_exists(
                proxy_geo_parent), 'Proxy geo parent "{}" does not exists in scene!'.format(proxy_geo_parent)
            if tpDcc.Dcc.node_parent(proxy_geo) != proxy_geo_parent:
                tpDcc.Dcc.set_parent(proxy_geo, proxy_geo_parent)

        # Parent the rest of nodes located in root to high group
        top_transforms = scene.get_top_dag_nodes(exclude_cameras=True)
        if len(top_transforms) > 1:
            high_geo_parent = '{}|{}|{}'.format(root_group_name, high_group_name, geo_group_name)
            assert tpDcc.Dcc.object_exists(
                high_geo_parent), 'High geo parent "{}" does not exists in scene!'.format(high_geo_parent)
            for top_transform in top_transforms:
                if top_transform == root_group_name:
                    continue
                tpDcc.Dcc.set_parent(top_transform, high_geo_parent)


class ValidatePlotTwistModelingHierarchy(pyblish.api.ContextPlugin):
    """
    Checks if modeling file has a valid hierarchy
    """

    label = 'General - Check Hierarchy'
    order = pyblish.api.ValidatorOrder
    hosts = ['maya']
    optional = False
    actions = [SetupHierachy]

    def process(self, context):
        assert tpDcc.is_maya(), 'Validate Modeling Hierarchy is only available in Maya!'

        from tpDcc.dccs.maya.core import scene

        multiple_roots = False
        create_root = False
        create_high = False
        create_proxy = False
        parent_high = False
        parent_proxy = False
        create_high_geo = False
        create_proxy_geo = False
        check_proxy_geo = False

        top_transforms = scene.get_top_dag_nodes(exclude_cameras=True)
        if len(top_transforms) > 1:
            self.log.warning(
                'Multiple root nodes ({}) found in the scene: {}! Only should be 1 root node (root)'.format(
                    len(top_transforms), top_transforms))
            multiple_roots = True

        root_group_name = artellapipe.NamesMgr().solve_name('root_group')
        if not root_group_name.startswith('|'):
            root_group_name = '|{}'.format(root_group_name)
        if not tpDcc.Dcc.object_exists(root_group_name):
            self.log.warning('Root Group "{}" does not exists in current scene!'.format(root_group_name))
            create_root = True

        geo_group_name = artellapipe.NamesMgr().solve_name('geo_group')

        high_group_name = artellapipe.NamesMgr().solve_name('high_group')
        if not tpDcc.Dcc.object_exists(high_group_name):
            self.log.warning('High Group "{}" does not exists in current scene!'.format(root_group_name))
            create_high = True
        if not create_root and not create_high:
            parent = tpDcc.Dcc.node_parent(high_group_name)
            if parent != root_group_name:
                self.log.warning(
                    'High Group "{}" is not parented to root group "{}"!'.format(high_group_name, root_group_name))
                parent_high = True
        if not create_high:
            high_children = tpDcc.Dcc.list_children(high_group_name, full_path=False, all_hierarchy=False)
            if geo_group_name not in high_children:
                create_high_geo = True

        proxy_group_name = artellapipe.NamesMgr().solve_name('proxy_group')
        if not tpDcc.Dcc.object_exists(proxy_group_name):
            self.log.warning('Root Group "{}" does not exists in current scene!'.format(root_group_name))
            create_proxy = True
        if not create_root and not create_proxy:
            parent = tpDcc.Dcc.node_parent(high_group_name)
            if parent != root_group_name:
                self.log.warning(
                    'Proxy Group "{}" is not parented to root group "{}"!'.format(high_group_name, root_group_name))
                parent_proxy = True
        if not create_proxy:
            proxy_chlidren = tpDcc.Dcc.list_children(proxy_group_name, full_path=False, all_hierarchy=False)
            if geo_group_name not in proxy_chlidren:
                create_proxy_geo = True

        proxy_geo_parent = '{}|{}|{}'.format(root_group_name, proxy_group_name, geo_group_name)
        proxy_geo = artellapipe.NamesMgr().solve_name('proxy_geo')
        if not proxy_geo or not tpDcc.Dcc.object_exists(proxy_geo):
            check_proxy_geo = True
            self.log.warning('Proxy Geometry "{}" does not exists!'.format(proxy_geo))
        else:
            if tpDcc.Dcc.node_parent(proxy_geo) != proxy_geo_parent:
                self.log.warning('Proxy Geometry {} is not parented under "{}"'.format(proxy_geo, proxy_geo_parent))
                check_proxy_geo = True

        context.data['create_root'] = create_root
        context.data['create_high'] = create_high
        context.data['create_proxy'] = create_proxy
        context.data['parent_high'] = parent_high
        context.data['parent_proxy'] = parent_proxy
        context.data['create_high_geo'] = create_high_geo
        context.data['create_proxy_geo'] = create_proxy_geo
        context.data['check_proxy_geo'] = check_proxy_geo

        assert not create_root and not create_high and not create_proxy and not parent_high and not \
            parent_proxy and not create_high_geo and not create_proxy and not multiple_roots and not \
            check_proxy_geo, 'Hierarchy is not valid!'
