# -*- coding: utf-8 -*-
# (c) Satelligence, see LICENSE.rst.
"""Common logging and monitoring utils
"""
import logging
import time

from google.cloud import monitoring_v3
from google.cloud.exceptions import NotFound

from arnoldpaperboy.utils.resource import (
    MONITORING_CLIENT, PROJECT_ID, monitoring_resource, stringify_label
)


logger = logging.getLogger(__name__)


def get_or_create_custom_metric_descriptor(client, project, name, description='', display_name=''):
    # try to get
    metric_descriptor_path = 'projects/{}/metricDescriptors/{}'.format(project, name)
    try:
        client.get_metric_descriptor(metric_descriptor_path)
        return True
    except NotFound:
        descriptor = monitoring_v3.types.MetricDescriptor()
        descriptor.type = name
        descriptor.metric_kind = monitoring_v3.enums.MetricKind.GAUGE
        descriptor.value_type = monitoring_v3.enums.ValueType.DOUBLE
        descriptor.unit = 's'
        if description:
            descriptor.description = description
        if display_name:
            descriptor.display_name = display_name

        descriptor = client.create_metric_descriptor(project, descriptor)
        return True
        # # give it some time to get created
        # test = 0
        # while test < 10:
        #     try:
        #         time.sleep(1)
        #         client.get_metric_descriptor(metric_descriptor_path)
        #         return True
        #     except NotFound:
        #         pass
        # # failed to create
        # logger.warning("Failed to create MetricDescriptor %s. Will not send metrics.", name)
        # return False


def send_metric(name,
                value,
                labels=None,
                timestamp=None,
                project=None,
                description='',
                display_name=''):
    if not project:
        project = PROJECT_ID
    project_name = MONITORING_CLIENT.project_path(project)
    if not name.startswith('custom.googleapis.com/'):
        name = 'custom.googleapis.com/{}'.format(name)

    get_or_create_custom_metric_descriptor(
        MONITORING_CLIENT, project, name, description=description, display_name=display_name
    )

    series = monitoring_v3.types.TimeSeries()

    series.metric.type = name
    if labels:
        labels = {k:stringify_label(v) for k, v in labels.items()}
        series.metric.labels.update(labels)
    resource = monitoring_resource()
    series.resource.type = resource['type']
    series.resource.labels.update(resource['labels'])
    point = series.points.add()
    point.value.double_value = value
    if not timestamp:
        timestamp = time.time()
    point.interval.end_time.seconds = int(timestamp)
    point.interval.end_time.nanos = int(
        (timestamp - point.interval.end_time.seconds) * 10 ** 9)

    MONITORING_CLIENT.create_time_series(project_name, [series])
    print('sent metric {}: {} [{}, {}]'.format(name, value, project, resource['type']))
