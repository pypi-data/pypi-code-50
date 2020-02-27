# -*- coding: utf-8 -*-
# (c) Satelligence, see LICENSE.rst.
"""Common logging and monitoring utils
"""
import os
import socket

from google.cloud.logging._helpers import retrieve_metadata_server  # pylint: disable=protected-access
from google.cloud.logging.resource import Resource as LoggingResource
from google.cloud import monitoring



PROJECT_ID = retrieve_metadata_server('project/project-id')
CLUSTER_NAME = retrieve_metadata_server('instance/attributes/cluster-name')
LOCATION = retrieve_metadata_server('instance/attributes/cluster-location')
NAMESPACE_NAME = os.environ.get('KUBERNETES_NAMESPACE', '')
CONTAINER_NAME = os.environ.get('KUBERNETES_CONTAINER_NAME', '')
NODE_NAME = os.environ.get('KUBERNETES_NODE_NAME', '')
POD_NAME = socket.gethostname()

MONITORING_CLIENT = monitoring.MetricServiceClient()


def labels_dict():
    return {
        'cluster_name': CLUSTER_NAME if CLUSTER_NAME else '',
        'project_id': PROJECT_ID if PROJECT_ID else '',
        'location': LOCATION if LOCATION else '',
        'pod_name': POD_NAME if POD_NAME else '',
        'namespace_name': NAMESPACE_NAME,
        'container_name': CONTAINER_NAME,
    }

def logging_k8s_container():
    if PROJECT_ID and CLUSTER_NAME:
        return LoggingResource(
            type='k8s_container',
            labels=labels_dict(),
        )
    return LoggingResource(
        type='global',
        labels=labels_dict(),
    )

def monitoring_resource():
    if PROJECT_ID and CLUSTER_NAME:
        resource_type = 'k8s_container'
        labels = labels_dict()
    else:
        resource_type = 'global'
        labels = {}
    return dict(type=resource_type, labels=labels)
