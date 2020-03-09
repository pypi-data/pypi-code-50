import subprocess
import sys


class CloudRunLoggingClient:
    def __init__(self, type, service, log_name, region='us-east1'):

        # Intsall google.cloud if it is not installed in the environment.

        try:
            from google.cloud import logging
        except ImportError:
            subprocess.call([sys.executable, "-m", "pip", "install", 'google-cloud-logging'])
        finally:
            from google.cloud import logging
            from google.cloud.logging.resource import Resource

            """
            :param type: Resource type to filter in Stackdriver Logging
            :param service: Service name to filter in Stackdriver Logging
            :param log_name: Log Name to filter in Stackdriver Logging
            :param region: GCP Service Region to filter in Stackdriver Logging
            """

            self._client = logging.Client()
            self._logger = self._client.logger(log_name)
            self._resource = Resource(type=type,
                                      labels={"service_name": service, "region": region})


    def report(self, struct, severity='INFO'):
        """
        :param struct: (Dict) Custom information for logging into Stackdriver Logging.
        :param severity: Severity Level for the logging.
        """
        self._logger.log_struct(struct, resource=self._resource, severity=severity)