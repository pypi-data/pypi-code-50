import hashlib
import json
import logging
import os
import sys
import uuid
import weakref
from enum import Enum
from typing import Dict, Set, Union, Iterable, List

from scrybe.internal.code_capture.source_code import CodeCapture
from scrybe.internal.code_capture.source_context import SourceContext, FrameHelper
from scrybe.internal.config import Config
from scrybe.internal.const import SCRYBE_CV_ID_KEY, SCRYBE_GRID_ID_KEY, SCRYBE_GRID_ID_KEY_KEYID
from scrybe.internal.depgraph.lineage_graph import LineageGraph, LineageGraphNode
from scrybe.internal.depgraph.node_util import get_scrybe_dashboard_url_for_node
from scrybe.internal.depgraph.ops import Operations
from scrybe.internal.util import ScrybeJSONEncoder

LOGGER = logging.getLogger("scrybe_logger")


class ArtifactType(Enum):
    PLOT_DATA = "Plot Data"
    PLOT_IMAGE = "Plot Image"
    PLOT_BAR = "Plot Bar"
    PLOT_MPLD3 = "Plot Mpld3"
    TABLE = "Table"
    STATS_NUMBER = "Stats Number"
    DATA_VALUES = "Data Values"


class BaseTrackingNode(object):
    FIRST_SEQUENCE_NUM = 1

    class Type(Enum):
        ARTIFACT = "artifact"
        DATA = "dataset"
        MODEL = "model"
        TEST_METRIC = "test_metric"
        TRAIN_METRIC = "train_metric"
        VALIDATION_METRIC = "validation_metric"
        GHOST_METRIC = "ghost_metric"
        DATASET_ARTIFACT = "dataset_artifact"
        PIPELINE_OBJ = "pipeline_obj"
        UTILITY = "utility"
        CODE = "code"

    def __init__(self, oid: int, version: int, node_type: Type):
        self._client_id = None
        self.sequence_num = self.FIRST_SEQUENCE_NUM
        self.predecessors = weakref.WeakKeyDictionary()
        self.successors = weakref.WeakSet()
        self.node_type = node_type
        self.name = None
        self.is_name_final = False
        self.labels = Config.get_labels()
        self.run_id = Config.get_run_id()
        self.bookmark = None
        self._dashboard_url_computed = False
        self._dashboard_url_displayed = False

        # Anchor nodes are special nodes which don't get compacted as long as there are child nodes to it
        # If an anchor node is added as predecessor to another node, we additionally add a reference to the
        # anchor node in the child node
        self.is_anchor = False

        # In case of certain datasets (e.g. y_pred), this node needs to keep a ref to the node objects
        # of parent datasets (e.g. x_test) or models (e.g. model used for prediction)
        self.references = list()

        # Note: DO NOT TAKE DEPENDENCY ON BELOW ATTRIBUTES -- they are kept here for debugging
        self.oid = oid
        self._version_ = version

    def __del__(self):
        if sys is None or sys.is_finalizing() or Config.has_exited:
            return

        # Perform compaction on successor nodes
        for predecessor_node, ops in self.predecessors.items():
            for successor_node in self.successors:
                # First allow sub classes to handle any compaction related activities
                successor_node.__handle_compaction__(predecessor_node=self)
                successor_node.add_predecessor(predecessor_node=predecessor_node, operations=ops,
                                               replace_predecessor=self)

    def __handle_compaction__(self, predecessor_node: 'BaseTrackingNode'):
        """
        This function can be implemented by sub classes if they need to do any special work during graph
        compaction
        """
        pass

    def __parent_node_ids__(self) -> Dict:
        out = dict(parent_models=list(),
                   parent_datasets=list(),
                   parent_models_ops=list(),
                   parent_datasets_ops=list())
        for predecessor_node, ops in self.predecessors.items():
            if predecessor_node is None or predecessor_node.client_id == self.client_id:
                continue
            if predecessor_node.node_type == self.Type.DATA:
                out["parent_datasets"].append(predecessor_node.client_id)
                out["parent_datasets_ops"].append([o.name for o in ops])
            elif predecessor_node.node_type == self.Type.MODEL:
                out["parent_models"].append(predecessor_node.client_id)
                out["parent_models_ops"].append([o.name for o in ops])
        return out

    def __maybe_print_dashboard_url__(self):
        pass

    def __get_upload_data__(self) -> Dict:
        raise NotImplementedError("Should be implemented by sub-classes")

    def __clear_upload_data__(self):
        raise NotImplementedError("Should be implemented by sub-classes")

    def __base_clear_upload_data__(self):
        self.labels = None
        self.bookmark = None
        self.run_id = None

    @classmethod
    def __dfs_walk__(cls, current: 'BaseTrackingNode', visited: Set[str], graph: LineageGraph):
        visited.add(current.client_id)
        # TODO(msachdev): This info needs to be properly populated
        graph_node = LineageGraphNode(id=current.client_id, name="", metadata=current.get_node_info())
        for predecessor_node, ops in current.predecessors.items():
            if predecessor_node is None:
                continue
            if predecessor_node.client_id not in visited:
                cls.__dfs_walk__(current=predecessor_node, visited=visited, graph=graph)
            edge_metadata = dict()
            edge_metadata["processing"] = ','.join([op.value for op in ops])
            graph_node.add_incoming_edge(src_id=predecessor_node.client_id, metadata=edge_metadata)
        graph.add_node(graph_node)

    def __cyclical_check__(self, proposed_predecessor_node: 'BaseTrackingNode'):
        # This function checks if a cycle will get created by add "proposed_predecessor_node" as a predecessor
        # to self
        proposed_predecessor_node_lineage = proposed_predecessor_node.get_lineage()
        return self.client_id in proposed_predecessor_node_lineage.nodes.keys()

    # --------- Properties --------- #
    @property
    def client_id(self):
        if self._client_id is None:
            self._client_id = str(uuid.uuid4())
        return self._client_id

    def set_node_name_if_not_final(self, name: str):
        if self.name and self.is_name_final:
            return
        if not name:
            max_depth = 10
            depth = 0
            current_node = self
            op_name = ""
            while current_node.predecessors and len(current_node.predecessors) == 1 and depth < max_depth:
                depth += 1
                for current_node, ops in current_node.predecessors.items():
                    if len(op_name) == 0:
                        op_name += ','.join([op.value for op in ops])
                    else:
                        op_name += ' | ' + ','.join([op.value for op in ops])
                    if current_node.name:
                        self.name = current_node.name + " (" + op_name + ")"
        else:
            self.name = name

    def set_node_name(self, name: str):
        self.name = name
        self.is_name_final = True

    def set_bookmark(self, msg: str):
        if msg:
            self.bookmark = msg

    def add_reference(self, node: 'BaseTrackingNode'):
        self.references.append(node)

    def add_predecessor(self, predecessor_node: 'BaseTrackingNode', operations: Set[Operations],
                        replace_predecessor: 'BaseTrackingNode' = None):
        # if self.__cyclical_check__(proposed_predecessor_node=predecessor_node):
        #     raise ValueError("Adding this predecessor would create a cycle")
        if predecessor_node not in self.predecessors:
            self.predecessors[predecessor_node] = set()
        self.predecessors[predecessor_node].update(operations)
        if replace_predecessor in self.predecessors:
            replace_predecessor_ops = self.predecessors[replace_predecessor]
            if replace_predecessor_ops is not None:
                self.predecessors[predecessor_node].update(replace_predecessor_ops)
        # Also add this node to the predecessor successor set to allow deletion callbacks
        predecessor_node.successors.add(self)

        if predecessor_node.is_anchor:
            self.add_reference(node=predecessor_node)

    # --------- Graph walk utilities --------- #

    def find_nearest_node_of_type(self, node_type: Type) -> Union['BaseTrackingNode', None]:
        visited = set()
        to_visit = list([self])

        while len(to_visit) > 0:
            node = to_visit.pop(0)
            if node is not self and node.node_type == node_type:
                return node
            visited.add(node.client_id)
            to_visit.extend([node for node, _ in node.predecessors.items() if node.client_id not in visited])

        return None

    def find_nearest_node_with_op(self, op: Operations) -> Union['BaseTrackingNode', None]:
        visited = set()
        to_visit = list([(node, ops) for node, ops in self.predecessors.items()])

        while len(to_visit) > 0:
            node, ops = to_visit.pop(0)
            if node is not self and op in ops:
                return node
            visited.add(node.client_id)
            to_visit.extend([(node, ops) for node, ops in node.predecessors.items() if node.client_id not in visited])

        return None

    def find_nearest_node_with_location(self) -> Union['BaseTrackingNode', None]:
        visited = set()
        to_visit = list([self])

        while len(to_visit) > 0:
            node = to_visit.pop(0)
            if node is not self and node.path is not None:
                return node
            visited.add(node.client_id)
            to_visit.extend([node for node, _ in node.predecessors.items() if node.client_id not in visited])

        return None

    def get_lineage(self) -> LineageGraph:
        graph = LineageGraph()
        self.__dfs_walk__(current=self, visited=set(), graph=graph)
        return graph

    def get_node_info(self) -> Dict:
        return dict(client_id=self.client_id,
                    oid=self.oid,
                    version=self._version_,
                    sequence_num=self.sequence_num,
                    node_type=self.node_type.value,
                    name=self.name if self.name is not None else "")

    def get_parent_with_op(self, op: Operations) -> Union['BaseTrackingNode', None]:
        for predecessor_node, ops in self.predecessors.items():
            if op in ops:
                return predecessor_node
        return None

    # --------- Upload --------- #
    def prepare_for_upload(self, visited: Set[str] = None) -> Iterable[Dict]:
        # FIXME(chandra): This should be done after getting an instance specific lock
        if visited is None:
            visited = set()
        out = dict(client_id=self.client_id, sequence_num=self.sequence_num, data_type=self.node_type.value)
        if self.labels is not None and len(self.labels) > 0:
            out['labels'] = list(set(self.labels))
        if self.bookmark:
            out['bookmark'] = self.bookmark
        if self.run_id:
            out['run_id'] = self.run_id
        visited.add(self.client_id)
        # We need to send info about our predecessors as well
        for predecessor_node, ops in self.predecessors.items():
            if predecessor_node is None or predecessor_node.sequence_num > self.FIRST_SEQUENCE_NUM:
                continue
            if predecessor_node.client_id in visited:
                # FIXME(msachdev): Add warning message
                continue
            for predecessor_data in predecessor_node.prepare_for_upload(visited=visited):
                yield predecessor_data

        out.update(self.__parent_node_ids__())
        out.update(self.__get_upload_data__())
        yield out

        # At the end
        self.__maybe_print_dashboard_url__()
        self.__clear_upload_data__()
        self.__base_clear_upload_data__()
        self.sequence_num += 1


