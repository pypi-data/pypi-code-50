#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Saifeddine ALOUI
Description:
Grapph object
"""
import enum
from QGraphViz.DotParser.Node import Node
from QGraphViz.DotParser.Edge import Edge

class GraphType(enum.Enum):
    SimpleGraph=0
    DirectedGraph=1        

class Graph(Node):
    """
    The graph object made of nodes, edges and subgraphs 
    """
    def __init__(self, name, graph_type = GraphType.SimpleGraph, parent_graph=None,  **kwargs):
        Node.__init__(self, name, parent_graph, **kwargs)
        self.parent_graph = parent_graph
        self.current_x=0
        self.current_y=0
        self.nodes=[]
        self.edges=[]
        self.graph_type = graph_type

    def addNode(self, node):
        """
        Adds a node to the graph
        :param node: Node to add to the graph
        """
        self.nodes.append(node)

    def addEdge(self, edge):
        """
        Adds an edge to the graph
        :param edge: An edge to be added to the graph
        """
        self.nodes.append(edge)
   
    def getNodeByName(self, name):
        nodenames = [n.name for n in self.nodes]
        if name in nodenames:
            return self.nodes[nodenames.index(name)]
        else:
            return None

    def findNode(self, node_name):
        for node in self.nodes:
            if(node.name==node_name):
                return node
            if(type(node)==Graph):
                nd = node.findNode(node_name)
                if(nd!=None):
                    return nd
        return None

    def toDICT(self):
        graph_dic = {}
        graph_dic["name"]=self.name
        graph_dic["graph_type"]=self.graph_type.value
        graph_dic["kwargs"]=self.kwargs
        graph_dic["nodes"]=[]
        graph_dic["edges"]=[]

        for node in self.nodes:
            graph_dic["nodes"].append(node.toDICT())
        for edge in self.edges:
            graph_dic["edges"].append(edge.toDICT())

        return graph_dic

    def fromDICT(self, graph_dic):
        self.name = graph_dic["name"]
        self.graph_type = GraphType(graph_dic["graph_type"])
        self.kwargs = graph_dic["kwargs"]
        self.nodes=[]
        for node in graph_dic["nodes"]:
            if("graph_type" in node.keys()):
                self.nodes.append(Graph(node["name"], self, **node["kwargs"]).fromDICT(node))
            else:
                self.nodes.append(Node(node["name"], self, **node["kwargs"]))

        for edge in graph_dic["edges"]:
            source = self.findNode(edge["source"])
            dest = self.findNode(edge["dest"])
            ed = Edge(source, dest)
            ed.kwargs = edge["kwargs"]
            self.edges.append(ed)
            
        return self
