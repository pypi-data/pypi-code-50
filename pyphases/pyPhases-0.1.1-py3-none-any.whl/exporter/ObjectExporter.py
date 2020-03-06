from .DataExporter import DataExporter
from pandas import DataFrame
import pyarrow
import numpy

class ObjectExporter(DataExporter):
    """ An Exporter that supports a lot of default formats using pyarrow"""
    def checkType(self, type):
        return type in (str, int, bool, float) or type in (numpy.ndarray, tuple) or type in (DataFrame, tuple) or type in [DataFrame, numpy.ndarray]
        # TODO: more generic with ?!

    def importData(self, byteString):
        context = pyarrow.default_serialization_context()
        buffer = pyarrow.py_buffer(byteString)
        df = context.deserialize(buffer)

        return df

    def export(self, df):
        context = pyarrow.default_serialization_context()
        serialized_df = context.serialize(df)
        buffer = serialized_df.to_buffer()
        byteString = buffer.to_pybytes()

        return byteString
