import scrybe
import pandas
import h5py
import numpy as np
import joblib

from scrybe.internal.depgraph import TrackingGraph

scrybe.init("scrybe e2e client testing")
g = h5py.File('data/sample_data.h5', 'r')
dataset = g["train"]
print(dataset.file.filename)
train = np.array(dataset)
train_node = TrackingGraph.get_node_for_tracked_object(obj=train)
assert train_node is not None
assert train_node.is_anchor
train = dataset[:]
train_node = TrackingGraph.get_node_for_tracked_object(obj=train)
assert train_node is not None
assert train_node.is_anchor
train = np.array(train)
train_node = TrackingGraph.get_node_for_tracked_object(obj=train)
assert train_node is not None
print(train.shape)


new_array = np.random.rand(10, 2)
new_array_node = TrackingGraph.get_node_for_tracked_object(obj=new_array)
assert new_array_node is not None
assert not new_array_node.is_anchor
h5 = h5py.File('/tmp/random.h5', 'w')
h5.create_dataset("random", data=new_array)
h5.close()
new_array_node = TrackingGraph.get_node_for_tracked_object(obj=new_array)
assert new_array_node is not None
assert new_array_node.is_anchor


url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
dataset_node = TrackingGraph.get_node_for_tracked_object(obj=dataset)
assert dataset_node is not None
assert dataset_node.is_anchor
labels = dataset['class']
labels.to_pickle(path="/tmp/iris_labels.pkl")
labels_node = TrackingGraph.get_node_for_tracked_object(obj=labels)
assert labels_node is not None
assert labels_node.is_anchor

features = dataset[dataset.columns[:4]]
fp = open("/tmp/features.csv", 'w')
features.to_csv(fp)
fp.close()
features_node = TrackingGraph.get_node_for_tracked_object(obj=features)
assert features_node is not None
assert features_node.is_anchor

new_array = np.random.rand(10, 2)
new_array_node = TrackingGraph.get_node_for_tracked_object(obj=new_array)
assert new_array_node is not None
assert not new_array_node.is_anchor
with open('/tmp/random.pkl', 'wb') as fp:
    joblib.dump(new_array, fp)
    fp.close()
new_array_node = TrackingGraph.get_node_for_tracked_object(obj=new_array)
assert new_array_node is not None
assert new_array_node.is_anchor

new_array = joblib.load('/tmp/random.pkl', 'rb')
new_array_node = TrackingGraph.get_node_for_tracked_object(obj=new_array)
assert new_array_node is not None
assert new_array_node.is_anchor

sepals = dataset[dataset.columns[:2]]
sepals_node = TrackingGraph.get_node_for_tracked_object(obj=sepals)
assert sepals_node is not None
assert not sepals_node.is_anchor
with open('/tmp/sepals.pkl', 'wb') as fp:
    joblib.dump(sepals, fp)
    fp.close()
sepals_node = TrackingGraph.get_node_for_tracked_object(obj=sepals)
assert sepals_node is not None
assert sepals_node.is_anchor

# sepals = joblib.load('/tmp/sepals.pkl', 'r')
# sepals_node = TrackingGraph.get_node_for_tracked_object(obj=sepals)
# assert sepals_node is not None
# assert sepals_node.is_anchor


# print(dataset.groupby('class').size())

