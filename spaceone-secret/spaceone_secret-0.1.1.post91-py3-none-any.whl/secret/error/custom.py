# -*- coding: utf-8 -*-

from spaceone.core.error import *


class ERROR_ALREADY_EXIST_CREDENTIAL_IN_GROUP(ERROR_BASE):
    _message = 'Credential is already exist in group. credential_group_id = {credential_group_id}, credential_id = {credential_id}'


class ERROR_NOT_EXIST_CREDENTIAL_IN_GROUP(ERROR_BASE):
    _message = 'Credential is not exist in group. credential_group_id = {credential_group_id}, credential_id = {credential_id}'