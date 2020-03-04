import scrybe
import os
import shutil
from pyspark.sql import SparkSession

from scrybe.internal.depgraph import TrackingGraph

scrybe.init("scrybe e2e client testing")
scrybe.set_label("Spark Testing")


def is_predecessor(pred_obj, obj):
    if not TrackingGraph.has_tracked_obj(obj=pred_obj) or not TrackingGraph.has_tracked_obj(obj=obj):
        return False

    pred_node = TrackingGraph.get_node_for_tracked_object(obj=pred_obj)
    obj_node = TrackingGraph.get_node_for_tracked_object(obj=obj)
    for predecessor_node, ops in obj_node.predecessors.items():
        if predecessor_node is pred_node:
            return True
    return False


spark = SparkSession.builder.getOrCreate()
# Prepare training documents, which are labeled.
training = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0),
    (4, "b spark who", 1.0),
    (5, "g d a y", 0.0),
    (6, "spark fly", 1.0),
    (7, "was mapreduce", 0.0),
    (8, "e spark program", 1.0),
    (9, "a e c l", 0.0),
    (10, "spark compile", 1.0),
    (11, "hadoop software", 0.0)
], ["id", "text", "label"])

rdd = training.toJSON()
assert is_predecessor(pred_obj=training, obj=rdd)

rdd = training.rdd
df = rdd.toDF()
assert is_predecessor(pred_obj=rdd, obj=df)
assert is_predecessor(pred_obj=training, obj=rdd)


sc = spark.sparkContext
rdd = sc.parallelize([('Ramesh', 1), ('Suresh', 2)])
assert TrackingGraph.has_tracked_obj(obj=rdd)

pickle_path = "/tmp/rdd_pickle"
if os.path.exists(pickle_path):
    shutil.rmtree(pickle_path)
rdd.saveAsPickleFile(pickle_path)
rdd_node = TrackingGraph.get_node_for_tracked_object(obj=rdd)
assert rdd_node.is_anchor

rdd = sc.pickleFile(name=pickle_path)
rdd_node = TrackingGraph.get_node_for_tracked_object(obj=rdd)
assert rdd_node.is_anchor

rdd2 = sc.parallelize([('Alice', 10), ('Bob', 20)])
rdd3 = sc.union([rdd, rdd2])
assert TrackingGraph.has_tracked_obj(obj=rdd2)
assert TrackingGraph.has_tracked_obj(obj=rdd3)
assert is_predecessor(pred_obj=rdd, obj=rdd3)
assert is_predecessor(pred_obj=rdd2, obj=rdd3)

df = spark.createDataFrame(data=rdd)
assert is_predecessor(pred_obj=rdd, obj=df)

rdd = df.rdd
df2 = spark.createDataFrame(data=rdd)
assert is_predecessor(pred_obj=rdd, obj=df2)
assert is_predecessor(pred_obj=df, obj=rdd)


rdd2 = df.toJSON()
assert is_predecessor(pred_obj=df, obj=rdd2)

rdd = df2.rdd
assert not TrackingGraph.has_tracked_obj(obj=rdd)
rdd2 = rdd.sortByKey()
assert TrackingGraph.has_tracked_obj(obj=rdd)
lineage = TrackingGraph.get_lineage_of_tracked_object(obj=rdd2)
assert TrackingGraph.get_node_for_tracked_object(obj=rdd).client_id in lineage.nodes.keys()
# TODO(chandra): Check why the following assertion fails
# assert is_predecessor(pred_obj=rdd, obj=rdd2)
