import functools
import json

from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.depgraph.nodes import BaseTrackingNode, UtilityNode, DatasetTrackingNode
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.util import get_func_arg_names, get_func_req_params

# TODO(chandra): Check where this needs to be patched
DATAFRAME_COLUMNS = [
    ('pyspark.sql.dataframe', 'DataFrame.colRegex'),
]

# TODO(chandra): Patch dataframe stats
DATAFRAME_STATS = [
    ('pyspark.sql.dataframe', 'DataFrame.approxQuantile'),
    ('pyspark.sql.dataframe', 'DataFrame.corr'),
    ('pyspark.sql.dataframe', 'DataFrame.count'),
    ('pyspark.sql.dataframe', 'DataFrame.cov'),
]

DATAFRAME_CREATION_FROM_GROUPDATA = [
    ('pyspark.sql.group', 'GroupedData.agg'),
    ('pyspark.sql.group', 'GroupedData.apply'),
]

DATASET_CREATION_FROM_SELF = [
    ('pyspark.sql.dataframe', 'DataFrame.agg'),
    ('pyspark.sql.dataframe', 'DataFrame.alias'),
    ('pyspark.sql.dataframe', 'DataFrame.checkpoint'),
    ('pyspark.sql.dataframe', 'DataFrame.coalesce'),
    ('pyspark.sql.dataframe', 'DataFrame.crosstab'),
    ('pyspark.sql.dataframe', 'DataFrame.describe'),
    ('pyspark.sql.dataframe', 'DataFrame.distinct'),
    ('pyspark.sql.dataframe', 'DataFrame.drop'),
    ('pyspark.sql.dataframe', 'DataFrame.dropDuplicates'),
    ('pyspark.sql.dataframe', 'DataFrame.dropna'),
    ('pyspark.sql.dataframe', 'DataFrame.fillna'),
    ('pyspark.sql.dataframe', 'DataFrame.filter'),
    ('pyspark.sql.dataframe', 'DataFrame.freqItems'),
    ('pyspark.sql.dataframe', 'DataFrame.hint'),
    ('pyspark.sql.dataframe', 'DataFrame.limit'),
    ('pyspark.sql.dataframe', 'DataFrame.localCheckpoint'),
    ('pyspark.sql.dataframe', 'DataFrame.repartition'),
    ('pyspark.sql.dataframe', 'DataFrame.repartitionByRange'),
    ('pyspark.sql.dataframe', 'DataFrame.replace'),
    ('pyspark.sql.dataframe', 'DataFrame.sample'),
    ('pyspark.sql.dataframe', 'DataFrame.sampleBy'),
    ('pyspark.sql.dataframe', 'DataFrame.select'),
    ('pyspark.sql.dataframe', 'DataFrame.selectExpr'),
    ('pyspark.sql.dataframe', 'DataFrame.sort'),
    ('pyspark.sql.dataframe', 'DataFrame.sortWithinPartitions'),
    ('pyspark.sql.dataframe', 'DataFrame.summary'),
    ('pyspark.sql.dataframe', 'DataFrame.toDF'),
    ('pyspark.sql.dataframe', 'DataFrame.withColumn'),
    ('pyspark.sql.dataframe', 'DataFrame.withColumnRenamed'),
    ('pyspark.sql.dataframe', 'DataFrame.withWatermark'),
    ('pyspark.rdd', 'RDD.aggregateByKey'),
    ('pyspark.rdd', 'RDD.cartesian'),
    ('pyspark.rdd', 'RDD.coalesce'),
    ('pyspark.rdd', 'RDD.cogroup'),
    ('pyspark.rdd', 'RDD.combineByKey'),
    ('pyspark.rdd', 'RDD.distinct'),
    ('pyspark.rdd', 'RDD.filter'),
    ('pyspark.rdd', 'RDD.flatMap'),
    ('pyspark.rdd', 'RDD.flatMapValues'),
    ('pyspark.rdd', 'RDD.foldByKey'),
    ('pyspark.rdd', 'RDD.glom'),
    ('pyspark.rdd', 'RDD.groupBy'),
    ('pyspark.rdd', 'RDD.groupByKey'),
    ('pyspark.rdd', 'RDD.keyBy'),
    ('pyspark.rdd', 'RDD.keys'),
    ('pyspark.rdd', 'RDD.map'),
    ('pyspark.rdd', 'RDD.mapPartitions'),
    ('pyspark.rdd', 'RDD.mapPartitionsWithIndex'),
    ('pyspark.rdd', 'RDD.mapPartitionsWithSplit'),
    ('pyspark.rdd', 'RDD.mapValues'),
    ('pyspark.rdd', 'RDD.partitionBy'),
    ('pyspark.rdd', 'RDD.pipe'),
    ('pyspark.rdd', 'RDD.reduceByKey'),
    ('pyspark.rdd', 'RDD.repartition'),
    ('pyspark.rdd', 'RDD.repartitionAndSortWithinPartitions'),
    ('pyspark.rdd', 'RDD.sample'),
    ('pyspark.rdd', 'RDD.sampleByKey'),
    ('pyspark.rdd', 'RDD.sortBy'),
    ('pyspark.rdd', 'RDD.sortByKey'),
    ('pyspark.rdd', 'RDD.values'),
    ('pyspark.rdd', 'RDD.zipWithIndex'),
    ('pyspark.rdd', 'RDD.zipWithUniqueId'),
    ('pyspark.sql.dataframe', 'DataFrame.toJSON'),
    ('pyspark.rdd', 'RDD.toDF'),
]

