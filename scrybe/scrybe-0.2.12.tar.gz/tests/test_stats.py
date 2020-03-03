import scrybe
import pandas
import numpy as np


scrybe.init("scrybe e2e client testing")
# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

scrybe.log_custom_data_statistic(dataset, "custom_stat", 150)

import time
start_time = time.time()
dataset.info(verbose=True)

dataset.describe()
dataset.sem()
dataset.var()
dataset.std()
dataset.mean()
dataset.skew()
dataset.kurt()
dataset.median()
dataset.max()
dataset.min()
dataset.count()
dataset.nunique()

dataset['sepal-length'].describe()
dataset['sepal-length'].sem()
dataset['sepal-length'].var()
dataset['sepal-length'].std()
dataset['sepal-length'].mean()
dataset['sepal-length'].skew()
dataset['sepal-length'].kurt()
dataset['sepal-length'].median()
dataset['sepal-length'].max()
dataset['sepal-length'].min()
# dataset['sepal-length'].ptp()
dataset['sepal-length'].count()
dataset['sepal-length'].nunique()


dataset['sepal-length'].value_counts()
dataset['sepal-length'].unique()
data = np.random.rand(150, 5)
np.unique(data, return_counts=True, return_index=True, return_inverse=True, axis=1)
np.unique(data, return_counts=True, return_index=True, return_inverse=True, axis=0)
np.unique(data, return_counts=True, return_index=True, return_inverse=True)
np.unique(data, return_counts=False, return_index=True, return_inverse=True)
np.max(data)
np.min(data)
np.mean(data)
np.ptp(data)
np.std(data)
np.var(data)
np.median(data)

np.max(data, axis=0)
np.min(data, axis=0)
np.mean(data, axis=0)
np.ptp(data, axis=0)
np.std(data, axis=0)
np.var(data, axis=0)
np.median(data, axis=0)

np.max(data, axis=1)
np.min(data, axis=1)
np.mean(data, axis=1)
np.ptp(data, axis=1)
np.std(data, axis=1)
np.var(data, axis=1)
np.median(data, axis=1)

np.quantile(data, q=0.75)
dataset.quantile(q=0.75)
dataset['sepal-length'].quantile(q=0.75)

dataset.corr()
dataset.cov()
dataset.corrwith(other=dataset)
dataset['sepal-length'].cov(other=dataset['sepal-width'])
dataset['sepal-length'].corr(other=dataset['sepal-width'])

np.cov(data, rowvar=False)
np.corrcoef(data, rowvar=False)
np.cov(data, y=data, rowvar=False)
np.corrcoef(data, y=data, rowvar=False)

np.cov(data, y=data, rowvar=True)
np.corrcoef(data, y=data, rowvar=True)

np.cov(data[:, 0], y=data[:, 1], rowvar=True)
np.corrcoef(data[:, 0], y=data[:, 1], rowvar=True)

np.cov(data[:, 0], y=data[:, 1], rowvar=False)
np.corrcoef(data[:, 0], y=data[:, 1], rowvar=False)

print("Total time: ", time.time() - start_time)