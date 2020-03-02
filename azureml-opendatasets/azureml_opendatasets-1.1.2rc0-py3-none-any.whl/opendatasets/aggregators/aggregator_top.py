# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Contains the aggregator top class."""

from .aggregator import Aggregator
from ..environ import SparkEnv, PandasEnv
from .._utils.random_utils import random_tag
from multimethods import multimethod

import pandas as pd

from pyspark.sql.functions import col, row_number
from pyspark.sql.window import Window


class AggregatorTop(Aggregator):
    """Defines an aggregator that gets the top N based on join keys.

    .. remarks::

        Aggregators are typically not instantiated directly. Instead, specify the the type of aggregator when
        using using an enricher such as the :class:`azureml.opendatasets.enrichers.holiday_enricher.HolidayEnricher`
        object.

        The ``process_public_dataset(env, _public_dataset, cols, join_keys)`` method gets the maximum value.
    """

    def get_log_property(self):
        """Get log property tuple, None if no property."""
        return ('Aggregator', 'top')

    def __init__(self, n: int = 1):
        """Initialize with top numbers."""
        self.top = n

    @multimethod(SparkEnv, object, object, list)
    def process_public_dataset(self, env, _public_dataset, cols, join_keys):
        """
        Get the top N values based on the input join keys.

        :param env: The runtime environment.
        :type env: azureml.opendatasets.environ.RuntimeEnv
        :param _public_dataset: The input public dataset.
        :type _public_dataset: azureml.opendatasets.accessories.public_data.PublicData
        :param cols: The column name list to retrieve.
        :type cols: builtin.list
        :param join_keys: A list of join key pairs.
        :type join_keys: builtin.list
        :return: An aggregated public dataset.
        """
        keys = [pair[1] for pair in join_keys]
        window = Window.partitionBy(keys).orderBy(*keys)
        rn = 'rn' + random_tag()
        top_public_dataset = _public_dataset.withColumn(rn, row_number().over(window))\
            .where(col(rn) <= self.top).drop(rn)
        return top_public_dataset

    @multimethod(PandasEnv, object, object, list)
    def process_public_dataset(self, env, _public_dataset, cols, join_keys):
        """
        Get the top N values based on the input join keys.

        :param env: The runtime environment.
        :type env: azureml.opendatasets.environ.RuntimeEnv
        :param _public_dataset: The input public dataset.
        :type _public_dataset: azureml.opendatasets.accessories.public_data.PublicData
        :param cols: The column name list to retrieve.
        :type cols: builtin.list
        :param join_keys: A list of join key pairs.
        :type join_keys: builtin.list
        :return: An aggregated public dataset.
        """
        keys = [pair[1] for pair in join_keys]
        agg_public_dataset = _public_dataset.groupby(by=keys)\
            .apply(pd.DataFrame.head, self.top)
        return agg_public_dataset.reset_index(drop=True)