DATASET_CREATION_FROM_SELF_AND_OTHER = [
    ('pyspark.sql.dataframe', 'DataFrame.crossJoin'),
    ('pyspark.sql.dataframe', 'DataFrame.join'),
    ('pyspark.sql.dataframe', 'DataFrame.exceptAll'),
    ('pyspark.sql.dataframe', 'DataFrame.intersect'),
    ('pyspark.sql.dataframe', 'DataFrame.intersectAll'),
    ('pyspark.sql.dataframe', 'DataFrame.subtract'),
    ('pyspark.sql.dataframe', 'DataFrame.union'),
    ('pyspark.sql.dataframe', 'DataFrame.unionAll'),
    ('pyspark.sql.dataframe', 'DataFrame.unionByName'),
    ('pyspark.rdd', 'RDD.groupWith'),
    ('pyspark.rdd', 'RDD.intersection'),
    ('pyspark.rdd', 'RDD.fullOuterJoin'),
    ('pyspark.rdd', 'RDD.join'),
    ('pyspark.rdd', 'RDD.leftOuterJoin'),
    ('pyspark.rdd', 'RDD.rightOuterJoin'),
    ('pyspark.rdd', 'RDD.subtract'),
    ('pyspark.rdd', 'RDD.subtractByKey'),
    ('pyspark.rdd', 'RDD.union'),
    ('pyspark.rdd', 'RDD.zip'),
]

LIST_DATASET_FROM_SELF = [
    ('pyspark.sql.dataframe', 'DataFrame.randomSplit'),
    ('pyspark.rdd', 'RDD.randomSplit'),
]

PANDAS_DF_FROM_SELF = [
    ('pyspark.sql.dataframe', 'DataFrame.toPandas'),
]

DATAFRAME_CREATION_FROM_SPARK_SESSION = [
    ('pyspark.sql.session', 'SparkSession.sql'),
    ('pyspark.sql.session', 'SparkSession.table'),
    ('pyspark.sql.session', 'SparkSession.createDataFrame'),
    ('pyspark.sql.session', 'SparkSession.range'),
]

