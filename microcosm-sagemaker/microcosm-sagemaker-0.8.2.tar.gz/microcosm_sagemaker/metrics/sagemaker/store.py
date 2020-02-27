import datetime
from typing import Optional

import boto3
from botocore.exceptions import ClientError, NoCredentialsError, NoRegionError
from microcosm_logging.decorators import logger

from microcosm_sagemaker.constants import CLOUDWATCH_MAX_DIMENSIONS
from microcosm_sagemaker.decorators import metrics_observer, training_initializer
from microcosm_sagemaker.hyperparameters import get_hyperparameters
from microcosm_sagemaker.metrics.sagemaker.models import LogMode, MetricUnit


@training_initializer()
@metrics_observer()
@logger
class SageMakerMetrics:
    def __init__(self, graph):
        self.graph = graph
        self.testing = graph.metadata.testing
        self.model_name = graph.metadata.name
        self.enabled = True

    @property
    def dimensions(self):
        return self._get_dimensions()

    def init(self):
        self.logger.info("`cloudwatch` was registered as a metric observer.")

    def _get_dimensions(self):
        # Metric dimensions allow us to analyze metric performance against the
        # hyperparameters of our model
        dimensions = [
            {
                "Name": flattened_hyperparam,
                "Value": str(value),
            }
            for flattened_hyperparam, value in get_hyperparameters(self.graph)
        ]

        if len(dimensions) > CLOUDWATCH_MAX_DIMENSIONS:
            self.logger.warning(
                f"The number of hyperparameters ({len(dimensions)}) is more than the maximum dimensions "
                f"allowed by `cloudwatch` ({CLOUDWATCH_MAX_DIMENSIONS}). "
                f"Truncating to first {CLOUDWATCH_MAX_DIMENSIONS} dimensions."
            )
            dimensions = dimensions[:CLOUDWATCH_MAX_DIMENSIONS]

        return dimensions

    def _metric_data(self, metric_name, metric_value, timestamp):
        metric_data = dict(
            MetricName=metric_name,
            Dimensions=self.dimensions,
            Value=metric_value,
            Unit=MetricUnit.NONE.name,
            StorageResolution=1,
        )

        if timestamp:
            metric_data.update(Timestamp=timestamp)

        return metric_data

    def _log_metric(self, log_mode: LogMode, **kwargs):

        timestamp: Optional[datetime.datetime]
        if log_mode == LogMode.TIMESERIES:
            timestamp = datetime.datetime.now()
        else:
            timestamp = None

        metric_data = [
            self._metric_data(metric_name, metric_value, timestamp)
            for metric_name, metric_value in kwargs.items()
        ]

        try:
            cloudwatch = boto3.client("cloudwatch")
            response = cloudwatch.put_metric_data(
                Namespace="/aws/sagemaker/" + self.model_name,
                MetricData=metric_data,
            )
        except (ClientError, NoCredentialsError, NoRegionError) as e:
            self.logger.warning("CloudWatch publishing disabled", extra=dict(metric_data=metric_data))  # type: ignore
            self.logger.warning(e)  # type: ignore
            # Disable cloudwatch logging if it fails to push metrics due to one of the above errors
            self.enabled = False
            response = None

        return response

    def log_static(self, **kwargs):
        if self.enabled:
            self._log_metric(LogMode.STATIC, **kwargs)

    def log_timeseries(self, **kwargs):
        if self.enabled:
            self._log_metric(LogMode.TIMESERIES, **kwargs)
