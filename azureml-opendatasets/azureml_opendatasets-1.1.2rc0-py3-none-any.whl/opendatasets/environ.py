# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""Defines runtime environment classes where opendatasets are used.

Environments are used to ensure functionality is optimized for the respective environments. In general,
you will not need to instantiate environment objects or worry about the implementation.
Use the ``get_environ`` module function to return the environment.
"""

from multimethods import multimethod
from pandas import DataFrame as PdDataFrame
from pyspark.sql.dataframe import DataFrame as SparkDataFrame


class RuntimeEnv(object):
    """Defines the base class definition of runtime environments."""


class SparkEnv(RuntimeEnv):
    """Represents a Spark runtime environment."""


class PandasEnv(RuntimeEnv):
    """Represents a pandas runtime environment."""


@multimethod(SparkDataFrame)
def get_environ(data):
    """Get the Spark runtime environment."""
    return SparkEnv()


@multimethod(PdDataFrame)
def get_environ(data):
    """Get the pandas runtime environment."""
    return PandasEnv()