RDD_CREATION_FROM_SPARK_CONTEXT = [
    ('pyspark.context', 'SparkContext.emptyRDD'),
    ('pyspark.context', 'SparkContext.range'),
    ('pyspark.context', 'SparkContext.parallelize'),
    # ('pyspark.context', 'SparkContext.newAPIHadoopRDD'),
    # ('pyspark.context', 'SparkContext.hadoopRDD'),
]

RDD_CREATION_FROM_UNION_OF_RDDS = [
    ('pyspark.context', 'SparkContext.union'),
]

DATASET_CREATION_FROM_FILE = [
    ('pyspark.sql.readwriter', 'DataFrameReader.load'),
    ('pyspark.sql.readwriter', 'DataFrameReader.orc'),
    ('pyspark.sql.readwriter', 'DataFrameReader.json'),  # path can be rdd
    ('pyspark.sql.readwriter', 'DataFrameReader.csv'),  # path can be rdd
    ('pyspark.sql.readwriter', 'DataFrameReader.parquet'),  # decipher paths
    ('pyspark.sql.readwriter', 'DataFrameReader.text'),  # decipher paths
    ('pyspark.sql.readwriter', 'DataFrameReader.table'),  # Capture tableName
    ('pyspark.sql.readwriter', 'DataFrameReader.jdbc'),  # Capture url, table name etc
    ('pyspark.context', 'SparkContext.pickleFile'),
    ('pyspark.context', 'SparkContext.textFile'),
    ('pyspark.context', 'SparkContext.wholeTextFiles'),
    ('pyspark.context', 'SparkContext.binaryFiles'),
    ('pyspark.context', 'SparkContext.binaryRecords'),
    ('pyspark.context', 'SparkContext.sequenceFile'),
    ('pyspark.context', 'SparkContext.newAPIHadoopFile'),
    ('pyspark.context', 'SparkContext.hadoopFile'),
]

# TODO(chandra): saveAsNewAPIHadoopDataset is unpatched yet. Figure out how to parse conf to get file path
DATASET_SAVE = [
    ('pyspark.sql.readwriter', 'DataFrameWriter.save'),
    ('pyspark.sql.readwriter', 'DataFrameWriter.orc'),
    ('pyspark.sql.readwriter', 'DataFrameWriter.json'),
    ('pyspark.sql.readwriter', 'DataFrameWriter.csv'),
    ('pyspark.sql.readwriter', 'DataFrameWriter.parquet'),
    ('pyspark.sql.readwriter', 'DataFrameWriter.text'),
    ('pyspark.sql.readwriter', 'DataFrameWriter.saveAsTable'),  # Capture tableName
    ('pyspark.sql.readwriter', 'DataFrameWriter.jdbc'),  # Capture url, table name etc
    ('pyspark.rdd', 'RDD.saveAsHadoopFile'),
    ('pyspark.rdd', 'RDD.saveAsNewAPIHadoopFile'),
    ('pyspark.rdd', 'RDD.saveAsPickleFile'),
    ('pyspark.rdd', 'RDD.saveAsSequenceFile'),
    ('pyspark.rdd', 'RDD.saveAsTextFile'),
    # ('pyspark.rdd', 'RDD.saveAsNewAPIHadoopDataset'),
    # ('pyspark.rdd', 'RDD.saveAsHadoopDataset'),
]

DATAFRAME_CREATION_FROM_TRANFORMER = [
    ('pyspark.ml.base', 'Transformer.transform'),
]

TABLE_CREATION_FROM_DATAFRAME = [
    ('pyspark.sql.dataframe', 'DataFrame.registerTempTable'),
    ('pyspark.sql.dataframe', 'DataFrame.createTempView'),
    ('pyspark.sql.dataframe', 'DataFrame.createOrReplaceTempView'),
    ('pyspark.sql.dataframe', 'DataFrame.createGlobalTempView'),
    ('pyspark.sql.dataframe', 'DataFrame.createOrReplaceGlobalTempView'),
]

