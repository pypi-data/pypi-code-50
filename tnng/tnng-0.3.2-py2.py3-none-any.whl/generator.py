import typing
import warnings

## for graph dumpping
import networkx as nx
import numpy as np

from .layer import Layer, LazyLayer, MultiHeadLinkedListLayer, DummyConcat


class Generator:
    def __init__(self,
                 multi_head_linked_list_layer: MultiHeadLinkedListLayer,
                 dump_nn_graph: bool = False,
    ):
        self.multi_head_linked_list_layer = multi_head_linked_list_layer
        self.dump_nn_graph = dump_nn_graph
        self._len, self.layer_num_list = self._preprocess(multi_head_linked_list_layer)
        if self.dump_nn_graph:
            self._backbone_graph, self._node_features = \
                self._create_backbone_graph(multi_head_linked_list_layer)

    def _create_backbone_graph(self, multi_head_linked_list_layer):
        ''' only work for lazy_layer, create a backbone graph using networkx.
        '''
        backbone_graph = nx.Graph()
        cur = [multi_head_linked_list_layer.tail,]
        node_idx = 0
        node_labels = {}
        node_labels[node_idx] = str(multi_head_linked_list_layer.tail.klass.__name__)
        node_features = set()
        for _ in range(multi_head_linked_list_layer.depth-1):
            parents = []
            for c in cur:
                cur_node_idx = node_idx
                for p in c.parent[::-1]:
                    if p is None or p.parent is None:
                        continue
                    node_idx += 1
                    try:
                        node_labels[node_idx] = str(p.klass.__name__)
                        node_features.add(p.klass.__name__)
                    except AttributeError as e:
                        warnings.warn(f"{e}")
                        node_labels[node_idx] = None
                    except Exception as e:
                        raise e
                    backbone_graph.add_node(node_idx)
                    backbone_graph.add_edge(cur_node_idx, node_idx)
                    parents.append(p)
            cur = parents
        node_features = sorted(node_features)
        return backbone_graph, node_features

    def _preprocess(self, multi_head_linked_list_layer) -> (int, typing.List[int]):
        ''' calculate each the number of layer's combination.
        '''
        cur = [multi_head_linked_list_layer.tail,]
        num = 1
        num *= len(multi_head_linked_list_layer.tail.layers)
        num_candidates = [[len(multi_head_linked_list_layer.tail.layers),],]
        for _ in range(multi_head_linked_list_layer.depth-1):
            parents = []
            _each_layer_num_candidates = []
            for c in cur:
                if  c is None or c.parent is None:
                    parents.append(None)
                    _each_layer_num_candidates.append(1)
                    continue
                for p in c.parent:
                    parents.append(p)
                    if p.layers is not None:
                        num *= len(p.layers)
                        _each_layer_num_candidates.append(len(p.layers))
                    else:
                        _each_layer_num_candidates.append(1)
            if _each_layer_num_candidates:
                num_candidates.append(_each_layer_num_candidates)
            cur = parents
        return num, num_candidates

    def __getitem__(self, idx):
        if idx > self._len:
            raise IndexError(f"access by {idx}, max length is {self._len}")
        layer_index_list = self._get_layer_index_list(idx)
        out = []
        cur = [self.multi_head_linked_list_layer.tail,]
        for layer_indcies in layer_index_list:
            # from tail to head
            layer = []
            parents = []
            for current_layer, l_idx in zip(cur, layer_indcies):
                if current_layer is None:
                    layer.append(None)
                elif current_layer.layers is not None:
                    if isinstance(current_layer, Layer):
                        layer.append(current_layer.layers[l_idx])
                    elif isinstance(current_layer, LazyLayer):
                        kwargs = current_layer.kwargs_list[l_idx]
                        klass = current_layer.klass
                        if klass == DummyConcat:
                            layer.append(current_layer.klass)
                        else:
                            layer.append(current_layer.klass(**kwargs))
                    else:
                        raise NotImplementedError
                else:
                    layer.append(None)
                if current_layer is None:
                    parents.append(None)
                    continue
                elif current_layer.parent is None:
                    parents.append(None)
                    continue
                for parent in current_layer.parent:
                    parents.append(parent)
            cur = parents
            out.append(layer)
        if self.dump_nn_graph:
            nodelist = range(len(self._backbone_graph.nodes()))
            adj = nx.to_numpy_matrix(self._backbone_graph, nodelist=nodelist)
            node_features = self._create_node_features(idx, layer_index_list)
            return out[::-1], (adj, node_features)
        else:
            return out[::-1]

    def _create_node_features(self, idx, layer_index_list):
        cur = [self.multi_head_linked_list_layer.tail,]
        node_idx = 0
        node_attributes = {}
        for layer_indcies in layer_index_list:
            # from tail to head
            layer = [] #TODO: refactor: layer is not necessary
            parents = []
            for current_layer, l_idx in zip(cur, layer_indcies):
                if current_layer is None:
                    layer.append(None)
                elif current_layer.layers is not None:
                    if isinstance(current_layer, Layer):
                        layer.append(current_layer.layers[l_idx])
                    elif isinstance(current_layer, LazyLayer):
                        kwargs = current_layer.kwargs_list[l_idx]
                        klass = current_layer.klass
                        x = np.zeros(len(self._node_features))
                        idx = self._node_features.index(current_layer.klass.__name__)
                        if klass == DummyConcat:
                            layer.append(current_layer.klass)
                            x[idx] = 1
                        else:
                            layer.append(current_layer.klass(**kwargs))
                            if kwargs:
                                value = list(kwargs.values())[0]
                            else:
                                value = 1
                            if not isinstance(value, (int, float)):
                                # for example, tuple arguments and list or something.
                                # current version can't convert one numpy value.
                                value = 1
                            x[idx] = value
                        node_attributes[node_idx] = {'features': x}
                        node_idx += 1
                    else:
                        raise NotImplementedError
                else:
                    layer.append(None)
                if current_layer is None:
                    parents.append(None)
                    continue
                elif current_layer.parent is None:
                    parents.append(None)
                    continue
                for parent in current_layer.parent:
                    parents.append(parent)
            cur = parents
        nx.set_node_attributes(self._backbone_graph, node_attributes)
        sorted_features = sorted(self._backbone_graph.nodes(data=True), key=lambda x: x[0])
        node_features = [x[1]['features'] for x in sorted_features]
        return np.vstack(node_features)

    def _get_layer_index_list(self, idx):
        _idx = idx
        layer_index_list = []
        for eles in self.layer_num_list:
            _index_list = []
            for _, ele in enumerate(eles):
                _index_list.append(_idx % ele)
                _idx //= ele
            layer_index_list.append(_index_list)
        return layer_index_list

    def __len__(self):
        return self._len
