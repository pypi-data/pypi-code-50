import copy
import json
import networkx as nx
from os.path import expanduser
from networkx.readwrite import json_graph
from jena_reasoning.owl import Knowledge
import matplotlib.pyplot as plt

DEFAULT_HUMAN_EXECUTION_TIME = (10, 20)
DEFAULT_ROBOT_EXECUTION_TIME = (20, 30)

class BaseSolution():
    def __init__(self):
        self.reasoner = Knowledge()
        self._graph = nx.DiGraph()
        self.synch_table = {}

    def relax_network(self):
        """ Relax the temporal constraints.

        The disjunctive constraints can be combined by taking only the lower and upper bounds.
        """
        for u, v, weight in self._graph.edges(data='temporal_constraint'):
            if not u=="Start":
                human_expectations = weight[0]
                robot_expectations = weight[1]
                self.set_relation(u, v, 'temporal_constraint', (min(human_expectations[0], robot_expectations[0]), max(human_expectations[1], robot_expectations[1])))

    def transform_dispatchable_graph(self, method="apsp"):
        """ Compute the Base Solution.

        The Base Solution consists in a dispatchable graph.
        One-step propagation makes explicit all constraints on neighboring events.
        """
        if method == "apsp":
            print("Construct distance graph:")
            self.construct_distance_graph()
            print("Writing resulting graph into dist.graphml")
            #nx.write_graphml(self._graph, "dist.graphml")
            print("Calculating the APSP form of the graph:")
            self.all_pairs_shortest_paths()
            print("Writing resulting graph into apsp.graphml")
            #nx.write_graphml(self._graph, "apsp.graphml")
            print("Removing dominated edges:")
            self.prune_redundant_constraints()
            #self.graph_to_json()
        elif method == "chordal":
            pass

    def model_temporal_problem(self, skill):
        """ Converts the problem into an STNU

        Translate the lists of steps and their constraints into timepoints and links between them.
        """
        list_steps = self.reasoner.retrieve_assembly_steps(skill)
        list_steps = [x[0].toPython() for x in list_steps]
        list_assemblies = []

        for assy_step in list_steps:
            list_assemblies.append(self.reasoner.retrieve_links(assy_step))

        step = 0
        while(list_assemblies):
            less_constrained = []
            min = 10

            for x in list_assemblies:
                if len(x) < min:
                    less_constrained = []
                    less_constrained.append(x)
                    min = len(x)
                elif len(x) == min:
                    less_constrained.append(x)
            if not less_constrained:
                min=min-1
            else:
                step=step+1
                # print("Round of less constrained: {}".format(less_constrained))
                list_assemblies = [item for item in list_assemblies if item not in less_constrained]
                # print("Round of assemblies: {}".format(list_assemblies))

                for list_link in less_constrained:
                    edges = self.reasoner.deduce_assembly_logic(list_link)
                    # print("Edges {}".format(edges))
                    if not isinstance(edges[0], tuple):
                        self.add_event(peg = edges[0], hole = edges[1], step=step)
                    else:
                        self.add_event(peg = (edges[0][0], edges[0][1]), hole = "", step=step)


        for id_node_a, data_node_a in list(self._graph.nodes.data()):
            for id_node_b, data_node_b in list(self._graph.nodes.data()):
                # print("Round of nodes: {},{} and {},{}".format(id_node_a, data_node_a, id_node_b, data_node_b))
                if data_node_a['step'] > data_node_b['step']:
                    self.set_relation(id_node_a, id_node_b, 'temporal_constraint', (DEFAULT_HUMAN_EXECUTION_TIME, DEFAULT_ROBOT_EXECUTION_TIME))

        return list_steps

    @property
    def timepoints(self):
        """Get the timepoints of the network."""
        return [task for task in self._graph.nodes(data=True) if not task[0] == "Start"]

    def update_after_completion(self, event, time):
        # print ("Before {}".format(self.synch_table))
        print("Graph before completion of node {}: {}".format(event, self._graph.nodes(data=True)))
        self._graph.nodes[event]['is_done'] = True
        print("Graph after completion of node {}: {}".format(event, self._graph.nodes(data=True)))
        # del self.synch_table[event]
        # for step, synch in self.synch_table.items():
        #    if event in synch:
        #         self.synch_table[step].remove(event)
        # print ("After {}".format(self.synch_table))

    def available_steps(self):
        """Get the available events in the network."""
        # print("Remaining steps are: {}".format([step for step, data in self._graph.nodes.data() if not data['is_done']]))
        return [step for step, data in self._graph.nodes.data() if not data['is_done']]

    def retrieve_subgraph(self, step):
        return self._graph.subgraph( [n for n,attrdict in self._graph.node.items() if not n == "Start" and attrdict['step'] == step ] )

    def _are_available(self, events):
        return False if False in map(self._is_available, events) else True

    def get_event(self, event, data=False):
        """Return the value for an attribute of the node 'event' if data. All the attributes otherwise."""
        return self._graph.nodes(data=data)[event] if data else self._graph.nodes(data=True)[event]

    def add_event(self, peg, hole, step, is_done=False):
        """Create a new node in the graph."""
        id = nx.number_of_nodes(self._graph)+1
        self._graph.add_node(id, step=step, peg=peg, hole=hole, is_done=is_done, is_claimed=False)
        return id

    def set_event(self, name, data, value):
        """ Set the attribute 'data' of the node 'name' to 'value'"""
        nx.set_node_attributes(self._graph, value, data)

    def has_relation(self, u, v):
        """ Return the value of an edge. False if it does not exist."""
        return self._graph.edges[u, v]['temporal_constraint'] if self._graph.has_edge(u, v) else False

    def set_relation(self, u, v, data, value):
        """Set the value of an edge. Create if it does not exist yet."""
        if not self.has_relation(u, v):
            self._graph.add_edge(u, v)
        self._graph.edges[u, v][data] = value

    def adjacent_nodes(self, node=False):
        """Return the list of events related to the argument"""
        return list(self._graph.adj[node[0]]) if type(node) is tuple else list(self._graph.adj[node])

    def construct_distance_graph(self):
        """ Translate the constraint form representation into its associated distance graph.

        The distance graph indicates the same interval as the constraint but yields two equivalent inequalities.
        """
        new_edges = []
        for u, v, weight in self._graph.edges(data='temporal_constraint'):
            lower_bound = weight[0] if not isinstance(weight, int) else weight
            upper_bound = weight[1] if not isinstance(weight, int) else weight
            self.set_relation(u, v, 'temporal_constraint', upper_bound)
            self.set_relation(v, u, 'temporal_constraint', -lower_bound)
            new_edges.append((v, u, -lower_bound))

    def all_pairs_shortest_paths(self):
        """ Compute all pairs shortest paths with Floyd-Warshall algorithm

        Computes a fully-connected network, with binary constraints relating each pair of events.
        """
        distance = nx.floyd_warshall(self._graph, weight='temporal_constraint')
        for node_a in distance:
            for node_b in distance[node_a]:
                if not(node_a==node_b or (node_a, node_b) in list(self._graph.edges)):
                    self.set_relation(node_a, node_b, 'temporal_constraint', distance[node_a][node_b])

    def prune_redundant_constraints(self):
        """ Remove dominated edges.

        Remove dominated edges to make STN dispatchable.
        """
        graph = copy.deepcopy(self._graph)
        for A, B, weight in self._graph.edges(data='temporal_constraint'):
            for C in set(self._graph.successors(A)).intersection(self._graph.successors(B)):
                a_c = self.has_relation(A, C)
                b_c = self.has_relation(B, C)
                if self.is_dominated(a_c, b_c, weight):
                    try:
                        graph.remove_edge(A, C)
                    except:
                        pass
                    break
        self._graph = graph

    def is_dominated(self, edge_ac, edge_bc, edge_ab):
        if (edge_ac > 0 and edge_bc > 0) or (edge_ac < 0 and edge_ab < 0):
            return True if edge_ac == edge_ab + edge_bc else False
        else:
            return False

    def graph_to_json(self):
        filename = raw_input("Enter a file name to save the plan: ")
        filename = expanduser("~")+"/"+filename+".owl"
        d = json_graph.node_link_data(self._graph)  # node-link format to serialize
        # write json
        file = open(filename, "w+")
        json.dump(d, file)

    def display_graph(self, title=""):
        pos = nx.shell_layout(self._graph)
        plt.title(title)
        nx.draw_networkx_nodes(self._graph, pos, cmap=plt.get_cmap('jet'), node_size = 500)
        nx.draw_networkx_labels(self._graph, pos)
        nx.draw_networkx_edges(self._graph, pos, edge_color='r', arrows=True)
        nx.draw_networkx_edge_labels(self._graph, pos=nx.spring_layout(self._graph))
        plt.show()

    def print_graph(self):
        print(list(self._graph.nodes(data=True)))
        print(list(self._graph.edges(data=True)))
