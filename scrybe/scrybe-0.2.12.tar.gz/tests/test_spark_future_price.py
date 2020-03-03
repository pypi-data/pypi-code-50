import shutil

import scrybe
import os

from pyspark.ml.evaluation import RegressionEvaluator
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import types, functions as F
from pyspark.sql.functions import unix_timestamp
from pyspark.sql.types import *
from pyspark.sql import Window
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.feature import VectorAssembler


scrybe.init("scrybe e2e client testing")
scrybe.set_label("Spark Testing")

sc = SparkContext()
sc.setSystemProperty("com.amazonaws.services.s3.enableV4", "true")
spark = SparkSession.builder.getOrCreate()

# file_path_prefix = "/Users/chandra/scrybe/clientsdk/scrybe_ml/tests/data/predict-future-sales/"
file_path_prefix = "s3a://scrybe-test-datasets/"

sales_train_file = file_path_prefix + "sales_train.csv"
cat_file = file_path_prefix + "item_categories.csv"
items_file = file_path_prefix + "items.csv"
shops_file = file_path_prefix + "shops.csv"
test_file = file_path_prefix + "test.csv"


sales_train = spark.read.csv(sales_train_file, header=True, inferSchema=True)
categories = spark.read.csv(cat_file, header=True, inferSchema=True)
items = spark.read.csv(items_file, header=True, inferSchema=True)
shops = spark.read.csv(shops_file, header=True, inferSchema=True)
sales_test = spark.read.csv(test_file, header=True, inferSchema=True)
sales_train.show()


def cast_types(df):
    dtypes = df.dtypes
    if "ID" in df.columns:
        df = df.withColumn("ID", df["ID"].cast(types.IntegerType()))
    if "date" in df.columns:
        # df = df.withColumn("date",df['date'].cast(types.DateType()))
        df = df.withColumn("date", F.from_unixtime(unix_timestamp('date', 'dd.MM.yyyy')))
    if "date_block_num" in df.columns:
        df = df.withColumn("date_block_num", df["date_block_num"].cast(types.ByteType()))
    if "shop_id" in df.columns:
        df = df.withColumn("shop_id", df["shop_id"].cast(types.ByteType()))
    if "item_id" in df.columns:
        df = df.withColumn("item_id", df["item_id"].cast(types.ShortType()))
    if "item_price" in df.columns:
        df = df.withColumn("item_price", df["item_price"].cast(types.FloatType()))
    if "item_cnt_day" in df.columns:
        df = df.withColumn("item_cnt_day", df["item_cnt_day"].cast(types.FloatType()))
    return df


sales_train = cast_types(sales_train)
train = sales_train.join(items, on='item_id').join(shops, on='shop_id').join(categories, on='item_category_id')
train = train.cache()
print("Sales Join with others done")
print(train.count())
train.show()

print('Initial Training Set Size: %s' % train.count())
test_shop_ids = sales_test.select('shop_id').distinct()
test_item_ids = sales_test.select('item_id').distinct()
train_filtered = train.join(test_shop_ids, "shop_id")
train_filtered = train_filtered.join(test_item_ids, "item_id")
print('Filtered Training Set Size: %s' % train_filtered.count())
train_filtered = train_filtered.sample(fraction=0.01)
print("Sampling done")
train_filtered.show()

train_monthly = train_filtered[
    ['date', 'date_block_num', 'shop_id', 'item_category_id', 'item_id', 'item_price', 'item_cnt_day']]
train_monthly.show()
print("Monthly train data created with columns")

group = train_monthly.sort('date').groupby("date_block_num", "shop_id", "item_category_id", "item_id")
train_monthly = group.agg(F.mean('item_price').alias('avg_item_price'), F.mean('item_cnt_day').alias('avg_item_cnt'),
                          F.sum('item_price').alias('item_price'), F.sum('item_cnt_day').alias('item_cnt'),
                          F.count('item_cnt_day').alias('transactions'))
train_monthly.show()
print("Monthly train data groupby done with agg")

shop_ids = train_monthly.select('shop_id').distinct().collect()
item_ids = train_monthly.select('item_id').distinct().collect()
shop_item_pairs = []
for i in range(34):
    for shop in shop_ids:
        for item in item_ids:
            shop_item_pairs.append([int(i), int(shop.__getitem__('shop_id')), int(item.__getitem__('item_id'))])
shop_item_pairs = spark.createDataFrame(shop_item_pairs, ['date_block_num', 'shop_id', 'item_id'])

train_monthly = shop_item_pairs.join(train_monthly, on=['date_block_num', 'shop_id', 'item_id'], how='left')
train_monthly = train_monthly.fillna(0)
train_monthly.describe().show()
print("Join with shop item pairs done")

