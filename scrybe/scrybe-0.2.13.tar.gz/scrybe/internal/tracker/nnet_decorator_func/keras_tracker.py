import logging

from scrybe.internal.threading_util import ThreadLocalVarHandler

from scrybe.internal.depgraph.tracking_graph import TrackingGraph
from scrybe.internal.tracker.data.missed_dataset_handler import track_data
from scrybe.internal.tracker.metrics import get_eval_metric_node
from scrybe.internal.tracker.save_and_load_tracker import save_func_after_decorator, keras_load_func_after_decorator
from scrybe.internal.tracker.tracker_util import predict_handler, create_associations, \
    all_func_enable_patching_decorator
from scrybe.internal.uploader import DataReceiver
from scrybe.internal.util import get_func_req_params, get_func_arg_names
from .keras_callback import get_keras_callback, get_tf_keras_callback

LOGGER = logging.getLogger(__name__)
KERAS = 'keras'
TF_KERAS = 'tf-keras'


def keras_predict_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    return predict_handler(arg_obj_names, kwargs_obj_names, ret_val, orig_func, *args, **kwargs)


def to_categorical_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    y, num_classes = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    y_name, num_classes_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
    if ret_val is not None and not TrackingGraph.has_tracked_obj(obj=ret_val):
        try:
            # This is a case of missed/bad data tracking -- better patch it up
            ret_val = track_data(data_obj=ret_val)
        except TypeError:
            # The error has been produced because a weakref cannot be created on this data type
            pass
    create_associations(obj=ret_val, target_obj_list=[(y, y_name)])
    return ret_val


@all_func_enable_patching_decorator
def keras_evaluate_func_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    # ret_val can be a single float or a list of floats. model.metric_names gives the metric names
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    model_obj = args[0]
    model_name = arg_obj_names[0]
    arg_names = get_func_arg_names(orig_func)
    x_test, y_test = get_func_req_params(arg_names, [1, 2], *args, **kwargs)
    x_test_name, y_test_name = get_func_req_params(arg_names, [1, 2], *arg_obj_names, **kwargs_obj_names)
    local_name_dict = {"y_true": y_test_name, "x_test": x_test_name, "model": model_name}
    metric_names = model_obj.metrics_names
    metrics = dict()
    if isinstance(ret_val, float):
        metrics[metric_names[0]] = ret_val
    else:
        for i in range(len(metric_names)):
            metrics[metric_names[i]] = ret_val[i]
    metric_tuple = get_eval_metric_node(y_true=y_test, x_test=x_test, ret_val=ret_val, model=model_obj,
                                        metric_names=list(metrics.keys()), local_name_dict=local_name_dict)
    if metric_tuple is None:
        return
    metric_node, metric_seq_dict = metric_tuple
    metrics.update(metric_seq_dict)
    metric_node.add_metric(metrics)
    DataReceiver.receive_batch(data_dict_list=metric_node.prepare_for_upload())
    # log_upload_data_to_file(upload_data=metric_node.prepare_for_upload(), func_name='_'.join(metrics.keys()))


def keras_func_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    return func_decorator(metadata_dict, KERAS, orig_func, *args, **kwargs)


def tf_keras_func_before_decorator(metadata_dict, orig_func, *args, **kwargs):
    return func_decorator(metadata_dict, TF_KERAS, orig_func, *args, **kwargs)


def keras_exception_handler_decorator(metadata_dict, orig_func, self_obj, *args, **kwargs):
    ThreadLocalVarHandler.all_func.enable_patching()


def keras_after_decorator(metadata_dict, orig_func, self_obj, *args, **kwargs):
    ThreadLocalVarHandler.all_func.enable_patching()


def func_decorator(metadata_dict, keras_src_module, orig_func, *args, **kwargs):
    ThreadLocalVarHandler.all_func.disable_patching()
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    x_sample, y_sample, validation_data, class_weights = get_func_req_params(arg_names, [1, 2, 8, 10], *args, **kwargs)
    # TODO(chandra): Try to get name of variable inside tuples
    model_name, x_sample_name, y_sample_name, validation_data_name = get_func_req_params(arg_names, [0, 1, 2, 8],
                                                                                         *arg_obj_names,
                                                                                         **kwargs_obj_names)
    local_name_dict = {"model": model_name, "x_sample": x_sample_name, "y_sample": y_sample_name,
                       "validation_data": validation_data_name}
    try:
        if keras_src_module == KERAS:
            callback = get_keras_callback(x_sample=x_sample, y_sample=y_sample, validation_data=validation_data,
                                          metadata_dict=metadata_dict, class_weights=class_weights,
                                          local_name_dict=local_name_dict)
        elif keras_src_module == TF_KERAS:
            callback = get_tf_keras_callback(x_sample=x_sample, y_sample=y_sample, validation_data=validation_data,
                                             metadata_dict=metadata_dict, class_weights=class_weights,
                                             local_name_dict=local_name_dict)
        else:
            return
    except Exception as e:
        LOGGER.warning("Exception occurred in getting keras callback. Error: %s" % str(e))
        return

    if "callbacks" in kwargs and kwargs["callbacks"] is not None:
        callbacks = kwargs["callbacks"]
        if not any(
            x.__class__.__name__ == callback.__class__.__name__ for x in callbacks
        ):
            callbacks.append(callback)
    else:
        kwargs["callbacks"] = [callback]

    # Evaluate collects support in callback. If the args, kwargs are changed then support cannot
    # be associated with other metrics returned by model.evaluate
    if orig_func.__name__ not in ["fit", "fit_generator", "predict", "predict_proba"]:
        return args, kwargs
    # noinspection PyUnresolvedReferences
    from scrybe.internal.tracker.data.instrumentation.numpy_datasets import array as TrackedNDArray
    import numpy as np
    modified_args = []
    modified_kwargs = {}
    for arg in args:
        if isinstance(arg, TrackedNDArray):
            modified_args.append(arg.view(np.ndarray))
        elif isinstance(arg, tuple) or isinstance(arg, list):
            new_item_list = []
            for item in arg:
                if isinstance(item, TrackedNDArray):
                    new_item_list.append(item.view(np.ndarray))
                else:
                    new_item_list.append(item)
            if isinstance(arg, tuple):
                modified_args.append(tuple(new_item_list))
            else:
                modified_args.append(new_item_list)
        else:
            modified_args.append(arg)
    for key, arg in kwargs.items():
        if isinstance(arg, TrackedNDArray):
            modified_kwargs[key] = arg.view(np.ndarray)
        elif isinstance(arg, tuple) or isinstance(arg, list):
            new_item_list = []
            for item in arg:
                if isinstance(item, TrackedNDArray):
                    new_item_list.append(item.view(np.ndarray))
                else:
                    new_item_list.append(item)
            if isinstance(arg, tuple):
                modified_kwargs[key] = tuple(new_item_list)
            else:
                modified_kwargs[key] = new_item_list
        else:
            modified_kwargs[key] = arg
    return tuple(modified_args), modified_kwargs


