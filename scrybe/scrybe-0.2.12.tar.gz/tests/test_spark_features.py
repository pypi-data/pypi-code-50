import scrybe

from pyspark.sql import SparkSession
from pyspark.ml.feature import OneHotEncoderEstimator, StringIndexer, VectorAssembler
from pyspark.ml import Pipeline
import pandas as pd


scrybe.init("scrybe e2e client testing")
spark = SparkSession.builder \
    .appName('bank-calls') \
    .getOrCreate()
df = spark.read.csv('data/mllib/bank.csv', header=True, inferSchema=True)
numeric_features = [t[0] for t in df.dtypes if t[1] == 'int']
numeric_features_df = df.select(numeric_features)
numeric_pd_data = numeric_features_df.toPandas()
numeric_scatter_matrix = pd.plotting.scatter_matrix(numeric_pd_data, figsize=(8, 8))

df = df.select('age', 'job', 'marital', 'education', 'default', 'balance', 'housing', 'loan', 'contact', 'duration',
               'campaign', 'pdays', 'previous', 'poutcome', 'deposit')
cols = df.columns

categoricalColumns = ['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'poutcome']

# setup ML pipeline stages
stages = []
for categoricalCol in categoricalColumns:
    stringIndexer = StringIndexer(inputCol=categoricalCol, outputCol=categoricalCol + 'Index')
    encoder = OneHotEncoderEstimator(inputCols=[stringIndexer.getOutputCol()], outputCols=[categoricalCol + "classVec"])
    stages += [stringIndexer, encoder]
label_stringIdx = StringIndexer(inputCol='deposit', outputCol='label')
stages += [label_stringIdx]
numericCols = ['age', 'balance', 'duration', 'campaign', 'pdays', 'previous']
assemblerInputs = [c + "classVec" for c in categoricalColumns] + numericCols
assembler = VectorAssembler(inputCols=assemblerInputs, outputCol="features")
stages += [assembler]

pipeline = Pipeline(stages=stages)
pipelineModel = pipeline.fit(df)
df = pipelineModel.transform(df)
selectedCols = ['label', 'features'] + cols
df = df.select(selectedCols)
df.write.json("/tmp/pipeline_transform", mode="overwrite")
df.printSchema()