class DatasetTrackingNode(BaseTrackingNode):
    # Derived classes of DatasetTrackingNode can override this value to prevent capturing source context
    CAPTURE_SRC_CTXT = True

    class ObjectType(Enum):
        NUMPY = "numpy"
        PANDAS = "pandas"
        BASIC_ITERATOR = "basic_iterator"
        SPARK_DATAFRAME = "spark_dataframe"
        SPARK_RDD = "spark_rdd"
        CATBOOST_POOL = "catboost_pool"
        UNKNOWN = "unknown"

    def __init__(self, oid: int, version: int, obj_type: ObjectType, path: str = None, name: str = None):
        super().__init__(oid=oid, version=version, node_type=BaseTrackingNode.Type.DATA)
        self.type = obj_type
        self.path = path
        self.name = name
        self.indexing_info = None
        self.cv_id = None
        self.is_anchor = self.path is not None and len(self.path) > 0
        self.info = None
        self.is_info_set = False
        self.created_in_run = True
        self.query_str = None
        self.code_prefixs = None
        if self.CAPTURE_SRC_CTXT and Config.is_src_code_enabled():
            self.src_contexts = [SourceContext.capture_current_context()]
        else:
            self.src_contexts = list()

    def __compute_src_frames__(self) -> List:
        if self.src_contexts is None:
            return list()
        src_frames = list()
        src_lines = set()
        for src_context in self.src_contexts:
            src_frame = src_context.get_src_line_based_on_current_stack()
            if src_frame:
                src_line = FrameHelper.to_string(frame=src_frame)
                if src_line not in src_lines:
                    src_frames.append(src_frame)
                    src_lines.add(src_line)
        return src_frames

    def __handle_compaction__(self, predecessor_node: 'BaseTrackingNode'):
        if self.src_contexts is None or len(self.src_contexts) > 2000:
            return
        parent_src_contexts = getattr(predecessor_node, 'src_contexts', None)
        if parent_src_contexts is not None and len(parent_src_contexts) > 0 and self.src_contexts is not None:
            psc = parent_src_contexts[0]
            ins_idx = 0
            for ins_idx in range(len(self.src_contexts)):
                sc = self.src_contexts[ins_idx]
                cmp = psc.compare(other=sc)
                if cmp in (0, -1, -2):
                    break
            for i in range(len(parent_src_contexts)):
                self.src_contexts.insert((ins_idx + i), parent_src_contexts[i])

    def __get_upload_data__(self):
        dataset_out = dict(sub_type=self.type.name)
        if self.created_in_run is not None:
            dataset_out["created_in_run"] = self.created_in_run
        if self.path is not None:
            dataset_out["location"] = self.path
        if self.name is not None:
            dataset_out["name"] = self.name
        if self.indexing_info is not None:
            dataset_out["indexing_info"] = self.indexing_info
        if self.info is not None:
            dataset_out["info"] = self.info
        if self.query_str is not None and len(self.query_str) > 0:
            dataset_out["query_str"] = self.query_str
        if self.src_contexts is not None and len(self.src_contexts) > 0:
            src_context_list = [
                dict(
                    file=os.path.relpath(frame.filename),
                    lineno=frame.lineno,
                    func=frame.name,
                    lines=SourceContext.get_context_lines_for_frame(frame=frame)
                )
                for frame in self.__compute_src_frames__()
            ]
            if len(src_context_list) > 0 and self.code_prefixs is not None and len(self.code_prefixs) > 0:
                src_context_list[-1]['lines'] = self.code_prefixs + src_context_list[-1]['lines']
            dataset_out["src_code"] = json.dumps(src_context_list)
        return dataset_out

    def __clear_upload_data__(self):
        self.path = None
        self.indexing_info = None
        self.info = None
        self.src_contexts = None
        self.code_prefixs = None
        self.query_str = None

    def get_node_info(self) -> Dict:
        info = super().get_node_info()
        info["src_lines"] = [FrameHelper.to_string(frame=src_frame) for src_frame in self.__compute_src_frames__()]
        return info

    def set_data_path(self, path: str):
        self.path = path
        self.is_anchor = self.path is not None and len(self.path) > 0

    def set_query_str(self, query_str: str):
        if isinstance(query_str, str) and query_str:
            self.query_str = query_str

    def set_created_in_run(self, val: bool):
        self.created_in_run = val

    def set_indexing_info(self, indexing_info: List):
        self.indexing_info = indexing_info

    def set_cv_id(self, cv_id: str):
        if self.cv_id is not None:
            LOGGER.warning("WARNING: CV ID is being overwritten")
        self.cv_id = cv_id

    def update_info(self, info: str, force_update=False):
        if force_update or not self.is_info_set:
            self.info = info
            self.is_info_set = True

    def add_code_prefix(self, comment):
        self.code_prefixs = []
        if isinstance(comment, str) and comment:
            self.code_prefixs.append(comment)
        elif isinstance(comment, dict) and len(comment) > 0:
            for key in comment:
                self.code_prefixs.append("# %s:%s" % (key, str(comment[key])))


