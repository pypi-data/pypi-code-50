from collections import Iterable, Sized

from scrybe.internal.depgraph.nodes import ArtifactType
from scrybe.internal.util import get_func_arg_names, get_func_req_params, get_default_func_params

MAX_COLUMNS = 50
MAX_ROWS = 100


STATS_FUNCS = ['sem', 'var', 'std', 'mean', 'skew', 'kurt', 'median', 'max', 'min', 'ptp']

NDFRAME_STATS = [
    ('pandas.core.generic', '_make_stat_function_ddof'),
    ('pandas.core.generic', '_make_stat_function'),
]

PANDAS_NUMPY_STATS = [
    ('pandas.core.generic', 'NDFrame.describe'),
    ('pandas.core.frame', 'DataFrame.count'),
    ('pandas.core.frame', 'DataFrame.nunique'),
    ('pandas.core.series', 'Series.count'),
    ('pandas.core.base', 'IndexOpsMixin.nunique'),
    # TODO(chandra): Will be added if users ask for this
    # ('numpy.core.fromnumeric', 'amax'),
    # ('numpy.core.fromnumeric', 'amin'),
    # ('numpy.core.fromnumeric', 'mean'),
    # ('numpy.core.fromnumeric', 'ptp'),
    # ('numpy.core.fromnumeric', 'std'),
    # ('numpy.core.fromnumeric', 'var'),
    # ('numpy.lib.function_base', 'median'),
]

QUANTILE_STATS = [
    ('pandas.core.frame', 'DataFrame.quantile'),
    ('pandas.core.series', 'Series.quantile'),
    ('numpy.lib.function_base', 'quantile'),
]

CO_STATS = [
    ('pandas.core.frame', 'DataFrame.corr'),
    ('pandas.core.frame', 'DataFrame.cov'),
    ('pandas.core.series', 'Series.corr'),
    ('pandas.core.series', 'Series.cov'),
    ('pandas.core.frame', 'DataFrame.corrwith'),
    ('numpy.lib.function_base', 'cov'),
    ('numpy.lib.function_base', 'corrcoef'),
]

VALUE_STATS = [
    ('pandas.core.series', 'Series.value_counts'),
    ('pandas.core.series', 'Series.unique'),
    ('numpy.lib.arraysetops', 'unique'),
]

INFO_STATS = [
    ('pandas.core.frame', 'DataFrame.info'),
]


def get_dict_from_2d_numpy_array(obj):
    return dict((i, dict(enumerate(obj[i]))) for i in range(obj.shape[0]))


def get_scalar_value(obj):
    if isinstance(obj, str) or isinstance(obj, int) or isinstance(obj, float):
        return obj
    else:
        try:
            import numpy
            if isinstance(obj, (numpy.int_, numpy.intc, numpy.intp, numpy.int8,
                                numpy.int16, numpy.int32, numpy.int64, numpy.uint8,
                                numpy.uint16, numpy.uint32, numpy.uint64)):
                return int(obj)
            elif isinstance(obj, (numpy.float_, numpy.float16, numpy.float32,
                                  numpy.float64)):
                return float(obj)
        except ImportError:
            pass
        try:
            int_val = int(obj)
            float_val = float(obj)
            if int_val == float_val:
                return int_val
            else:
                return float_val
        except Exception:
            return None


def get_metric(obj, stats_func, axis):
    if not isinstance(obj, Iterable) and not isinstance(obj, Sized):
        val = get_scalar_value(obj)
        if val is None:
            return None
        else:
            return {stats_func: val}, ArtifactType.STATS_NUMBER
    if axis is not None and axis != 0:
        return None
    # noinspection PyBroadException
    try:
        import numpy
        if isinstance(obj, numpy.ndarray):
            if len(obj.shape) != 1 or obj.shape[0] > MAX_COLUMNS:
                return None
            return dict(map(lambda t: (str(t[0]), {stats_func: t[1]}), enumerate(obj))), ArtifactType.TABLE
    except Exception:
        pass
    try:
        # noinspection PyPackageRequirements
        from pandas import DataFrame, Series
        if isinstance(obj, DataFrame):
            if obj.shape[0] > MAX_ROWS or obj.shape[1] > MAX_COLUMNS:
                return None
            return obj.to_dict(), ArtifactType.TABLE
        elif isinstance(obj, Series):
            column_dict = obj.to_dict()
            if stats_func == 'describe':
                return column_dict, ArtifactType.STATS_NUMBER
            column_stats_dict = dict()
            for key in column_dict:
                column_stats_dict[key] = {stats_func: column_dict[key]}
            return column_stats_dict, ArtifactType.TABLE
    except Exception:
        pass
    return None


