
from . import _qdk_loader
from ._qdk_loader import *
for name in [n for n in _qdk_loader.__dict__ if n.startswith('_') and not n.startswith('__')]:
  globals()[name] = getattr(_qdk_loader, name)
globals()['__builtin__'] = getattr(_qdk_loader, '__builtin__')

del _qdk_loader
del name

def _swig_repr(self):
  try:
    strthis = "proxy of " + self.this.__repr__()
  except __builtin__.Exception:
    strthis = ""
  return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


class AlgorithmAgent(_object):
    """

    The instances derived from this are in charge of running an optimization problem.

    Attributes:
        timeout (int): The timeout in milliseconds.
        has_timeout (bool): True if a timeout is set, False otherwise.
        timing (int): The time taken to execute the run function.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, AlgorithmAgent, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, AlgorithmAgent, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_AlgorithmAgent
    __del__ = lambda self: None

    def run(self):
        """

        Runs the algorithm.

        This function has the following signature: ::

            run(self)


        """
        return _qdk.AlgorithmAgent_run(self)


    def request_cancellation(self):
        """

        This can be called to request canceling the execution of the algorithm.
        This will set the ``cancel_requested`` flag to True.

        This function has the following signature: ::

            request_cancellation(self)


        """
        return _qdk.AlgorithmAgent_request_cancellation(self)

    __swig_setmethods__["timeout"] = _qdk.AlgorithmAgent_timeout_set
    __swig_getmethods__["timeout"] = _qdk.AlgorithmAgent_timeout_get
    if _newclass:
        timeout = _swig_property(_qdk.AlgorithmAgent_timeout_get, _qdk.AlgorithmAgent_timeout_set)
    __swig_getmethods__["has_timeout"] = _qdk.AlgorithmAgent_has_timeout_get
    if _newclass:
        has_timeout = _swig_property(_qdk.AlgorithmAgent_has_timeout_get)
    __swig_getmethods__["timing"] = _qdk.AlgorithmAgent_timing_get
    if _newclass:
        timing = _swig_property(_qdk.AlgorithmAgent_timing_get)
AlgorithmAgent_swigregister = _qdk.AlgorithmAgent_swigregister
AlgorithmAgent_swigregister(AlgorithmAgent)

class InputBundle(_object):
    """

    Parent class to all inputs used by the ``AlgorithmAgent``.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, InputBundle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, InputBundle, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_InputBundle
    __del__ = lambda self: None
InputBundle_swigregister = _qdk.InputBundle_swigregister
InputBundle_swigregister(InputBundle)

class OutputBundle(_object):
    """

    Parent class to all outputs made by the ``AlgorithmAgent``.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, OutputBundle, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, OutputBundle, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_OutputBundle
    __del__ = lambda self: None
OutputBundle_swigregister = _qdk.OutputBundle_swigregister
OutputBundle_swigregister(OutputBundle)

class IOHandler(_object):
    """

    This is in charge of handling input and output for an ``AlgorithmAgent``.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, IOHandler, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, IOHandler, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_IOHandler
    __del__ = lambda self: None

    def clear_io(self):
        return _qdk.IOHandler_clear_io(self)

    def clear_output(self):
        return _qdk.IOHandler_clear_output(self)
IOHandler_swigregister = _qdk.IOHandler_swigregister
IOHandler_swigregister(IOHandler)

class UpdateInput(_object):
    """

    Defines an interface for all the command objects that can set up the input for
    an ``IOHandler``.

    This constructor has the following signatures: ::

        UpdateInput()
        UpdateInput(receiver)

    Args:
        receiver (IOHandler): The object that will be updated.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UpdateInput, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UpdateInput, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_UpdateInput
    __del__ = lambda self: None

    def execute(self):
        """

        Execute the command encapuslated by the instance.

        This function  has the following signature: ::

            execute()


        """
        return _qdk.UpdateInput_execute(self)

UpdateInput_swigregister = _qdk.UpdateInput_swigregister
UpdateInput_swigregister(UpdateInput)

class PolynomialFormulation(_object):
    """

    Base class for algorithms that reduce their instances into a polynomial
    optimization.

    Attributes:
        solver (QUSolver): The solver made to solve the QUBO of this instance.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PolynomialFormulation, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PolynomialFormulation, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_PolynomialFormulation
    __del__ = lambda self: None

    def _solver(self):
        return _qdk.PolynomialFormulation__solver(self)

    def _set_solver(self, solver):
        return _qdk.PolynomialFormulation__set_solver(self, solver)

    def get_qubo(self):
        return _qdk.PolynomialFormulation_get_qubo(self)

    __swig_getmethods__["solver"] = _qdk.PolynomialFormulation__solver
    __swig_setmethods__["solver"] = (
        _qdk.PolynomialFormulation__set_solver)
    if _newclass: solver = _swig_property(
        _qdk.PolynomialFormulation__solver,
        _qdk.PolynomialFormulation__set_solver)


    def get_polynomial(self):
        """

        Builds a BinaryPolynomial from the problem's QuadraticBinaryPolynomial. This
        BinaryPolynomial changes if the problem changes and cannot be used to modify the
        problem.

        This function has the following signature: ::

            get_polynomial(self)

        Returns:
            BinaryPolynomial: The HOBO formulation.

        """
        return _qdk.PolynomialFormulation_get_polynomial(self)

PolynomialFormulation_swigregister = _qdk.PolynomialFormulation_swigregister
PolynomialFormulation_swigregister(PolynomialFormulation)

