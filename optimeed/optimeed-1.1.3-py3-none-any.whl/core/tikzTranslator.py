import os
from .graphs import Graphs, Graph, Data
from .tools import indentParagraph
import numpy as np
import colorsys

templates_tikz = os.path.join(os.path.dirname(__file__), 'templates_tikz')


def convert_linestyle(linestyle):
    try:
        linestyles = {"-": "solid", "--": "dashed", "..": "dotted", ".": "dotted"}
        return linestyles[linestyle]
    except KeyError:
        return linestyle


def convert_color(color):
    try:
        colors = {"b": (0, 0, 255), "r": (255, 0, 0), "g": (0, 255, 0), "y": (255, 255, 0), "c": (0, 255, 255), "k": (0, 0, 0), "w": (255, 255, 255)}
        return colors[color]
    except KeyError:
        return color


def convert_marker(marker):
    try:
        markers = {"o": "*", "t1": "triangle", "t2": "triangle", "t3": "triangle", "t": "triangle", "s": "square", "d": "diamond", "p": "pentagon"}
        return markers[marker]
    except KeyError:
        return marker


def do_preamble():
    with open(os.path.join(templates_tikz, "preamble.txt"), "r") as f:
        return f.read()


def do_axis_options():
    """Do axis options"""

    with open(os.path.join(templates_tikz, "axis_options.txt"), "r") as f:
        return f.read()


def do_specific_axis_options(theGraph: Graph):
    """Get graph-specific axis options"""

    theStr = ''
    for key in theGraph.get_all_traces():
        xlabel = theGraph.get_trace(key).get_x_label()
        if xlabel:
            theStr += "xlabel={{ {} }},\n".format(xlabel)
            break
    for key in theGraph.get_all_traces():
        ylabel = theGraph.get_trace(key).get_y_label()
        if ylabel:
            theStr += "ylabel={{ {} }},\n".format(ylabel)
            break
    return theStr


def do_trace_options(theTrace: Data):
    """Get latex trace options from Data"""
    # width_line = theTrace.get_width()
    linestyle = convert_linestyle(theTrace.get_linestyle())
    color = theTrace.get_color()
    is_filled = theTrace.symbol_isfilled()
    markerstyle = convert_marker(theTrace.get_symbol())
    # markersize = theTrace.get_symbolsize()
    is_scattered = theTrace.is_scattered()
    outline = theTrace.get_symbolOutline()

    theStr = ''
    if color is not None:
        theStr += "color={{rgb, 255:red,{};green,{};blue,{}}},\n".format(*convert_color(color))
    theStr += "line width={}pt,\n".format(1)
    if is_scattered:
        theStr += "only marks,\n"
    else:
        theStr += "{},\n".format(linestyle)
    mark_options = ''
    mark_options += 'solid,\n'
    mark_options += '%fill=blue,\n'
    if color is not None:
        c = colorsys.rgb_to_hls(*[i/255 for i in convert_color(color)])
        color_rgb = colorsys.hls_to_rgb(c[0], max(0, min(1, c[1]/theTrace.get_symbolOutline())), c[2])
        mark_options += "draw={{rgb, 255:red,{};green,{};blue,{}}},\n".format(*[int(i*255) for i in color_rgb])
    if not is_filled:
        mark_options += "fill opacity=0,\n"
    mark_options += 'line width=0.1pt,\n'
    mark_options += 'mark size=1pt,\n'
    mark_options += 'mark={},\n'.format(markerstyle)

    theStr += "mark options={{\n{}}},\n".format(indentParagraph(mark_options, 1))
    return theStr


