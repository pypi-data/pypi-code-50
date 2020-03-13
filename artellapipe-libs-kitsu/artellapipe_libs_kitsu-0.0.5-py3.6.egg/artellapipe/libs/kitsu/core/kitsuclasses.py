#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains implementation for Kitsu data objects to work with a more OO approach
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

import artellapipe.libs.kitsu as kitsu_lib


class KitsuProject(object):
    def __init__(self, data):
        super(KitsuProject, self).__init__()

        self._dict = data
        self._id = data.get('id', None)
        self._name = data.get('name', None)
        self._created_at = data.get('created_at', None)
        self._data = data.get('data', None)
        self._end_date = data.get('end_date', None)
        self._file_tree = data.get('file_tree', None)
        self._fps = data.get('fps', 24)
        self._file_tree = data.get('file_tree', None)
        self._has_avatar = data.get('has_avatar', False)
        self._man_days = data.get('man_days', None)
        self._production_type = data.get('production_type', None)
        self._project_status_id = data.get('project_status_id', None)
        self._project_status_name = data.get('project_status_name', None)
        self._ratio = data.get('ratio', None)
        self._resolution = data.get('resolution', None)
        self._shotgun_id = data.get('shotgun_id', None)
        self._start_date = data.get('start_date', None)
        self._team = data.get('team', list())
        self._type = data.get('type', None)
        self._updated_at = data.get('updated_at', None)

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    @property
    def fps(self):
        return self._fps

    @property
    def resolution(self):
        return self._resolution


class KitsuUserInfo(object):
    def __init__(self, data):
        super(KitsuUserInfo, self).__init__()

        self._dict = data
        self._first_name = data.get('first_name', '')
        self._last_name = data.get('last_name', '')
        self._has_avatar = data.get('has_avatar', False)
        self._locale = data.get('locale', '')
        self._last_presence = data.get('last_presence', None)
        self._created_at = data.get('created_at', '')
        self._notifications_enabled = data.get('notifications_enabled', None)
        self._shotgun_id = data.get('shotgun_id', None)
        self._updated_at = data.get('updated_at', '')
        self._email = data.get('email', '')
        self._phone = data.get('phone', '')
        self._role = data.get('role', '')
        self._data = data.get('data', None)
        self._full_name = data.get('full_name', '')
        self._timezone = data.get('timezone', '')
        self._active = data.get('active', False)
        self._skills = data.get('skills', list())
        self._desktop_login = data.get('desktop_login', '')
        self._type = data.get('type', '')
        self._id = data.get('id', '')

    @property
    def first_name(self):
        """
        Returns first name of the user
        :return: str
        """

        return self._first_name

    @property
    def last_name(self):
        """
        Returns last name of the user
        :return: str
        """

        return self._last_name

    @property
    def locale(self):
        """
        Returns locale of the user
        :return: str
        """

        return self._locale

    @property
    def full_name(self):
        """
        Returns full name of the user
        :return: str
        """

        return self._full_name

    @property
    def email(self):
        """
        Returns the email of the user
        :return: str
        """

        return self._email

    @property
    def role(self):
        """
        Returns the role of the user
        :return: str
        """

        return self._role

    @property
    def timezone(self):
        """
        Returns time zone of the user
        :return: str
        """

        return self._timezone


class KitsuAsset(object):
    def __init__(self, data):
        super(KitsuAsset, self).__init__()

        self._dict = data

        self._name = data.get('name', '')
        self._id = data.get('id', '')
        self._type = data.get('type', None)
        self._entity_type_id = data.get('entity_type_id', '')
        self._code = data.get('code', None)
        self._description = data.get('description', '')
        self._canceled = data.get('canceled', False)
        self._preview_file_id = data.get('preview_file_id', None)
        self._created_at = data.get('created_at', '')
        self._instance_casting = data.get('instance_casting', list())
        self._shotgun_id = data.get('shotgun_id', None)
        self._updated_at = data.get('updated_at', '')
        self._data = data.get('data', dict())
        self._parent_id = data.get('parent_id', None)
        self._source_id = data.get('source_id', None)
        self._entities_in = data.get('entities_in', list())
        self._project_id = data.get('project_id', '')
        self._entities_out = data.get('entities_out', list())
        self._number_frames = data.get('nb_frames', None)

    @property
    def name(self):
        """
        Returns asset name
        :return: str
        """

        return self._name

    @property
    def id(self):
        """
        Returns asset id
        :return: str
        """

        return self._id

    @property
    def type(self):
        """
        Returns asset type
        :return: str
        """

        return self._type

    @property
    def entity_type_id(self):
        """
        Returns asset entity type id
        :return: str
        """

        return self._entity_type_id

    @property
    def preview_file_id(self):
        """
        Returns asset preview file id
        :return: str
        """

        return self._preview_file_id

    @property
    def data(self):
        """
        Returns extra metadata attributes associated to this asset
        :return: dict
        """

        return self._data

    @property
    def canceled(self):
        """
        Returns whether the asset has been cancelled or not
        :return: bool
        """

        return self._canceled

    def get_data(self):
        """
        Returns data of the asset
        :return: dict
        """

        asset_id = self.id
        custom_id_attr = kitsu_lib.config.get('custom_id_attribute', default=None)
        if custom_id_attr:
            asset_metadata = self.data or dict()
            asset_id = asset_metadata.get(custom_id_attr, asset_id)

        return {
            'asset': self,
            'name': self.name,
            'thumb': self.preview_file_id,
            'id': asset_id
        }


