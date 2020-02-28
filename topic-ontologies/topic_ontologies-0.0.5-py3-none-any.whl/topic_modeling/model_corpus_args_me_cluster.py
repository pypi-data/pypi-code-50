#docker exec -u befi8957 -it webis-datascience-image-befi8957 bash -l -c 'cd; exec /opt/spark/bin/spark-submit   /home/yamenajjour/git/topic-ontologies/topic_modeling/model_corpus_args_me_cluster.py'
#docker exec -u befi8957 -it webis-datascience-image-befi8957 bash -l -c 'cd; exec /opt/spark/bin/spark-submit --deploy-mode cluster --py-files /home/yamenajjour/tmp/topic-ontologies-dep.zip --executor-memory 2G --driver-memory 4G /home/yamenajjour/git/topic-ontologies/topic_modeling/model_corpus_args_me_cluster.py'
import sys
sys.path.insert(0,"/home/yamenajjour/git/topic-ontologies/")
from argument_esa_model.esa import ESA
from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, LongType
import pandas as pd
import numpy as np
spark = SparkSession.builder.appName('topic-ontologies').config('master','yarn').getOrCreate()
args_me = spark.read.format('csv').option('header','true').option('delimiter',',')
import pickle
import codecs
def dict_to_list(dictionary):
    vector  = []
    for key in sorted(dictionary):
        vector.append(dictionary[key])
    pickled = codecs.encode(pickle.dumps(vector), "base64").decode()
    return pickled

def project_arguments():
    esa_model_debatepedia = ESA('/mnt/ceph/storage/data-in-progress/args-topic-modeling/topic-models/esa/debatepedia.mat')
    #esa_model_debatepedia = ESA ('/mnt/ceph/storage/data-in-progress/args-topic-modeling/topic-models/esa/debatepedia.mat')
    def project_argument(argument):
        dict_vect  = esa_model_debatepedia.process(argument, False)
        return dict_to_list(dict_vect)

    args_me_arguments_df  = spark.read.format("csv").option("header", "true").option("delimiter", "|", ).option('quote', '"').load('/user/befi8957/topic-ontologies/args-me/corpus-args-me-preprocessed-documents.csv').na.drop()
    arguments = args_me_arguments_df.select("text").rdd.map(lambda r: r[0]).repartition(400)

    ids = (args_me_arguments_df.select("argument-id").rdd.map(lambda r: r[0])).repartition(400)
    # vectors = list(arguments.map(lambda argument:project_argument(argument)).collect())
    # topic_vectors_df = pd.DataFrame({'id':ids,'topic-vector':vectors})
    # topic_vectors_df.to_csv("args-me-esa-topic-vectors.csv",sep=",",encoding='utf-8')
    vectors = arguments.map(lambda argument:project_argument(argument))
    ids_with_vectors=vectors.zip(ids)
    ids_with_vectors.saveAsTextFile('/user/befi8957/args-me-esa-topic-vectors')



project_arguments()