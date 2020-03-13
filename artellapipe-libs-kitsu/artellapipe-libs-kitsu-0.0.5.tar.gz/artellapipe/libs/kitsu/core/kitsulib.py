#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility module that contains useful utilities and classes related with Kitsu
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import logging
import traceback

import gazu

from artellapipe.libs.kitsu.core import kitsuclasses

LOGGER = logging.getLogger()


def set_host(new_host):
    """
    Sets current configured host on which requests are sent
    :param new_host: variant, str or None
    """

    gazu.set_host(new_host)


def host_is_up():
    """
    Returns whether host is up or not
    :return: bool
    """

    try:
        return gazu.client.host_is_up()
    except Exception as exc:
        LOGGER.warning('Kitsu server is not available: {} | {}'.format(exc, traceback.format_exc()))

    return False


def log_in(email, password):
    """
    Login to Kitsu with given email and password
    :param email: str
    :param password: str
    :return:
    """

    if not email or not password:
        return False

    return gazu.log_in(email, password)


def get_project(project_id, as_dict=False):
    """
    Returns project with the given ID
    :param project_id: str
    :return: dict or KitsuProject
    """

    kitsu_project = gazu.project.get_project(project_id)
    if not kitsu_project:
        return None

    if as_dict:
        return kitsu_project

    return kitsuclasses.KitsuProject(kitsu_project)


def get_current_user(as_dict=False):
    """
    Returns user database information for user linked to auth tokens
    :param as_dict: bool
    :return: variant, dict or KitsuUserInfo
    """

    user_data = gazu.client.get_current_user()
    if as_dict:
        return user_data

    return kitsuclasses.KitsuUserInfo(user_data)


def all_assets_for_project(project_id, as_list=False):
    """
    Returns a list with all assets in the given project
    :param project_id: str
    :param as_list: bool
    :return: variant, dict or list
    """

    if type(project_id) != dict:
        project_id = {'id': project_id}

    assets_list = gazu.asset.all_assets_for_project(project_id)
    if as_list:
        return assets_list

    return [kitsuclasses.KitsuAsset(asset) for asset in assets_list]


def all_asset_types_for_project(project_id, as_dict=False):
    """
    Returns asset types from assets listed in the given project
    :param project_id: variant, str or dict
    :param as_dict: bool, Whether to return data as dict or as Kitsu class
    :return: variant, list(dict) or list(KitsuAssetType)
    """

    if type(project_id) != dict:
        project_id = {'id': project_id}

    asset_types = gazu.asset.all_asset_types_for_project(project_id)
    if as_dict:
        return asset_types

    return [kitsuclasses.KitsuAssetType(asset_type) for asset_type in asset_types]


def download_preview_file_thumbnail(preview_id, file_path):
    """
    Downloads given preview file thumbnail and save it at given location
    :param preview_id:  str or dict, The preview file dict or ID.
    :param target_path: str, Location on ahrd drive where to save the file.
    """

    if type(preview_id) != dict:
        preview_id = {'id': preview_id}

    gazu.files.download_preview_file_thumbnail(preview_id, file_path)


def get_project_entity_types():
    """
    Returns all entity types in the project
    :return: list
    """

    return gazu.client.fetch_one('entity-types', '')


def get_all_sequences(project_id, as_dict=False):
    """
    Returns all sequences for the given project
    :param project_id: variant, str or dict
    :param as_dict: bool, Whether to return data as dict or as Kitsu class
    :return: list(dict) or list(KitsuSequence)
    """

    if type(project_id) != dict:
        project_id = {'id': project_id}

    sequences = gazu.shot.all_sequences_for_project(project_id)

    if as_dict:
        return sequences

    return [kitsuclasses.KitsuSequence(sequence) for sequence in sequences]


def get_all_shots(project_id, as_dict=False):
    """
    Returns all shots for the given project
    :param project_id: variant, str or dict
    :param as_dict: bool, Whether to return data as dict or as Kitsu class
    :return: list(dict) or list(KitsuShot)
    """

    if type(project_id) != dict:
        project_id = {'id': project_id}

    shots = gazu.shot.all_shots_for_project(project_id)

    if as_dict:
        return shots

    return [kitsuclasses.KitsuShot(shot) for shot in shots]


def get_shot_sequence(shot_dict, as_dict=False):
    """
    Returns sequence given shot belongs to
    :param shot_dict:
    :param as_dict:  bool, Whether to return data as dict or as Kitsu class
    :return:
    """

    if 'parent_id' not in shot_dict:
        LOGGER.warning('Impossible to retrieve sequence from shot!')
        return None

    shot = gazu.shot.get_sequence_from_shot(shot_dict)

    if as_dict:
        return shot

    return kitsuclasses.KitsuSequence(shot)


def get_all_assets_in_shot(shot_id, as_dict=False):
    """
    Returns all assets in given shot (defined in breakdown)
    :param shot_id: str
    :param as_dict: bool
    :return:
    """

    shot_assets = gazu.asset.all_assets_for_shot(shot_id)

    if as_dict:
        return shot_assets

    return [kitsuclasses.KitsuAsset(asset) for asset in shot_assets]


def get_shot_casting(project_id, shot_id):
    """
    Returns casting (breakdown data) of the given shot
    :param shot_id: str
    :return: dict
    """

    cast_dict = {
        'project_id': project_id,
        'id': shot_id
    }

    return gazu.casting.get_shot_casting(cast_dict)


def get_task(task_id, as_dict):
    """
    Returns task with given id in current project
    :param task_id: str
    :param as_dict: bool
    :return: dict or KitsuTask
    """

    kitsu_task = gazu.task.get_task(task_id)
    if as_dict:
        return kitsu_task

    return kitsuclasses.KitsuTask(kitsu_task)


def get_all_tasks_for_shot(shot_id, as_dict=False):
    """
    Returns all tasks in given shot
    :param shot_id: str
    :param as_dict: bool
    :return:
    """

    all_tasks = gazu.task.all_tasks_for_shot(shot_id)

    if as_dict:
        return all_tasks

    return [kitsuclasses.KitsuTask(task) for task in all_tasks]


def get_all_task_types(as_dict=False):
    """
    Returns all task types in current project
    :param as_dict: dict
    :return: list
    """

    all_task_types = gazu.task.all_task_types()

    if as_dict:
        return all_task_types

    return [kitsuclasses.KitsuTaskType(task_type) for task_type in all_task_types]


def get_task_status(task_id, as_dict=False):
    """
    Returns status of the given task id
    :param task_id: str
    :param as_dict: bool
    :return: dict or KitsuTaskStatus
    """

    kitsu_task = get_task(task_id, as_dict=True)
    if not kitsu_task:
        return

    task_status = gazu.task.get_task_status(kitsu_task)
    if as_dict:
        return task_status

    return kitsuclasses.KitsuTaskStatus(task_status)


def upload_shot_task_preview(task_id, preview_file_path, comment):
    """
    Uploads shot task to Kitsu server
    :param task_id: st
    :param preview_file_path: str
    :param comment: str
    :return:
    """

    if not comment:
        comment = {'id': ''}

    return gazu.task.add_preview(task_id, comment, preview_file_path)
