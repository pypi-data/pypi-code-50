# -*- coding: utf-8 -*-

import logging
import functools

from spaceone.core.pygrpc.message_type import *
from spaceone.api.secret.v1 import credential_pb2
from spaceone.secret.model.credential_model import Credential


__all__ = ['CredentialInfo', 'CredentialsInfo', 'IssueInfo']
_LOGGER = logging.getLogger(__name__)


def IssueInfo(issue_type, secret):
    info = {
        'issue_type': issue_type,
        'secret': change_struct_type(secret)
    }

    return credential_pb2.IssueInfo(**info)


def CredentialInfo(credential_vo: Credential, minimal=False):
    info = {
        'credential_id': credential_vo.credential_id,
        'name': credential_vo.name
    }

    if minimal is False:
        info.update({
            'issue_type': credential_vo.issue_type,
            'project_id': credential_vo.project_id,
            # 'plugin_info': credential_vo.plugin_info,
            'created_at': change_timestamp_type(credential_vo.created_at),
            'domain_id': credential_vo.domain_id,
            'tags': change_struct_type(credential_vo.tags)
        })

        if getattr(credential_vo, 'credential_groups', None) is not None:
            credential_groups = credential_vo.credential_groups
            credential_group_infos = list(map(lambda credential_group: CredentialGroupInfo(credential_group),
                                              credential_groups))

            info.update({
                'credential_groups': change_list_value_type(credential_group_infos)
            })

    return credential_pb2.CredentialInfo(**info)


def CredentialsInfo(credential_vos, total_count, **kwargs):
    results = list(map(functools.partial(CredentialInfo, **kwargs), credential_vos))

    return credential_pb2.CredentialsInfo(results=results, total_count=total_count)


def CredentialGroupInfo(credential_group_vo):
    return {
        'credential_group_id': credential_group_vo.credential_group_id,
        'name': credential_group_vo.name
    }
