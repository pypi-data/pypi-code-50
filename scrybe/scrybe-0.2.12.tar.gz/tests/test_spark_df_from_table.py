import scrybe
from pyspark.sql import SparkSession

from scrybe.internal.depgraph import TrackingGraph


def is_predecessor(pred_obj, obj):
    if not TrackingGraph.has_tracked_obj(obj=pred_obj) or not TrackingGraph.has_tracked_obj(obj=obj):
        return False

    pred_node = TrackingGraph.get_node_for_tracked_object(obj=pred_obj)
    obj_node = TrackingGraph.get_node_for_tracked_object(obj=obj)
    for predecessor_node, ops in obj_node.predecessors.items():
        if predecessor_node is pred_node:
            return True
    return False


scrybe.init("scrybe e2e client testing")
scrybe.set_label("Spark Testing")

spark = SparkSession.builder.getOrCreate()
train_file = "data/train.csv"
gb_file = "data/gb_5.csv"

# ===== Simple SQL =====
df = spark.read.csv(train_file, header=True, inferSchema=True)
df.registerTempTable("train_data")
query_str = "SELECT MSZoning, LotFrontage, LotArea FROM train_data WHERE MSSubClass = 60"
df2 = spark.sql(query_str)
df2_node = TrackingGraph.get_node_for_tracked_object(obj=df2)
assert df2_node.query_str == query_str
assert TrackingGraph.has_tracked_obj(obj=df)
assert is_predecessor(pred_obj=df, obj=df2)


# ===== Simple SQL w/ caching =====
df = spark.read.csv(train_file, header=True, inferSchema=True)
df = df.cache()
df.createTempView("train_data_cached")
df2 = spark.sql("SELECT MSZoning, LotFrontage, LotArea FROM train_data_cached WHERE MSSubClass = 60")
assert TrackingGraph.has_tracked_obj(obj=df)
assert TrackingGraph.has_tracked_obj(obj=df2)
assert is_predecessor(pred_obj=df, obj=df2)

# ===== Agg SQL Query =====
df = spark.read.csv(train_file, header=True, inferSchema=True)
df.createOrReplaceTempView("train_data_cached")
df2 = spark.sql("""SELECT MSSubClass, SUM(LotFrontage) as TotalLotFrontage, SUM(LotArea) AS TotalLotArea 
    FROM train_data_cached GROUP BY MSSubClass""")
assert TrackingGraph.has_tracked_obj(obj=df)
assert TrackingGraph.has_tracked_obj(obj=df2)
assert is_predecessor(pred_obj=df, obj=df2)

# ===== SQL Query w/ Joins =====
df_left = spark.read.csv(train_file, header=True, inferSchema=True)
df_left.createTempView("left_table")
df_right = spark.read.csv(gb_file, header=True, inferSchema=True)
df_right.createTempView("right_table")
df2 = spark.sql("SELECT * FROM left_table t1 JOIN right_table t2 WHERE t1.MSSubClass = t2.`Column 0`")
assert TrackingGraph.has_tracked_obj(obj=df_left)
assert TrackingGraph.has_tracked_obj(obj=df_right)
assert TrackingGraph.has_tracked_obj(obj=df2)
assert is_predecessor(pred_obj=df_left, obj=df2)
assert is_predecessor(pred_obj=df_right, obj=df2)

# ===== SQL Query w/ join on sub-query =====
df_left = spark.read.csv(train_file, header=True, inferSchema=True)
df_left.createOrReplaceTempView("left_table")
df_right = spark.read.csv(gb_file, header=True, inferSchema=True)
df_right.createOrReplaceTempView("right_table")
df2 = spark.sql("""SELECT * FROM left_table t1 JOIN (SELECT `Column 0`, `Column 1` FROM right_table) t2 
    WHERE t1.MSSubClass = t2.`Column 0`""")
assert TrackingGraph.has_tracked_obj(obj=df_left)
assert TrackingGraph.has_tracked_obj(obj=df_right)
assert TrackingGraph.has_tracked_obj(obj=df2)
assert is_predecessor(pred_obj=df_left, obj=df2)
assert is_predecessor(pred_obj=df_right, obj=df2)

# ===== SQL Query w/ agg on nested query =====
df_left = spark.read.csv(train_file, header=True, inferSchema=True)
df_left.createOrReplaceTempView("left_table")
df_right = spark.read.csv(gb_file, header=True, inferSchema=True)
df_right.createOrReplaceTempView("right_table")
df2 = spark.sql("""SELECT q.MSSubClass, SUM(q.LotFrontage) as TotalLotFrontage, SUM(q.LotArea) AS TotalLotArea 
    FROM (SELECT * FROM left_table t1 JOIN 
        (SELECT `Column 0`, `Column 1` FROM right_table) t2 ON t1.MSSubClass = t2.`Column 0`
    ) q
    GROUP BY q.MSSubClass""")
assert TrackingGraph.has_tracked_obj(obj=df_left)
assert TrackingGraph.has_tracked_obj(obj=df_right)
assert TrackingGraph.has_tracked_obj(obj=df2)
assert is_predecessor(pred_obj=df_left, obj=df2)
assert is_predecessor(pred_obj=df_right, obj=df2)

# ===== SQL View on top of DF from query =====
df2.createTempView('agg_query')
df3 = spark.sql("SELECT SUM(TotalLotFrontage) as TotalFrontage FROM agg_query")
assert TrackingGraph.has_tracked_obj(obj=df2)
assert is_predecessor(pred_obj=df2, obj=df3)
df3.write.mode(saveMode="overwrite").csv("/tmp/sql.query")

df3 = spark.table("agg_query")
df3_node = TrackingGraph.get_node_for_tracked_object(obj=df3)
assert df3_node.query_str == "agg_query"
assert TrackingGraph.has_tracked_obj(obj=df2)
assert is_predecessor(pred_obj=df2, obj=df3)
df3.write.mode(saveMode="overwrite").csv("/tmp/sql.table")

from scrybe.internal.tracker.data.instrumentation.spark_util import TABLE_DATAFRAME_NODE_DICT
assert "agg_query" in TABLE_DATAFRAME_NODE_DICT
spark.catalog.dropTempView("agg_query")
assert "agg_query" not in TABLE_DATAFRAME_NODE_DICT