class KitsuAssetType(object):
    def __init__(self, data):
        super(KitsuAssetType, self).__init__()

        self._dict = data

        self._name = data.get('name', '')
        self._id = data.get('id', '')
        self._type = data.get('type', '')
        self._created_at = data.get('created_at', '')
        self._updated_at = data.get('updated_at')

    @property
    def name(self):
        """
        Returns asset type name
        :return: str
        """

        return self._name

    @property
    def id(self):
        """
        Returns asset type id
        :return: str
        """

        return self._id

    @property
    def type(self):
        """
        Returns asset Kitsu type
        :return: str
        """

        return self._type

    @property
    def created_at(self):
        """
        Returns data where the asset type was created
        :return: str
        """

        return self._created_at

    @property
    def updated_at(self):
        """
        Returns last date when the asset type was updated
        :return: str
        """

        return self._updated_at


class KitsuEntityType(object):
    def __init__(self, data):
        super(KitsuEntityType, self).__init__()

        self._dict = data

        self._id = data.get('id', '')
        self._name = data.get('name', '')
        self._type = data.get('type', '')
        self._created_at = data.get('created_at', '')
        self._updated_at = data.get('updated_at', '')

    @property
    def id(self):
        """
        Returns entity type id
        :return: str
        """

        return self._id

    @property
    def name(self):
        """
        Returns entity type name
        :return: str
        """

        return self._name

    @property
    def type(self):
        """
        Returns entity type type
        :return: str
        """

        return self._type

    @property
    def created_at(self):
        """
        Returns created date of the entity type
        :return: str
        """

        return self._created_at

    @property
    def updated_at(self):
        """
        Returns last update date of the entity type
        :return: str
        """

        return self._updated_at


class KitsuSequence(object):
    def __init__(self, data):
        super(KitsuSequence, self).__init__()

        self._dict = data

        self._id = data.get('id', None)
        self._number_of_frames = data.get('nb_frames', None)
        self._description = data.get('description', None)
        self._entity_type_id = data.get('entity_type_id', None)
        self._code = data.get('code', None)
        self._name = data.get('name', '')
        self._instance_casting = data.get('instance_casting', list())
        self._preview_file_id = data.get('preview_file_id', None)
        self._data = data.get('data', None)
        self._created_at = data.get('created_at', '')
        self._shotgun_id = data.get('shotgun_id', None)
        self._updated_at = data.get('upadted_at', '')
        self._entities_out = data.get('entities_out', list())
        self._entities_in = data.get('entities_in', list())
        self._canceled = data.get('canceled', False)
        self._parent_id = data.get('parent_id', None)
        self._source_id = data.get('source_id', None)
        self._project_id = data.get('project_id', None)
        self._type = data.get('type', None)

    @property
    def name(self):
        """
        Returns the name of the sequence
        :return: str
        """

        return self._name

    @property
    def id(self):
        """
        Returns sequence ID
        :return: str
        """

        return self._id

    @property
    def type(self):
        """
        Returns sequence type
        :return: str
        """

        return self._type

    @property
    def entity_type_id(self):
        """
        Returns sequence entity type id
        :return: str
        """

        return self._entity_type_id

    @property
    def number_of_frames(self):
        """
        Returns the number of frames of the shot
        :return: int
        """

        return self._number_of_frames

    @property
    def description(self):
        """
        Returns sequence description
        :return: str
        """

        return self._description

    @property
    def preview_file_id(self):
        """
        Returns asset preview file id
        :return: str
        """

        return self._preview_file_id

    @property
    def canceled(self):
        """
        Returns whether the asset has been cancelled or not
        :return: bool
        """

        return self._canceled


class KitsuShot(object):
    def __init__(self, data):
        super(KitsuShot, self).__init__()

        self._dict = data

        self._id = data.get('id', None)
        self._number_of_frames = data.get('nb_frames', None)
        self._description = data.get('description', None)
        self._entity_type_id = data.get('entity_type_id', None)
        self._code = data.get('code', None)
        self._name = data.get('name', '')
        self._preview_file_id = data.get('preview_file_id', None)
        self._data = data.get('data', None)
        self._created_at = data.get('created_at', '')
        self._shotgun_id = data.get('shotgun_id', None)
        self._updated_at = data.get('upadted_at', '')
        self._canceled = data.get('canceled', False)
        self._parent_id = data.get('parent_id', None)
        self._source_id = data.get('source_id', None)
        self._project_id = data.get('project_id', None)
        self._type = data.get('type', None)

    @property
    def name(self):
        """
        Returns the name of the shot
        :return: str
        """

        return self._name

    @property
    def id(self):
        """
        Returns shot ID
        :return: str
        """

        return self._id

    @property
    def parent_id(self):
        """
        Returns shot parent ID (ID of the sequence this shot belongs to)
        :return:
        """

        return self._parent_id

    @property
    def type(self):
        """
        Returns shot type
        :return: str
        """

        return self._type

    @property
    def entity_type_id(self):
        """
        Returns shot entity type id
        :return: str
        """

        return self._entity_type_id

    @property
    def number_of_frames(self):
        """
        Returns the number of frames of the shot
        :return: int
        """

        return self._number_of_frames

    @property
    def description(self):
        """
        Returns shot description
        :return: str
        """

        return self._description

    @property
    def preview_file_id(self):
        """
        Returns shot preview file id
        :return: str
        """

        return self._preview_file_id

    def to_dict(self):
        """
        Returns dict data of the shot
        :return: dict
        """

        return self._dict


