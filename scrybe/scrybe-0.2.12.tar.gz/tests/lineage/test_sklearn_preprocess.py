import json
import numpy as np

from sklearn import preprocessing
from sklearn.impute import SimpleImputer
from scrybe.internal.depgraph import TrackingGraph


input_arrays = dict(
    flt_2d=np.array([[1., -1., 2.], [2., 0., 0.], [0., 1., -1.]]),
    binary_2d=np.array([[1, 0, 1], [1, 0, 0], [0, 1, 1]]),
    int_1d=np.array([1, 2, 2, 6]),
    int_2d=np.array([[1, 1], [1, 2], [1, 2], [1, 6]])
)


all_members = ['Binarizer', 'FunctionTransformer', 'Imputer', 'KBinsDiscretizer', 'KernelCenterer', 'LabelBinarizer',
               'LabelEncoder', 'MaxAbsScaler', 'MinMaxScaler', 'MultiLabelBinarizer', 'Normalizer', 'OneHotEncoder',
               'OrdinalEncoder', 'PolynomialFeatures', 'PowerTransformer', 'QuantileTransformer', 'RobustScaler',
               'StandardScaler', 'add_dummy_feature', 'binarize', 'maxabs_scale', 'minmax_scale', 'normalize',
               'power_transform', 'quantile_transform', 'robust_scale', 'scale']

data_format = ['flt_2d', 'flt_2d', 'flt_2d', 'flt_2d', 'flt_2d', 'binary_2d', 'int_1d', 'flt_2d', 'flt_2d', 'flt_2d',
               'flt_2d', 'int_2d', 'flt_2d', 'flt_2d', 'flt_2d', 'flt_2d', 'flt_2d', 'flt_2d', 'flt_2d', 'flt_2d',
               'flt_2d', 'flt_2d', 'flt_2d', 'int_2d']


def check_if_associated(X_in, X_out):
    if not TrackingGraph.has_tracked_obj(obj=X_out):
        return False
    out_lineage = TrackingGraph.get_lineage_of_tracked_object(X_out)
    X_in_node = TrackingGraph.get_node_for_tracked_object(obj=X_in)
    return X_in_node.client_id in set(out_lineage.nodes.keys())


def test_simple_imputer():
    X_in = np.array([[1, 2], [np.nan, 3], [7, 6]])
    imp = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer = imp.fit(X_in)
    X_out = imputer.transform(X_in)
    print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(X_out).to_json(), indent=2))
    print(check_if_associated(X_in=X_in, X_out=X_out))


def test_fn(fn_name, X_in, verbose=False):
    fn = preprocessing.__dict__[fn_name]
    X_out = fn(X_in)
    is_associated = check_if_associated(X_in=X_in, X_out=X_out)
    if verbose:
        print(fn_name, ":", is_associated)
        if TrackingGraph.has_tracked_obj(X_out):
            print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(X_out).to_json(), indent=2))
        else:
            print("Result is untracked")
    return is_associated


def test_class(cls_name, X_in, verbose=False):
    cls_obj = preprocessing.__dict__[cls_name]
    obj = cls_obj()

    obj = obj.fit(X_in)
    X_out = obj.transform(X_in)
    is_associated = check_if_associated(X_in=X_in, X_out=X_out)
    if verbose:
        print(cls_name, ":", is_associated)
        if TrackingGraph.has_tracked_obj(X_out):
            print(json.dumps(TrackingGraph.get_lineage_of_tracked_object(X_out).to_json(), indent=2))
        else:
            print("Result is untracked")
    return is_associated


def test_module(verbose=False):
    import warnings
    warnings.filterwarnings("ignore")
    failed_classes = list()
    failed_fns = list()
    for i in range(len(all_members)):
        member = all_members[i]
        data_format_to_use = data_format[i] if i < len(data_format) else 'flt_2d'
        data = input_arrays[data_format_to_use]
        print("Testing :: ", member, " :: ", data_format_to_use)
        if member[0].isupper():
            if not test_class(cls_name=member, X_in=data, verbose=verbose):
                failed_classes.append(member)
        else:
            if not test_fn(fn_name=member, X_in=data, verbose=verbose):
                failed_fns.append(member)
    return failed_classes, failed_fns


failed_cases = test_module(verbose=True)
print(failed_cases)

failed_cls_name = failed_cases[0][0]
idx = all_members.index(failed_cls_name)
data_format_to_use = data_format[idx] if idx < len(data_format) else 'flt_2d'
data = input_arrays[data_format_to_use]
test_class(cls_name=failed_cls_name, X_in=data, verbose=True)