class ModelTrackingNode(BaseTrackingNode):
    CV_NAME_PREFIX = "CV:"
    SEQUENCE_NUM_SUFFIX = "_sequence_num"
    BEST_ESTIMATOR_KEY = "grid_search_best_estimator"

    def __init__(self, oid: int, version: int, approach, name=None, path=None, created_in_run=True):
        super().__init__(oid=oid, version=version, node_type=BaseTrackingNode.Type.MODEL)
        self.approach = approach
        self.spec = dict()
        self.name = name
        if name and path:
            self.is_name_final = True
        self.path = path
        self.created_in_run = created_in_run
        self.cross_validation_id = None
        self.grid_search_id = None
        self.is_anchor = True
        self.mdata = dict()  # {'BEST_ESTIMATOR_KEY': true}
        self.is_created_in_pipeline = False
        self.features = None
        self.feature_importance = None
        self._last_uploaded_feature_importance = None
        self.metric_seq_num_map = dict()
        if Config.is_code_capture_enabled():
            self.code_client_id = CodeCapture.get_code_client_id()
        else:
            self.code_client_id = None

    def add_predecessor(self, predecessor_node: BaseTrackingNode, operations: Set[Operations],
                        replace_predecessor: 'BaseTrackingNode' = None):
        super().add_predecessor(predecessor_node=predecessor_node, operations=operations,
                                replace_predecessor=replace_predecessor)
        self.add_reference(predecessor_node)

    def set_as_grid_search_best_estimator(self):
        self.mdata[self.BEST_ESTIMATOR_KEY] = True
        # In order to print the dashboard URL, the following must be done
        if not self._dashboard_url_displayed:
            self._dashboard_url_computed = False

    def set_cv_and_grid_id_if_possible(self, metadata_dict: dict):
        if metadata_dict is None:
            return
        if SCRYBE_CV_ID_KEY in metadata_dict and metadata_dict[SCRYBE_CV_ID_KEY] is not None:
            self.cross_validation_id = metadata_dict[SCRYBE_CV_ID_KEY]
            if self.name is not None:
                self.set_node_name_if_not_final(self.CV_NAME_PREFIX + self.name)
            else:
                self.set_node_name_if_not_final(self.CV_NAME_PREFIX + "estimator")
        if SCRYBE_GRID_ID_KEY in metadata_dict and metadata_dict[SCRYBE_GRID_ID_KEY] is not None:
            self.grid_search_id = metadata_dict[SCRYBE_GRID_ID_KEY][SCRYBE_GRID_ID_KEY_KEYID]

    def set_hyperparams(self, hyperparams):
        if 'hyperparameters' not in self.spec:
            self.spec['hyperparameters'] = dict()
        self.spec['hyperparameters'].update(hyperparams)

    def get_hyperparams(self):
        if 'hyperparameters' in self.spec:
            return self.spec['hyperparameters']
        return None

    def set_architecture(self, architecture):
        self.spec['architecture'] = architecture

    def set_path(self, path):
        self.path = path

    def set_approach(self, approach):
        self.approach = approach

    def set_features(self, features: list):
        self.features = features
        if self._last_uploaded_feature_importance is not None:
            self.set_feature_importance(feature_importance=self._last_uploaded_feature_importance)

    def get_features(self):
        return self.features

    def set_feature_importance(self, feature_importance):
        self._last_uploaded_feature_importance = feature_importance
        if feature_importance is None:
            return
        if isinstance(feature_importance, dict) and len(feature_importance) > 0:
            self.feature_importance = feature_importance
            if self.features is None or len(self.features) == 0:
                self.features = list(self.feature_importance.keys())
        is_type_list = False
        if isinstance(feature_importance, list):
            is_type_list = True
        else:
            try:
                import numpy as np
                if isinstance(feature_importance, np.ndarray):
                    is_type_list = True
            except Exception:
                pass
        if is_type_list:
            imp_dict = dict()
            if self.features is not None and len(self.features) > 0 and len(self.features) == len(feature_importance):
                for i in range(len(self.features)):
                    imp_dict[self.features[i]] = feature_importance[i]
            else:
                for i in range(len(feature_importance)):
                    imp_dict['f' + str(i)] = feature_importance[i]
            self.feature_importance = imp_dict

    def get_feature_importance(self):
        return self.feature_importance

    def set_node_name_if_not_final(self, name: str):
        if self.name is not None and self.name.startswith(self.CV_NAME_PREFIX) and name is not None \
                and not name.startswith(self.CV_NAME_PREFIX):
            name = self.CV_NAME_PREFIX + name
        super().set_node_name_if_not_final(name)
        if self.name is not None and self.approach not in self.name:
            self.name += ":" + self.approach

    def __maybe_print_dashboard_url__(self):
        if self._dashboard_url_computed:
            return

        should_display_url = True
        if self.grid_search_id is not None:
            should_display_url = False
        elif self.cross_validation_id is not None:
            should_display_url = False

        if self.mdata is not None and self.BEST_ESTIMATOR_KEY in self.mdata and self.mdata[self.BEST_ESTIMATOR_KEY]:
            should_display_url = True

        if should_display_url:
            url, error_msg = get_scrybe_dashboard_url_for_node(obj_node=self)
            if url:
                model_name = self.name if self.name else self.approach
                print("Scrybe dashboard URL for %s: %s" % (model_name, url))
                self._dashboard_url_displayed = True
        self._dashboard_url_computed = True

    def __get_upload_data__(self):
        def default_json(non_serializable_obj):
            try:
                return float(non_serializable_obj)
            except Exception:
                return "%s.%s" % (non_serializable_obj.__class__.__module__, non_serializable_obj.__class__.__name__)

        model_data = dict(
            created_in_run=self.created_in_run,
            name=self.name,
            approach=self.approach
        )

        if self.spec is not None:
            model_data["spec"] = json.dumps(self.spec, default=default_json)

        if self.path is not None:
            model_data["location"] = self.path

        if self.grid_search_id is not None:
            model_data["grid_search_id"] = self.grid_search_id

        if self.cross_validation_id is not None:
            model_data["cross_validation_id"] = self.cross_validation_id

        if self.mdata and len(self.mdata) > 0:
            model_data["mdata"] = self.mdata

        if self.features is not None and len(self.features) > 0:
            model_data["features"] = self.features

        if self.feature_importance is not None and len(self.feature_importance) > 0:
            feature_importance = json.loads(json.dumps(self.feature_importance, cls=ScrybeJSONEncoder))
            model_data["feature_importance"] = feature_importance

        if self.code_client_id:
            model_data["code_client_id"] = self.code_client_id
        return model_data

    def __clear_upload_data__(self):
        self.spec = None
        self.path = None
        self.features = None
        self.feature_importance = None
        self.code_client_id = None
        # grid_search_id, cross_validation_id and mdata should be sent every time


