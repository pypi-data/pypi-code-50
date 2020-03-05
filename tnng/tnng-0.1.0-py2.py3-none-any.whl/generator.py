from .layer import MultiHeadLinkedListLayer


class Generator:
    def __init__(self, multi_head_linked_list_layer: MultiHeadLinkedListLayer):
        self.multi_head_linked_list_layer = multi_head_linked_list_layer
        self._len, self.layer_num_list = self._preprocess(self.multi_head_linked_list_layer)

    def _preprocess(self, multi_head_linked_list_layer) -> int:
        cur = [multi_head_linked_list_layer.tail,]
        num = 1
        num *= len(multi_head_linked_list_layer.tail.layers)
        num_parents = [[len(multi_head_linked_list_layer.tail.layers),],]
        for _ in range(multi_head_linked_list_layer.depth-1):
            parents = []
            _each_layer_num_parents = []
            for c in cur:
                if  c is None or c.parent is None:
                    parents.append(None)
                    _each_layer_num_parents.append(1)
                    continue
                for p in c.parent:
                    parents.append(p)
                    if p.layers is not None:
                        num *= len(p.layers)
                        _each_layer_num_parents.append(len(p.layers))
                    else:
                        _each_layer_num_parents.append(1)
            if _each_layer_num_parents:
                num_parents.append(_each_layer_num_parents)
            cur = parents
        return num, num_parents

    def __getitem__(self, idx):
        if idx > self._len:
            raise IndexError(f"access by {idx}, max length is {self._len}")
        layer_index_list = self._get_layer_index_list(idx)
        out = []
        cur = [self.multi_head_linked_list_layer.tail,]
        for layer_indcies in layer_index_list:
            layer = []
            parents = []
            _each_layer_num_parents = []
            for c, l_idx in zip(cur, layer_indcies):
                if c is None:
                    layer.append(None)
                elif c.layers is not None:
                    layer.append(c.layers[l_idx])
                else:
                    layer.append(None)
                if c is None:
                    parents.append(None)
                    continue
                elif c.parent is None:
                    parents.append(None)
                    continue
                for p in c.parent:
                    parents.append(p)
            cur = parents
            out.append(layer)
        return out[::-1]

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