def post_tensorflow_load_func(module):
    from tensorflow.python.framework import type_spec
    from scrybe.internal.tracker.data.instrumentation.numpy_datasets import array as TrackedNDArray
    type_spec.register_type_spec_from_value_converter(
        TrackedNDArray,
        lambda array: module.TensorSpec(array.shape, array.dtype))


KERAS_CALLBACK_MODULES = [
    ("keras.models", "Model.fit"),
    ("keras.models", "Model.fit_generator"),
]

TF_KERAS_CALLBACK_MODULES = [
    ("tensorflow.python.keras.models", "Model.fit"),
    ("tensorflow.python.keras.models", "Model.fit_generator"),
]


PREDICT_MODULES = [
    ("keras.models", "Model.predict"),
    ("keras.models", "Model.predict_proba"),
    ("tensorflow.python.keras.models", "Model.predict"),
    ("tensorflow.python.keras.models", "Model.predict_proba"),
]

KERAS_EVALUATE_MODULES = [
    ("keras.models", "Model.evaluate"),
]

TF_KERAS_EVALUATE_MODULES = [
    ("tensorflow.python.keras.models", "Model.evaluate"),
]

SAVE_MODULES = [
    ("keras.models", "Model.save"),
    ("keras.models", "Model.save_weights"),
    ("tensorflow.python.keras.models", "Model.save"),
    ("tensorflow.python.keras.models", "Model.save_weights"),
]

LOAD_MODULES = [
    ("keras.models", "load_model"),
    ("keras.models", "Model.load_weights"),
    ("tensorflow.python.keras.models", "load_model"),
    ("tensorflow.python.keras.models", "Model.load_weights"),
]


def patch(patcher_obj):
    for module_name, function_name in KERAS_CALLBACK_MODULES:
        patcher_obj.register_before(module_name, function_name, keras_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, function_name, keras_exception_handler_decorator)
        patcher_obj.register_after(module_name, function_name, keras_after_decorator)
    for module_name, function_name in TF_KERAS_CALLBACK_MODULES:
        patcher_obj.register_before(module_name, function_name, tf_keras_func_before_decorator)
        patcher_obj.register_exception_handler(module_name, function_name, keras_exception_handler_decorator)
        patcher_obj.register_after(module_name, function_name, keras_after_decorator)

    for module, function_name in SAVE_MODULES:
        patcher_obj.register_after(module, function_name, save_func_after_decorator)

    for module, function_name in LOAD_MODULES:
        patcher_obj.register_after(module, function_name, keras_load_func_after_decorator)

    for module, function_name in PREDICT_MODULES:
        patcher_obj.register_after(module, function_name, keras_predict_func_after_decorator)

    for module, function_name in KERAS_EVALUATE_MODULES:
        patcher_obj.register_before(module, function_name, keras_func_before_decorator)
        patcher_obj.register_exception_handler(module, function_name, keras_exception_handler_decorator)
        patcher_obj.register_after(module, function_name, keras_evaluate_func_after_decorator)

    for module, function_name in TF_KERAS_EVALUATE_MODULES:
        patcher_obj.register_before(module, function_name, tf_keras_func_before_decorator)
        patcher_obj.register_exception_handler(module, function_name, keras_exception_handler_decorator)
        patcher_obj.register_after(module, function_name, keras_evaluate_func_after_decorator)

    patcher_obj.register_after("keras.utils.np_utils", "to_categorical", to_categorical_func_after_decorator)
    patcher_obj.register_after("tensorflow.python.keras.utils.np_utils", "to_categorical",
                               to_categorical_func_after_decorator)
    patcher_obj.register_post_module_load("tensorflow", post_tensorflow_load_func)