class BaseMetricTrackingNode(BaseTrackingNode):
    METRIC_NODE_MAP = dict()

    class LearningType(Enum):
        SUPERVISED = "supervised"
        UNSUPERVISED = "unsupervised"

    @classmethod
    def metric_node_type(cls) -> BaseTrackingNode.Type:
        raise NotImplementedError("Subclasses need to specify node type")

    @classmethod
    def get_node(cls, *args, **kwargs) -> 'BaseMetricTrackingNode':
        raise NotImplementedError("Subclasses need to specify node type")

    @classmethod
    def __del_node_key__(cls, node_key):
        if sys is None or sys.is_finalizing():
            return
        if node_key in cls.METRIC_NODE_MAP:
            del cls.METRIC_NODE_MAP[node_key]

    @classmethod
    def __construct_key__(cls, x_data_node: BaseTrackingNode, y_data_node: BaseTrackingNode,
                          model_node: BaseTrackingNode, key_suffix: Union[str, None]):
        node_key = ""
        node_key += x_data_node.client_id if x_data_node else ""
        node_key += ("_" + y_data_node.client_id) if y_data_node else ""
        node_key += ("_" + model_node.client_id) if model_node else ""
        node_key += ("_" + key_suffix) if key_suffix else ""
        if len(node_key) == 0:
            raise ValueError("All parent ids cannot be None")
        node_key = cls.metric_node_type().name + "_" + node_key
        return node_key

    @classmethod
    def __get_metric_node__(cls, oid: int, x_data_node: 'BaseTrackingNode', y_data_node: 'BaseTrackingNode',
                            model_node: BaseTrackingNode, key_suffix: Union[str, None]):
        node_key = cls.__construct_key__(x_data_node=x_data_node, y_data_node=y_data_node, model_node=model_node,
                                         key_suffix=key_suffix)
        if node_key in cls.METRIC_NODE_MAP:
            return cls.METRIC_NODE_MAP[node_key][0]
        self = cls(oid=oid, x_data_node=x_data_node, y_data_node=y_data_node, model_node=model_node)
        weak_refs = [weakref.ref(node, lambda r: cls.__del_node_key__(node_key=node_key)) for node in
                     [x_data_node, y_data_node, model_node] if node is not None]
        cls.METRIC_NODE_MAP[node_key] = (self, weak_refs)
        return self

    def __init__(self, oid: int, x_data_node: BaseTrackingNode, y_data_node: BaseTrackingNode,
                 model_node: BaseTrackingNode):
        super().__init__(oid=oid, version=0, node_type=self.metric_node_type())
        self.metric_data = dict()
        # IMP: These fields are meant for debugging only. DO NOT TAKE A DEPENDENCY ON THEM
        self._x_data_id_ = x_data_node.client_id
        self._y_data_id_ = y_data_node.client_id if y_data_node else None
        self._model_id_ = model_node.client_id if model_node else None
        self.learning_type = self.LearningType.SUPERVISED

    def add_metric(self, metric_data: Dict):
        self.metric_data = metric_data

    def __get_upload_data__(self) -> Dict:
        def default_json(non_serializable_obj):
            try:
                return float(non_serializable_obj)
            except Exception:
                return "%s.%s" % (non_serializable_obj.__class__.__module__, non_serializable_obj.__class__.__name__)

        metrics_dict = json.loads(json.dumps(self.metric_data, default=default_json))
        out = dict(metrics=metrics_dict)
        if self.learning_type:
            out["learning_type"] = self.learning_type.name
        return out

    def __clear_upload_data__(self):
        self.metric_data = dict()
        self.learning_type = None


