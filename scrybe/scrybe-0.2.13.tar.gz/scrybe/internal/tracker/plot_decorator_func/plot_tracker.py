import functools

from scrybe.internal.depgraph import TrackingGraph
from scrybe.internal.threading_util import *
from scrybe.internal.tracker.plot_decorator_func.plot_util import MATPLOTLIB_FUNC_PLOT, MATPLOTLIB_FUNC_X, \
    MATPLOTLIB_FUNC_X_Y, MATPLOTLIB_FUNC_ARANGE_TYPE, PANDAS_PLOT_ACCESSOR, PANDAS_PLOT_FUNC, PANDAS_PLOT_TABLE, \
    SEABORN_FUNC_X_Y, SEABORN_FUNC_X, DATASET_NAME_SETTER_CLASS_INIT, SEABORN_CLASS_FUNC, AXES_SETTERS, \
    create_and_upload_plot
from scrybe.internal.util import get_func_req_params, get_func_arg_names


def _unset_plot_in_progress_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        ret_val = func(*args, **kwargs)
        unset_plotting_in_progress()
        return ret_val
    return inner


def plot_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    if is_plotting_in_progress():
        return False
    set_plotting_in_progress()


def plot_func_exception_handler_decorator(metadata_dict, orig_func, ret_val, *args, **kwargs):
    unset_plotting_in_progress()


def set_dataset_name_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    data = get_func_req_params(arg_names, [1], *args, **kwargs)
    data_name = get_func_req_params(arg_names, [1], *arg_obj_names, **kwargs_obj_names)
    if TrackingGraph.has_tracked_obj(obj=data):
        data_node = TrackingGraph.get_node_for_tracked_object(obj=data)
        data_node.set_node_name_if_not_final(data_name)


@_unset_plot_in_progress_decorator
def handle_mpl_plot_class_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    plot_args = args[1:]
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    func_name = orig_func.__name__
    datasets = []
    dataset_names = []
    if 'data' in kwargs and kwargs['data'] is not None:
        datasets.append(kwargs['data'])
        if 'data' in kwargs_obj_names:
            dataset_names.append(kwargs_obj_names['data'])
    else:
        while plot_args:
            data_items, plot_args = plot_args[:2], plot_args[2:]
            data_item_names, arg_obj_names = arg_obj_names[:2], arg_obj_names[2:]
            if plot_args and isinstance(plot_args[0], str):
                plot_args = plot_args[1:]
                arg_obj_names = arg_obj_names[1:]
            for i in range(len(data_items)):
                dataset = data_items[i]
                if len(data_item_names) > i:
                    dataset_name = data_item_names[i]
                else:
                    dataset_name = None
                datasets.append(dataset)
                dataset_names.append(dataset_name)
    fig = None
    ax = args[0]
    if hasattr(ax, 'figure') and ax.figure is not None:
        fig = ax.figure
    create_and_upload_plot(datasets=datasets, dataset_names=dataset_names, plot_func_name=func_name, fig=fig)


@_unset_plot_in_progress_decorator
def handle_x_type_class_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    func_name = orig_func.__name__
    arg_names = get_func_arg_names(orig_func)
    data_index = -1
    if 'data' in arg_names and arg_names.index('data') != 1:
        data_index = arg_names.index('data')
    dataset_x, data = get_func_req_params(arg_names, [1, data_index], *args, **kwargs)
    dataset_x_name, data_name = get_func_req_params(arg_names, [1, data_index], *arg_obj_names, **kwargs_obj_names)
    ax = args[0]
    if hasattr(ax, 'figure') and ax.figure is not None:
        fig = ax.figure
    create_and_upload_plot(datasets=[dataset_x, data], dataset_names=[dataset_x_name, data_name],
                           plot_func_name=func_name, fig=fig)


@_unset_plot_in_progress_decorator
def handle_x_y_type_class_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    func_name = orig_func.__name__
    arg_names = get_func_arg_names(orig_func)
    data_index = -1
    if 'data' in arg_names and arg_names.index('data') != 1 and arg_names.index('data') != 2:
        data_index = arg_names.index('data')
    dataset_x, dataset_y, data = get_func_req_params(arg_names, [1, 2, data_index], *args, **kwargs)
    dataset_x_name, dataset_y_name, data_name = get_func_req_params(arg_names, [1, 2, data_index], *arg_obj_names,
                                                                    **kwargs_obj_names)
    ax = args[0]
    if hasattr(ax, 'figure') and ax.figure is not None:
        fig = ax.figure
    create_and_upload_plot(datasets=[dataset_x, dataset_y, data],
                           dataset_names=[dataset_x_name, dataset_y_name, data_name],
                           plot_func_name=func_name, fig=fig)


@_unset_plot_in_progress_decorator
def handle_arange_type_class_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    func_name = orig_func.__name__
    datasets = [args[1]]
    dataset_names = [arg_obj_names[1]]
    # Try a second one
    if len(args) > 2:
        datasets.append(args[2])
        dataset_names.append(arg_obj_names[2])
    ax = args[0]
    if hasattr(ax, 'figure') and ax.figure is not None:
        fig = ax.figure
    create_and_upload_plot(datasets=datasets, dataset_names=dataset_names, plot_func_name=func_name, fig=fig)