TABLE_DELETION = [
    ('pyspark.sql.catalog', 'Catalog.dropTempView'),
    ('pyspark.sql.catalog', 'Catalog.dropGlobalTempView'),
]

TABLE_DATAFRAME_NODE_DICT = dict()


def create_transformation_association(node, metadata_dict, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    self_obj, dataset_obj = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    self_name, dataset_obj_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
    if dataset_obj is not None and TrackingGraph.has_tracked_obj(obj=dataset_obj):
        dataset_node = TrackingGraph.get_node_for_tracked_object(obj=dataset_obj)
        dataset_node.set_node_name_if_not_final(name=dataset_obj_name)
        node.add_predecessor(predecessor_node=dataset_node, operations={Operations.TRANSFORM})
    if TrackingGraph.has_tracked_obj(self_obj):
        self_node = TrackingGraph.get_node_for_tracked_object(obj=self_obj)
        if self_node.node_type == BaseTrackingNode.Type.MODEL:
            self_node.set_node_name_if_not_final(name=self_name)
            node.add_predecessor(predecessor_node=self_node, operations={Operations.PREDICTION})
            node.add_reference(node=self_node)


def get_table_names(dataframe_obj):
    logical_plan = json.loads(dataframe_obj._jdf.queryExecution().logical().toJSON())
    return [x['tableIdentifier']['table'] for x in logical_plan
            if x['class'] == "org.apache.spark.sql.catalyst.analysis.UnresolvedRelation"]


def javatopython_wrapper(dataframe_obj, javatopython_func):
    @functools.wraps(javatopython_func)
    def inner(*args, **kwargs):
        ret_val = javatopython_func(*args, **kwargs)
        if not TrackingGraph.has_tracked_obj(obj=ret_val):
            node = UtilityNode(oid=id(ret_val), version=0)
            TrackingGraph.add_tracked_object(obj=ret_val, node=node)
            dataframe_node = TrackingGraph.get_node_for_tracked_object(obj=dataframe_obj)
            node.add_reference(dataframe_node)
        return ret_val
    return inner


def track_rdd_if_possible(rdd_obj):
    try:
        from pyspark import RDD
        if not isinstance(rdd_obj, RDD):
            return
        if TrackingGraph.has_tracked_obj(obj=rdd_obj):
            return
        elif TrackingGraph.has_tracked_obj(obj=rdd_obj._jrdd):
            parent_jrdd_node = TrackingGraph.get_node_for_tracked_object(obj=rdd_obj._jrdd)
            parent_rdd_node = DatasetTrackingNode(oid=id(rdd_obj), version=0,
                                                  obj_type=DatasetTrackingNode.ObjectType.SPARK_RDD)
            TrackingGraph.add_tracked_object(obj=rdd_obj, node=parent_rdd_node)
            parent_rdd_node.add_predecessor(predecessor_node=parent_jrdd_node.references[0],
                                            operations={Operations.VIEW})
            return
    except Exception as e:
        return


def track_spark_dataset_and_parent_if_possible(dataset_obj, parent_obj_list=None) -> DatasetTrackingNode:
    from pyspark.sql import DataFrame
    from pyspark import RDD
    obj_type = DatasetTrackingNode.ObjectType.SPARK_DATAFRAME
    if isinstance(dataset_obj, RDD):
        obj_type = DatasetTrackingNode.ObjectType.SPARK_RDD
    node = DatasetTrackingNode(oid=id(dataset_obj), version=0, obj_type=obj_type)
    TrackingGraph.add_tracked_object(obj=dataset_obj, node=node)
    if isinstance(dataset_obj, DataFrame):
        dataset_obj._jdf.javaToPython = javatopython_wrapper(dataframe_obj=dataset_obj,
                                                             javatopython_func=dataset_obj._jdf.javaToPython)
    if parent_obj_list is not None:
        for parent_obj in parent_obj_list:
            track_rdd_if_possible(rdd_obj=parent_obj)
    return node
