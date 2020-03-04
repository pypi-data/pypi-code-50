from typing import Iterable

from scrybe.internal.tracker.data.utils import set_dataset_info, safe_extract_name_and_path, \
    set_dataset_info_and_upload, remove_predecessors
from .spark_util import *


def dataframe_creation_from_groupdata_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    node = track_spark_dataset_and_parent_if_possible(dataset_obj=ret_val)
    self_obj = args[0]
    # noinspection PyProtectedMember
    dataframe_obj = self_obj._df
    if dataframe_obj is not None and TrackingGraph.has_tracked_obj(obj=dataframe_obj):
        dataframe_node = TrackingGraph.get_node_for_tracked_object(obj=dataframe_obj)
        node.add_predecessor(predecessor_node=dataframe_node, operations={Operations.TRANSFORM})


def dataframe_creation_from_transformer_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    try:
        from pyspark.sql import DataFrame as pyspark_dataframe
        if not isinstance(ret_val, pyspark_dataframe):
            return
    except Exception as e:
        return
    self_obj = args[0]
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        try:
            from pyspark.ml import PipelineModel
            if isinstance(self_obj, PipelineModel):
                ret_val_node = remove_predecessors(ret_val=ret_val)
                from scrybe.internal.tracker.pyspark_decorator_func.pyspark_util import get_pipeline_model_parameters
                _, _, hyperparameters = get_pipeline_model_parameters(pipeline_model_obj=self_obj)
                ret_val_node.add_code_prefix(comment=hyperparameters)
                create_transformation_association(ret_val_node, metadata_dict, orig_func, *args, **kwargs)
        except ImportError:
            pass
        return
    node = track_spark_dataset_and_parent_if_possible(dataset_obj=ret_val)
    try:
        from scrybe.internal.tracker.pyspark_decorator_func.pyspark_util import get_hyperparams
        comment = {self_obj.__class__.__name__: get_hyperparams(model_obj=self_obj, trim=True)}
        node.add_code_prefix(comment=comment)
    except:
        pass
    create_transformation_association(node, metadata_dict, orig_func, *args, **kwargs)


def dataset_creation_from_file_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        return
    node = track_spark_dataset_and_parent_if_possible(dataset_obj=ret_val)
    arg_names = get_func_arg_names(orig_func)
    path = get_func_req_params(arg_names, [1], *args, **kwargs)
    filename, file_path = safe_extract_name_and_path(args=(path,), kwargs=dict())
    if isinstance(file_path, str) and len(file_path) > 0:
        node.set_node_name(name=filename)
        node.set_data_path(path=path)
        node.set_created_in_run(val=False)
        set_dataset_info(dataset_obj=ret_val)


def dataset_creation_from_self_and_other_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        return
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    self_obj, other_obj = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    self_obj_name, other_obj_name = get_func_req_params(arg_names, [0, 1], *arg_obj_names, **kwargs_obj_names)
    node = track_spark_dataset_and_parent_if_possible(dataset_obj=ret_val, parent_obj_list=[self_obj, other_obj])
    if TrackingGraph.has_tracked_obj(obj=self_obj):
        self_obj_node = TrackingGraph.get_node_for_tracked_object(obj=self_obj)
        self_obj_node.set_node_name_if_not_final(name=self_obj_name)
        node.add_predecessor(predecessor_node=self_obj_node, operations={Operations.TRANSFORM})
    if other_obj is not None and TrackingGraph.has_tracked_obj(obj=other_obj):
        other_obj_node = TrackingGraph.get_node_for_tracked_object(obj=other_obj)
        other_obj_node.set_node_name_if_not_final(name=other_obj_name)
        node.add_predecessor(predecessor_node=other_obj_node, operations={Operations.TRANSFORM})


def dataset_creation_from_self_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        return
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    self_obj = get_func_req_params(arg_names, [0], *args, **kwargs)
    self_obj_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    node = track_spark_dataset_and_parent_if_possible(dataset_obj=ret_val, parent_obj_list=[self_obj])
    if TrackingGraph.has_tracked_obj(obj=self_obj):
        self_obj_node = TrackingGraph.get_node_for_tracked_object(obj=self_obj)
        self_obj_node.set_node_name_if_not_final(name=self_obj_name)
        node.add_predecessor(predecessor_node=self_obj_node, operations={Operations.TRANSFORM})