class TrainMetricTrackingNode(BaseMetricTrackingNode):
    @classmethod
    def metric_node_type(cls) -> BaseTrackingNode.Type:
        return BaseTrackingNode.Type.TRAIN_METRIC

    @classmethod
    def get_node(cls, oid: int, x_train_data_node: BaseTrackingNode, y_train_data_node: BaseTrackingNode,
                 trained_model_node: BaseTrackingNode):
        return cls.__get_metric_node__(oid=oid, x_data_node=x_train_data_node, y_data_node=y_train_data_node,
                                       model_node=trained_model_node, key_suffix=None)

    def __init__(self, oid: int, x_data_node: BaseTrackingNode, y_data_node: BaseTrackingNode,
                 model_node: BaseTrackingNode):
        super().__init__(oid=oid, x_data_node=x_data_node, y_data_node=y_data_node, model_node=model_node)
        self.add_predecessor(predecessor_node=x_data_node, operations={Operations.TRAINING_DATA})
        if y_data_node is not None:
            self.add_predecessor(predecessor_node=y_data_node, operations={Operations.TRAINING_LABELS})
        self.add_predecessor(predecessor_node=model_node, operations={Operations.EVALUATION})


class ValidationMetricTrackingNode(BaseMetricTrackingNode):
    @classmethod
    def metric_node_type(cls) -> BaseTrackingNode.Type:
        return BaseTrackingNode.Type.VALIDATION_METRIC

    @classmethod
    def get_node(cls, oid: int, x_val_data_node: BaseTrackingNode, y_val_data_node: BaseTrackingNode,
                 trained_model_node: BaseTrackingNode):
        return cls.__get_metric_node__(oid=oid, x_data_node=x_val_data_node, y_data_node=y_val_data_node,
                                       model_node=trained_model_node, key_suffix=None)

    def __init__(self, oid: int, x_data_node: BaseTrackingNode, y_data_node: BaseTrackingNode,
                 model_node: BaseTrackingNode):
        super().__init__(oid=oid, x_data_node=x_data_node, y_data_node=y_data_node, model_node=model_node)
        self.add_predecessor(predecessor_node=x_data_node, operations={Operations.VALIDATION_DATA})
        if y_data_node is not None:
            self.add_predecessor(predecessor_node=y_data_node, operations={Operations.VALIDATION_LABELS})
        self.add_predecessor(predecessor_node=model_node, operations={Operations.EVALUATION})


