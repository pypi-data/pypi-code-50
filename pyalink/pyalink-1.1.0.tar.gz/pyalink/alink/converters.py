# -*- coding: utf-8 -*-
import os

import numpy as np
import pandas as pd

from .config import g_config
from .py4j_util import get_java_class, get_java_gateway

__all__ = ["dataframeToOperator", "collectToDataframes"]


# Basic type conversion
# Basic type conversion
_G_ALINK_TYPE_TO_PTYPE = {
    'BOOL': 'bool',
    'BOOLEAN': 'bool',
    'JAVA.LANG.BOOLEAN': 'bool',

    'TINYINT': 'Int8',
    'BYTE': 'Int8',
    'JAVA.LANG.BYTE': 'Int8',

    'SMALLINT': 'Int16',
    'JAVA.LANG.SHORT': 'Int16',

    'INT': 'Int32',
    'INTEGER': 'Int32',
    'JAVA.LANG.INTEGER': 'Int32',

    'BIGINT': 'Int64',
    'LONG': 'Int64',
    'JAVA.LANG.LONG': 'Int64',

    'FLOAT': 'float32',
    'JAVA.LANG.FLOAT': 'float32',

    'DOUBLE': 'float64',
    'JAVA.LANG.DOUBLE': 'float64',

    'STRING': 'object',
    'VARCHAR': 'object',
    'LONGVARCHAR': 'object',
    'JAVA.LANG.STRING': 'object',

    'DATETIME': 'datetime64',
    'JAVA.SQL.TIMESTAMP': 'datetime64',

    'VEC_TYPES_VECTOR': 'object',
    'COM.ALIBABA.ALINK.COMMON.LINALG.VECTOR': 'object',
    'ANY<COM.ALIBABA.ALINK.COMMON.LINALG.VECTOR>': 'object',

    'VEC_TYPES_DENSE_VECTOR': 'object',
    'COM.ALIBABA.ALINK.COMMON.LINALG.DENSEVECTOR': 'object',
    'ANY<COM.ALIBABA.ALINK.COMMON.LINALG.DENSEVECTOR>': 'object',

    'VEC_TYPES_SPARSE_VECTOR': 'object',
    'COM.ALIBABA.ALINK.COMMON.LINALG.SPARSEVECTOR': 'object',
    'ANY<COM.ALIBABA.ALINK.COMMON.LINALG.SPARSEVECTOR>': 'object'
}


def j_type_to_py_type(t):
    typeclass = t.getTypeClass()
    typeclass_name = typeclass.getName()
    if typeclass_name in ['java.lang.Double', 'java.lang.Float', 'double', 'float']:
        return np.float64
    elif typeclass_name in ['java.lang.Long', 'java.lang.Integer', 'int', 'long']:
        return pd.Int64Dtype()
    elif typeclass_name == 'java.lang.String':
        return np.object
    elif typeclass_name == 'java.sql.Timestamp':
        return np.datetime64
    elif typeclass_name == "com.alibaba.alink.common.linalg.Vector" or typeclass_name == "com.alibaba.alink.common.linalg.DenseVector" or typeclass_name == "com.alibaba.alink.common.linalg.SparseVector":
        return np.str
    elif typeclass_name in ["java.lang.Boolean", 'boolean']:
        return np.bool
    else:
        print("Java type is not supported in Python for automatic conversion of values: %s" % typeclass_name)
        return t


# basic value conversion

def j_value_to_py_value(value):
    import py4j
    if type(value) == py4j.java_collections.JavaArray:  # extract java array
        value = j_array_to_py_list(value)
        if len(value) > 0 and type(value[0]) == py4j.java_collections.JavaArray:    # extract java 2d array
            value = [j_array_to_py_list(row) for row in value]
    elif type(value) == py4j.java_gateway.JavaObject and value.getClass().getName() == "org.apache.flink.api.java.tuple.Tuple2":    # extract Tuple2
        return j_array_to_py_list(value.f0), j_array_to_py_list(value.f1)
    return value


# java array <-> python list


def j_array_to_py_list(arr):
    return [d for d in arr]


