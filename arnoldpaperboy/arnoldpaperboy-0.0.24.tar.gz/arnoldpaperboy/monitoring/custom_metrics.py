# -*- coding: utf-8 -*-
# (c) Satelligence, see LICENSE.rst.
"""Common logger and monitoring utils
"""
import time

from google.cloud import monitoring

from arnoldpaperboy.utils.resource import MONITORING_CLIENT, PROJECT_ID, monitoring_resource


def send_metric(name, value, labels=None, timestamp=None, project=None):
    if not project:
        project = PROJECT_ID
    project_name = MONITORING_CLIENT.project_path(project)
    series = monitoring.types.TimeSeries()
    if not name.startswith('custom.googleapis.com/'):
        name = 'custom.googleapis.com/{}'.format(name)
    series.metric.type = name
    if labels:
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
