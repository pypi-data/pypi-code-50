import os

from autogluon import TabularPrediction as tabular_task

#### Requieres to install mlmodels
#### print(data)
VERBOSE = False


if __name__ == '__main__':
   VERBOSE = True
   df = get_dataset(data_path="../dataset/milk.csv", uri_type="csv")
   print(df)
