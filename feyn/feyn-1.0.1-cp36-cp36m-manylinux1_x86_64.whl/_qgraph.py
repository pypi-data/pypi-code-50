from typing import List

import networkx as nx

import _feyn
from feyn import DotRenderer, Graph


class QGraph:
    """
    The QGraph is generated from the QLattice and contains all theoretically possible combinations for given Input Registers to output Registers.

    It is tuned to solve a specific task, so we can evaluate its performance and extract learnings to send back to our QLattice.

    This is equivalent to a model in other frameworks.
    """
    def __init__(self, graph_dict: dict):
        """Construct a new 'QGraph' object.

        Arguments:
            graph_dict {dict} -- A dictionary of QGraphs
        """
        # TODO: Documentation: What are the keys graph_dict?
        self.G = nx.readwrite.json_graph.node_link_graph(graph_dict)
        self.out_reg = graph_dict["out_reg"]

        self.graphs = self._extract_graphs()

    def render(self):
        """ Render Qgraph.

        Returns:
            graphviz.Digraph -- GraphViz representation.
        """
        return DotRenderer.renderqgraph(self.G)

    def head(self, n=5):
        """ Render most probable Graphs.

        Keyword Arguments:
            n {int} -- Number of graphs to display (default: {5}).
        """
        import IPython
        for i in range(n):
            IPython.display.display(self.graphs[i])

    def tune(self, X, Y, epochs=100, showgraph=True, edgepenalty=0.001):
        """ Tune Qgraph with given samples.

        Arguments:
            X {Iterable} -- Input values.
            Y {Iterable} -- Expected output.

        Keyword Arguments:
            epochs {int} -- Number of epochs to run (default: {100}).
            showgraph {bool} -- show a live updated graph sample.
            edgepenalty {float} -- Penalty configuration (default: {0.001}).
        """

        # Magic support for pandas DataFrame and Series
        if type(X).__name__ == "DataFrame":
            X = {col: X[col].values for col in X.columns}

        if type(Y).__name__ == "Series":
            Y = Y.values

        # If graphviz is not installed don't print
        if not DotRenderer.check_render():
            showgraph=False

        for epoch in range(epochs):
            for wg in self.graphs:
                wg._tune(X, Y, 1)

            # Sort by decreasing loss after adding penalty for number of edges
            self.graphs.sort(key=lambda g: g.loss_ema * (1 + g.edge_count * edgepenalty), reverse=False)

            status = "Epoch %i: Squared Error: %.6f" % (epoch, self.graphs[0].loss_ema)
            if showgraph:
                import IPython
                dot = DotRenderer.rendergraph(self.graphs[0])
                dot.attr(label=status)
                IPython.display.clear_output(wait=True)
                IPython.display.display(dot)

            else:
                print(status)

    def _extract_graphs(self) -> List[Graph]:
        graphs = []

        for nodeid, data in self.G.nodes(data=True):
            if data["type"] != "reg":
                graphs.append(self._prune(nodeid))

        # TODO: This should not be neccesary
        graphs = list(set(graphs))
        return sorted(graphs, key=lambda n: n.strength, reverse=True)

    def _prune(self, nodeid: int) -> Graph:
        needed = nx.algorithms.dag.ancestors(self.G, nodeid)
        needed.add(nodeid)
        subgraph = self.G.subgraph(needed)

        # The following algorithm builds a 1D array of nodes
        # that preserverves execution order
        nodelist = []
        current = [nodeid]
        while len(current) > 0:
            node = current.pop(0)
            if node in nodelist:
                nodelist.remove(node)
            nodelist.insert(0, node)
            for pred in subgraph.predecessors(node):
                current.append(pred)

        # Build a graph with the interactions
        sz = len(nodelist)+1
        graph = Graph(sz)

        for i, nodeid in enumerate(nodelist):
            data = subgraph.nodes[nodeid]

            interaction = Graph._get_interaction(data)
            graph.set_interaction(i, interaction)

            if data["type"]=="reg":
                interaction.set_source(0, -1)
                continue

            interaction.linkdata = [None, None]

            for pred, _, data in subgraph.in_edges(nodeid, data=True):
                source_idx = nodelist.index(pred)
                ordinal = data["ord"]
                interaction.set_source(ordinal, source_idx)
                interaction.linkdata[ordinal] = data

        out_reg = Graph._get_interaction(self.out_reg)
        out_reg.linkdata = [{"ord": 0}]

        out_reg.set_source(0, sz-2)
        graph.set_interaction(sz-1, out_reg)

        graph.strength = self.G.nodes[nodeid]["output_strength"]

        return graph

    def __repr__(self):
        regcnt = 0
        double = 0
        single = 0
        for n, data in self.G.nodes.data():
            if data["type"] == "reg":
                regcnt += 1

            else:
                legs = data["legs"]
                if legs == 1:
                    single += 1
                else:
                    double += 1

        out_label = self.out_reg["label"]
        return "QGraph for '%s' <size: %i (%i registers, %i singles, %i doubles)>" % (out_label, regcnt+double+single, regcnt, single, double)
