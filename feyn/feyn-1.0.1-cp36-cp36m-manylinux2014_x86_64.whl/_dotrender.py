"""Helpers to render objects into DOT source"""
import numpy as np
import subprocess

def is_graphviz_installed():
    try:
        subprocess.run(['dot', '-V'])
        return True
    except:
        return False

class DotRenderer:
    @staticmethod
    def check_render():
        return is_graphviz_installed()

    @staticmethod
    def rendergraph(graph, viewport=None):
        """
        Render a graph from a qgraph as a graphviz DOT representation.

        It is suitable for rendering as a graph.

        Arguments:
            graph {feyn.Graph} -- The 'Graph' object to render.

        Keyword Arguments:
            viewport {str} -- The viewport to speficify the final size of the output (default: {None})

        Returns:
            graphviz.Digraph -- The graphviz DOT representation of the graph.
        """

        if not is_graphviz_installed():
            return "GraphViz is not installed, see instructions on how to install to plot the graphs"

        import graphviz

        dot = graphviz.Digraph("Graph")
        if viewport is not None:
            dot.attr("graph", viewport=viewport)

        dot.attr("node", fontsize="7")
        dot.attr("node", fixedsize="true")
        dot.attr("node", width=".6")
        dot.attr("node", height=".3")
        dot.attr("edge", fontsize="6")
        dot.attr("edge", penwidth=".4")
        dot.attr("edge", arrowsize=".5")

        dot.attr("node", fixedsize="true")
        dot.graph_attr['rankdir'] = 'LR'

        for d in range(graph.size):
            interaction = graph.get_interaction(d)
            nodeid = str(interaction.latticeloc)

            if interaction.errcode:
                if interaction.errcode == 1:
                    color = "#ff4040"
                else:
                    color = "#c00000"
            else:
                if interaction.type in ("cat", "cont"):
                    color = "#008c88"
                else:
                    color = "#c0c0c0"

            if d == graph.size-1 and graph.accuracy_ema is not None:
                rmse = np.sqrt(graph.loss_ema)
                label = "Acc: %.1f%%\nE: %.3E" % (graph.accuracy_ema*100, rmse)
            else:
                label = interaction.label
                if len(label) > 10:
                    label = label[:10]+".."

            tooltip = "%r: %i\n%s" % (interaction.latticeloc, interaction.gluamine, interaction.tooltip)
            dot.node(nodeid, label=label, style="filled", color=color, tooltip=tooltip)

            for ix, src in enumerate(interaction.sources):
                if src != -1:
                    scrinteraction = graph.get_interaction(src)
                    srcid = str(scrinteraction.latticeloc)
                    dot.edge(srcid, nodeid, label=str(ix))

        return dot

    @staticmethod
    def renderqgraph(graph):
        """
        Render an entire qgraph as a graphviz DOT representation.

        It is suitable for rendering as a graph.

        Arguments:
            graph {feyn.QGraph} -- The 'QGraph' object to render.

        Returns:
            graphviz.Digraph -- The graphviz DOT representation of the graph.
        """
        if not is_graphviz_installed():
            return "GraphViz is not installed, see instructions on how to install to plot the graphs"
            
        import graphviz

        dot = graphviz.Digraph("Graph", engine="twopi")

        dot.attr("node", fontsize="6")
        dot.attr("node", fixedsize="true")
        dot.attr("node", width=".5")
        dot.attr("node", height=".2")
        dot.attr("edge", fontsize="6")
        dot.attr("edge", penwidth=".3")
        dot.attr("edge", arrowsize=".4")

        dot.graph_attr['rankdir'] = 'LR'

        for nodeid, data in graph.nodes.data():
            if data["type"] == "reg":
                # A register node
                tooltip = "%s (%s)" % (data['label'], data['celltype'])
                label = data['label']
                if len(label) > 13:
                    label = label[:12] + ".."
                dot.node(str(nodeid), label=label, style="filled", tooltip=tooltip, color="#ff2020")
            else:
                # A cell node
                if data["output_strength"] > 0:
                    color = "#5050ff"
                else:
                    color = "#a0a0a0"

                tooltip = "%s%i (output strength: %f)" % (data["celltype"], data["legs"], data["output_strength"])
                dot.node(str(nodeid), label=str(data['location']), style="filled", color=color, tooltip=tooltip)

        for src, nxt, data in graph.edges.data():
            dot.edge(str(src), str(nxt), label=str("%i:%i" % (data["ord"], data["direction"])))

        return dot
