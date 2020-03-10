# -*- coding: utf-8 -*-
import logging
import functools

from spaceone.api.inventory.v1 import collector_pb2
from spaceone.core.pygrpc.message_type import *

__all__ = ['CollectorInfo', 'CollectorsInfo', 'SchedulerInfo', 'SchedulersInfo']

_LOGGER = logging.getLogger(__name__)


def PluginInfo(vo, minimal=False):
    if vo is None:
        return None

    info = {
        'plugin_id': vo.plugin_id,
        'version': vo.version,
    }

    if not minimal:
        info.update({
            'options': change_struct_type(vo.options),
            'credential_id': vo.credential_id,
            'credential_group_id': vo.credential_group_id
        })
    return collector_pb2.PluginInfo(**info)


def CollectorInfo(vo, minimal=False):
    info = {
        'collector_id': vo.collector_id,
        'name': vo.name,
        'plugin_info': PluginInfo(vo.plugin_info, minimal),
        'state': vo.state
    }

    if not minimal:
        info.update({
            'priority': vo.priority,
            'created_at': change_timestamp_type(vo.created_at),
            'last_collected_at': change_timestamp_type(vo.last_collected_at),
            'tags': change_struct_type(vo.tags),
            'domain_id': vo.domain_id
        })

    return collector_pb2.CollectorInfo(**info)


def CollectorsInfo(vos, total_count, **kwargs):
    return collector_pb2.CollectorsInfo(results=list(map(functools.partial(CollectorInfo, **kwargs), vos)),
                                        total_count=total_count)


def ScheduleInfo(vo):
    info = {
        'cron': vo.cron,
        'interval': vo.interval,
        'hours': vo.hours,
        'minutes': vo.minutes
    }
    return collector_pb2.Schedule(**info)


def SchedulerInfo(vo, minimal=False):
    info = {
        'scheduler_id': vo.scheduler_id,
        'collect_mode': vo.collect_mode,
        'name': vo.name,
    }

    if not minimal:
        info.update({
            'collector_info': CollectorInfo(vo.collector, minimal=True),
            'created_at': change_timestamp_type(vo.created_at),
            'last_scheduled_at': change_timestamp_type(vo.last_scheduled_at),
            'filter': change_struct_type(vo.filters),
            'schedule': ScheduleInfo(vo.schedule)
        })
    return collector_pb2.SchedulerInfo(**info)

def SchedulersInfo(vos, total_count, **kwargs):
    return collector_pb2.SchedulersInfo(results=list(map(functools.partial(SchedulerInfo, **kwargs), vos)),
                                        total_count=total_count)