class PolynomialAlgorithmAgent(AlgorithmAgent, PolynomialFormulation):
    """

    This is an abstract class for outlining the behaviour of algorithm agents.

    """

    __swig_setmethods__ = {}
    for _s in [AlgorithmAgent, PolynomialFormulation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PolynomialAlgorithmAgent, name, value)
    __swig_getmethods__ = {}
    for _s in [AlgorithmAgent, PolynomialFormulation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PolynomialAlgorithmAgent, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_PolynomialAlgorithmAgent
    __del__ = lambda self: None
PolynomialAlgorithmAgent_swigregister = _qdk.PolynomialAlgorithmAgent_swigregister
PolynomialAlgorithmAgent_swigregister(PolynomialAlgorithmAgent)

class CliqueOutput(_object):
    """

    This class wraps the output from the clique finding algorithm. It contains
    the number of nodes, a copy of the subgraph, and the vertex descriptors
    of the selected nodes in the input graph.

    This constructor has the following signature: ::

        CliqueOutput(self)

    Attributes:
        graph (networkx.Graph): The subgraph generated by the optimization.
        value (float): The value of the objective function with the chosen nodes.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CliqueOutput, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CliqueOutput, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _qdk.new_CliqueOutput()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def _get_graph(self):
        return _qdk.CliqueOutput__get_graph(self)

    __swig_getmethods__["graph"] = _qdk.CliqueOutput__get_graph
    if _newclass: graph = _swig_property(_qdk.CliqueOutput__get_graph)

    __swig_setmethods__["value"] = _qdk.CliqueOutput_value_set
    __swig_getmethods__["value"] = _qdk.CliqueOutput_value_get
    if _newclass:
        value = _swig_property(_qdk.CliqueOutput_value_get, _qdk.CliqueOutput_value_set)
    __swig_destroy__ = _qdk.delete_CliqueOutput
    __del__ = lambda self: None
CliqueOutput_swigregister = _qdk.CliqueOutput_swigregister
CliqueOutput_swigregister(CliqueOutput)

class CliqueOutputBundle(OutputBundle):
    """

    This class uses a vector of networkx.Graph instances to hold the graphs from
    each solution returned by the solver.

    This constructor has the following signature: ::

        CliqueOutputBundle(self)

    Attributes:
        solutions (list): The list of solutions returned by the solver as a
         collection of ``CliqueOutput``.

    """

    __swig_setmethods__ = {}
    for _s in [OutputBundle]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CliqueOutputBundle, name, value)
    __swig_getmethods__ = {}
    for _s in [OutputBundle]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CliqueOutputBundle, name)

    def __init__(self):
        """

        This class uses a vector of networkx.Graph instances to hold the graphs from
        each solution returned by the solver.

        This constructor has the following signature: ::

            CliqueOutputBundle(self)

        Attributes:
            solutions (list): The list of solutions returned by the solver as a
             collection of ``CliqueOutput``.

        """
        this = _qdk.new_CliqueOutputBundle()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def _get_solutions(self):
        val = _qdk.CliqueOutputBundle__get_solutions(self)

        return list(val)


        return val


    def __repr__(self):
        return _qdk.CliqueOutputBundle___repr__(self)

    __swig_getmethods__["solutions"] = _get_solutions
    if _newclass: solutions = _swig_property(_get_solutions)

    __swig_destroy__ = _qdk.delete_CliqueOutputBundle
    __del__ = lambda self: None
CliqueOutputBundle_swigregister = _qdk.CliqueOutputBundle_swigregister
CliqueOutputBundle_swigregister(CliqueOutputBundle)

class GraphBundle(InputBundle, OutputBundle):
    """

    This class contains the edge properties and the structure of the graph which
    AlgorithmAgent instances work on.

    Attributes:
        graph (networkx.Graph): The graph in the bundle.

    """

    __swig_setmethods__ = {}
    for _s in [InputBundle, OutputBundle]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphBundle, name, value)
    __swig_getmethods__ = {}
    for _s in [InputBundle, OutputBundle]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GraphBundle, name)
    __swig_destroy__ = _qdk.delete_GraphBundle
    __del__ = lambda self: None

    def __repr__(self):
        return _qdk.GraphBundle___repr__(self)

    def _get_graph(self):
        return _qdk.GraphBundle__get_graph(self)

    def _get_node_prop_map(self):
        return _qdk.GraphBundle__get_node_prop_map(self)

    def _get_edge_prop_map(self):
        return _qdk.GraphBundle__get_edge_prop_map(self)

    import networkx as nx
    global nx

    def _get_graph(self):
        graph =  _qdk.GraphBundle__get_graph(self)
        node_prop = _qdk.GraphBundle__get_node_prop_map(self)
        edge_prop = _qdk.GraphBundle__get_edge_prop_map(self)

        for k, v in node_prop.items():
            nx.set_node_attributes(graph, values = v, name = k)

        for k, v in edge_prop.items():
            nx.set_edge_attributes(graph, values = v, name = k)

        return graph

    __swig_getmethods__["graph"] = _get_graph
    if _newclass: graph = _swig_property(_get_graph)


    def __init__(self):
        """

        This class contains the edge properties and the structure of the graph which
        AlgorithmAgent instances work on.

        Attributes:
            graph (networkx.Graph): The graph in the bundle.

        """
        this = _qdk.new_GraphBundle()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
GraphBundle_swigregister = _qdk.GraphBundle_swigregister
GraphBundle_swigregister(GraphBundle)

class GraphIOHandler(IOHandler):
    """

    Adds the ability to receive graphs as an input.

    This constructor has the following signature: ::

        GraphIOHandler(self)


    """

    __swig_setmethods__ = {}
    for _s in [IOHandler]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphIOHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [IOHandler]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GraphIOHandler, name)
    __repr__ = _swig_repr

    def __init__(self):
        """

        Adds the ability to receive graphs as an input.

        This constructor has the following signature: ::

            GraphIOHandler(self)


        """
        this = _qdk.new_GraphIOHandler()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_GraphIOHandler
    __del__ = lambda self: None

    def peek_input(self):
        """

        Gets the current state of the input.

        This function has the following signature: ::

            peek_input(self)

        Returns:
            GraphBundle: An ``OutputBundle`` containing the current state of the graph
             generated from user input.

        """
        return _qdk.GraphIOHandler_peek_input(self)


    def clear_io(self):
        """

        This clears the input currently set up using the commands received
        and also the output produced so far.

        This function has the following signature: ::

            clear_io(self)


        """
        return _qdk.GraphIOHandler_clear_io(self)


    def add_node(self, node_index):
        """

        This adds a node to the graph.

        This funtion has the following signature: ::

            add_node(self, node_index)

        Args:
            node_index (int): The index of the node to be added.

        """
        return _qdk.GraphIOHandler_add_node(self, node_index)


    def add_edge(self, source_index, dest_index):
        """

        This adds an edge to the graph.

        This function has the following signature: ::

            add_edge(self, source_index, dest_index)

        Args:
            source_index (int): The source index of the edge to be added.
            dest_index (int): The destination index of the edge to be added.

        """
        return _qdk.GraphIOHandler_add_edge(self, source_index, dest_index)


    def remove_node(self, node_index):
        """

        This removes a node from the handler.

        This function has the following signature: ::

            remove_node(self, node_index)

        Args:
            node_index (int): The index of the node to be removed.

        """
        return _qdk.GraphIOHandler_remove_node(self, node_index)


    def remove_edge(self, src_index, dest_index):
        """

        This removes an edge from the handler.

        This function has the following signature: ::

            remove_edge(self, src_index, dest_index)

        Args:
            src_index (int): The index of the source of the edge to be removed.
            dest_index (int): The index of the destination node of the edge to be
             removed.

        """
        return _qdk.GraphIOHandler_remove_edge(self, src_index, dest_index)


    def set_node_property(self, index, key, value):
        """

        This sets a node property.

        This function has the following signature: ::

            set_node_property(self, index, key, value)

        Args:
            index (int): Index of the node to be updated.
            key (str): Name of the parameter to be added/updated.
            value (str): The value of the parameter.

        """
        return _qdk.GraphIOHandler_set_node_property(self, index, key, value)


    def set_edge_property(self, src_index, dest_index, key, value):
        """

        This sets an edge property.

        This function has the following signature: ::

            set_edge_property(self, src_index, dest_index, key, value)

        Args:
            src_index (int): The source index of the edge to be updated.
            dest_index (int): The destination index of the edge to be updated.
            key (str): Name of the parameter to be added/updated.
            value (str) The value of the parameter.

        """
        return _qdk.GraphIOHandler_set_edge_property(self, src_index, dest_index, key, value)


    def get_node_property(self, index, key):
        """

        This gets a node property.

        This funtion has the following signature: ::

            get_node_property(self, node_index, key)

        Args:
            node_index (int): The index of the node.
            key (str): Name of the property.

        Returns:
            string: The value of the property.

        """
        return _qdk.GraphIOHandler_get_node_property(self, index, key)


    def get_edge_property(self, src_index, dest_index, key):
        """

        This gets an edge property.

        This function has the following signature: ::

            get_edge_property(self, src_index, dest_index, key)

        Args:
            src_index (int): The source index.
            dest_index (int): The destination index.
            key (str): The name of the property.

        Returns:
            string: The value of the property.

        """
        return _qdk.GraphIOHandler_get_edge_property(self, src_index, dest_index, key)


    def clear_output(self):
        """

        Clears the output associated with the handler.

        The function has the following signature: ::
            clear_output()


        """
        return _qdk.GraphIOHandler_clear_output(self)


    def parse_graph(self, graph):
        """

        This parses the networkx.Graph through the GraphIOHandler.

        This function has the following signature: ::

            parse_graph(self, graph)

        Args:
            graph (networkx.Graph): The graph to be parsed.

        """
        return _qdk.GraphIOHandler_parse_graph(self, graph)

GraphIOHandler_swigregister = _qdk.GraphIOHandler_swigregister
GraphIOHandler_swigregister(GraphIOHandler)

class GraphListBundle(InputBundle):
    """

    A collection of graphs handled by a GraphListIOHandler.

    The constructor has the following signature: ::

        GraphListBundle()

    Attributes:
        graphs (dict): The dictionary of networkx.Graphs in the bundle. Each graph
            in the dictionary is mapped by its graph index.

    """

    __swig_setmethods__ = {}
    for _s in [InputBundle]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphListBundle, name, value)
    __swig_getmethods__ = {}
    for _s in [InputBundle]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GraphListBundle, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _qdk.new_GraphListBundle()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_GraphListBundle
    __del__ = lambda self: None

    def _get_graphs(self):
        return _qdk.GraphListBundle__get_graphs(self)

    def _get_node_prop_maps(self):
        return _qdk.GraphListBundle__get_node_prop_maps(self)

    def _get_edge_prop_maps(self):
        return _qdk.GraphListBundle__get_edge_prop_maps(self)

    import networkx as nx
    global nx

    def _get_graphs(self):
        ret = {}
        graphs = _qdk.GraphListBundle__get_graphs(self)
        node_props = _qdk.GraphListBundle__get_node_prop_maps(self)
        edge_props = _qdk.GraphListBundle__get_edge_prop_maps(self)

        for idx, graph in graphs.items():
            g = nx.from_dict_of_lists(graph)

            if node_props:
                for k, v in node_props[idx].items():
                    nx.set_node_attributes(g, values = v, name = k)
            if edge_props:
                for k, v in edge_props[idx].items():
                    nx.set_edge_attributes(g, values = v, name = k)

            ret[idx] = g
        return ret

    __swig_getmethods__["graphs"] = _get_graphs
    if _newclass: graphs = _swig_property(_get_graphs)

GraphListBundle_swigregister = _qdk.GraphListBundle_swigregister
GraphListBundle_swigregister(GraphListBundle)

class GraphListIOHandler(IOHandler):
    """

    This class is similar to GraphIOHandler but is able to handle
    map of graph indices to networkx.Graph objects.

    This constructor has the following signature: ::

        GraphListIOHandler(self)


    """

    __swig_setmethods__ = {}
    for _s in [IOHandler]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphListIOHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [IOHandler]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GraphListIOHandler, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _qdk.new_GraphListIOHandler()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def peek_input(self):
        """

        Gets the input of the agent.

        This function has the following signature: ::

            peek_input(self)


        """
        return _qdk.GraphListIOHandler_peek_input(self)


    def clear_io(self):
        """

        Clears the input and output bundles.

        This function has the following signature: ::

            clear_io(self)


        """
        return _qdk.GraphListIOHandler_clear_io(self)


    def clear_output(self):
        """

        Clears output, agents need to implement this based on what their output bundles are.

        This function has the following signature: ::

            clear_output(self)


        """
        return _qdk.GraphListIOHandler_clear_output(self)


    def add_graph(self, graph_index):
        """

        Adds an empty graph with the given index. Does nothing if the graph already
        exists.

        This function has the following signature: ::

            add_graph(self, graph_index)

        Args:
            graph_index (int): The index of the graph to create.

        """
        return _qdk.GraphListIOHandler_add_graph(self, graph_index)


    def add_node(self, node_index, graph_index):
        """

        Adds a node with the given index to the specified graph. Creates a new graph
        if the one with the given index does not exist. Does nothing if the node already
        exists. Adds the graph if it does not.

        This function has the following signature: ::

            add_node(self, node_index, graph_index)

        Args:
            node_index (int): The node index to add.
            graph_index (int): The index of the graph to add the node to.

        """
        return _qdk.GraphListIOHandler_add_node(self, node_index, graph_index)


    def add_edge(self, source_index, end_index, graph_index):
        """

        Adds an edge from the source to the target node in the specified graph. Adds
        either nodes if they don't exist. Adds the graph if it doesn't exist. Does
        nothing if the edge already exists.

        This function has the following signature: ::

            add_edge(self, src_index, dest_index, graph_index)

        Args:
            src_index (int): The source node index to add the edge.
            dest_index (int): The destination node index to add the edge.
            graph_index (int): The graph to which to add the edge.

        """
        return _qdk.GraphListIOHandler_add_edge(self, source_index, end_index, graph_index)


    def remove_node(self, index, graph_index):
        """

        Removes a node from the specified graph and removes any edges that connect
        that node. If the node does not exist it does nothing.

        This function has the following signature: ::

            remove_node(self, node_index, grpah_index)

        Args:
            node_index (int): The index of the node to remove.
            graph_index (int): The index of the graph to remove the node.

        """
        return _qdk.GraphListIOHandler_remove_node(self, index, graph_index)


    def remove_edge(self, source_index, end_index, GraphIndex):
        """

        This removes an edge from the specified graph. Does nothing if the node does not
        exist.

        This function has the following signature: ::

            remove_edge(self, src_index, dest_index, graph_index)

        Args:
            src_index (int): The source node index of the edge to remove.
            dest_index (int): The destination node index of the edge to remove.
            graph_index (int): The index of the graph from which to remove the edge.

        """
        return _qdk.GraphListIOHandler_remove_edge(self, source_index, end_index, GraphIndex)


    def remove_graph(self, graph_index):
        """

        Removes the graph with the selected index. Does nothing if the graph does not
        exist.

        This function has the following signature: ::

            remove_graph(self, graph_index)

        Args:
            graph_index (int): The index of the graph to remove.

        """
        return _qdk.GraphListIOHandler_remove_graph(self, graph_index)


    def set_node_property(self, index, graph_index, key, value):
        """

        This sets a node property.

        This function has the following signature: ::

            set_node_property(self, node_index, graph_index, key, value)

        Args:
            node_index (int): Index of the node to be updated.
            graph_index (int): The index of the graph to set the node property for.
            key (str): The name of the node property to be set.
            value (str): The value of the property.

        """
        return _qdk.GraphListIOHandler_set_node_property(self, index, graph_index, key, value)


    def set_edge_property(self, src_index, dest_index, graph_index, key, value):
        """

        This sets an edge property.

        This function has the following signature: ::

            set_edge_property(self, src_index, dest_index, graph_index, key, value)

        Args:
            src_index (int): The source index of the edge to be updated.
            dest_index (int): The destination index of the edge to be updated.
            graph_index (int): The index of the graph to set the edge property for.
            key (str): The name of the edge property to be set.
            value (str): The value of the property.

        """
        return _qdk.GraphListIOHandler_set_edge_property(self, src_index, dest_index, graph_index, key, value)


    def get_node_property(self, index, graph_index, key):
        """

        This gets a node property.

        This function has the following signature: ::

            get_node_property(index, graph_index, key)

        Args:
            index (int): Index of the node.
            graph_index (int): The index of the graph to operate on.
            key (str): Name of the property.

        Returns:
            str: The value of the property.

        """
        return _qdk.GraphListIOHandler_get_node_property(self, index, graph_index, key)


    def get_node_property_keys(self, index, graph_index):
        return _qdk.GraphListIOHandler_get_node_property_keys(self, index, graph_index)

    def get_edge_property(self, src_index, dest_index, graph_index, key):
        """

        This gets an edge property.

        This function has the following signature: ::

         get_edge_property(src_index, dest_index, graph_index, key)

        Args:
            src_index (int): The source index of the edge.
            dest_index (int): The destination index of the edge.
            graph_index (int): The index of the graph to operate on.
            key (str): The name of the property.

        Returns:
            str: The value of the edge property.

        """
        return _qdk.GraphListIOHandler_get_edge_property(self, src_index, dest_index, graph_index, key)


    def get_edge_property_keys(self, src_index, dest_index, graph_index):
        return _qdk.GraphListIOHandler_get_edge_property_keys(self, src_index, dest_index, graph_index)

    def is_edge(self, src_index_i, tar_index_i, graph_i):
        """

        This checks whether or not the requested edge exists.

        This function has the following signature: ::

            is_edge(self, src_index, dest_index, graph_index)

        Args:
            src_index (int): Index of the source node holding the edge.
            dest_index (int): Index of the target node holding the edge.
            graph_index (int): The index of the graph to check.

        Returns:
            bool: True if the requested edge exists and False otherwise.

        """
        return _qdk.GraphListIOHandler_is_edge(self, src_index_i, tar_index_i, graph_i)


    def parse_graph(self, graph_index, graph):
        """

        This parses the networkx.Graphs through the GraphListIOHandler.

        This function has the following signature: ::

            parse_graph(self, index, graph)

        Args:
          index (int): The graph index.
          graph (networkx.Graph): The networkx.Graph to be parsed.

        """
        return _qdk.GraphListIOHandler_parse_graph(self, graph_index, graph)

    __swig_destroy__ = _qdk.delete_GraphListIOHandler
    __del__ = lambda self: None
GraphListIOHandler_swigregister = _qdk.GraphListIOHandler_swigregister
GraphListIOHandler_swigregister(GraphListIOHandler)

class MatchingCriteria(_object):
    """

    Defines how two nodes or edges of the two input graphs are going
    to be matched to create the conflict graph. This class is
    used by the GraphSimilarityAgent to generate the conflict graph.

    This constructor has the following signature: ::

        MatchingCriteria(agent)

    Args:
        agent (GraphListIOHandler): The agent that contains the graphs. This is
            used to retrieve properties of the nodes and edges in the matching
            evaluation.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatchingCriteria, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MatchingCriteria, name)
    __repr__ = _swig_repr

    def __init__(self, handler):
        this = _qdk.new_MatchingCriteria(handler)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_MatchingCriteria
    __del__ = lambda self: None

    def add_conflict_node(self, index_i, index_j):
        return _qdk.MatchingCriteria_add_conflict_node(self, index_i, index_j)

    def add_conflict_edge(self, index_i0, index_i1, index_j0, index_j1):
        """

        Function for matching conflict edges. This could be overriden by
        users to customize the matching. In the default implementation here,
        it returns true iff exactly one of the pairs (i0, i1), or (j0, j1)
        has an edge.

        This function has the following signature: ::

            add_conflict_edge(index_i0, index_i1, index_j0, index_j1)

        Args:
            index_i0 (int): The first index from the first graph.
            index_i1 (int): The second index of the first graph.
            index_j0 (int): The first index of the second graph.
            index_j1 (int): The second index of the second graph.

        Returns:
            bool: True if a conflict edge should be added.

        """
        return _qdk.MatchingCriteria_add_conflict_edge(self, index_i0, index_i1, index_j0, index_j1)


    def _agent(self):
        return _qdk.MatchingCriteria__agent(self)

    __swig_getmethods__["_agent"] = _qdk.MatchingCriteria__agent
    if _newclass: _agent = _swig_property(_qdk.MatchingCriteria__agent)

