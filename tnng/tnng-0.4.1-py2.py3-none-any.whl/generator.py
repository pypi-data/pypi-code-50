import typing
import warnings
import numbers

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
        self._len, self._node_type_layers, _node_types = \
            self._calc_num_of_all_combination(multi_head_linked_list_layer)
        self._node_types_list = sorted(list(_node_types))

    def _calc_num_of_all_combination(self, multi_head_linked_list_layer) -> (int, typing.List[int], set):
        ''' calculate each the number of layer's combination.
        '''
        num = 1
        node_type_layers = []
        node_types = set()
        for node in self.multi_head_linked_list_layer.graph.nodes(data=True):
            if not 'args' in node[1].keys():
                continue
            if not node[1]['args']:
                continue
            if 'layer' in node[1].keys():
                # append_lazy
                _n_type = len(node[1]['args'])
                node_types.add(node[1]['layer'].__name__)
            else:
                _n_type = len(node[1]['args'][0])
                node_types.add('value')
            node_type_layers.append(_n_type)
            num *= _n_type
        return num, node_type_layers, node_types

    def __getitem__(self, idx):
        if idx > self._len:
            raise IndexError(f"access by {idx}, max length is {self._len}")
        graph = self.multi_head_linked_list_layer.graph
        layer_index_list = self._get_layer_index_list(idx, self._node_type_layers)
        last_node = len(graph.nodes()) - 1
        no_ordered_outputs = []
        outputs = []
        for layer_idx, node in zip(layer_index_list, graph.nodes(data=True)):
            if 'layer' in node[1].keys():
                # append_lazy
                layer = node[1]['layer']
                if layer == DummyConcat:
                    no_ordered_outputs.append('concat')
                else:
                    kwargs = node[1]['args'][layer_idx]
                    no_ordered_outputs.append(layer(**kwargs))
            else:
                value = node[1]['args'][0][layer_idx]
                no_ordered_outputs.append(value)
        outputs.append([no_ordered_outputs[last_node],])

        parents = list(graph.predecessors(last_node))
        while True:
            if parents.count(None) == len(parents):
                break
            _output = []
            _parents = []
            for parent in parents:
                if parent is None:
                    _output.append(None)
                    __parents = [None,]
                else:
                    _output.append(no_ordered_outputs[parent])
                    __parents = list(graph.predecessors(parent))
                if not __parents:
                    _parents += [None,]
                else:
                    _parents += __parents
            outputs.append(_output)
            parents = _parents
        if self.dump_nn_graph:
            nodelist = range(len(graph.nodes()))
            graph = graph.to_undirected()
            adj = nx.to_numpy_matrix(graph, nodelist=nodelist)
            node_features = self._create_node_features(idx, layer_index_list)
            return outputs[::-1], (adj, node_features)
        else:
            return outputs[::-1]

    def _create_node_features(self, idx, layer_index_list):
        graph = self.multi_head_linked_list_layer.graph
        node_features = []
        dim_features = len(self._node_types_list)
        for layer_idx, node in zip(layer_index_list, graph.nodes(data=True)):
            x = np.zeros(dim_features)
            if 'layer' in node[1].keys():
                # append_lazy
                layer_name = node[1]['layer'].__name__
                idx = self._node_types_list.index(layer_name)
                kwargs = node[1]['args'][layer_idx]
                # only support one kwarg.
                values = list(kwargs.values())
                if values:
                    value = values[0]
                    if isinstance(value, numbers.Number):
                        x[idx] = value
                    else:
                        warnings.warn(f"not support {kwargs} in node features")
                else:
                    # for a layer with no arguments.
                    x[idx] = 1
            else:
                idx = self._node_types_list.index('value')
                value = node[1]['args'][0][layer_idx]
                x[idx] = value

            node_features.append(x)
        return np.vstack(node_features)

    def _get_layer_index_list(self, idx: int, node_type_layers):
        _idx = idx
        layer_index_list = []
        for n_args in node_type_layers:
            layer_index_list.append(_idx % n_args)
            _idx //= n_args
        return layer_index_list

    def __len__(self):
        return self._len

    def draw_graph(self, filename: str):
        import matplotlib.pyplot as plt
        G = self.multi_head_linked_list_layer.graph
        pos = nx.spring_layout(G, iterations=200)
        nx.draw(G, pos, with_labels=True)
        plt.savefig(filename)
        return G
