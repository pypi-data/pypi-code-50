import networkx as nx
from itertools import combinations

class DFGraph(nx.DiGraph):

    def __init__(self, nodes:list=None, edges:list=None, starts:list=None, ends:list=None, eps:int=0):
        super().__init__()

        if nodes is not None:
            self.add_nodes_from(nodes)
        if edges is not None:
            if all(len(e) == 2 for e in edges) or not all(len(e) == 3 for e in edges):
                edges = [(e[0], e[1], 1) for e in edges]
            self.add_weighted_edges_from(edges)
        if starts is not None:    
            self.starts = starts
        if ends is not None:
            self.ends = ends
        self.eps = eps

    def __eq__(self, other):
        return nx.is_isomorphic(self, other)
    
    def edge_freq(self):
        return {k: self.edges[k]['weight'] for k in self.edges()}

    def invert(self) -> "DFGraph":
        """Invert the graph, s.t. we remove all bidirectional edges, and
        add bidirctional edges to pairs of nodes that didn't had them before.

        Returns
        -------
        DFGraph
            The directly follows graph representation of a log.

        Examples
        --------
        >>> G = pm.DFGraph(nodes=["a", "b", "c", "d"], edges=[
            ("a", "b"),
            ("c", "d"),
            ("d", "c")
        ])
        >>> G.invert()
        DFGraph(nodes=['a', 'b', 'c', 'd'], edges=[
            ('a', 'b'): 1,
            ('a', 'c'): 1,
            ('a', 'd'): 1,
            ('b', 'a'): 1,
            ('b', 'c'): 1,
            ('b', 'd'): 1,
            ('c', 'a'): 1,
            ('c', 'b'): 1,
            ('d', 'a'): 1,
            ('d', 'b'): 1
        ])

        """
        G = self.copy()

        for u, v in combinations(self.nodes, r=2):
            if self.has_edge(u, v) and self.has_edge(v, u):
                G.remove_edges_from([(u, v), (v, u)])
            elif self.has_edge(u, v):
                G.add_edge(v, u, weight=1)
            elif self.has_edge(v, u):
                G.add_edge(u, v, weight=1)
            else:
                G.add_weighted_edges_from([(u, v, 1), (v, u, 1)])
        
        return G

    def __str__(self):
        edges = []
        for edge in list(sorted(self.edges)):
            freq = 0
            attr = self.get_edge_data(edge[0], edge[1])
            if attr is not None and "weight" in attr:
                freq = attr["weight"]
            edges.append("{}: {}".format(edge, freq))
        
        return "DFGraph(nodes={}, edges=[{}])".format(list(sorted(self.nodes)), ", ".join(edges))

    def __repr__(self):
        return self.__str__()
                