def list_dataset_creation_from_self_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    self_obj = get_func_req_params(arg_names, [0], *args, **kwargs)
    self_obj_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    if not isinstance(ret_val, list):
        return
    self_obj_node = None
    if TrackingGraph.has_tracked_obj(obj=self_obj):
        self_obj_node = TrackingGraph.get_node_for_tracked_object(obj=self_obj)
        self_obj_node.set_node_name_if_not_final(name=self_obj_name)
    is_first_trial = True
    for dataset in ret_val:
        if TrackingGraph.has_tracked_obj(obj=dataset):
            continue
        if is_first_trial:
            node = track_spark_dataset_and_parent_if_possible(dataset_obj=dataset, parent_obj_list=[self_obj])
            if TrackingGraph.has_tracked_obj(obj=self_obj):
                self_obj_node = TrackingGraph.get_node_for_tracked_object(obj=self_obj)
                self_obj_node.set_node_name_if_not_final(name=self_obj_name)
            is_first_trial = False
        else:
            node = track_spark_dataset_and_parent_if_possible(dataset_obj=dataset)
        if self_obj_node is not None:
            node.add_predecessor(predecessor_node=self_obj_node, operations={Operations.TRANSFORM})


def dataframe_creation_from_session_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        return
    arg_names = get_func_arg_names(orig_func)
    reference = get_func_req_params(arg_names, [1], *args, **kwargs)
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    reference_name = get_func_req_params(arg_names, [1], *arg_obj_names, **kwargs_obj_names)
    node = track_spark_dataset_and_parent_if_possible(dataset_obj=ret_val, parent_obj_list=[reference])
    # TODO(chandra): Where to store sql query
    if orig_func.__name__ == "table" and isinstance(reference, str):
        node.set_query_str(reference)
        if reference in TABLE_DATAFRAME_NODE_DICT:
            reference_node = TABLE_DATAFRAME_NODE_DICT[reference]
            node.add_predecessor(predecessor_node=reference_node, operations={Operations.VIEW})
        return
    elif orig_func.__name__ == "sql" and isinstance(reference, str):
        node.set_query_str(reference)
        table_names = get_table_names(dataframe_obj=ret_val)
        for table_name in table_names:
            if table_name not in TABLE_DATAFRAME_NODE_DICT:
                continue
            reference_node = TABLE_DATAFRAME_NODE_DICT[table_name]
            node.add_predecessor(predecessor_node=reference_node, operations={Operations.VIEW})
        return
    if reference is None or isinstance(reference, str) or isinstance(reference, list) or isinstance(reference, int):
        return
    elif TrackingGraph.has_tracked_obj(reference):
        reference_node = TrackingGraph.get_node_for_tracked_object(obj=reference)
        reference_node.set_node_name_if_not_final(name=reference_name)
        node.add_predecessor(predecessor_node=reference_node, operations={Operations.VIEW})


def rdd_from_context_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        return
    track_spark_dataset_and_parent_if_possible(dataset_obj=ret_val)


def rdd_from_union_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        return
    node = track_spark_dataset_and_parent_if_possible(dataset_obj=ret_val)
    arg_names = get_func_arg_names(orig_func)
    references = get_func_req_params(arg_names, [1], *args, **kwargs)
    if not isinstance(references, Iterable):
        return
    for parent_rdd in references:
        if not TrackingGraph.has_tracked_obj(obj=parent_rdd):
            track_rdd_if_possible(rdd_obj=parent_rdd)
        if TrackingGraph.has_tracked_obj(obj=parent_rdd):
            parent_rdd_node = TrackingGraph.get_node_for_tracked_object(obj=parent_rdd)
            node.add_predecessor(predecessor_node=parent_rdd_node, operations={Operations.CONCATENATION})


def pandas_df_creation_from_self_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    if ret_val is None:
        return
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    arg_names = get_func_arg_names(orig_func)
    self_obj = get_func_req_params(arg_names, [0], *args, **kwargs)
    self_obj_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    if TrackingGraph.has_tracked_obj(obj=ret_val):
        node = TrackingGraph.get_node_for_tracked_object(obj=ret_val)
    else:
        node = DatasetTrackingNode(oid=id(ret_val), version=0, obj_type=DatasetTrackingNode.ObjectType.PANDAS)
        TrackingGraph.add_tracked_object(obj=ret_val, node=node)
    if TrackingGraph.has_tracked_obj(obj=self_obj):
        self_obj_node = TrackingGraph.get_node_for_tracked_object(obj=self_obj)
        self_obj_node.set_node_name_if_not_final(name=self_obj_name)
        node.add_predecessor(predecessor_node=self_obj_node, operations={Operations.VIEW})