def py_list_to_j_array(type, num, items):
    arr = get_java_gateway().new_array(type, num)
    for i, item in enumerate(items):
        arr[i] = item
    return arr


# dict -> Params

def dict_to_j_params(d):
    j_params_cls = get_java_class("org.apache.flink.ml.api.misc.param.Params")
    j_params = j_params_cls()
    for (key, value) in d.items():
        j_params.set(key, value)
    return j_params


# Flink row(s) -> np array

def row_to_list(row):
    """
    Convert Flink row to Python list
    Primitive values will be stored in Python types; other values are kept in Java types
    :param row: Flink row
    :return:
    """
    return [
        row.getField(i)
        for i in range(row.getArity())
    ]


# Flink rows <-> pd dataframe

def schema_type_to_py_type(raw_type):
    t = raw_type.upper()
    if t in _G_ALINK_TYPE_TO_PTYPE:
        return _G_ALINK_TYPE_TO_PTYPE[t]
    else:
        print("Java type is not supported in Python for automatic conversion of values: %s" % t)
        return np.object


def adjust_dataframe_types(df, colnames, coltypes):
    for (colname, coltype) in zip(colnames, coltypes):
        col = df[colname]
        py_type = schema_type_to_py_type(coltype)
        if not pd.api.types.is_float_dtype(py_type)\
                and not pd.api.types.is_integer_dtype(py_type)\
                and col.isnull().values.any():
            print("Warning: null values exist in column %s, making it cannot be cast to type: %s automatically" % (
                colname, str(coltype)))
            continue
        df = df.astype({colname: py_type}, copy=False, errors='ignore')
    return df


def rows_with_columns_to_dataframe(rows, colnames, coltypes):
    df = pd.DataFrame(columns=colnames)
    row_list = [row_to_list(row) for row in rows]
    item_df = pd.DataFrame(row_list, columns=colnames)
    df = df.append(item_df)
    df = adjust_dataframe_types(df, colnames, coltypes)
    return df


# operator(s) -> dataframe(s)

def download_hdfs_file(filename):
    alink_endpoint = g_config["alink_endpoint"]
    collect_storage_root = g_config["collect_storage_root"]
    path = alink_endpoint + "/alink/hdfs_files" + filename.replace(collect_storage_root, "")

    import tempfile
    (fd, local_filename) = tempfile.mkstemp(suffix=".csv")

    import urllib3
    http = urllib3.PoolManager()
    response = http.request('GET', path)
    if response.status != 200:
        raise Exception("Download file: %s error: %d", path, response.status)
    content = response.data

    with open(local_filename, "w+b") as f:
        f.write(content)
    os.close(fd)
    return local_filename


def csv_file_to_dataframe(filename, colnames, coltypes):
    df = pd.read_csv(filename, names=colnames)
    os.unlink(filename)
    df = adjust_dataframe_types(df, colnames, coltypes)
    return df


def collect_to_dataframes_csv(*ops, **kwargs):
    """
    Collect the output table of operators to dataframes, with csv files as the intermediate storage
    :param ops:
    :return:
    """
    from .batch import BatchOperator, CsvSinkBatchOp

    import uuid
    storage_path = g_config["collect_storage_root"] + g_config["collect_storage_path"]
    filenames = [
        os.path.join(storage_path, uuid.uuid4().hex + ".csv")
        for op in ops
    ]
    for index, op in enumerate(ops):
        sink = CsvSinkBatchOp().setFilePath(filenames[index]).setOverwriteSink(True)
        sink.linkFrom(op)
    BatchOperator.execute()
    results = [
        csv_file_to_dataframe(filename, ops[index].getColNames(), ops[index].getColTypes())
        for index, filename in enumerate(filenames)
    ]

    return results


def collect_to_dataframes_memory(*ops):
    j_batch_operator_class = get_java_class('com.alibaba.alink.operator.batch.BatchOperator')
    j_ops = map(lambda op: op.get_j_obj(), ops)
    args = py_list_to_j_array(j_batch_operator_class, len(ops), j_ops)
    j_results = ops[0].get_j_obj().collect(args)
    return [
        rows_with_columns_to_dataframe(rows, ops[index].getColNames(), ops[index].getColTypes())
        for index, rows in enumerate(j_results)
    ]