class TestMetricTrackingNode(BaseMetricTrackingNode):
    @classmethod
    def metric_node_type(cls) -> BaseTrackingNode.Type:
        return BaseTrackingNode.Type.TEST_METRIC

    @classmethod
    def get_node(cls, oid: int, y_test_label_node: BaseTrackingNode, y_pred_data_node: BaseTrackingNode = None,
                 model_node: BaseTrackingNode = None):
        return cls.__get_metric_node__(oid=oid, x_data_node=y_test_label_node, y_data_node=y_pred_data_node,
                                       model_node=model_node, key_suffix=None)

    def __init__(self, oid: int, x_data_node: BaseTrackingNode, y_data_node: BaseTrackingNode = None,
                 model_node: BaseTrackingNode = None):
        super().__init__(oid=oid, x_data_node=x_data_node, y_data_node=y_data_node, model_node=model_node)
        if y_data_node is None and model_node is None:
            raise ValueError("Either model node or prediction output is required")
        self.add_predecessor(predecessor_node=x_data_node, operations={Operations.TEST_LABELS})
        if y_data_node is not None:
            self.add_predecessor(predecessor_node=y_data_node, operations={Operations.TEST_PREDICTIONS})
        if model_node is not None:
            self.add_predecessor(predecessor_node=model_node, operations={Operations.EVALUATION})

    def add_x_test(self, x_test_node: BaseTrackingNode):
        self.add_predecessor(predecessor_node=x_test_node, operations={Operations.TEST_INPUT})


class GhostMetricTrackingNode(BaseMetricTrackingNode):
    @classmethod
    def metric_node_type(cls) -> BaseTrackingNode.Type:
        return BaseTrackingNode.Type.GHOST_METRIC

    @classmethod
    def get_node(cls, oid: int, y_test_label_node: BaseTrackingNode, server_model_id: str,
                 y_pred_data_node: BaseTrackingNode = None):
        return cls.__get_metric_node__(oid=oid, x_data_node=y_test_label_node, y_data_node=y_pred_data_node,
                                       model_node=None, key_suffix=server_model_id)

    def __init__(self, oid: int, x_data_node: BaseTrackingNode, y_data_node: BaseTrackingNode = None,
                 model_node: BaseTrackingNode = None):
        super().__init__(oid=oid, x_data_node=x_data_node, y_data_node=y_data_node, model_node=model_node)
        self.add_predecessor(predecessor_node=x_data_node, operations={Operations.TEST_LABELS})
        if y_data_node is not None:
            self.add_predecessor(predecessor_node=y_data_node, operations={Operations.TEST_PREDICTIONS})
        if model_node is not None:
            self.add_predecessor(predecessor_node=model_node, operations={Operations.EVALUATION})
        self.server_model_id = None

    def set_model_id(self, server_model_id):
        self.server_model_id = server_model_id

    def add_x_test(self, x_test_node: BaseTrackingNode):
        self.add_predecessor(predecessor_node=x_test_node, operations={Operations.TEST_INPUT})

    def __get_upload_data__(self):
        out = super().__get_upload_data__()
        out["server_model_id"] = self.server_model_id
        return out


class ArtifactTrackingNode(BaseMetricTrackingNode):
    @classmethod
    def metric_node_type(cls) -> BaseTrackingNode.Type:
        return BaseTrackingNode.Type.ARTIFACT

    @classmethod
    def get_node(cls, oid: int, y_test_label_node: BaseTrackingNode, y_pred_data_node: BaseTrackingNode,
                 artifact_identifier: str, model_node: BaseTrackingNode = None):
        return cls.__get_metric_node__(oid=oid, x_data_node=y_test_label_node, y_data_node=y_pred_data_node,
                                       model_node=model_node, key_suffix=artifact_identifier)

    def __init__(self, oid: int, x_data_node: BaseTrackingNode, y_data_node: BaseTrackingNode,
                 model_node: BaseTrackingNode = None):
        super().__init__(oid=oid, x_data_node=x_data_node, y_data_node=y_data_node,
                         model_node=model_node)
        self.object_type = None
        self.add_predecessor(predecessor_node=x_data_node, operations={Operations.TEST_LABELS})
        self.add_predecessor(predecessor_node=y_data_node, operations={Operations.TEST_PREDICTIONS})
        if model_node is not None:
            self.add_predecessor(predecessor_node=model_node, operations={Operations.EVALUATION})

    def set_object_type(self, object_type: ArtifactType):
        self.object_type = object_type

    def __get_upload_data__(self):
        if self.object_type is None:
            raise ValueError("Artifact object type not set")

        def default_json(non_serializable_obj):
            try:
                return float(non_serializable_obj)
            except Exception as e:
                return "%s.%s" % (non_serializable_obj.__class__.__module__, non_serializable_obj.__class__.__name__)

        out = dict(object_type=self.object_type.name)
        out["name"] = "UNKNOWN"
        if len(self.metric_data.keys()) > 0:
            metrics_dict = json.dumps(self.metric_data, default=default_json)
            out["content"] = metrics_dict
            out["name"] = list(self.metric_data.keys())[0]
        if self.learning_type is not None:
            out["learning_type"] = self.learning_type
        return out



