# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Public data telemetry base class."""
import copy
import platform
from datetime import datetime

from azureml import telemetry
from azureml._base_sdk_common import __version__
from azureml.telemetry.contracts import (Event, ExtensionFields,
                                         RequiredFields, StandardFields)

from .._utils.telemetry_utils import (INSTRUMENTATION_KEY_KEY,
                                      OPENDATASETS_INSTRUMENTATION_KEY,
                                      SUBSCRIPTION_ID, WORKSPACE_ID,
                                      WORKSPACE_LOCATION)

try:
    from azureml._base_sdk_common import _ClientSessionId
except ImportError:
    from uuid import uuid4
    _ClientSessionId = str(uuid4())


class _PublicDataTelemetry:
    """Public data telemetry base class contains telemetry logger for each open datasets."""

    @staticmethod
    def log_event(event_name, **kwargs):
        """
        Log the event to app insights.

        :param event_name: name of the event
        :type event_name: str
        :param kwargs: a list of the key/value pairs which will be stored in event
        :type kwargs: dict
        """
        _common_logger = telemetry.get_event_logger(
            **{INSTRUMENTATION_KEY_KEY: OPENDATASETS_INSTRUMENTATION_KEY})
        req = RequiredFields()
        std = StandardFields()
        dct = copy.deepcopy(kwargs)
        req.component_name = 'OpenDatasets'
        req.client_type = 'SDK'
        req.client_version = __version__
        std.client_os = platform.system()
        if WORKSPACE_ID in kwargs:
            req.workspace_id = kwargs[WORKSPACE_ID]
            dct.pop(WORKSPACE_ID)
        if SUBSCRIPTION_ID in kwargs:
            req.subscription_id = kwargs[SUBSCRIPTION_ID]
            dct.pop(SUBSCRIPTION_ID)
        if WORKSPACE_LOCATION in kwargs:
            std.workspace_region = kwargs[WORKSPACE_LOCATION]
            dct.pop(WORKSPACE_LOCATION)
        dct['sessionId'] = _ClientSessionId
        for key, value in dct.items():
            if isinstance(value, datetime):
                dct[key] = value.strftime(
                    "%Y-%m-%dT%H:%M:%S") if value is not None else ''
            elif isinstance(value, list):
                dct[key] = ",".join(value)
        ext = ExtensionFields(**dct)
        event = Event(name=event_name, required_fields=req, standard_fields=std,
                      extension_fields=ext)
        _common_logger.log_event(event)
        _common_logger.flush()