MatchingCriteria_swigregister = _qdk.MatchingCriteria_swigregister
MatchingCriteria_swigregister(MatchingCriteria)

class GraphSimilarityOutput(_object):
    """

    The output produced by a GraphSimilarityAgent.

    Attributes:
        solution (list): A list of tuples of size 2, which contain
            matched nodes (int) from the user's input
            graphs ``[(node_A1, node_B1), (node_A2, node_B2)]``
        similarity (float): Similarity value of the current solution.
        feasible (bool): Feasibility of the current solution.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphSimilarityOutput, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GraphSimilarityOutput, name)
    __repr__ = _swig_repr

    def _get_solution(self):
        val = _qdk.GraphSimilarityOutput__get_solution(self)

        return list(val)


        return val


    def _get_similarity(self):
        return _qdk.GraphSimilarityOutput__get_similarity(self)

    def _get_feasibility(self):
        return _qdk.GraphSimilarityOutput__get_feasibility(self)

    __swig_getmethods__["solution"] = _get_solution
    if _newclass: solution = _swig_property(_get_solution)
    __swig_getmethods__["similarity"] = _get_similarity
    if _newclass: similarity = _swig_property(_get_similarity)
    __swig_getmethods__["feasible"] = _get_feasibility
    if _newclass: feasible = _swig_property(_get_feasibility)


    def __init__(self):
        """

        The output produced by a GraphSimilarityAgent.

        Attributes:
            solution (list): A list of tuples of size 2, which contain
                matched nodes (int) from the user's input
                graphs ``[(node_A1, node_B1), (node_A2, node_B2)]``
            similarity (float): Similarity value of the current solution.
            feasible (bool): Feasibility of the current solution.

        """
        this = _qdk.new_GraphSimilarityOutput()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_GraphSimilarityOutput
    __del__ = lambda self: None
GraphSimilarityOutput_swigregister = _qdk.GraphSimilarityOutput_swigregister
GraphSimilarityOutput_swigregister(GraphSimilarityOutput)

class GraphSimilarityOutputBundle(OutputBundle):
    """

    A collection of ``GraphSimilarityOutput`` objects.

    Attributes:
        solution_list (list): List of solutions returned by the agent.
            The type of the solution is ``GraphSimilarityOutput``.

    """

    __swig_setmethods__ = {}
    for _s in [OutputBundle]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphSimilarityOutputBundle, name, value)
    __swig_getmethods__ = {}
    for _s in [OutputBundle]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GraphSimilarityOutputBundle, name)

    def _solution_list(self):
        return _qdk.GraphSimilarityOutputBundle__solution_list(self)

    def __repr__(self):
        return _qdk.GraphSimilarityOutputBundle___repr__(self)

    __swig_getmethods__["solution_list"] = _solution_list
    if _newclass: solution_list = _swig_property(_solution_list)


    def __init__(self):
        """

        A collection of ``GraphSimilarityOutput`` objects.

        Attributes:
            solution_list (list): List of solutions returned by the agent.
                The type of the solution is ``GraphSimilarityOutput``.

        """
        this = _qdk.new_GraphSimilarityOutputBundle()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_GraphSimilarityOutputBundle
    __del__ = lambda self: None
GraphSimilarityOutputBundle_swigregister = _qdk.GraphSimilarityOutputBundle_swigregister
GraphSimilarityOutputBundle_swigregister(GraphSimilarityOutputBundle)

class GraphSimilarityAgent(GraphListIOHandler, AlgorithmAgent):
    """

    This agent is in charge of finding the similarity and common
    subgraphs of two labeled graphs. Note that The quasi number
    of the default CoKPlex is 0.

    Attributes:
        delta (float): delta is a parameter for calculating the graph similarity.
            Similarity is calculated as: delta * beta + (1 - delta) * alpha.
            alpha and beta are the number of nodes the two input graphs contribute
            to the final QMIS divided by the number of nodes in each graph.
            The valid range of delta is [0, 1].
        qmis_finder (CoKPlexAgent): The CoKPlexAgent used to find the CoKPlex
            of the conflict graph of the two input graphs.
        matching_criteria (MatchingCriteria): The matching criteria object that
            defines how two nodes or edges of the two input graphs are going
            to be matched to create the conflict graph.

    This constructor has the following signatures: ::

        GraphSimilarityAgent(self)
        GraphSimilarityAgent(self, qmis_finder, matching_criteria)

    Args:
        qmis (CoKPlexAgent): qmis_finder The CoKPlexAgent used to find the CoKPlex
            of the conflict graph of the two input graphs.
        matching_criteria (MatchingCriteria): The matching criteria object that
            defines how two nodes or edges of the two input graphs are going
            to be matched to create the conflict graph.

    """

    __swig_setmethods__ = {}
    for _s in [GraphListIOHandler, AlgorithmAgent]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphSimilarityAgent, name, value)
    __swig_getmethods__ = {}
    for _s in [GraphListIOHandler, AlgorithmAgent]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GraphSimilarityAgent, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_GraphSimilarityAgent
    __del__ = lambda self: None

    def __init__(self, *args):
        """

        This agent is in charge of finding the similarity and common
        subgraphs of two labeled graphs. Note that The quasi number
        of the default CoKPlex is 0.

        Attributes:
            delta (float): delta is a parameter for calculating the graph similarity.
                Similarity is calculated as: delta * beta + (1 - delta) * alpha.
                alpha and beta are the number of nodes the two input graphs contribute
                to the final QMIS divided by the number of nodes in each graph.
                The valid range of delta is [0, 1].
            qmis_finder (CoKPlexAgent): The CoKPlexAgent used to find the CoKPlex
                of the conflict graph of the two input graphs.
            matching_criteria (MatchingCriteria): The matching criteria object that
                defines how two nodes or edges of the two input graphs are going
                to be matched to create the conflict graph.

        This constructor has the following signatures: ::

            GraphSimilarityAgent(self)
            GraphSimilarityAgent(self, qmis_finder, matching_criteria)

        Args:
            qmis (CoKPlexAgent): qmis_finder The CoKPlexAgent used to find the CoKPlex
                of the conflict graph of the two input graphs.
            matching_criteria (MatchingCriteria): The matching criteria object that
                defines how two nodes or edges of the two input graphs are going
                to be matched to create the conflict graph.

        """
        this = _qdk.new_GraphSimilarityAgent(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def _matching_criteria(self):
        return _qdk.GraphSimilarityAgent__matching_criteria(self)

    def _set_matching_criteria(self, matching_criteria):
        return _qdk.GraphSimilarityAgent__set_matching_criteria(self, matching_criteria)

    def get_all_solutions(self):
        """

        Returns the ``OutputBundle`` of all solutions returned from the solver. Each
        ``GraphSimilarityOutput`` in the ``GraphSimilarityOutputBundle`` represents a
        common substructure of the two graphs. The feasibility of solutions is not
        guaranteed. For feasible solutions call
        :py:meth:`qdk.algorithms.GraphSimilarityAgent.get_feasible_solutions`.

        This funtion has the following signature: ::

            get_all_solutions(self)

        Returns:
          GraphSimilarityOutputBundle: The output bundle which contains a list of
           ``GraphSimilarityOutput`` solutions. All solutions returned from the solver
           are stored in this list.

        """
        return _qdk.GraphSimilarityAgent_get_all_solutions(self)


    def get_feasible_solutions(self):
        """

        Returns the ``OutputBundle`` of all feasible solutions returned from the solver.
        Each ``GraphSimilarityOutput`` in the ``GraphSimilarityOutputBundle`` represents
        a common substructure of the two graphs. A solution is considered feasible if
        the QMIS finder (``CoKPlexAgent``) returns a feasible solution.

        This funtion has the following signature: ::

            get_feasible_solutions(self)

        Returns:
          GraphSimilarityOutputBundle: The output bundle which contains a list of
           ``GraphSimilarityOutput`` solutions. All feasible solutions returned from the
           solver are stored in this list.

        """
        return _qdk.GraphSimilarityAgent_get_feasible_solutions(self)


    def get_qubo(self):
        return _qdk.GraphSimilarityAgent_get_qubo(self)

    def run(self, *args):
        """
        Runs the algorithm.

        This function has the following signatures: ::

            run(self)
            run(self, *args)

        Args:
            *args (networkx.Graph): any number of Graph objects (default 'None')

        Returns:
            GraphSimilarityOutputBundle: The ``OutputBundle`` which contains a
            list of ``GraphSimilarityOutput`` solutions. All feasible solutions
            returned from the solver are stored in this list.
        """
        if args:
            self.clear_io()
            for idx, arg in enumerate(args):
                self.parse_graph(idx, arg)
        super(GraphSimilarityAgent, self).run()
        return self.get_feasible_solutions()

    __swig_getmethods__["matching_criteria"] = _qdk.GraphSimilarityAgent__matching_criteria
    __swig_setmethods__["matching_criteria"] = (
        _qdk.GraphSimilarityAgent__set_matching_criteria)
    if _newclass: matching_criteria = _swig_property(
        _qdk.GraphSimilarityAgent__matching_criteria,
        _qdk.GraphSimilarityAgent__set_matching_criteria)

    __swig_setmethods__["delta"] = _qdk.GraphSimilarityAgent_delta_set
    __swig_getmethods__["delta"] = _qdk.GraphSimilarityAgent_delta_get
    if _newclass:
        delta = _swig_property(_qdk.GraphSimilarityAgent_delta_get, _qdk.GraphSimilarityAgent_delta_set)
    __swig_setmethods__["qmis_finder"] = _qdk.GraphSimilarityAgent_qmis_finder_set
    __swig_getmethods__["qmis_finder"] = _qdk.GraphSimilarityAgent_qmis_finder_get
    if _newclass:
        qmis_finder = _swig_property(_qdk.GraphSimilarityAgent_qmis_finder_get, _qdk.GraphSimilarityAgent_qmis_finder_set)
GraphSimilarityAgent_swigregister = _qdk.GraphSimilarityAgent_swigregister
GraphSimilarityAgent_swigregister(GraphSimilarityAgent)

class CoKPlexAgent(AlgorithmAgent, GraphIOHandler):
    __swig_setmethods__ = {}
    for _s in [AlgorithmAgent, GraphIOHandler]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, CoKPlexAgent, name, value)
    __swig_getmethods__ = {}
    for _s in [AlgorithmAgent, GraphIOHandler]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, CoKPlexAgent, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_CoKPlexAgent
    __del__ = lambda self: None

    def clear_output(self):
        """

        Clears the output associated with the handler.

        The function has the following signature: ::
            clear_output()


        """
        return _qdk.CoKPlexAgent_clear_output(self)


    def get_all_solutions(self):
        return _qdk.CoKPlexAgent_get_all_solutions(self)

    def get_feasible_solutions(self):
        return _qdk.CoKPlexAgent_get_feasible_solutions(self)
    __swig_setmethods__["k_quasi"] = _qdk.CoKPlexAgent_k_quasi_set
    __swig_getmethods__["k_quasi"] = _qdk.CoKPlexAgent_k_quasi_get
    if _newclass:
        k_quasi = _swig_property(_qdk.CoKPlexAgent_k_quasi_get, _qdk.CoKPlexAgent_k_quasi_set)
CoKPlexAgent_swigregister = _qdk.CoKPlexAgent_swigregister
CoKPlexAgent_swigregister(CoKPlexAgent)

class PolyCoKPlexAgent(CoKPlexAgent, PolynomialFormulation):
    """

    The AlgorithmAgent for finding the co-k-plexes in a graph.

    Attributes:
        k_quasi (int): The maximum number of edges that each node can have in the
                       final co-k-plex.
        epsilon (double): Used only when `k_quasi=0`, `use_weighted=True`, and
                          the penalty coefficient is default. The offset added to
                          the minimum of the weights of the two nodes contributing
                          to a penalty term to give the coefficient of the term.

    This constructor has the following signature: ::

        PolyCoKPlexAgent(self, k_quasi)

    Args:
      k_quasi (int): The maximum number of edges that each node in the sub-graph can
                     have.

    """

    __swig_setmethods__ = {}
    for _s in [CoKPlexAgent, PolynomialFormulation]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PolyCoKPlexAgent, name, value)
    __swig_getmethods__ = {}
    for _s in [CoKPlexAgent, PolynomialFormulation]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PolyCoKPlexAgent, name)
    __repr__ = _swig_repr

    def __init__(self, k_quasi, is_weighted=True):
        """

        The AlgorithmAgent for finding the co-k-plexes in a graph.

        Attributes:
            k_quasi (int): The maximum number of edges that each node can have in the
                           final co-k-plex.
            epsilon (double): Used only when `k_quasi=0`, `use_weighted=True`, and
                              the penalty coefficient is default. The offset added to
                              the minimum of the weights of the two nodes contributing
                              to a penalty term to give the coefficient of the term.

        This constructor has the following signature: ::

            PolyCoKPlexAgent(self, k_quasi)

        Args:
          k_quasi (int): The maximum number of edges that each node in the sub-graph can
                         have.

        """
        this = _qdk.new_PolyCoKPlexAgent(k_quasi, is_weighted)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def get_polynomial(self):
        """

        Builds a BinaryPolynomial from the problem's QuadraticBinaryPolynomial. This
        BinaryPolynomial changes if the problem changes and cannot be used to modify the
        problem.

        This function has the following signature: ::

            get_polynomial(self)

        Returns:
            BinaryPolynomial: The HOBO formulation.

        """
        return _qdk.PolyCoKPlexAgent_get_polynomial(self)


    def set_penalty_coefficient(self, new_penalty):
        return _qdk.PolyCoKPlexAgent_set_penalty_coefficient(self, new_penalty)

    def reset_penalty_coefficient(self):
        return _qdk.PolyCoKPlexAgent_reset_penalty_coefficient(self)

    def clear_output(self):
        """

        Resets the output to a new ``CliqueOutputBundle``.

        This function has the following signature: ::

            clear_output(self)

        """
        return _qdk.PolyCoKPlexAgent_clear_output(self)


    def run(self, graph=None):
        """
        Runs the algorithm

        This function has the following signatures: ::

            run(self)
            run(self, graph)

        Args:
            graph (networkx.Graph): Graph object (default 'None')

        Returns:
            CliqueOutputBundle: The ``OutputBundle`` which contains a list of
            ``CliqueOutput`` solutions. All feasible solutions returned from the
            solver are stored in this list.
        """
        if graph:
            self.clear_io()
            self.parse_graph(graph)
        super(PolyCoKPlexAgent, self).run()
        return self.get_feasible_solutions()


    def get_qubo(self, graph=None):
        """
        Returns the QUBO representation of the problem

        This function has the following signatures: ::

            get_qubo(self)
            get_qubo(self, graph)

        Args:
            graph (networkx.Graph): The graph to be solved (default 'None')

        Returns:
            QuadraticBinaryPolynomial: The QUBO minimized to solve the problem
        """
        if graph:
            self.clear_io()
            self.parse_graph(graph)
        return super(PolyCoKPlexAgent, self).get_qubo()


    def get_polynomial(self, graph=None):
        """
        The BinaryPolynomial representation of the problem

        This function has the following signatures: ::

            get_polynomial(self)
            get_polynomial(self, graph)

        Args:
            graph (networkx.Graph): The graph to be solved (default 'None')

        Returns:
            BinaryPolynomial: The HOBO minimized to solve the problem
        """
        if graph:
            self.clear_io()
            self.parse_graph(graph)
        return super(PolyCoKPlexAgent, self).get_polynomial()

    __swig_setmethods__["k_quasi"] = _qdk.PolyCoKPlexAgent_k_quasi_set
    __swig_getmethods__["k_quasi"] = _qdk.PolyCoKPlexAgent_k_quasi_get
    if _newclass:
        k_quasi = _swig_property(_qdk.PolyCoKPlexAgent_k_quasi_get, _qdk.PolyCoKPlexAgent_k_quasi_set)
    __swig_setmethods__["use_weighted"] = _qdk.PolyCoKPlexAgent_use_weighted_set
    __swig_getmethods__["use_weighted"] = _qdk.PolyCoKPlexAgent_use_weighted_get
    if _newclass:
        use_weighted = _swig_property(_qdk.PolyCoKPlexAgent_use_weighted_get, _qdk.PolyCoKPlexAgent_use_weighted_set)
    __swig_setmethods__["epsilon"] = _qdk.PolyCoKPlexAgent_epsilon_set
    __swig_getmethods__["epsilon"] = _qdk.PolyCoKPlexAgent_epsilon_get
    if _newclass:
        epsilon = _swig_property(_qdk.PolyCoKPlexAgent_epsilon_get, _qdk.PolyCoKPlexAgent_epsilon_set)
    __swig_destroy__ = _qdk.delete_PolyCoKPlexAgent
    __del__ = lambda self: None
PolyCoKPlexAgent_swigregister = _qdk.PolyCoKPlexAgent_swigregister
PolyCoKPlexAgent_swigregister(PolyCoKPlexAgent)

class KnapsackInputBundle(InputBundle):
    """

    This class wraps the input for a knapsack problem. Contains the capacity of
    the knapsack, a map from item indices to values, and a map from item indices
    to weights.

    This constructor has the following signatures: ::

        KnapsackInputBundle(self)
        KnapsackInputBundle(self, other)

    Args:
        other (KnapsackInputBundle): Bundle to copy.

    Attributes:
        values (dict): Dictionary mapping item indices (int) to their respective
            values (float).
        weights (dict): Dictionary mapping item indices (int) to their respective
            weights (int).
        capacity (int): The knapsack capacity.

    """

    __swig_setmethods__ = {}
    for _s in [InputBundle]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, KnapsackInputBundle, name, value)
    __swig_getmethods__ = {}
    for _s in [InputBundle]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, KnapsackInputBundle, name)

    def __init__(self):
        this = _qdk.new_KnapsackInputBundle()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_KnapsackInputBundle
    __del__ = lambda self: None

    def _get_values(self):
        val = _qdk.KnapsackInputBundle__get_values(self)

        return val.asdict()


        return val


    def _get_weights(self):
        val = _qdk.KnapsackInputBundle__get_weights(self)

        return val.asdict()


        return val


    __swig_getmethods__["values"] = _get_values
    if _newclass: values = _swig_property(_get_values)
    __swig_getmethods__["weights"] = _get_weights
    if _newclass: weights = _swig_property(_get_weights)


    def __repr__(self):
        return _qdk.KnapsackInputBundle___repr__(self)
    __swig_setmethods__["capacity"] = _qdk.KnapsackInputBundle_capacity_set
    __swig_getmethods__["capacity"] = _qdk.KnapsackInputBundle_capacity_get
    if _newclass:
        capacity = _swig_property(_qdk.KnapsackInputBundle_capacity_get, _qdk.KnapsackInputBundle_capacity_set)
KnapsackInputBundle_swigregister = _qdk.KnapsackInputBundle_swigregister
KnapsackInputBundle_swigregister(KnapsackInputBundle)

class KnapsackOutputBundle(OutputBundle):
    """

    Class that wraps the output of a knapsack problem. Contains a list of
    ``KnapsackOutput`` solutions, one for each solution returned by the solver.

    Attributes:
        solutions (list): List of ``KnapsackOutput`` solutions returned by
        the solver as a collection of ``KnapsackOutput``.

    """

    __swig_setmethods__ = {}
    for _s in [OutputBundle]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, KnapsackOutputBundle, name, value)
    __swig_getmethods__ = {}
    for _s in [OutputBundle]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, KnapsackOutputBundle, name)
    __swig_destroy__ = _qdk.delete_KnapsackOutputBundle
    __del__ = lambda self: None

    def __repr__(self):
        return _qdk.KnapsackOutputBundle___repr__(self)

    def _get_solutions(self):
        return _qdk.KnapsackOutputBundle__get_solutions(self)

    __swig_getmethods__["solutions"] = _get_solutions
    if _newclass: solutions = _swig_property(_get_solutions)


    def __init__(self):
        this = _qdk.new_KnapsackOutputBundle()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
KnapsackOutputBundle_swigregister = _qdk.KnapsackOutputBundle_swigregister
KnapsackOutputBundle_swigregister(KnapsackOutputBundle)

class KnapsackOutput(_object):
    """

    Class that wraps the solution of a knapsack problem. Contains the value of
    the items chosen and a map of item indices to booleans indicating if they
    have been selected.

    This constructor has the following signatures: ::

        KnapsackOutput(self)
        KnapsackOutput(self, feasible, val, weight, config)

    Args:
        feasible (bool): If the solution is feasible or not.
        val (float): The value of the items chosen in the solution.
        weight (int): The weight of the items chosen in the solution.
        config (dict): A dictionary that maps the items in the knapsack (int)
            and a True or False value (bool) representing if the item is selected.

    Attributes:
        feasible (bool): Indicates whether the weight of the chosen items is below
            the capacity of the knapsack.
        value (float): Values of the items that have been selected.
        weight (int): The weight of the items chosen in the solution.
        configuration (dict): The configuration dictionary. Its key is the item in
            the knapsack (int), its value (bool) is True if the item is selected,
            False otherwise.


    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, KnapsackOutput, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, KnapsackOutput, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _qdk.new_KnapsackOutput(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["feasible"] = _qdk.KnapsackOutput_feasible_set
    __swig_getmethods__["feasible"] = _qdk.KnapsackOutput_feasible_get
    if _newclass:
        feasible = _swig_property(_qdk.KnapsackOutput_feasible_get, _qdk.KnapsackOutput_feasible_set)
    __swig_setmethods__["value"] = _qdk.KnapsackOutput_value_set
    __swig_getmethods__["value"] = _qdk.KnapsackOutput_value_get
    if _newclass:
        value = _swig_property(_qdk.KnapsackOutput_value_get, _qdk.KnapsackOutput_value_set)
    __swig_setmethods__["weight"] = _qdk.KnapsackOutput_weight_set
    __swig_getmethods__["weight"] = _qdk.KnapsackOutput_weight_get
    if _newclass:
        weight = _swig_property(_qdk.KnapsackOutput_weight_get, _qdk.KnapsackOutput_weight_set)

    def _get_configuration(self):
        val = _qdk.KnapsackOutput__get_configuration(self)

        return val.asdict()


        return val


    __swig_getmethods__["configuration"] = _get_configuration
    if _newclass: configuration = _swig_property(_get_configuration)

    __swig_destroy__ = _qdk.delete_KnapsackOutput
    __del__ = lambda self: None
KnapsackOutput_swigregister = _qdk.KnapsackOutput_swigregister
KnapsackOutput_swigregister(KnapsackOutput)

class KnapsackIOHandler(IOHandler):
    """

    This is the IO handler for knapsack problems.

    This constructor has the following signature: ::

        KnapsackIOHandler(self)


    """

    __swig_setmethods__ = {}
    for _s in [IOHandler]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, KnapsackIOHandler, name, value)
    __swig_getmethods__ = {}
    for _s in [IOHandler]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, KnapsackIOHandler, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _qdk.new_KnapsackIOHandler()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_KnapsackIOHandler
    __del__ = lambda self: None

    def peek_input(self):
        """

        Gets the current state of the input.

        This function has the following signature: ::

            peek_input(self)

        Returns:
            KnapsackInputBundle: An ``InputBundle`` containing the current state of
             the input.

        """
        return _qdk.KnapsackIOHandler_peek_input(self)


    def clear_io(self):
        """

        This clears the input currently set up and the output produced so far.

        This function has the following signature: ::

            clear_io(self)


        """
        return _qdk.KnapsackIOHandler_clear_io(self)


    def remove_item(self, item_index):
        """

        Removes an item from the problem specification if it exists.

        This function has the following signature: ::

            remove_item(self, item_index)

        Args:
            item_index(int): The index of the item to remove.

        """
        return _qdk.KnapsackIOHandler_remove_item(self, item_index)


    def add_item(self, weight, value, item_index):
        """

        Adds a new item to the problem formulation.

        This function has the following signature: ::

            add_item(self, weight, vlaue, item_index)

        Args:
            weight (int): The weight of the new item.
            value (float): The value of the new item.
            item_index (int): The index of the new item.

        """
        return _qdk.KnapsackIOHandler_add_item(self, weight, value, item_index)


    def update_capacity(self, capacity):
        """

        Updates the capacity of the problem.

        This function has the following signature: ::

            update_capacity(self, capacity)

        Args:
            capacity (int): The new capacity.

        """
        return _qdk.KnapsackIOHandler_update_capacity(self, capacity)


    def update_weight(self, weight, item_index):
        """

        Updates the weight of an item in the problem specification.

        This function has the following signature: ::

            update_weight(self, weight, item_index)

        Args:
            weight (int): The new weight of the item to adds.
            item_index (int): The index of the item to add.

        """
        return _qdk.KnapsackIOHandler_update_weight(self, weight, item_index)


    def update_value(self, value, item_index):
        """

        Updates the value of an item in the problem specification.

        This function has the following signature: ::

            update_value(self, value, item_index)

        Args:
            value (float): The new value.
            item_index (int): The index of the item to update.

        """
        return _qdk.KnapsackIOHandler_update_value(self, value, item_index)


    def clear_output(self):
        """

        Resets the output to an empty ``KnapsackOutput``.

        This function has the following signature: ::

            clear_output(self)


        """
        return _qdk.KnapsackIOHandler_clear_output(self)