class KitsuTaskType(object):
    def __init__(self, data):
        super(KitsuTaskType, self).__init__()

        self._dict = data

        self._id = data.get('id', None)
        self._name = data.get('name', None)
        self._short_name = data.get('short_name', None)
        self._type = data.get('type', None)
        self._color = data.get('color', None)
        self._created_at = data.get('created_at', None)
        self._department_id = data.get('department_id', None)
        self._for_entity = data.get('for_entity', None)
        self._for_shots = data.get('for_shots', True)
        self._priority = data.get('priority', 0)
        self._update_at = data.get('updated_at', None)
        self._allow_timelog = data.get('allow_timelog', False)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def for_shots(self):
        return self._for_shots

    @property
    def for_entity(self):
        return self._for_entity


class KitsuTaskStatus(object):
    def __init__(self, data):
        super(KitsuTaskStatus, self).__init__()

        self._dict = data

        self._id = data.get('id', None)
        self._name = data.get('name', None)
        self._short_name = data.get('short_name', None)
        self._type = data.get('type', None)
        self._create_at = data.get('created_at', None)
        self._is_artist_allowed = data.get('is_artist_allowed', False)
        self._is_client_allowed = data.get('is_client_allowed', False)
        self._is_done = data.get('is_done', False)
        self._is_retake = data.get('is_retake', False)
        self._is_reviewable = data.get('is_reviewable', False)
        self._shotgun_id = data.get('shotgun_id', None)
        self._updated_at = data.get('updated_at', None)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def short_name(self):
        return self._short_name


class KitsuTask(object):
    def __init__(self, data):
        super(KitsuTask, self).__init__()

        self._dict = data

        self._id = data.get('id', None)
        self._assigner_id = data.get('assigner_id', None)
        self._completion_rate = data.get('completion_rate', 0)
        self._data = data.get('data', None)
        self._description = data.get('description', None)
        self._due_date = data.get('due_date', None)
        self._duration = data.get('duration', 0)
        self._end_data = data.get('end_date', None)
        self._entity_id = data.get('entity_id', None)
        self._entity_name = data.get('entity_name', None)
        self._entity_type_name = data.get('entity_type_name', None)
        self._estimation = data.get('estimation', 0)
        self._last_comment_date = data.get('last_comment_date', None)
        self._name = data.get('name', None)
        self._priority = data.get('priority', 0)
        self._project_id = data.get('project_id', None)
        self._project_name = data.get('project_name', None)
        self._real_start_date = data.get('real_start_date', None)
        self._retake_count = data.get('retake_count', 0)
        self._sort_order = data.get('sort_order', 0)
        self._start_date = data.get('start_date', None)
        self._task_status_id = data.get('task_status_id', None)
        self._task_type_id = data.get('task_type_id', None)
        self._task_type_name = data.get('task_type_name', None)
        self._type = data.get('type', None)
        self._updated_at = data.get('updated_at', None)

    @property
    def id(self):
        """
        Returns ID of the task
        :return: str
        """

        return self._id

    @property
    def name(self):
        """
        Returns the name of the task
        :return: str
        """

        return self._task_type_name

    @property
    def description(self):
        """
        Returns description of the task
        :return: str
        """

        return self._description


class KitsuComment(object):
    def __init__(self, data):
        super(KitsuComment, self).__init__()

        self._dict = data

        self._id = data.get('id', None)
        self._type = data.get('type', None)
        self._text = data.get('text', '')
        self._created_at = data.get('created_at', None)
        self._data = data.get('data', None)
        self._mentions = data.get('mentions', list())
        self._object_id = data.get('object_id', None)
        self._object_type = data.get('object_type', None)
        self._person = data.get('person', None)
        self._person_id = data.get('person_id', None)
        self._pinned = data.get('pinned', None)
        self._preview_file_id = data.get('preview_file_id', None)
        self._previews = data.get('previews', list())
        self._shotgun_id = data.get('shotgun_id', None)
        self._task_status = data.get('task_status', None)
        self._task_status_id = data.get('task_status_id', None)
        self._updated_at = data.get('updated_at', None)

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def text(self):
        return self._text
