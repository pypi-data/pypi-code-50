from typing import Dict


class LineageGraphEdge(object):
    def __init__(self, src_id: str, metadata: Dict):
        self.src_id = src_id
        self.metadata = metadata


class LineageGraphNode(object):
    def __init__(self, id: str, name: str, metadata: Dict):
        self.id = id
        self.name = name
        self.metadata = metadata
        self.incoming_edges = set()

    def add_incoming_edge(self, src_id: str, metadata: Dict):
        self.incoming_edges.add(LineageGraphEdge(src_id=src_id, metadata=metadata))


class LineageGraph(object):
    def __init__(self):
        self.nodes = dict()

    def add_node(self, node: LineageGraphNode):
        self.nodes[node.id] = node

    def to_json(self):
        out = list()
        for _, n in self.nodes.items():
            node_dict = dict()
            node_dict["id"] = n.id
            node_dict["info"] = n.metadata
            node_dict["incoming_edges"] = list([dict(predecessor=e.src_id, info=e.metadata) for e in n.incoming_edges])
            out.append(node_dict)
        return out

