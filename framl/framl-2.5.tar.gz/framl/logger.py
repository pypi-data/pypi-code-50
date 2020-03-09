import time
from typing import  List
from google.cloud.logging.handlers import CloudLoggingHandler
from google.cloud.logging.handlers.transports import  BackgroundThreadTransport

from framl.config_model import ConfigModel
from google.cloud import logging
from google.cloud.logging.resource import Resource


class Logger:
    MESSAGE_VERSION = 1

    def __init__(self, app_path: str):
        model_conf_ob = ConfigModel(app_path)

        self._model_name = model_conf_ob.get_model_name()
        self._model_version = model_conf_ob.get_model_version()
        self._logs_buffer: List[dict] = []

        logging_client = logging.Client(project=model_conf_ob.get_gcp_project_id())
        transport = BackgroundThreadTransport(logging_client, "foo", 5, 100, 1)
        my_handler = CloudLoggingHandler(client=logging_client, name="xyz", transport=BackgroundThreadTransport)

        self.sd_logger = logging_client.logger("framl.blablacar.com%2F" + self._model_name.replace("-", "_"))
        self.sd_logger.addHandler(my_handler)

        self.log_res = Resource(
            type="api",
            labels={
                "project_id": model_conf_ob.get_gcp_project_id(),
                "service":    self._model_name,
                "method":     "/predict",
                "version":    str(model_conf_ob.get_model_version()),
                "location":   "global"
            },
        )

    def add(self, prediction_id: str, model_input: dict, model_output: dict, latency: int):
        full_log = {
            "request_latency_in_ms": latency,
            "prediction_id":         prediction_id,
            "message_version":       self.MESSAGE_VERSION,
            "prediction_time":       int(time.time()),
            "metadata":              {
                "model_name":    self._model_name,
                "model_version": self._model_version,
            },
            "input":                 {**model_input},
            "output":                {**model_output}
        }

        self.sd_logger.log_struct(full_log, resource=self.log_res)