def get_values(ret_val, orig_func, *args, **kwargs):
    counts = None
    if orig_func.__name__ == 'value_counts':
        unique = list(ret_val.to_dict().keys())
        counts = list(ret_val.to_dict().values())
    elif isinstance(ret_val, tuple) and len(ret_val) >= 2:
        if len(ret_val[0].shape) > 2 or (len(ret_val[0].shape) > 1 and ret_val[0].shape[1] > MAX_COLUMNS):
            return None
        unique = ret_val[0].tolist()
        counts_index = -1
        arg_names = get_func_arg_names(orig_func)
        return_index, return_inverse, return_counts, axis = get_func_req_params(arg_names, [1, 2, 3, 4], *args, **kwargs)
        if axis is not None and axis != 0:
            return None
        if return_counts:
            counts_index = 1
            counts_index += 1 if return_index else 0
            counts_index += 1 if return_inverse else 0
        else:
            # TODO(chandra): Unique without counts will be send if users ask for this
            return
        if counts_index > 0:
            counts = list(ret_val[counts_index])
    else:
        # noinspection PyBroadException
        try:
            unique = ret_val.tolist()
        except Exception:
            return None
    num_values = len(unique)
    if num_values > MAX_ROWS:
        unique = unique[:MAX_ROWS]
        unique.append("Other Values (%d)" % (num_values - MAX_ROWS))
        if counts is not None:
            sum_of_rest = sum(counts[MAX_ROWS:])
            counts = counts[:MAX_ROWS]
            counts.append(sum_of_rest)
    values = {'unique': unique}
    if counts is not None:
        values['counts'] = counts
    return values


def get_co_stats(obj):
    if not isinstance(obj, Iterable) and not isinstance(obj, Sized):
        val = get_scalar_value(obj)
        if val is None:
            return None
        else:
            return val
    try:
        import numpy
        if isinstance(obj, numpy.ndarray):
            if len(obj.shape) != 2 or obj.shape[0] > MAX_COLUMNS or obj.shape[1] > MAX_COLUMNS:
                return None
            return get_dict_from_2d_numpy_array(obj), ArtifactType.TABLE
    except Exception:
        pass
    try:
        # noinspection PyPackageRequirements
        from pandas import DataFrame, Series
        if isinstance(obj, DataFrame):
            if obj.shape[0] > MAX_COLUMNS or obj.shape[1] > MAX_COLUMNS:
                return None
            return obj.to_dict(), ArtifactType.TABLE
        if isinstance(obj, Series):
            if obj.shape[0] > MAX_ROWS:
                return None
            return obj.to_dict(), ArtifactType.STATS_NUMBER
    except Exception:
        pass
    return None


def get_param(name, arg_names, orig_func, *args, **kwargs):
    if name in arg_names:
        name_index = arg_names.index(name)
        name_val = get_func_req_params(arg_names, [name_index], *args, **kwargs)
        if name_val is not None:
            return name_val
        else:
            args, default_dict = get_default_func_params(orig_func)
            if name in default_dict:
                name_val = default_dict[name]
                return name_val
    return None


def get_artifact_identifier(artifact_type: ArtifactType, stats_type: str):
    if artifact_type == ArtifactType.STATS_NUMBER:
        return "stats"
    elif artifact_type == ArtifactType.TABLE:
        return "%s_%s" % (stats_type, 'table')
    elif artifact_type == ArtifactType.DATA_VALUES:
        return "values"


def is_stats_function(func):
    module_name = func.__module__
    func_name = func.__name__
    if module_name in ['pandas.core.series', 'pandas.core.frame'] and func_name in STATS_FUNCS:
        return True
    all_func = PANDAS_NUMPY_STATS + QUANTILE_STATS + CO_STATS + VALUE_STATS
    for patched_module_name, class_func_name in all_func:
        if patched_module_name == module_name:
            patched_func_name = class_func_name.split(".")[-1]
            if func_name == patched_func_name:
                return True
    return False