def collect_to_dataframes(*ops, **kwargs):
    if len(ops) == 0:
        return []
    storage_type = g_config["collect_storage_type"]

    if storage_type == "csv":
        return collect_to_dataframes_csv(*ops, **kwargs)
    else:
        return collect_to_dataframes_memory(*ops)


def collectToDataframes(*ops, **kwargs):
    return collect_to_dataframes(*ops, **kwargs)


# dataframe(s) ->  operator(s)

def dataframe_to_operator_csv(df, schema_str, op_type):
    location = g_config["collect_storage_root"] + g_config["collect_storage_path"]
    import uuid
    filename = os.path.join(location, uuid.uuid4().hex + ".csv")
    df.to_csv(filename, header=False, index=False)

    from .batch import CsvSourceBatchOp
    from .stream import CsvSourceStreamOp

    if op_type == "batch":
        op = CsvSourceBatchOp()
    else:
        op = CsvSourceStreamOp()

    op = op.setFilePath(filename) \
        .setSchemaStr(schema_str)
    return op


def dataframe_to_operator_memory(df, schema_str, op_type):
    j_csv_util_cls = get_java_class("com.alibaba.alink.operator.common.io.csv.CsvUtil")
    j_table_schema = j_csv_util_cls.schemaStr2Schema(schema_str)
    j_col_names = j_csv_util_cls.getColNames(schema_str)
    j_col_types = j_csv_util_cls.getColTypes(schema_str)

    field_delimiter = ","
    quote_char = "\""

    j_csv_parser_cls = get_java_class("com.alibaba.alink.operator.common.io.csv.CsvParser")
    j_csv_parser = j_csv_parser_cls(j_col_types, field_delimiter, quote_char)

    df_copy = df.copy()
    for index, col_name in enumerate(df_copy.columns):
        j_col_type = j_col_types[index]
        # If the column is bool type, we need to convert 'True' to 'true', and 'False' to 'false'
        if j_col_type.toString() == "Boolean":
            df_copy[col_name] = df_copy[col_name].apply(lambda x: x if x is None else str(x).lower())

    j_array_list_cls = get_java_class("java.util.ArrayList")
    j_row_cls = get_java_class("org.apache.flink.types.Row")
    row_list = j_array_list_cls()
    for i in range(len(df_copy)):
        df_row = df_copy.loc[i:i]
        line = df_row.to_csv(index=False, header=False).strip()
        row = j_csv_parser.parse(line)
        row_copy = j_row_cls.copy(row)
        row_list.add(row_copy)

    if op_type == "batch":
        j_mem_source_op_cls =get_java_class("com.alibaba.alink.operator.batch.source.MemSourceBatchOp")
        from .batch.base import BatchOperatorWrapper
        wrapper = BatchOperatorWrapper
    else:
        j_mem_source_op_cls = get_java_class("com.alibaba.alink.operator.stream.source.MemSourceStreamOp")
        from .stream.base import StreamOperatorWrapper
        wrapper = StreamOperatorWrapper

    j_op = j_mem_source_op_cls(row_list, j_table_schema)

    return wrapper(j_op)


def dataframe_to_operator(df, schema_str, op_type):
    """
    Convert a dataframe to a batch operator in alink.
    If null values exist in df, it is better to provide schema_str, so that the operator can have correct type information.
    :param df:
    :param schema_str: column schema string, like "col1 string, col2 int, col3 boolean"
    :return:
    """
    storage_type = g_config["collect_storage_type"]
    if storage_type == "csv":
        return dataframe_to_operator_csv(df, schema_str, op_type)
    else:
        return dataframe_to_operator_memory(df, schema_str, op_type)


def dataframeToOperator(df, schemaStr, op_type=None, opType=None):
    if opType is None:
        opType = op_type
    if opType not in ["batch", "stream"]:
        raise 'opType %s not supported, please use "batch" or "stream"' % opType
    return dataframe_to_operator(df, schemaStr, opType)
