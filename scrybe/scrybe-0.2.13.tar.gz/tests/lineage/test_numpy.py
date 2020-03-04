import scrybe
import json
import numpy as np

from scrybe.internal.depgraph import TrackingGraph


def is_predecessor(pred_obj, obj):
    if not TrackingGraph.has_tracked_obj(obj=pred_obj) or not TrackingGraph.has_tracked_obj(obj=obj):
        return False

    pred_node = TrackingGraph.get_node_for_tracked_object(obj=pred_obj)
    node_lineage = TrackingGraph.get_lineage_of_tracked_object(obj=obj)
    return pred_node.client_id in node_lineage.nodes.keys()


def test_base_cases():
    print("===== Array subsets =====")
    x = np.zeros(12)
    y = x[:4]
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))
    # print("id(x)=%s, id(y)=%s" % (id(x.node), id(y.node)))

    print("===== asarray =====")
    x = np.zeros(12)
    y = np.asarray(x)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))


def test_ufuncs():
    x = np.array([1, 2, 3])
    y = np.array([11, 12, 13])
    z = x + y
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))
    # print("id(x)=%s, id(y)=%s, id(z)=%s" % (id(x.node), id(y.node), id(z.node)))


def test_funcs():
    print("=== np.concatenate ===")
    x = np.array([1, 2, 3])
    y = np.array([11, 12, 13])
    z = np.concatenate([x, y], 0)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))
    print("id(x)=%s, id(y)=%s, id(z)=%s" % (id(x), id(y), id(z)))

    print("=== np.hstack ===")
    x = np.array([1, 2, 3])
    y = np.array([11, 12, 13])
    z = np.hstack((x, y))
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))
    print("id(x)=%s, id(y)=%s, id(z)=%s" % (id(x), id(y), id(z)))

    print("=== np.vstack ===")
    x = np.array([1, 2, 3])
    y = np.array([11, 12, 13])
    z = np.vstack((x, y))
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))
    print("id(x)=%s, id(y)=%s, id(z)=%s" % (id(x), id(y), id(z)))

    print("=== label_binarize transforms ===")
    classes = np.array(["C1"])
    y = np.array(["C1", "C1", "C2", "C1", "C3", "C1", "C2", "C2", "C3"])
    y_in_classes = np.in1d(y, classes)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y_in_classes).to_json(), indent=2))

    y_seen = y[y_in_classes]
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y_seen).to_json(), indent=2))

    indices = np.searchsorted(classes, y_seen)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(indices).to_json(), indent=2))

    y_cumsum = np.cumsum(y_in_classes)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y_cumsum).to_json(), indent=2))


def test_priority():
    x = np.array([[1, 2, 3], [1, 4, 9]])
    z = np.argmax(x, axis=-1)
    type(z)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))

    x = np.array([[1, 2, 3], [1, 4, 9]])
    z = x.argmax(axis=-1)
    print(type(z))
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))


def test_to_categorical():
    ### Check keras to_categorical
    x = np.array([[1, 2, 3], [1, 4, 9]])
    y = x.argmax(axis=-1)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))
    y = np.array(y, dtype='int')
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

    input_shape = y.shape
    if input_shape and input_shape[-1] == 1 and len(input_shape) > 1:
        input_shape = tuple(input_shape[:-1])
    y = y.ravel()
    num_classes = 3
    if not num_classes:
        num_classes = np.max(y) + 1
    n = y.shape[0]
    dtype='float32'
    categorical = np.zeros((n, num_classes), dtype=dtype)
    categorical[np.arange(n), y] = 1

    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(categorical).to_json(), indent=2))

    output_shape = input_shape + (num_classes,)
    categorical = np.reshape(categorical, output_shape)


def test_indexers():
    x = np.array([[1, 1], [2, 4], [3, 9], [4, 16]])
    idx = np.array([0, 1])
    y = x[idx]
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))
    print("id(x)=%s, id(idx)=%s, id(y)=%s" % (id(x), id(idx), id(y)))


def test_save_load():
    x = np.arange(5).astype('float')
    with open('/tmp/test.txt', 'w') as flx:
        np.savetxt(flx, x)

    print("======= np.fromfile ==========")
    y = np.fromfile(open('/tmp/test.txt', 'r'), sep=' ')
    print(TrackingGraph.get_node_for_tracked_object(obj=y).path)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

    print("======= np.loadtxt ==========")
    y = np.loadtxt('/tmp/test.txt')
    print(TrackingGraph.get_node_for_tracked_object(obj=y).path)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

    print("======= np.load (npy) ==========")
    np.save('/tmp/123', np.array([[1, 2, 3], [4, 5, 6]]))
    y = np.load('/tmp/123.npy')
    print(TrackingGraph.get_node_for_tracked_object(obj=y).path)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))

    print("======= np.load (npz) ==========")
    a = np.array([[1, 2, 3], [4, 5, 6]])
    b = np.array([1, 2])
    np.savez('/tmp/123.npz', a=a, b=b)
    data = np.load('/tmp/123.npz')
    y, z = (data['a'], data['b'])
    print(TrackingGraph.get_node_for_tracked_object(obj=y).path)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))
    print(TrackingGraph.get_node_for_tracked_object(obj=z).path)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))


def test_copy():
    x = np.array([[1, 2, 3], [1, 4, 9]])
    y = x.copy()
    print("======= [obj].copy() =========")
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))
    print("id(x)=%s, id(idy)=%s" % (id(x), id(y)))
    y = np.copy(x)
    print("======= np.copy([obj]) =========")
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))
    print("id(x)=%s, id(idy)=%s" % (id(x), id(y)))


def test_pickle():
    import pickle
    x = np.random.rand(23)
    x_pkl = pickle.dumps(x)
    x_2 = pickle.loads(x_pkl)
    print("IsEqual =", np.array_equal(x, x_2))
    print("IsTracked =", TrackingGraph.has_tracked_obj(x_2))
    print("IsParent =", is_predecessor(pred_obj=x, obj=x_2))


def test_compaction():
    x = np.random.rand(20)
    y = x[:10]
    y = np.fabs(y)
    print("======= compaction =========")
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(y).to_json(), indent=2))
    print("id(x)=%s, id(idy)=%s" % (id(x), id(y)))


test_base_cases()

test_ufuncs()

test_funcs()

test_priority()

test_indexers()

test_save_load()

test_copy()

test_pickle()

test_compaction()

x = np.random.rand(12)
y = np.array([1, 4, 6])
z = x[np.ix_(y)]
print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(z).to_json(), indent=2))
#
# x_comp = x > 0.1
# print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(x_comp).to_json(), indent=2))
#
# x_node = TrackingGraph.get_node_for_tracked_object(x)
#
# src_frame = x_node.src_contexts[0].get_src_line_based_on_current_stack()
# print(src_frame)
# print(src_frame.src_line)

# x_node = TrackingGraph.get_node_for_tracked_object(x)
# y_node = TrackingGraph.get_node_for_tracked_object(y)

# y_pred_nodes = [n for n in y_node.predecessors.keys()]
# import gc
# import sys
#
# sys.getrefcount(y_pred_nodes[0])
# y_pred_node = y_pred_nodes[0]
# refs = gc.get_referrers(y_pred_node)
#
# y_pred = [o for o in gc.get_objects() if id(o) == y_pred_node.oid][0]
# sys.getrefcount(y_pred)
# y_refs = gc.get_referrers(y_pred)
