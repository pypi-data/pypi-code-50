# -*- coding: utf-8 -*-

import logging
import functools

from spaceone.core.pygrpc.message_type import *
from spaceone.api.secret.v1 import credential_group_pb2
from spaceone.secret.model.credential_group_model import CredentialGroup


__all__ = ['CredentialGroupInfo', 'CredentialGroupsInfo']
_LOGGER = logging.getLogger(__name__)


def CredentialGroupInfo(credential_group_vo: CredentialGroup, minimal=False):
    info = {
        'credential_group_id': credential_group_vo.credential_group_id,
        'name': credential_group_vo.name
    }

    if minimal is False:
        info.update({
            'created_at': change_timestamp_type(credential_group_vo.created_at),
            'domain_id': credential_group_vo.domain_id,
            'tags': change_struct_type(credential_group_vo.tags)
        })

    return credential_group_pb2.CredentialGroupInfo(**info)


def CredentialGroupsInfo(credential_group_vos, total_count, **kwargs):
    results = list(map(functools.partial(CredentialGroupInfo, **kwargs), credential_group_vos))

    return credential_group_pb2.CredentialGroupsInfo(results=results, total_count=total_count)