def export_to_tikz(theGraphs: Graphs, additionalPreamble=lambda: '', additionalAxisOptions=lambda graphId: '', additionalTraceOptions=lambda graphId, traceId: ''):
    theStr = ''
    theStr += do_preamble() + additionalPreamble()
    theStr += "\\begin{document}\n"

    for graphId in theGraphs.get_all_graphs_ids():
        theGraph = theGraphs.get_graph(graphId)
        theStr += indentParagraph("\\begin{tikzpicture}\n", 1)
        theStr += indentParagraph("\\begin{{axis}}[\n{}\n".format(indentParagraph(do_axis_options() + do_specific_axis_options(theGraph) + additionalAxisOptions(graphId) + "]", indent_level=2)), 3)

        for traceId in theGraph.get_all_traces():
            theTrace = theGraph.get_trace(traceId)
            theStr += indentParagraph("\\addplot[\n{}]{{x^2 - 2*x - 1}};\n".format(indentParagraph(do_trace_options(theTrace) + additionalTraceOptions(graphId, traceId), indent_level=2)), 3)
            if theTrace.get_legend():
                theStr += indentParagraph("\\addlegendentry{{{}}}".format(theTrace.get_legend()), 3)
        theStr += indentParagraph("\\end{axis}\n", 2)
        theStr += indentParagraph("\\end{tikzpicture}\n", 1)

    theStr += "\\end{document}\n"
    return theStr


def export_to_tikz_groupGraphs(theGraphs: Graphs, foldername, additionalPreamble=lambda: '', additionalAxisOptions=lambda graphId: '', additionalTraceOptions=lambda graphId, traceId: ''):
    """
    Export the graphs as group

    :param theGraphs: Graphs to save
    :param foldername: Foldername to save
    :param additionalPreamble: method that returns string for custom tikz options
    :param additionalAxisOptions: method that returns string for custom tikz options
    :param additionalTraceOptions: method that returns string for custom tikz options
    :return:
    """
    if not foldername:
        return
    os.makedirs(foldername, exist_ok=True)
    source_folder = os.path.join(foldername, "source")
    os.makedirs(source_folder, exist_ok=True)

    # Data file creation
    for graphId in theGraphs.get_all_graphs_ids():
        theGraph = theGraphs.get_graph(graphId)
        for traceId in theGraph.get_all_traces():
            filename = os.path.join(source_folder, "g{}t{}.dat".format(graphId, traceId))
            theTrace = theGraph.get_trace(traceId)
            x, y = theTrace.get_plot_data()
            np.savetxt(filename, np.array([[x[i], y[i]] for i in range(len(x))]), header='x\ty')
            # add_body += "\\pgfplotstableread{{source/g{}t{}.dat}}{{\\g{}t{}}}\n".format(graphId, traceId, graphId, traceId)

    # Main file creation
    theStr = ''
    theStr += do_preamble() + additionalPreamble()
    theStr += "\\begin{document}\n"  # + add_body
    theStr += indentParagraph("\\begin{tikzpicture}\n", 1)
    groupStyle = "group style={{group size=1 by {},}},\n".format(len(theGraphs.get_all_graphs_ids()))
    theStr += indentParagraph("\\begin{{groupplot}}[\n{}\n".format(indentParagraph(groupStyle +
                                                                                   do_axis_options() + "]", indent_level=2)), 3)

    for graphId in theGraphs.get_all_graphs_ids():
        theGraph = theGraphs.get_graph(graphId)
        theStr += indentParagraph("\\nextgroupplot[{}]".format(indentParagraph(do_specific_axis_options(theGraph) + additionalAxisOptions(graphId), 2)), 3)
        for traceId in theGraph.get_all_traces():
            theTrace = theGraph.get_trace(traceId)
            filename = "source/g{}t{}.dat".format(graphId, traceId)
            theStr += indentParagraph("\\addplot[\n{}] file {{{}}};\n".format(indentParagraph(do_trace_options(theTrace) + additionalTraceOptions(graphId, traceId), indent_level=1), filename), 4)
            if theTrace.get_legend():
                theStr += indentParagraph("\\addlegendentry{{{}}}".format(theTrace.get_legend()), 4)
    theStr += indentParagraph("\\end{groupplot}\n", 2)
    theStr += indentParagraph("\\end{tikzpicture}\n", 1)
    theStr += "\\end{document}\n"
    with open(os.path.join(foldername, "main.tex"), "w") as f:
        f.write(theStr)