class DataArtifactTrackingNode(BaseMetricTrackingNode):
    @classmethod
    def metric_node_type(cls) -> BaseTrackingNode.Type:
        return BaseTrackingNode.Type.DATASET_ARTIFACT

    @classmethod
    def get_node(cls, oid: int, dataset_node_1: BaseTrackingNode, dataset_node_2: BaseTrackingNode,
                 artifact_identifier: str):
        return cls.__get_metric_node__(oid=oid, x_data_node=dataset_node_1, y_data_node=dataset_node_2, model_node=None,
                                       key_suffix=artifact_identifier)

    def __init__(self, oid: int, x_data_node: BaseTrackingNode, y_data_node: BaseTrackingNode,
                 model_node: BaseTrackingNode = None):
        super().__init__(oid=oid, x_data_node=x_data_node, y_data_node=y_data_node,
                         model_node=model_node)
        self.object_type = None
        if x_data_node is not None:
            self.add_predecessor(predecessor_node=x_data_node, operations={Operations.DATA_STATS})
        if y_data_node is not None:
            self.add_predecessor(predecessor_node=y_data_node, operations={Operations.DATA_STATS})

    def set_object_type(self, object_type: ArtifactType):
        self.object_type = object_type

    def __get_upload_data__(self):
        if self.object_type is None:
            raise ValueError("Artifact object type not set")

        def default_json(non_serializable_obj):
            try:
                return float(non_serializable_obj)
            except Exception as e:
                return "%s.%s" % (non_serializable_obj.__class__.__module__, non_serializable_obj.__class__.__name__)

        out = dict(object_type=self.object_type.name)
        out["name"] = "UNKNOWN"
        if len(self.metric_data.keys()) > 0:
            metrics_dict = json.dumps(self.metric_data, cls=ScrybeJSONEncoder)
            out["content"] = metrics_dict
            out["name"] = list(self.metric_data.keys())[0]

        return out


class BasicIteratorTrackingNode(DatasetTrackingNode):
    # TODO(msachdev): Disable source capture for native types until we find a clean means of doing it
    CAPTURE_SRC_CTXT = False
    ITERABLE_NODE_MAP = dict()

    @classmethod
    def __construct_key__(cls, parent_nodes):
        node_key = ""
        for item_node in parent_nodes:
            node_key += item_node.client_id
        node_key = hashlib.md5(node_key.encode('utf-8')).hexdigest()
        return node_key

    @classmethod
    def __del_node_key__(cls, node_key):
        if sys is None or sys.is_finalizing():
            return
        if node_key in cls.ITERABLE_NODE_MAP:
            del cls.ITERABLE_NODE_MAP[node_key]

    @classmethod
    def get_node(cls, oid: int, obj) -> Union['BasicIteratorTrackingNode', None]:
        # This import cannot be at the top-level since it ends up creating a cyclical dependency between this
        # file and tracking_graph.py
        from scrybe.internal.depgraph import TrackingGraph
        if obj is None:
            return None
        parent_nodes = []
        if isinstance(obj, list) or isinstance(obj, tuple):
            iterable = obj
        elif isinstance(obj, dict):
            iterable = obj.values()
        else:
            return None
        for item in iterable:
            if not TrackingGraph.has_tracked_obj(item):
                continue
            item_node = TrackingGraph.get_node_for_tracked_object(item)
            parent_nodes.append(item_node)
        if len(parent_nodes) == 0:
            return None
        node_key = cls.__construct_key__(parent_nodes=parent_nodes)
        if node_key in cls.ITERABLE_NODE_MAP:
            return cls.ITERABLE_NODE_MAP[node_key][0]
        self = cls(oid=oid, version=0, obj_type=cls.ObjectType.BASIC_ITERATOR)
        weak_refs = []
        for parent_node in parent_nodes:
            self.add_predecessor(predecessor_node=parent_node, operations={Operations.CONCATENATION})
            weak_refs.append(weakref.ref(parent_node, lambda r: cls.__del_node_key__(node_key=node_key)))
        cls.ITERABLE_NODE_MAP[node_key] = (self, weak_refs)
        return self