KnapsackIOHandler_swigregister = _qdk.KnapsackIOHandler_swigregister
KnapsackIOHandler_swigregister(KnapsackIOHandler)

class UpdateKnapsackInput(UpdateInput):
    """

    This abstract class sends an update to the ``KnapsackIOHandler`` input.

    This constructor has the following signature: ::

        UpdateKnapsackInput(self)


    """

    __swig_setmethods__ = {}
    for _s in [UpdateInput]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, UpdateKnapsackInput, name, value)
    __swig_getmethods__ = {}
    for _s in [UpdateInput]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, UpdateKnapsackInput, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_UpdateKnapsackInput
    __del__ = lambda self: None
UpdateKnapsackInput_swigregister = _qdk.UpdateKnapsackInput_swigregister
UpdateKnapsackInput_swigregister(UpdateKnapsackInput)

class AddItem(UpdateKnapsackInput):
    """

    This class sends an update to the ``KnapsackIOHandler`` to add an item.

    This constructor has the following signature: ::

        AddItem(self, weight, value, item_index, kio)

    Args:
        weight (float): The weight of the new item.
        value (float): The value if the new item.
        item_index (int): The index of the item to add.
        kio (KnapsackIOHandler): The ``KnapsackIOHandler`` that processes the request.

    """

    __swig_setmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, AddItem, name, value)
    __swig_getmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, AddItem, name)
    __repr__ = _swig_repr

    def __init__(self, weight, value, item_index, kio):
        this = _qdk.new_AddItem(weight, value, item_index, kio)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def execute(self):
        """

        This sends the add item command to the ``KnapsackIOHandler``.

        This function has the following signature: ::

            execute(self)

        """
        return _qdk.AddItem_execute(self)

    __swig_destroy__ = _qdk.delete_AddItem
    __del__ = lambda self: None
