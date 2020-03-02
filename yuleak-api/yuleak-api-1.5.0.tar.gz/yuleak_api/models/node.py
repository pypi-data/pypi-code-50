class Node:
    """Graph node model"""
    def __init__(self):
        self.id = None
        self.label = None
        self.type = None
        self.clean = False
        self.neighbors = set()

    @classmethod
    def from_json(cls, node_json):
        node = cls()
        node.id = node_json.get('id')
        node.label = node_json.get('label')
        node.type = node_json.get('type')
        node.clean = node_json.get('ok', True)
        return node

    def connect(self, child):
        """Connect the current node and the child node.

        Args:
            child (Node): Node to connect
        """
        self.neighbors.add(child)
        child.neighbors.add(self)

    def __repr__(self):
        return '<Node {0}> {1} - {2}'.format(self.id, self.type, self.label)