def dataset_save_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    self_obj = args[0]
    from pyspark.sql.readwriter import DataFrameWriter
    if isinstance(self_obj, DataFrameWriter):
        dataset = self_obj._df
    else:
        dataset = self_obj
    if dataset is None:
        return
    if not TrackingGraph.has_tracked_obj(obj=dataset):
        track_rdd_if_possible(rdd_obj=dataset)
        if not TrackingGraph.has_tracked_obj(obj=dataset):
            return
    node = TrackingGraph.get_node_for_tracked_object(obj=dataset)
    arg_names = get_func_arg_names(orig_func)
    path = get_func_req_params(arg_names, [1], *args, **kwargs)
    filename, file_path = safe_extract_name_and_path(args=(path,), kwargs=dict())
    if isinstance(file_path, str) and len(file_path) > 0:
        node.set_node_name(name=filename)
        node.set_data_path(path=path)
        node.set_created_in_run(val=True)
        set_dataset_info_and_upload(dataset_obj=dataset)


def table_creation_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    dataframe_obj, table_name = get_func_req_params(arg_names, [0, 1], *args, **kwargs)
    arg_obj_names = metadata_dict["arg_obj_names"]
    kwargs_obj_names = metadata_dict["kwargs_obj_names"]
    dataframe_obj_name = get_func_req_params(arg_names, [0], *arg_obj_names, **kwargs_obj_names)
    if not TrackingGraph.has_tracked_obj(obj=dataframe_obj) or not isinstance(table_name, str) or not table_name:
        return
    dataframe_node = TrackingGraph.get_node_for_tracked_object(obj=dataframe_obj)
    dataframe_node.set_node_name_if_not_final(name=dataframe_obj_name)
    TABLE_DATAFRAME_NODE_DICT[table_name] = dataframe_node


def table_deletion_after_decorator(metadata_dict, ret_val, orig_func, *args, **kwargs):
    arg_names = get_func_arg_names(orig_func)
    table_name = get_func_req_params(arg_names, [1], *args, **kwargs)
    if table_name in TABLE_DATAFRAME_NODE_DICT:
        TABLE_DATAFRAME_NODE_DICT.pop(table_name)


def patch(patcher_obj):
    for module_name, func_name in DATASET_CREATION_FROM_SELF:
        patcher_obj.register_after(module_name, func_name, dataset_creation_from_self_after_decorator)
    for module_name, func_name in DATASET_CREATION_FROM_SELF_AND_OTHER:
        patcher_obj.register_after(module_name, func_name, dataset_creation_from_self_and_other_after_decorator)
    for module_name, func_name in DATASET_CREATION_FROM_FILE:
        patcher_obj.register_after(module_name, func_name, dataset_creation_from_file_after_decorator)
    for module_name, func_name in DATAFRAME_CREATION_FROM_TRANFORMER:
        patcher_obj.register_after(module_name, func_name, dataframe_creation_from_transformer_after_decorator)
    for module_name, func_name in DATAFRAME_CREATION_FROM_GROUPDATA:
        patcher_obj.register_after(module_name, func_name, dataframe_creation_from_groupdata_after_decorator)
    for module_name, func_name in LIST_DATASET_FROM_SELF:
        patcher_obj.register_after(module_name, func_name, list_dataset_creation_from_self_after_decorator)
    for module_name, func_name in DATAFRAME_CREATION_FROM_SPARK_SESSION:
        patcher_obj.register_after(module_name, func_name, dataframe_creation_from_session_after_decorator)
    for module_name, func_name in PANDAS_DF_FROM_SELF:
        patcher_obj.register_after(module_name, func_name, pandas_df_creation_from_self_after_decorator)
    for module_name, func_name in DATASET_SAVE:
        patcher_obj.register_after(module_name, func_name, dataset_save_after_decorator)
    for module_name, func_name in TABLE_CREATION_FROM_DATAFRAME:
        patcher_obj.register_after(module_name, func_name, table_creation_after_decorator)
    for module_name, func_name in TABLE_DELETION:
        patcher_obj.register_after(module_name, func_name, table_deletion_after_decorator)
    for module_name, func_name in RDD_CREATION_FROM_SPARK_CONTEXT:
        patcher_obj.register_after(module_name, func_name, rdd_from_context_after_decorator)
    for module_name, func_name in RDD_CREATION_FROM_UNION_OF_RDDS:
        patcher_obj.register_after(module_name, func_name, rdd_from_union_after_decorator)