AddItem_swigregister = _qdk.AddItem_swigregister
AddItem_swigregister(AddItem)

class RemoveItem(UpdateKnapsackInput):
    """

    This class sends an update to the ``KnapsackIOHandler`` input to remove an item.

    This constructor has the following signature: ::

        RemoveItem(self, item_index, kio)

    Args:
        item_index (int): The index of the item to remove.
        kio (KnapsackIOHandler): The ``KnapsackIOHandler`` that processes the request.

    """

    __swig_setmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, RemoveItem, name, value)
    __swig_getmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, RemoveItem, name)
    __repr__ = _swig_repr

    def __init__(self, item_index, kio):
        this = _qdk.new_RemoveItem(item_index, kio)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def execute(self):
        """

        This sends the remove item command to the ``KnapsackIOHandler``.

        This function has the following signature: ::

            execute(self)


        """
        return _qdk.RemoveItem_execute(self)

    __swig_destroy__ = _qdk.delete_RemoveItem
    __del__ = lambda self: None
RemoveItem_swigregister = _qdk.RemoveItem_swigregister
RemoveItem_swigregister(RemoveItem)

class UpdateCapacity(UpdateKnapsackInput):
    """

    This class sends an update to the KnapsackIOHandler to update the capacity.

    This constructor has the following signature: ::

        UpdateCapacity(self, capacity, kio)

    Args:
        capacity (int): The new capacity of the knapsack problem.
        kio (KnapsackIOHandler): The KnapsackIOHandler that processes the request.

    """

    __swig_setmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, UpdateCapacity, name, value)
    __swig_getmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, UpdateCapacity, name)
    __repr__ = _swig_repr

    def __init__(self, capacity, kio):
        this = _qdk.new_UpdateCapacity(capacity, kio)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def execute(self):
        """

        This sends the update capacity command to the KnapsackIOHandler.

        This function has the following signature: ::

            execute(self)


        """
        return _qdk.UpdateCapacity_execute(self)

    __swig_destroy__ = _qdk.delete_UpdateCapacity
    __del__ = lambda self: None
