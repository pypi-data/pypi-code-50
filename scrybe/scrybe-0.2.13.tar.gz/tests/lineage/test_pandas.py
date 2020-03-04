import scrybe
import json
import pandas as pd
import numpy as np

from scrybe.internal.depgraph import TrackingGraph


def get_rand_bool():
    import random
    return random.randint(0, 1) == 1


def is_predecessor(pred_obj, obj):
    if not TrackingGraph.has_tracked_obj(obj=pred_obj) or not TrackingGraph.has_tracked_obj(obj=obj):
        return False

    pred_node = TrackingGraph.get_node_for_tracked_object(obj=pred_obj)
    node_lineage = TrackingGraph.get_lineage_of_tracked_object(obj=obj)
    return pred_node.client_id in node_lineage.nodes.keys()


def test_pickle():
    import pickle
    x = pd.DataFrame([(1, 1), (2, 4)])
    x_pkl = pickle.dumps(x)
    x_2 = pickle.loads(x_pkl)
    print("IsEqual =", x.equals(x_2))
    print("IsTracked =", TrackingGraph.has_tracked_obj(x_2))
    print("IsParent =", is_predecessor(pred_obj=x, obj=x_2))

    x = pd.Series([1, 1, 2, 4])
    x_pkl = pickle.dumps(x)
    x_2 = pickle.loads(x_pkl)
    print("IsEqual =", x.equals(x_2))
    print("IsTracked =", TrackingGraph.has_tracked_obj(x_2))
    print("IsParent =", is_predecessor(pred_obj=x, obj=x_2))


x = pd.read_csv('../data/SalesJan2009.csv')
x_node = TrackingGraph.get_node_for_tracked_object(obj=x)
print(x_node.name)
print(x_node.path)

# x.info()

y = x['Price']
assert is_predecessor(x, y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

y = y[:50]
assert TrackingGraph.has_tracked_obj(y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))


y = x.loc[1:2]
assert is_predecessor(x, y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

y = x.iloc[23:25]
assert is_predecessor(x, y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

y = x['Price'] == "1200"
assert is_predecessor(x, y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

# Indexer cases:
cols = ['Product', 'Price']
y = x[cols]
assert is_predecessor(x, y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

cols = pd.Series(['Product', 'Price'])
y = x[cols]
assert is_predecessor(x, y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

y = x.loc[x['Price'] == "1200"]
assert is_predecessor(x, y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

y = pd.DataFrame({'row_id': [i for i in range(len(x))]})
z = y.loc[x['Product'] == "Product1"]
assert is_predecessor(y, z)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))

y = pd.DataFrame({'train': [get_rand_bool() for i in range(len(x))]})
z = x.loc[y['train']]
assert is_predecessor(y, z)
assert is_predecessor(x, z)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))

y = pd.Series([get_rand_bool() for i in range(len(x))])
z = x.loc[y]
assert is_predecessor(y, z)
assert is_predecessor(x, z)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))

y = [get_rand_bool() for i in range(len(x))]
z = x.loc[y]
assert is_predecessor(x, z)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))


idx = pd.Series([23, 24, 25])
y = x.iloc[idx]
assert is_predecessor(x, y)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))


# Create a dataframe
raw_data = {'first_name': ['Jason', 'Molly', np.nan, np.nan, np.nan],
            'nationality': ['USA', 'USA', 'France', 'UK', 'UK'],
            'age': [42, 52, 36, 24, 70]}
df2 = pd.DataFrame(raw_data, columns=['first_name', 'nationality', 'age'])
cond_1 = df2['first_name'].notnull()
cond_2 = df2['nationality'] == "USA"
final_cond = cond_1 & cond_2
df3 = df2[final_cond]
assert is_predecessor(df2, df3)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(df3).to_json(), indent=2))
# print("ids = ", id(df2), id(cond_1), id(cond_2), id(final_cond), id(df3))


df = pd.DataFrame([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)], columns=['x', 'y'])

test_pickle()


df2 = pd.DataFrame([(6, 36), (7, 49)], columns=['x', 'y'])
df3 = pd.concat([df, df2])
assert is_predecessor(df2, df3)
assert is_predecessor(df, df3)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(df3).to_json(), indent=2))

df3 = pd.merge(df, df2)
assert is_predecessor(df2, df3)
assert is_predecessor(df, df3)
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(df3).to_json(), indent=2))

import scrybe
from scrybe.internal.depgraph import TrackingGraph
import pandas as pd
import numpy as np
df = pd.DataFrame([(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)], columns=['x', 'y'])
array = np.arange(5)
df['z'] = array
# df.assign(w=array)
assert TrackingGraph.has_tracked_obj(array)
assert TrackingGraph.has_tracked_obj(df.z)
# assert is_predecessor(array, df.w) or array is df.w
assert is_predecessor(array, df.z)

df2 = pd.DataFrame([(1, 1), (2, 4), (3, 6), (4, 8), (5, 10)], columns=['x', 'y'])
df['x'] = df2['y']
assert is_predecessor(df2.y, df.x)


df[['x', 'y']] = df2[['y', 'x']]
assert TrackingGraph.has_tracked_obj(df2.y)
assert TrackingGraph.has_tracked_obj(df2.x)
assert TrackingGraph.has_tracked_obj(df.y)
assert TrackingGraph.has_tracked_obj(df.x)

print(id(df2.y), id(df.x))
assert is_predecessor(df2, df.x)
assert is_predecessor(df2, df.y)

array = df.values[:, 1:]
assert TrackingGraph.get_node_for_tracked_object(df).client_id in TrackingGraph.get_lineage_of_tracked_object(obj=array).nodes
df[['x', 'y']] = array
assert TrackingGraph.get_node_for_tracked_object(array).client_id in TrackingGraph.get_lineage_of_tracked_object(obj=df.x).nodes
