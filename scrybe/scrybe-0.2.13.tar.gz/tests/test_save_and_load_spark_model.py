import scrybe
from pyspark.ml import Pipeline, PipelineModel
from pyspark.ml.feature import Tokenizer
from pyspark.ml.feature import HashingTF

from pyspark.sql import SparkSession
from pyspark.ml.classification import LogisticRegression, LogisticRegressionModel
from pyspark.ml.evaluation import BinaryClassificationEvaluator
from scrybe.internal.depgraph import TrackingGraph

scrybe.init("scrybe e2e client testing")
spark = SparkSession.builder.getOrCreate()
data = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")
splits = data.randomSplit([0.6, 0.4], 1234)
training = splits[0]
test = splits[1]

lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)

# Fit the model
lrModel = lr.fit(training)
model_path = "/tmp/Sample_LR_Model"
lrModel.write().overwrite().save(model_path)
assert TrackingGraph.get_node_for_tracked_object(obj=lrModel).is_name_final

m_lr = LogisticRegressionModel.load(model_path)
p_node = TrackingGraph.get_node_for_tracked_object(m_lr)
preds = [predecessor_node for predecessor_node, ops in p_node.predecessors.items()]
assert len(preds) == 0
assert TrackingGraph.get_node_for_tracked_object(obj=m_lr).path
predictions = m_lr.transform(test)
evaluator = BinaryClassificationEvaluator()
print(evaluator.evaluate(predictions))
assert not TrackingGraph.get_node_for_tracked_object(obj=m_lr).path

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

val = spark.createDataFrame([
    (0, "a b c d e spark", 1.0),
    (1, "b d", 0.0),
    (2, "spark f g h", 1.0),
    (3, "hadoop mapreduce", 0.0),
    (4, "b spark who", 1.0),
], ["id", "text", "label"])

# Configure an ML pipeline, which consists of tree stages: tokenizer, hashingTF, and lr.
tokenizer = Tokenizer(inputCol="text", outputCol="words")
hashingTF = HashingTF(inputCol=tokenizer.getOutputCol(), outputCol="features")
lr = LogisticRegression(maxIter=10)
pipeline = Pipeline(stages=[tokenizer, hashingTF, lr])
pipe_model = pipeline.fit(training)

pipe_model_path = "/tmp/pipe_model"
pipe_model.write().overwrite().save(pipe_model_path)
assert TrackingGraph.get_node_for_tracked_object(obj=pipe_model).is_name_final

pModel = PipelineModel.load(pipe_model_path)
p_node = TrackingGraph.get_node_for_tracked_object(pModel)
preds = [predecessor_node for predecessor_node, ops in p_node.predecessors.items()]
assert len(preds) == 1
assert not preds[0].created_in_run
assert preds[0].path
preds_2 = [predecessor_node for predecessor_node, ops in preds[0].predecessors.items()]
assert len(preds_2) == 0
assert TrackingGraph.get_node_for_tracked_object(obj=pModel).path
predictions = pModel.transform(val)
print(evaluator.evaluate(predictions))
assert not TrackingGraph.get_node_for_tracked_object(obj=pModel).path

pipeline = Pipeline(stages=[hashingTF, lr])
pipe_of_pipeline = Pipeline(stages=[tokenizer, pipeline])
pipe_pModel = pipe_of_pipeline.fit(training)
pipe_of_pipe_path = "/tmp/pipe_of_pipe_fit"
pipe_pModel.write().overwrite().save(pipe_of_pipe_path)
assert TrackingGraph.get_node_for_tracked_object(obj=pipe_pModel).is_name_final

nested_pipe_model = PipelineModel.load(pipe_of_pipe_path)
p_node = TrackingGraph.get_node_for_tracked_object(nested_pipe_model)
preds = [predecessor_node for predecessor_node, ops in p_node.predecessors.items()]
assert len(preds) == 1
assert not preds[0].created_in_run
assert preds[0].path
preds_2 = [predecessor_node for predecessor_node, ops in preds[0].predecessors.items()]
assert len(preds_2) == 1
assert not preds_2[0].created_in_run
assert preds_2[0].path
assert TrackingGraph.get_node_for_tracked_object(obj=nested_pipe_model).path
predictions = nested_pipe_model.transform(val)
print(evaluator.evaluate(predictions))
assert not TrackingGraph.get_node_for_tracked_object(obj=nested_pipe_model).path

pipeline = Pipeline(stages=[tokenizer, hashingTF])
pipe_of_pipeline = Pipeline(stages=[pipeline, lr])
pipe_pModel = pipe_of_pipeline.fit(training)
pipe_of_pipe_transformer_path = "/tmp/pipe_of_pipe_transform"
pipe_pModel.write().overwrite().save(pipe_of_pipe_transformer_path)
assert TrackingGraph.get_node_for_tracked_object(obj=pipe_pModel).is_name_final

nested_pipe_transform = PipelineModel.load(pipe_of_pipe_transformer_path)
p_node = TrackingGraph.get_node_for_tracked_object(nested_pipe_transform)
preds = [predecessor_node for predecessor_node, ops in p_node.predecessors.items()]
assert len(preds) == 1
assert not preds[0].created_in_run
assert preds[0].path
preds_2 = [predecessor_node for predecessor_node, ops in preds[0].predecessors.items()]
assert len(preds_2) == 0
assert TrackingGraph.get_node_for_tracked_object(obj=nested_pipe_transform).path
predictions = nested_pipe_transform.transform(val)
print(evaluator.evaluate(predictions))
assert not TrackingGraph.get_node_for_tracked_object(obj=nested_pipe_transform).path