UpdateCapacity_swigregister = _qdk.UpdateCapacity_swigregister
UpdateCapacity_swigregister(UpdateCapacity)

class UpdateValue(UpdateKnapsackInput):
    __swig_setmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, UpdateValue, name, value)
    __swig_getmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, UpdateValue, name)
    __repr__ = _swig_repr

    def __init__(self, value, item_index, kio):
        this = _qdk.new_UpdateValue(value, item_index, kio)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def execute(self):
        """

        Execute the command encapuslated by the instance.

        This function  has the following signature: ::

            execute()


        """
        return _qdk.UpdateValue_execute(self)

    __swig_destroy__ = _qdk.delete_UpdateValue
    __del__ = lambda self: None
UpdateValue_swigregister = _qdk.UpdateValue_swigregister
UpdateValue_swigregister(UpdateValue)

class UpdateWeight(UpdateKnapsackInput):
    """

    This class sends an update to the ``KnapsackIOHandler`` to update an item weight.

    This constructor has the following signature: ::

        UpdateWeight(self, weight, item_index, kio)

    Args:
        weight (float): The new weight.
        item_index (int): The item to add or modify.
        kio (KnapsackIOHandler): The ``KnapsackIOHandler`` that processes the request.

    """

    __swig_setmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, UpdateWeight, name, value)
    __swig_getmethods__ = {}
    for _s in [UpdateKnapsackInput]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, UpdateWeight, name)
    __repr__ = _swig_repr

    def __init__(self, weight, item_index, kio):
        """

        This class sends an update to the ``KnapsackIOHandler`` to update an item weight.

        This constructor has the following signature: ::

            UpdateWeight(self, weight, item_index, kio)

        Args:
            weight (float): The new weight.
            item_index (int): The item to add or modify.
            kio (KnapsackIOHandler): The ``KnapsackIOHandler`` that processes the request.

        """
        this = _qdk.new_UpdateWeight(weight, item_index, kio)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def execute(self):
        """

        This sends the update item weight command to the ``KnapsackIOHandler``.

        This function has the following signature: ::

            execute(self)


        """
        return _qdk.UpdateWeight_execute(self)

    __swig_destroy__ = _qdk.delete_UpdateWeight
    __del__ = lambda self: None
UpdateWeight_swigregister = _qdk.UpdateWeight_swigregister
UpdateWeight_swigregister(UpdateWeight)