year = F.udf(lambda x: ((x // 12) + 2013), IntegerType())
month = F.udf(lambda x: (x % 12), IntegerType())
train_monthly = train_monthly.withColumn("year", year(train_monthly.date_block_num))
train_monthly = train_monthly.withColumn("month", month(train_monthly.date_block_num))
train_monthly.show(10)

train_monthly = train_monthly.filter('item_cnt >= 0 and item_cnt <= 20 and item_price < 400000')
train_monthly = train_monthly.withColumn("item_cnt_month", F.lag("item_cnt", 1).over(
    Window.partitionBy("shop_id", "item_id").orderBy("date_block_num")))

train_monthly = train_monthly.withColumn('item_cnt_mean', F.avg('item_cnt').over(
    Window.partitionBy("shop_id", "item_category_id", "item_id").orderBy("date_block_num").rangeBetween(-2, 0)))
train_monthly = train_monthly.withColumn('item_cnt_std', F.stddev('item_cnt').over(
    Window.partitionBy("shop_id", "item_category_id", "item_id").orderBy("date_block_num").rangeBetween(-2, 0)))

train_monthly = train_monthly.withColumn("item_cnt_shifted1", F.lag("item_cnt", 1).over(
    Window.partitionBy("shop_id", "item_category_id", "item_id").orderBy("date_block_num")))
train_monthly = train_monthly.withColumn("item_cnt_shifted2", F.lag("item_cnt", 2).over(
    Window.partitionBy("shop_id", "item_category_id", "item_id").orderBy("date_block_num")))
train_monthly = train_monthly.withColumn("item_cnt_shifted3", F.lag("item_cnt", 3).over(
    Window.partitionBy("shop_id", "item_category_id", "item_id").orderBy("date_block_num")))
print("With column window done")
train_monthly = train_monthly.fillna(0)
print("FillNA done")

train_set = train_monthly.filter(train_monthly['date_block_num'] >= 3).filter(train_monthly['date_block_num'] < 28)
validation_set = train_monthly.filter(train_monthly['date_block_num'] >= 28).filter(
    train_monthly['date_block_num'] < 33)
test_set = train_monthly.filter(train_monthly['date_block_num'] == 33)
train_set.dropna(subset=['item_cnt_month'])
validation_set.dropna(subset=['item_cnt_month'])
train_set.dropna()
validation_set.dropna()
total_count = train_monthly.count()
train_count = train_set.count()
val_count = validation_set.count()
test_count = test_set.count()
print("Data spliting to train, val test done")
print('Train set records:', train_count)
print('Validation set records:', val_count)
print('Test set records:', test_count)
print('Train set records: %s (%.f%% of complete data)' % (train_count, (train_count * 100 / total_count)))
print('Validation set records: %s (%.f%% of complete data)' % (val_count, (val_count * 100 / total_count)))
print('Test set records: %s (%.f%% of complete data)' % (test_count, (test_count * 100 / total_count)))

train_set = train_set.withColumn('gp_shop_mean', F.avg('item_cnt_month').over(Window.partitionBy("shop_id")))
train_set = train_set.withColumn('gp_item_mean', F.avg('item_cnt_month').over(Window.partitionBy("item_id")))
validation_set = validation_set.withColumn('gp_shop_mean', F.avg('item_cnt_month').over(Window.partitionBy("shop_id")))
validation_set = validation_set.withColumn('gp_item_mean', F.avg('item_cnt_month').over(Window.partitionBy("item_id")))
test_set = test_set.withColumn('gp_shop_mean', F.avg('item_cnt_month').over(Window.partitionBy("shop_id")))
test_set = test_set.withColumn('gp_item_mean', F.avg('item_cnt_month').over(Window.partitionBy("item_id")))
test_set.show(10)

train = train_set.drop('date_block_num')
validation = validation_set.drop('date_block_num')
test = test_set.drop('date_block_num', 'item_cnt_month')
test = sales_test.join(test, on=['shop_id', 'item_id'], how="full")
test = test.fillna(0)  # X_test.mean())
test.drop('ID')

train.drop('item_category_id')
validation.drop('item_category_id')
test.drop('item_category_id')
rf_features = ['shop_id', 'item_id', 'item_cnt', 'transactions', 'year', 'item_cnt_mean', 'item_cnt_std',
               'item_cnt_shifted1', 'item_cnt_month']  # , 'shop_mean', 'item_mean', 'item_trend', 'avg_item_cnt']
rf_train = train[rf_features]
rf_val = validation[rf_features]
test_features = ['shop_id', 'item_id', 'item_cnt', 'transactions', 'year', 'item_cnt_mean', 'item_cnt_std',
                 'item_cnt_shifted1']  # , 'shop_mean', 'item_mean', 'item_trend', 'avg_item_cnt']
print("RF train and val created")

assembler_input_cols = ['shop_id', 'item_id', 'transactions', 'year', 'item_cnt_mean', 'item_cnt_std',
                        'item_cnt_shifted1']
assembler = VectorAssembler(
    inputCols=assembler_input_cols,
    outputCol="features")
transformed = assembler.transform(rf_train)
print("Feature column created")
rf = RandomForestRegressor(featuresCol="features", labelCol="item_cnt_month")
rf_test = test[test_features]
rf_test.show(10)
rf_test.count()
print("RF test created")


rf_model = rf.fit(transformed)
rf_val_pred = rf_model.transform(assembler.transform(rf_val))
evaluator = RegressionEvaluator(predictionCol="prediction", labelCol="item_cnt_month", metricName="rmse")
rmse = evaluator.evaluate(dataset=rf_val_pred)
print("RMSE:", rmse)
predictions = rf_model.transform(assembler.transform(rf_test))
predictions = predictions.select(["shop_id", "prediction"])

prediction_path = "/tmp/tests/data/predict-future-sales"
if os.path.exists(prediction_path):
    shutil.rmtree(prediction_path)

os.makedirs(prediction_path, exist_ok=True)
predictions.write.csv(prediction_path + "/predictions")