class PlotArtifactTrackingNode(BaseTrackingNode):
    def __init__(self, oid: int, version: int):
        super().__init__(oid=oid, version=version, node_type=BaseTrackingNode.Type.DATASET_ARTIFACT)
        self.object_type = ArtifactType.PLOT_IMAGE
        self.content = None
        self.thumbnail = None
        self.name = ''

    def set_object_type(self, object_type: ArtifactType):
        self.object_type = object_type

    def set_content(self, figure, name):
        try:
            plot_title = None
            try:
                labels = set()
                for axes in figure.axes:
                    labels.add(axes.get_label())
                    handles, axes_labels = axes.get_legend_handles_labels()
                    for label in axes_labels:
                        labels.add(label)
                    if not plot_title:
                        plot_title = axes.get_title()
                    labels.add(axes.get_title())
                    labels.add(axes.get_xlabel())
                    xticks = axes.get_xticklabels()
                    if len(xticks) == 1 and hasattr(xticks[0], 'get_text'):
                        labels.add(xticks[0].get_text())
                    labels.add(axes.get_ylabel())
                    yticks = axes.get_yticklabels()
                    if len(yticks) == 1 and hasattr(yticks[0], 'get_text'):
                        labels.add(yticks[0].get_text())
                if hasattr(figure, '_suptitle') and hasattr(figure._suptitle, 'get_text'):
                    if not plot_title:
                        plot_title = figure._suptitle.get_text()
                    labels.add(figure._suptitle.get_text())
                if '' in labels:
                    labels.remove('')
                if None in labels:
                    labels.remove(None)
                if len(labels) > 0:
                    if self.labels is None:
                        self.labels = list(labels)
                    else:
                        self.labels = list(set(self.labels + list(labels)))
            except Exception as e:
                LOGGER.debug("Unable to get plot labels: %s" % str(e))
            max_dim = 32
            if figure.get_figheight() > max_dim or figure.get_figwidth() > max_dim:
                figure = figure.copy()
                figure.set_figheight(figure.get_figheight() / 2)
                figure.set_figwidth(figure.get_figwidth() / 2)
            import io, base64
            bytes_image = io.BytesIO()
            figure.savefig(bytes_image, format='png')
            self.content = base64.b64encode(bytes_image.getvalue()).decode('utf-8')
            bytes_image.seek(0)
            from PIL import Image
            img = Image.open(bytes_image)
            img.thumbnail((200, 200))
            byte_arr = io.BytesIO()
            img.save(byte_arr, format='PNG')
            self.thumbnail = base64.b64encode(byte_arr.getvalue()).decode('utf-8')

            if plot_title is not None and isinstance(plot_title, str) and len(plot_title) > 0:
                self.name = plot_title
                self.is_name_final = True
            elif name is not None and not self.is_name_final:
                if not self.name:
                    self.name = name
                elif name != self.name.split(" ")[-1]:
                    self.name += ' ' + name
        except Exception as e:
            LOGGER.debug("Unable to get plot content: %s" % str(e))

    def __maybe_print_dashboard_url__(self):
        if self._dashboard_url_computed:
            return
        url, error_msg = get_scrybe_dashboard_url_for_node(obj_node=self)
        if url:
            plot_name = self.name if self.name else "Plot"
            print("Scrybe dashboard URL for %s: %s" % (plot_name, url))
            self._dashboard_url_displayed = True
        self._dashboard_url_computed = True

    def __get_upload_data__(self):
        if self.object_type is None:
            raise ValueError("Artifact object type not set")

        out = dict(object_type=self.object_type.name)
        out["name"] = "UNKNOWN"
        if self.content is not None and self.thumbnail is not None:
            out["content"] = self.content
            out["thumbnail"] = self.thumbnail
            out["name"] = self.name
        return out

    def __clear_upload_data__(self):
        pass


class PipelineTrackingNode(BaseTrackingNode):
    def __init__(self, oid: int, version: int, approach: str, name: str, path: str, hyperparameters: dict,
                 architecture: dict):
        super().__init__(oid=oid, version=version, node_type=BaseTrackingNode.Type.PIPELINE_OBJ)
        self.approach = approach
        self.name = name
        self.path = path
        self.hyperparameters = hyperparameters
        self.architecture = architecture

    def add_predecessor(self, predecessor_node: BaseTrackingNode, operations: Set[Operations],
                        replace_predecessor: 'BaseTrackingNode' = None):
        super().add_predecessor(predecessor_node=predecessor_node, operations=operations,
                                replace_predecessor=replace_predecessor)
        self.add_reference(predecessor_node)

    def set_node_name_if_not_final(self, name: str):
        super().set_node_name_if_not_final(name)
        if self.name is not None:
            self.name += ":" + self.approach

    def __get_upload_data__(self):
        pass

    def __clear_upload_data__(self):
        pass


class UtilityNode(BaseTrackingNode):
    def __init__(self, oid: int, version: int):
        super().__init__(oid=oid, version=version, node_type=BaseTrackingNode.Type.UTILITY)

    def __get_upload_data__(self):
        pass

    def __clear_upload_data__(self):
        pass


class CodeTrackingNode(BaseTrackingNode):
    def __clear_upload_data__(self):
        self.files_dict = None
        if self.uploaded_packages is not None:
            self.uploaded_packages.update(self.packages)
        else:
            self.uploaded_packages = self.packages
        self.packages = None

    def __get_upload_data__(self) -> Dict:
        out = dict()
        if self.commit_id:
            out["commit_id"] = self.commit_id
        if self.branch:
            out["branch"] = self.branch
        if self.files_dict is not None and len(self.files_dict) > 0:
            out["files"] = json.dumps(self.files_dict)
        if self.packages is not None and len(self.packages) > 0:
            out["packages"] = json.dumps(self.packages)
        return out

    def __is_module_already_in_dict__(self, package, fullname):
        if package is None:
            return False
        if fullname in package:
            return True
        sub_modules = fullname.split(".")
        for i in range(len(sub_modules)):
            if ".".join(sub_modules[:i]) in package:
                return True
        return False

    def __init__(self, oid: int, version: int):
        super().__init__(oid=oid, version=version, node_type=BaseTrackingNode.Type.CODE)
        self.commit_id = None
        self.branch = None
        self.files_dict = None
        self.packages = None
        self.uploaded_packages = None

    def set_src_code_for_filename(self, filename: str, src_code: Union[str, list], overwrite=False):
        if self.files_dict is None:
            self.files_dict = dict()

        if filename not in self.files_dict:
            self.files_dict[filename] = {'content': [], 'overwrite': overwrite}

        if isinstance(src_code, str):
            self.files_dict[filename]['content'] = [src_code]
        elif isinstance(src_code, list):
            self.files_dict[filename]['content'] += src_code

    def add_package(self, module_name: str, version: str):
        if self.packages is None:
            self.packages = dict()
        if self.__is_module_already_in_dict__(package=self.packages, fullname=module_name) or (
                self.uploaded_packages is not None
                and self.__is_module_already_in_dict__(package=self.uploaded_packages, fullname=module_name)
        ):
            return
        self.packages[module_name] = version
        keys_to_pop = []
        for key in self.packages:
            if key.startswith(module_name + "."):
                keys_to_pop.append(key)
        for key in keys_to_pop:
            self.packages.pop(key)