class PolyKnapsackAgent(PolynomialAlgorithmAgent, KnapsackIOHandler):
    """

    Class that lets the user describe a Knapsack problem instance, set a solver,
    and solve the optimization.
    If no solver is specified, a Tabu solver with heuristically set
    parameters will be used.

    This constructor has the following signature: ::

        PolyKnapsackAgent(self)

    Attributes:
        configuration (list): List of
         configurations from the solver. Each entry in the list contains the
         ``KnapsackOutput.configuration``, ``KnapsackOutput.value``, and
         ``KnapsackOutput.feasible`` for every ``KnapsackOutputBundle`` solution.

         ``[({KnapsackOutput.configuration_A}, value_A, feasible_A), ({KnapsackOutput.configuration_B}, value_B, feasible_B), ...]``

    """

    __swig_setmethods__ = {}
    for _s in [PolynomialAlgorithmAgent, KnapsackIOHandler]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PolyKnapsackAgent, name, value)
    __swig_getmethods__ = {}
    for _s in [PolynomialAlgorithmAgent, KnapsackIOHandler]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PolyKnapsackAgent, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _qdk.new_PolyKnapsackAgent()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def get_polynomial(self):
        """

        Builds a BinaryPolynomial from the problem's QuadraticBinaryPolynomial. This
        BinaryPolynomial changes if the problem changes and cannot be used to modify the
        problem.

        This function has the following signature: ::

            get_polynomial(self)

        Returns:
            BinaryPolynomial: The HOBO formulation.

        """
        return _qdk.PolyKnapsackAgent_get_polynomial(self)


    def remove_item(self, item_index):
        """

        Removes an item from the problem specification if it exists.

        This function has the following signature: ::

            remove_item(self, item_index)

        Args:
            item_index (int): The index of the item to remove.

        """
        return _qdk.PolyKnapsackAgent_remove_item(self, item_index)


    def add_item(self, weight, value, item_index):
        """

        Adds a new item to the problem formulation.

        This function has the following signature: ::

            add_item(self, weight, value, item_index)

        Args:
            weight (int): The weight of the new item.
            value (float): The value of the new item.
            item_index (int): The index of the new item.

        """
        return _qdk.PolyKnapsackAgent_add_item(self, weight, value, item_index)


    def update_capacity(self, capacity):
        """

        Updates the capacity of the problem.

        This function has the following signature: ::

            update_capacity(self, capacity)

        Args:
            capacity (int): The new knapsack capacity.

        """
        return _qdk.PolyKnapsackAgent_update_capacity(self, capacity)


    def update_weight(self, weight, item_index):
        """

        Updates the weight of an item in the problem specification.

        This function has the following signature: ::

            update_weight(self, weight, item_index)

        Args:
            weight (int): The weight of the item to add.
            item_index (int): The index of the item to add.

        """
        return _qdk.PolyKnapsackAgent_update_weight(self, weight, item_index)


    def update_value(self, value, item_index):
        """

        Updates the value of an item in the problem specification.

        This function has the following signature: ::

            update_value(self, value, item_index)

        Args:
            value (float): The new value.
            item_index (int): The item to update.

        """
        return _qdk.PolyKnapsackAgent_update_value(self, value, item_index)


    def clear_io(self):
        """

        Resets the input currently set up and the output produced so far.

        This function has the following signature: ::

            clear_io(self)

        """
        return _qdk.PolyKnapsackAgent_clear_io(self)


    def get_all_solutions(self):
        """

        Gets the ``OutputBundle`` of all solutions returned from the solver. The
        feasibility of the solutions is not guaranteed. For feasible solutions call
        :py:meth:`qdk.algorithms.PolyKnapsackAgent.get_feasible_solutions`.

        This function has the following signature: ::

            get_all_solutions(self)

        Returns:
            KnapsackOutputBundle: The ``OutputBundle`` which contains a list of
             ``KnapsackOutput`` solutions. All solutions returned from the solver are
             stored in this list.

        """
        return _qdk.PolyKnapsackAgent_get_all_solutions(self)


    def get_feasible_solutions(self):
        """

        Gets the ``OutputBundle`` of all feasible solutions returned from the solver. A
        solutions is considered feasible if its weight of the selected items does not
        exceed the agent's capacity.


        This function has the following signature: ::

            get_feasible_solutions(self)

        Returns:
          KnapsackOutputBundle: The ``OutputBundle`` which contains a list of
           ``KnapsackOutput`` solutions. All feasible solutions returned from the solver
           are stored in this list.

        """
        return _qdk.PolyKnapsackAgent_get_feasible_solutions(self)


    def parse_user_input(self, capacity, items):
        """

        Parse user input for validity.

        This function has the following signature: ::

            parse_user_input(self, capacity, items)

        Args:
            capacity (int): Knapsack problem capacity.
            items (dict): Dictionary of item keys mapped to tuples of item weight and
             values ``{item_A: (weight_A, value_A), item_B: (weight_B, value_B), ...}``.

        """
        return _qdk.PolyKnapsackAgent_parse_user_input(self, capacity, items)


    def _configuration(self):
        return _qdk.PolyKnapsackAgent__configuration(self)

    def run(self, *args):
        """
        Executes the PolyKnapsackAgent

        This function has the following signature: ::

            run()
            run(capacity, items)

        Args:
          capacity (int): Knapsack problem capacity
          items (dict): Dictionary of item keys mapped to tuples of item weight and
           values ``{item_A:(weight_A, value_A), item_B:(weight_B, value_B), ...}``

        Returns:
            KnapsackOutputBundle: The ``OutputBundle`` which contains a list
            of ``KnapsackOutput`` solutions. All feasible solutions returned
            from the solver are stored in this list.
        """
        if args:
            if len(args) is 2:
                self.clear_io()
                self.parse_user_input(args[0], args[1])
            else:
                raise ValueError(
                  """ Wrong number or type of arguments for function run()
                        Possible prototypes are:
                          run()
                          run(capacity, items)""");
        super(PolyKnapsackAgent, self).run()
        return self.get_feasible_solutions()

    def get_qubo(self, *args):
        """
        Get the QUBO representation of the problem

        This function has the following signatures: ::

            get_qubo()
            get_qubo(capacity, items)

        Args:
            capacity (int): Knapsack problem capacity
            items (dict): Dictionary of item keys mapped to tuples of item weight and
             values ``{item_A:(weight_A, value_A), item_B:(weight_B, value_B), ...}``

        Returns:
            QuadraticBinaryPolynomial: The QuadraticBinaryPolynomial representation of the problem
        """
        if args:
            if len(args) is 2:
                self.clear_io()
                self.parse_user_input(args[0], args[1])
            else:
                raise ValueError(
                    """ Wrong number or type of arguments for function get_qubo()
                          Possible prototypes are:
                            get_qubo()
                            get_qubo(capacity, items)""");
        return super(PolyKnapsackAgent, self).get_qubo()

    def get_polynomial(self, *args):
        """
        Get the polynomial representation of the problem

        This function has the following signatures: ::

            get_polynomial()
            get_polynomial(capacity, items)

        Args:
            capacity (int): Knapsack problem capacity
            items (dict): Dictionary of item keys mapped to tuples of item weight and
             values ``{item_A:(weight_A, value_A), item_B:(weight_B, value_B), ...}``

        Returns:
            BinaryPolynomial: BinaryPolynomial representation of the problem
        """
        if args:
            if len(args) is 2:
                self.clear_io()
                self.parse_user_input(args[0], args[1])
            else:
                raise ValueError(
                    """ Wrong number or type of arguments for function get_polynomial()
                          Possible prototypes are:
                            get_polynomial()
                            get_polynomial(capacity, items)""");
        return super(PolyKnapsackAgent, self).get_polynomial()

    __swig_getmethods__["configuration"] = _qdk.PolyKnapsackAgent__configuration
    if _newclass: configuration = _swig_property(
        _qdk.PolyKnapsackAgent__configuration)

    __swig_destroy__ = _qdk.delete_PolyKnapsackAgent
    __del__ = lambda self: None
PolyKnapsackAgent_swigregister = _qdk.PolyKnapsackAgent_swigregister
PolyKnapsackAgent_swigregister(PolyKnapsackAgent)