@_unset_plot_in_progress_decorator
def handle_pandas_plot_accessor_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    accessor = args[0]
    try:
        self = args[0]
        from pandas.plotting._core import _get_plot_backend
        plot_backend = _get_plot_backend()

        x, y, kind, kwargs = self._get_call_args(
            plot_backend.__name__, self._parent, args[1:], kwargs
        )
        name = kind
        if name is not None:
            name = kind + "_plot"
    except Exception:
        name = "Plot"
    if hasattr(accessor, '_parent') and accessor._parent is not None:
        datasets = [accessor._parent]
    else:
        return
    create_and_upload_plot(datasets=datasets, dataset_names=[None], plot_func_name=name)


@_unset_plot_in_progress_decorator
def handle_seaborn_axisgrid_class_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    accessor = args[0]
    func_name = accessor.__class__.__name__
    if hasattr(accessor, 'data') and accessor.data is not None:
        datasets = [accessor.data]
    else:
        return
    create_and_upload_plot(datasets=datasets, dataset_names=[None], plot_func_name=func_name)


@_unset_plot_in_progress_decorator
def handle_axes_setters_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    ax = args[0]
    fig = None
    if hasattr(ax, 'figure') and ax.figure is not None:
        fig = ax.figure
    create_and_upload_plot(datasets=[], dataset_names=[], plot_func_name=None, fig=fig)


@_unset_plot_in_progress_decorator
def handle_x_type_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    func_name = orig_func.__name__
    arg_names = get_func_arg_names(orig_func)
    data_index = -1
    if 'data' in arg_names and arg_names.index('data') != 0:
        data_index = arg_names.index('data')
    data_x, data = get_func_req_params(arg_names, [0, data_index], *args, **kwargs)
    dataset_x_name, data_name = get_func_req_params(arg_names, [0, data_index], *arg_obj_names, **kwargs_obj_names)
    fig = None
    if func_name == 'bootstrap_plot':
        fig = get_func_req_params(arg_names, [1], *args, **kwargs)
    create_and_upload_plot(datasets=[data_x, data], dataset_names=[dataset_x_name, data_name], plot_func_name=func_name,
                           fig=fig)


@_unset_plot_in_progress_decorator
def handle_x_y_type_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    func_name = orig_func.__name__
    arg_names = get_func_arg_names(orig_func)
    data_index = -1
    if 'data' in arg_names and arg_names.index('data') != 0 and arg_names.index('data') != 1:
        data_index = arg_names.index('data')
    dataset_x, dataset_y, data = get_func_req_params(arg_names, [0, 1, data_index], *args, **kwargs)
    dataset_x_name, dataset_y_name, data_name = get_func_req_params(arg_names, [0, 1, data_index], *arg_obj_names,
                                                                    **kwargs_obj_names)
    create_and_upload_plot(datasets=[dataset_x, dataset_y, data],
                           dataset_names=[dataset_x_name, dataset_y_name, data_name],
                           plot_func_name=func_name)


def patch(patcher_obj):
    for module_name, func_name in MATPLOTLIB_FUNC_PLOT:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_mpl_plot_class_after_decorator)

    for module_name, func_name in MATPLOTLIB_FUNC_X:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_x_type_class_after_decorator)

    for module_name, func_name in MATPLOTLIB_FUNC_X_Y:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_x_y_type_class_after_decorator)

    for module_name, func_name in MATPLOTLIB_FUNC_ARANGE_TYPE:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_arange_type_class_after_decorator)

    for module_name, func_name in PANDAS_PLOT_ACCESSOR:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_pandas_plot_accessor_after_decorator)

    for module_name, func_name in PANDAS_PLOT_FUNC:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_x_type_func_after_decorator)

    for module_name, func_name in PANDAS_PLOT_TABLE:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_x_type_class_after_decorator)

    for module_name, func_name in SEABORN_FUNC_X_Y:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_x_y_type_func_after_decorator)

    for module_name, func_name in SEABORN_FUNC_X:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_x_type_func_after_decorator)

    for module_name, func_name in SEABORN_CLASS_FUNC:
        patcher_obj.register_before(module_name, func_name, plot_before_decorator)
        patcher_obj.register_exception_handler(module_name, func_name, plot_func_exception_handler_decorator)
        patcher_obj.register_after(module_name, func_name, handle_seaborn_axisgrid_class_after_decorator)

    for func_name in AXES_SETTERS:
        patcher_obj.register_before('matplotlib.axes._axes', 'Axes.' + func_name, plot_before_decorator)
        patcher_obj.register_exception_handler('matplotlib.axes._axes', 'Axes.' + func_name,
                                               plot_func_exception_handler_decorator)
        patcher_obj.register_after('matplotlib.axes._axes', 'Axes.' + func_name, handle_axes_setters_after_decorator)

    for module_name, func_name in DATASET_NAME_SETTER_CLASS_INIT:
        patcher_obj.register_before(module_name, func_name, set_dataset_name_before_decorator)