class NodePropMap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, NodePropMap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, NodePropMap, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _qdk.NodePropMap_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _qdk.NodePropMap___nonzero__(self)

    def __bool__(self):
        return _qdk.NodePropMap___bool__(self)

    def __len__(self):
        return _qdk.NodePropMap___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _qdk.NodePropMap___getitem__(self, key)

    def __delitem__(self, key):
        return _qdk.NodePropMap___delitem__(self, key)

    def has_key(self, key):
        return _qdk.NodePropMap_has_key(self, key)

    def keys(self):
        return _qdk.NodePropMap_keys(self)

    def values(self):
        return _qdk.NodePropMap_values(self)

    def items(self):
        return _qdk.NodePropMap_items(self)

    def __contains__(self, key):
        return _qdk.NodePropMap___contains__(self, key)

    def key_iterator(self):
        return _qdk.NodePropMap_key_iterator(self)

    def value_iterator(self):
        return _qdk.NodePropMap_value_iterator(self)

    def __setitem__(self, *args):
        return _qdk.NodePropMap___setitem__(self, *args)

    def asdict(self):
        return _qdk.NodePropMap_asdict(self)

    def __init__(self, *args):
        this = _qdk.new_NodePropMap(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _qdk.NodePropMap_empty(self)

    def size(self):
        return _qdk.NodePropMap_size(self)

    def swap(self, v):
        return _qdk.NodePropMap_swap(self, v)

    def begin(self):
        return _qdk.NodePropMap_begin(self)

    def end(self):
        return _qdk.NodePropMap_end(self)

    def rbegin(self):
        return _qdk.NodePropMap_rbegin(self)

    def rend(self):
        return _qdk.NodePropMap_rend(self)

    def clear(self):
        return _qdk.NodePropMap_clear(self)

    def get_allocator(self):
        return _qdk.NodePropMap_get_allocator(self)

    def count(self, x):
        return _qdk.NodePropMap_count(self, x)

    def erase(self, *args):
        return _qdk.NodePropMap_erase(self, *args)

    def find(self, x):
        return _qdk.NodePropMap_find(self, x)

    def lower_bound(self, x):
        return _qdk.NodePropMap_lower_bound(self, x)

    def upper_bound(self, x):
        return _qdk.NodePropMap_upper_bound(self, x)
    __swig_destroy__ = _qdk.delete_NodePropMap
    __del__ = lambda self: None
NodePropMap_swigregister = _qdk.NodePropMap_swigregister
NodePropMap_swigregister(NodePropMap)

class CliqueOutputList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CliqueOutputList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CliqueOutputList, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _qdk.CliqueOutputList_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _qdk.CliqueOutputList___nonzero__(self)

    def __bool__(self):
        return _qdk.CliqueOutputList___bool__(self)

    def __len__(self):
        return _qdk.CliqueOutputList___len__(self)

    def __getslice__(self, i, j):
        return _qdk.CliqueOutputList___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _qdk.CliqueOutputList___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _qdk.CliqueOutputList___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _qdk.CliqueOutputList___delitem__(self, *args)

    def __getitem__(self, *args):
        return _qdk.CliqueOutputList___getitem__(self, *args)

    def __setitem__(self, *args):
        return _qdk.CliqueOutputList___setitem__(self, *args)

    def pop(self):
        return _qdk.CliqueOutputList_pop(self)

    def append(self, x):
        return _qdk.CliqueOutputList_append(self, x)

    def empty(self):
        return _qdk.CliqueOutputList_empty(self)

    def size(self):
        return _qdk.CliqueOutputList_size(self)

    def swap(self, v):
        return _qdk.CliqueOutputList_swap(self, v)

    def begin(self):
        return _qdk.CliqueOutputList_begin(self)

    def end(self):
        return _qdk.CliqueOutputList_end(self)

    def rbegin(self):
        return _qdk.CliqueOutputList_rbegin(self)

    def rend(self):
        return _qdk.CliqueOutputList_rend(self)

    def clear(self):
        return _qdk.CliqueOutputList_clear(self)

    def get_allocator(self):
        return _qdk.CliqueOutputList_get_allocator(self)

    def pop_back(self):
        return _qdk.CliqueOutputList_pop_back(self)

    def erase(self, *args):
        return _qdk.CliqueOutputList_erase(self, *args)

    def __init__(self, *args):
        this = _qdk.new_CliqueOutputList(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _qdk.CliqueOutputList_push_back(self, x)

    def front(self):
        return _qdk.CliqueOutputList_front(self)

    def back(self):
        return _qdk.CliqueOutputList_back(self)

    def assign(self, n, x):
        return _qdk.CliqueOutputList_assign(self, n, x)

    def resize(self, *args):
        return _qdk.CliqueOutputList_resize(self, *args)

    def insert(self, *args):
        return _qdk.CliqueOutputList_insert(self, *args)

    def reserve(self, n):
        return _qdk.CliqueOutputList_reserve(self, n)

    def capacity(self):
        return _qdk.CliqueOutputList_capacity(self)
    __swig_destroy__ = _qdk.delete_CliqueOutputList
    __del__ = lambda self: None
CliqueOutputList_swigregister = _qdk.CliqueOutputList_swigregister
CliqueOutputList_swigregister(CliqueOutputList)

class GraphSimilarityOutputList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphSimilarityOutputList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GraphSimilarityOutputList, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _qdk.GraphSimilarityOutputList_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _qdk.GraphSimilarityOutputList___nonzero__(self)

    def __bool__(self):
        return _qdk.GraphSimilarityOutputList___bool__(self)

    def __len__(self):
        return _qdk.GraphSimilarityOutputList___len__(self)

    def __getslice__(self, i, j):
        return _qdk.GraphSimilarityOutputList___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _qdk.GraphSimilarityOutputList___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _qdk.GraphSimilarityOutputList___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _qdk.GraphSimilarityOutputList___delitem__(self, *args)

    def __getitem__(self, *args):
        return _qdk.GraphSimilarityOutputList___getitem__(self, *args)

    def __setitem__(self, *args):
        return _qdk.GraphSimilarityOutputList___setitem__(self, *args)

    def pop(self):
        return _qdk.GraphSimilarityOutputList_pop(self)

    def append(self, x):
        return _qdk.GraphSimilarityOutputList_append(self, x)

    def empty(self):
        return _qdk.GraphSimilarityOutputList_empty(self)

    def size(self):
        return _qdk.GraphSimilarityOutputList_size(self)

    def swap(self, v):
        return _qdk.GraphSimilarityOutputList_swap(self, v)

    def begin(self):
        return _qdk.GraphSimilarityOutputList_begin(self)

    def end(self):
        return _qdk.GraphSimilarityOutputList_end(self)

    def rbegin(self):
        return _qdk.GraphSimilarityOutputList_rbegin(self)

    def rend(self):
        return _qdk.GraphSimilarityOutputList_rend(self)

    def clear(self):
        return _qdk.GraphSimilarityOutputList_clear(self)

    def get_allocator(self):
        return _qdk.GraphSimilarityOutputList_get_allocator(self)

    def pop_back(self):
        return _qdk.GraphSimilarityOutputList_pop_back(self)

    def erase(self, *args):
        return _qdk.GraphSimilarityOutputList_erase(self, *args)

    def __init__(self, *args):
        this = _qdk.new_GraphSimilarityOutputList(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _qdk.GraphSimilarityOutputList_push_back(self, x)

    def front(self):
        return _qdk.GraphSimilarityOutputList_front(self)

    def back(self):
        return _qdk.GraphSimilarityOutputList_back(self)

    def assign(self, n, x):
        return _qdk.GraphSimilarityOutputList_assign(self, n, x)

    def resize(self, *args):
        return _qdk.GraphSimilarityOutputList_resize(self, *args)

    def insert(self, *args):
        return _qdk.GraphSimilarityOutputList_insert(self, *args)

    def reserve(self, n):
        return _qdk.GraphSimilarityOutputList_reserve(self, n)

    def capacity(self):
        return _qdk.GraphSimilarityOutputList_capacity(self)
    __swig_destroy__ = _qdk.delete_GraphSimilarityOutputList
    __del__ = lambda self: None
GraphSimilarityOutputList_swigregister = _qdk.GraphSimilarityOutputList_swigregister
GraphSimilarityOutputList_swigregister(GraphSimilarityOutputList)

class PMap(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PMap, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PMap, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _qdk.PMap_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _qdk.PMap___nonzero__(self)

    def __bool__(self):
        return _qdk.PMap___bool__(self)

    def __len__(self):
        return _qdk.PMap___len__(self)
    def __iter__(self):
        return self.key_iterator()
    def iterkeys(self):
        return self.key_iterator()
    def itervalues(self):
        return self.value_iterator()
    def iteritems(self):
        return self.iterator()

    def __getitem__(self, key):
        return _qdk.PMap___getitem__(self, key)

    def __delitem__(self, key):
        return _qdk.PMap___delitem__(self, key)

    def has_key(self, key):
        return _qdk.PMap_has_key(self, key)

    def keys(self):
        return _qdk.PMap_keys(self)

    def values(self):
        return _qdk.PMap_values(self)

    def items(self):
        return _qdk.PMap_items(self)

    def __contains__(self, key):
        return _qdk.PMap___contains__(self, key)

    def key_iterator(self):
        return _qdk.PMap_key_iterator(self)

    def value_iterator(self):
        return _qdk.PMap_value_iterator(self)

    def __setitem__(self, *args):
        return _qdk.PMap___setitem__(self, *args)

    def asdict(self):
        return _qdk.PMap_asdict(self)

    def __init__(self, *args):
        this = _qdk.new_PMap(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def empty(self):
        return _qdk.PMap_empty(self)

    def size(self):
        return _qdk.PMap_size(self)

    def swap(self, v):
        return _qdk.PMap_swap(self, v)

    def begin(self):
        return _qdk.PMap_begin(self)

    def end(self):
        return _qdk.PMap_end(self)

    def rbegin(self):
        return _qdk.PMap_rbegin(self)

    def rend(self):
        return _qdk.PMap_rend(self)

    def clear(self):
        return _qdk.PMap_clear(self)

    def get_allocator(self):
        return _qdk.PMap_get_allocator(self)

    def count(self, x):
        return _qdk.PMap_count(self, x)

    def erase(self, *args):
        return _qdk.PMap_erase(self, *args)

    def find(self, x):
        return _qdk.PMap_find(self, x)

    def lower_bound(self, x):
        return _qdk.PMap_lower_bound(self, x)

    def upper_bound(self, x):
        return _qdk.PMap_upper_bound(self, x)
    __swig_destroy__ = _qdk.delete_PMap
    __del__ = lambda self: None
PMap_swigregister = _qdk.PMap_swigregister
PMap_swigregister(PMap)

class MatchedNodesPair(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MatchedNodesPair, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MatchedNodesPair, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _qdk.new_MatchedNodesPair(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_setmethods__["first"] = _qdk.MatchedNodesPair_first_set
    __swig_getmethods__["first"] = _qdk.MatchedNodesPair_first_get
    if _newclass:
        first = _swig_property(_qdk.MatchedNodesPair_first_get, _qdk.MatchedNodesPair_first_set)
    __swig_setmethods__["second"] = _qdk.MatchedNodesPair_second_set
    __swig_getmethods__["second"] = _qdk.MatchedNodesPair_second_get
    if _newclass:
        second = _swig_property(_qdk.MatchedNodesPair_second_get, _qdk.MatchedNodesPair_second_set)
    def __len__(self):
        return 2
    def __repr__(self):
        return str((self.first, self.second))
    def __getitem__(self, index): 
        if not (index % 2):
            return self.first
        else:
            return self.second
    def __setitem__(self, index, val):
        if not (index % 2):
            self.first = val
        else:
            self.second = val
    __swig_destroy__ = _qdk.delete_MatchedNodesPair
    __del__ = lambda self: None
MatchedNodesPair_swigregister = _qdk.MatchedNodesPair_swigregister
MatchedNodesPair_swigregister(MatchedNodesPair)

class GraphSimilaritySolution(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, GraphSimilaritySolution, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, GraphSimilaritySolution, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _qdk.GraphSimilaritySolution_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _qdk.GraphSimilaritySolution___nonzero__(self)

    def __bool__(self):
        return _qdk.GraphSimilaritySolution___bool__(self)

    def __len__(self):
        return _qdk.GraphSimilaritySolution___len__(self)

    def __getslice__(self, i, j):
        return _qdk.GraphSimilaritySolution___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _qdk.GraphSimilaritySolution___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _qdk.GraphSimilaritySolution___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _qdk.GraphSimilaritySolution___delitem__(self, *args)

    def __getitem__(self, *args):
        return _qdk.GraphSimilaritySolution___getitem__(self, *args)

    def __setitem__(self, *args):
        return _qdk.GraphSimilaritySolution___setitem__(self, *args)

    def pop(self):
        return _qdk.GraphSimilaritySolution_pop(self)

    def append(self, x):
        return _qdk.GraphSimilaritySolution_append(self, x)

    def empty(self):
        return _qdk.GraphSimilaritySolution_empty(self)

    def size(self):
        return _qdk.GraphSimilaritySolution_size(self)

    def swap(self, v):
        return _qdk.GraphSimilaritySolution_swap(self, v)

    def begin(self):
        return _qdk.GraphSimilaritySolution_begin(self)

    def end(self):
        return _qdk.GraphSimilaritySolution_end(self)

    def rbegin(self):
        return _qdk.GraphSimilaritySolution_rbegin(self)

    def rend(self):
        return _qdk.GraphSimilaritySolution_rend(self)

    def clear(self):
        return _qdk.GraphSimilaritySolution_clear(self)

    def get_allocator(self):
        return _qdk.GraphSimilaritySolution_get_allocator(self)

    def pop_back(self):
        return _qdk.GraphSimilaritySolution_pop_back(self)

    def erase(self, *args):
        return _qdk.GraphSimilaritySolution_erase(self, *args)

    def __init__(self, *args):
        this = _qdk.new_GraphSimilaritySolution(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _qdk.GraphSimilaritySolution_push_back(self, x)

    def front(self):
        return _qdk.GraphSimilaritySolution_front(self)

    def back(self):
        return _qdk.GraphSimilaritySolution_back(self)

    def assign(self, n, x):
        return _qdk.GraphSimilaritySolution_assign(self, n, x)

    def resize(self, *args):
        return _qdk.GraphSimilaritySolution_resize(self, *args)

    def insert(self, *args):
        return _qdk.GraphSimilaritySolution_insert(self, *args)

    def reserve(self, n):
        return _qdk.GraphSimilaritySolution_reserve(self, n)

    def capacity(self):
        return _qdk.GraphSimilaritySolution_capacity(self)
    __swig_destroy__ = _qdk.delete_GraphSimilaritySolution
    __del__ = lambda self: None
GraphSimilaritySolution_swigregister = _qdk.GraphSimilaritySolution_swigregister
GraphSimilaritySolution_swigregister(GraphSimilaritySolution)


