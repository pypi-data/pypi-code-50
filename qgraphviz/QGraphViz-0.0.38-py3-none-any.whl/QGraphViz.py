#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Author: Saifeddine ALOUI
Description:
Main Class to QGraphViz tool
"""
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QPainterPath, QImage, QLinearGradient
from PyQt5.QtCore import Qt, QRect
import os
import sys
import enum
import datetime
from QGraphViz.DotParser import DotParser, Node, Edge, Graph, GraphType
import math

class QGraphVizManipulationMode(enum.Enum):
    Static=0
    Nodes_Move_Mode=1
    Edges_Connect_Mode=2
    Node_remove_Mode=3
    Edge_remove_Mode=4
    Subgraph_remove_Mode=5

class QGraphViz(QWidget):
    """
    Main graphviz widget to draw and interact with graphs
    """
    def __init__(
                    self, 
                    parent=None, 
                    engine=None, 
                    show_subgraphs = True,
                    manipulation_mode=QGraphVizManipulationMode.Nodes_Move_Mode,
                    # Callbacks
                    new_edge_beingAdded_callback=None, # A callback called when a new connection is being added (should return True or False to accept or not the edge, as well as return the edge parameters)
                    new_edge_created_callback=None, # A callbakc called when a new connection is created between two nodes using the GUI
                    node_selected_callback=None, # A callback called when a node is clicked
                    edge_selected_callback=None, # A callback called when an edge is clicked
                    node_invoked_callback=None, # A callback called when a node is double clicked
                    edge_invoked_callback=None, # A callback called when an edge is double clicked
                    node_removed_callback=None, # A callback called when a node is removed
                    edge_removed_callback=None, # A callback called when an edge is removed

                    # Custom options
                    min_cursor_edge_dist=3,
                    hilight_Nodes=False,
                    hilight_Edges=False
                ):
        """
        QGraphViz widget Constructor
        :param parent: A QWidget parent of the QGraphViz widget
        :param engine: The graph processing engine (exemple Dot engine)
        :param show_subgraphs: Tells whether to show the content of subgraphs or not
        :param manipulation_mode: Sets the current graph manipulations mode
        :param new_edge_beingAdded_callback: A callback issued when a new edge is being added. This callback should return a boolean to accept or refuse adding the edge.
        :param new_edge_created_callback: A callback issued when a new edge is added.
        :param node_selected_callback: A callback issued when a node is selected.
        :param edge_selected_callback: A callback issued when an edge is selected.
        :param node_removed_callback: A callback issued when an node is removed.
        :param edge_removed_callback: A callback issued when an edge is removed.
        :param min_cursor_edge_dist: Minimal distance between sursor edge.
        :param hilight_Nodes: If True, whenever mouse is hovered on a node, it is hilighted.
        :param hilight_Edges: If True, whenever mouse is hovered on an edge, it is hilighted.
        """
        QWidget.__init__(self,parent)
        self.parser = DotParser()
        self.engine=engine
        
        # Pfrepare lists
        self.qnodes=[]
        self.qedges=[]

        # Nodes manipulation
        self.manipulation_mode = manipulation_mode
        self.selected_Node = None  
        self.hovered_Node = None
        self.hovered_Edge = None
        self.hovered_Edge_id = None
        self.current_pos = [0,0]
        self.mouse_down=False
        self.min_cursor_edge_dist=min_cursor_edge_dist
        self.show_subgraphs=show_subgraphs

        # Set callbacks
        self.new_edge_beingAdded_callback = new_edge_beingAdded_callback
        self.new_edge_created_callback = new_edge_created_callback
        self.node_selected_callback = node_selected_callback
        self.edge_selected_callback = edge_selected_callback
        self.node_invoked_callback = node_invoked_callback
        self.edge_invoked_callback = edge_invoked_callback
        self.node_removed_callback=node_removed_callback
        self.edge_removed_callback=edge_removed_callback

        self.hilight_Nodes=hilight_Nodes
        self.hilight_Edges=hilight_Edges

        self.setAutoFillBackground(True)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setMouseTracking(True)

    def build(self):
        self.engine.build()
        """
        for node in self.engine.graph.nodes:
            qnode = QNode(node, self)
            qnode.setParent(self)
            self.qnodes.append(qnode)
        for edge in self.engine.graph.edges:
            qedge = QEdge(edge, self)
            qedge.setParent(self)
            self.qedges.append(qedge)
        """
    def paintSubgraph(self, subgraph, painter, pen, brush):
        if("color" in subgraph.kwargs.keys()):
            pen.setColor(QColor(subgraph.kwargs["color"]))
        else:
            pen.setColor(QColor("black"))

        if("fillcolor" in subgraph.kwargs.keys()):
            if(":" in subgraph.kwargs["fillcolor"]):
                gradient=QLinearGradient(subgraph.pos[0]-subgraph.size[0]/2, subgraph.pos[1], subgraph.pos[0]+subgraph.size[0]/2, subgraph.pos[1])
                c=subgraph.kwargs["fillcolor"].split(":")
                for i, col in enumerate(c):
                    stop = i/(len(c)-1)
                    gradient.setColorAt(stop, QColor(col))

                brush = QBrush(gradient)
            else:
                brush=QBrush(QColor(subgraph.kwargs["fillcolor"]))
        else:
            brush=QBrush(QColor("white"))



        if("width" in subgraph.kwargs.keys()):
            pen.setWidth(int(subgraph.kwargs["width"]))
        else:
            pen.setWidth(1)

        painter.setPen(pen)
        painter.setBrush(brush)
        gpos = subgraph.global_pos

        painter.drawRect(
                    gpos[0]-subgraph.size[0]/2,
                    gpos[1]-subgraph.size[1]/2,
                    subgraph.size[0], subgraph.size[1])

        if("label" in subgraph.kwargs.keys()):
            painter.drawText(
                gpos[0]-subgraph.size[0]/2,
                gpos[1]-subgraph.size[1]/2,
                subgraph.size[0], subgraph.size[1],
                Qt.AlignCenter|Qt.AlignTop,subgraph.kwargs["label"])

    def paintGraph(self, graph, painter):
        brush = QBrush(Qt.SolidPattern)
        pen=QPen()
        brush.setColor(Qt.white)

        if(self.show_subgraphs):
            for node in graph.nodes:
                if type(node)==Graph:
                    subgraph = node
                    self.paintSubgraph(subgraph, painter, pen, brush)

        for i,edge in enumerate(graph.edges):
            if("color" in edge.kwargs.keys()):
                pen.setColor(QColor(edge.kwargs["color"]))
            else:
                pen.setColor(QColor("black"))

            if("width" in edge.kwargs.keys()):
                pen.setWidth(int(edge.kwargs["width"]))
            else:
                pen.setWidth(1)

            painter.setPen(pen)
            painter.setBrush(brush)
            if(edge.source.parent_graph !=graph and not self.show_subgraphs):
                gspos = edge.source.parent_graph.global_pos
            else:
                gspos = edge.source.global_pos

            if(edge.dest.parent_graph !=graph and not self.show_subgraphs):
                gspos = edge.dest.parent_graph.global_pos
            else:
                gdpos = edge.dest.global_pos

            nb_next=0
            for j in range(i, len(graph.edges)):
                if(graph.edges[j].source==edge.source and graph.edges[j].dest==edge.dest):
                    nb_next+=1

            offset=[0,0]
            if(nb_next%2==1):
                offset[0]=20*(nb_next/2)
            else:
                offset[0]=-20*(nb_next/2)
            path = QPainterPath()
            path.moveTo(gspos[0],gspos[1])
            path.cubicTo(gspos[0],gspos[1],offset[0]+(gspos[0]+gdpos[0])/2,(gspos[1]+gdpos[1])/2,gdpos[0],gdpos[1])
            painter.strokePath(path, pen)
            """
            painter.drawLine(gspos[0],gspos[1],
            gdpos[0],
            gdpos[1])
            """
         # TODO : add more painting parameters
        for node in graph.nodes:
            if type(node)!=Graph:
                if("color" in node.kwargs.keys()):
                    pen.setColor(QColor(node.kwargs["color"]))
                else:
                    pen.setColor(QColor("black"))

                if("fillcolor" in node.kwargs.keys()):
                    if(":" in node.kwargs["fillcolor"]):
                        gradient=QLinearGradient(node.pos[0]-node.size[0]/2, node.pos[1], node.pos[0]+node.size[0]/2, node.pos[1])
                        c=node.kwargs["fillcolor"].split(":")
                        for i, col in enumerate(c):
                            stop = i/(len(c)-1)
                            gradient.setColorAt(stop, QColor(col))

                        brush = QBrush(gradient)
                    else:
                        brush=QBrush(QColor(node.kwargs["fillcolor"]))
                else:
                    brush=QBrush(QColor("white"))

                if("width" in node.kwargs.keys()):
                    pen.setWidth(int(node.kwargs["width"]))
                else:
                    pen.setWidth(1)

                gpos = node.global_pos

                painter.setPen(pen)
                painter.setBrush(brush)
                if("shape" in node.kwargs.keys()):
                    if(node.kwargs["shape"]=="box"):
                        painter.drawRect(
                                    gpos[0]-node.size[0]/2,
                                    gpos[1]-node.size[1]/2,
                                    node.size[0], node.size[1])

                    if(node.kwargs["shape"]=="circle"):
                        painter.drawEllipse(
                                    gpos[0]-node.size[0]/2,
                                    gpos[1]-node.size[1]/2,
                                    node.size[0], node.size[1])
                    
                    # Image as a node, this implementation checks to see if a 
                    # file path was provided in the shape parameter
                    if(os.path.isfile(node.kwargs["shape"])): 
                        img_path = node.kwargs["shape"]
                        painter.drawImage(
                            QRect(
                                gpos[0]-node.size[0]/2,
                                gpos[1]-node.size[1]/2,
                                node.size[0],
                                node.size[1]), 
                            QImage(img_path))
                else:
                    painter.drawEllipse(
                                gpos[0]-node.size[0]/2,
                                gpos[1]-node.size[1]/2,
                                node.size[0], node.size[1])


                if("label" in node.kwargs.keys()):
                    painter.drawText(
                        gpos[0]-node.size[0]/2,
                        gpos[1]-node.size[1]/2,
                        node.size[0], node.size[1],
                        Qt.AlignCenter|Qt.AlignTop,node.kwargs["label"])
            else:
                if(self.show_subgraphs):
                    self.paintGraph(subgraph, painter)
                else:
                    subgraph = node
                    self.paintSubgraph(subgraph, painter, pen, brush)

    def paintEvent(self, event):
        painter = QPainter(self) 
        painter.setFont(self.engine.font)
        self.paintGraph(self.engine.graph,painter)
        if( self.manipulation_mode==QGraphVizManipulationMode.Edges_Connect_Mode and 
            self.mouse_down and 
            self.selected_Node is not None):
            bkp = painter.pen()
            pen=QPen(Qt.DashLine)
            painter.setPen(pen)
            painter.drawLine(self.selected_Node.pos[0], self.selected_Node.pos[1],
                             self.current_pos[0],self.current_pos[1])
            painter.setPen(bkp)
        painter.end()

    def new(self, engine):
        """
        Creates a new engine
        :param engine: An engine object (for example a Dot engine)
        """
        self.engine=engine

    def addNode(self, graph, node_name, **kwargs):
        """
        Adds a node to a graph or subgraph
        """
        node = Node(node_name, graph, **kwargs)
        graph.nodes.append(node)
        return node

    def addEdge(self, source, dest, kwargs):
        """
        Connects two nodes from the same subgraph or 
        from two different subgraphs
        If source and dest nodes belong to the same
        Subgraph, the connection added to the subgraph
        if the connection is between different subgraph notes
        the connection is added to the main subgraph 
        """
        edge = Edge(source, dest)
        edge.kwargs=kwargs
        if(source.parent_graph == dest.parent_graph):
            source.parent_graph.edges.append(edge)
        else:
            self.engine.graph.edges.append(edge)
        
        return edge

    def addSubgraph(self, parent_graph, subgraph_name, subgraph_type= GraphType.SimpleGraph, **kwargs):
        subgraph = Graph(subgraph_name,subgraph_type, parent_graph, **kwargs)
        subgraph.name = subgraph_name
        subgraph.parent_graph = parent_graph
        parent_graph.nodes.append(subgraph)
        return subgraph

    def removeNode(self, node):
        graph = node.parent_graph
        if(node in graph.nodes):
            idx = graph.nodes.index(node)
            node = graph.nodes[idx]
            if(self.node_removed_callback is not None):
                self.node_removed_callback(node)
            for edge in node.in_edges:
                del edge.source.out_edges[edge.source.out_edges.index(edge)]
                if edge.source.parent_graph == edge.dest.parent_graph:
                    del edge.source.parent_graph.edges[edge.source.parent_graph.edges.index(edge)]
                else:
                    del self.engine.graph.edges[self.engine.graph.edges.index(edge)]

            for edge in node.out_edges:
                del edge.source.out_edges[edge.source.out_edges.index(edge)]
                if edge.source.parent_graph == edge.dest.parent_graph:
                    del edge.source.parent_graph.edges[edge.source.parent_graph.edges.index(edge)]
                else:
                    del self.engine.graph.edges[self.engine.graph.edges.index(edge)]
            del graph.nodes[idx]
            self.repaint()

    def removeSubgraph(self, subgraph):
        graph = subgraph.parent_graph
        if(subgraph in graph.subgraphs):
            idx = graph.subgraphs.index(subgraph)
            subgraph = graph.subgraphs[idx]
            if(self.node_removed_callback is not None):
                self.node_removed_callback(subgraph)
            del graph.subgraphs[idx]
            self.repaint()

    def removeEdge(self, edge):
        if(edge in self.engine.graph.edges):
            source = edge.source
            dest = edge.dest
            if(self.edge_removed_callback is not None):
                self.edge_removed_callback(edge)

            idx = source.out_edges.index(edge)
            del source.out_edges[idx]

            idx = dest.in_edges.index(edge)
            del dest.in_edges[idx]

            if edge.source.parent_graph == edge.dest.parent_graph:
                del edge.source.parent_graph.edges[edge.source.parent_graph.edges.index(edge)]
            else:
                del self.engine.graph.edges[self.engine.graph.edges.index(edge)]

            self.repaint()

    def findSubNode(self, graph, x, y):
        for node in graph.nodes:
            gpos=node.global_pos
            if(
                type(node)==Graph and
                gpos[0]-node.size[0]/2<x and gpos[0]+node.size[0]/2>x and
                gpos[1]-node.size[1]/2<y and gpos[1]+node.size[1]/2>y

            ):
                return node
        return None

    def isNodeHovered(self, n, x, y):
        gpos=n.global_pos
        if(
            gpos[0]-n.size[0]/2<x and gpos[0]+n.size[0]/2>x and
            gpos[1]-n.size[1]/2<y and gpos[1]+n.size[1]/2>y
        ):
            return True
        else:
            return False

    def isEdgeHovered(self, graph, i, e, x, y):
        nb_next=0
        for j in range(i, len(graph.edges)):
            if(graph.edges[j].source==e.source and graph.edges[j].dest==e.dest):
                nb_next+=1

        offset=[0,0]
        if(nb_next%2==1):
            offset[0]=20*(nb_next/2)
        else:
            offset[0]=-20*(nb_next/2)

        sx=e.source.pos[0] if e.source.pos[0]< e.dest.pos[0] else e.dest.pos[0]
        sy=e.source.pos[1] if e.source.pos[1]< e.dest.pos[1] else e.dest.pos[1]

        ex=e.source.pos[0] if e.source.pos[0]> e.dest.pos[0] else e.dest.pos[0]
        ey=e.source.pos[1] if e.source.pos[1]> e.dest.pos[1] else e.dest.pos[1]

        sx += +offset[0]
        ex += +offset[0]

        if(x>sx-self.min_cursor_edge_dist and x<ex+self.min_cursor_edge_dist and
            y>sy-self.min_cursor_edge_dist and y<ey+self.min_cursor_edge_dist):
            x2 = x-sx
            y2 = y-sy 
            dx = (ex-sx)
            dy = (ey-sy)
            if(dx == 0):
                if(abs(x2)<self.min_cursor_edge_dist):
                    return True
            elif(dy == 0):
                if(abs(y2)<self.min_cursor_edge_dist):
                    return True
            else:
                a = -dy/dx
                if(abs(a*x2+y2)/math.sqrt(a**2)<self.min_cursor_edge_dist):
                    return True
        return False
                    
    def findNode(self, graph, x, y):
        for n in graph.nodes:
            if(self.isNodeHovered(n, x, y)):
                return n
        return None

    def findEdge(self, graph, x, y):
        for i,e in enumerate(graph.edges):
            if(self.isEdgeHovered(graph, i, e, x, y)):
                return e,i
        return None,0

    def load_file(self, filename):
        self.engine.graph = self.parser.parseFile(filename)
        self.build()
        self.update()

    def loadAJson(self, filename):
        self.engine.graph = self.parser.fromJSON(filename)
        self.build()
        self.update()

    def save(self, filename):
        self.parser.save(filename, self.engine.graph)

    def saveAsJson(self, filename):
        self.parser.toJSON(filename, self.engine.graph)


    def mouseDoubleClickEvent(self, event):
        x = event.x()
        y = event.y()
        n = self.findNode(self.engine.graph, x,y)
        if n is not None:
            if(self.node_invoked_callback is not None):
                self.node_invoked_callback(n)
        else:
            e,_ = self.findEdge(self.engine.graph, x, y)
            if e is not None:
                if(self.edge_invoked_callback is not None):
                    self.edge_invoked_callback(e)

        QWidget.mouseDoubleClickEvent(self, event)
        self.leaveEvent()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            x = event.x()
            y = event.y()
            self.current_pos = [x,y]
            self.mouse_down=True
            n = self.findNode(self.engine.graph, x, y)
            self.selected_Node = n 

            if(n is None):
                n = self.findSubNode(self.engine.graph, x,y)
                self.selected_Node = n                

        QWidget.mousePressEvent(self, event)

    def leaveEvent(self, event=None):
        """
        Used to reset some parameters when the mouse leaves the QWidget
        """
        self.selected_Node=None

        self.mouse_down=False

        if(self.hovered_Node is not None):
            self.hovered_Node.kwargs["width"] = self.hovered_Node_Back_width
            self.hovered_Node = None
        
        if(self.hovered_Edge is not None):
            self.hovered_Edge.kwargs["width"] = self.hovered_Edge_Back_width
            self.hovered_Edge = None

        self.update()
        if(event!=None):
            event.accept()
        

    def mouseMoveEvent(self, event):
        if self.selected_Node is not None and self.mouse_down:
            x = event.x()
            y = event.y()
            if(self.manipulation_mode==QGraphVizManipulationMode.Nodes_Move_Mode):
                self.selected_Node.pos[0] += x-self.current_pos[0]
                self.selected_Node.pos[1] += y-self.current_pos[1]

            self.current_pos = [x,y]
            self.repaint()
        else:
            x = event.x()
            y = event.y()
            if(self.hilight_Nodes):
                if(self.hovered_Node is None):
                    self.hovered_Node = self.findNode(self.engine.graph, x, y)
                    if(self.hovered_Node is not None):
                        if "width" in list(self.hovered_Node.kwargs.keys()):
                            self.hovered_Node_Back_width=self.hovered_Node.kwargs["width"]
                        else:
                            self.hovered_Node_Back_width=1
                        self.hovered_Node.kwargs["width"] = self.hovered_Node_Back_width+3
                        self.update()
                else:
                    if not(self.isNodeHovered(self.hovered_Node, x, y)):
                        self.hovered_Node.kwargs["width"] = self.hovered_Node_Back_width
                        self.hovered_Node = None
                        self.update()
            if(self.hilight_Edges):
                if(self.hovered_Edge is None):
                    self.hovered_Edge, self.hovered_Edge_id = self.findEdge(self.engine.graph, x, y)
                    if(self.hovered_Edge is not None):
                        if "width" in list(self.hovered_Edge.kwargs.keys()):
                            self.hovered_Edge_Back_width=self.hovered_Edge.kwargs["width"]
                        else:
                            self.hovered_Edge_Back_width=1
                        self.hovered_Edge.kwargs["width"] = self.hovered_Edge_Back_width+3
                        self.update()
                else:
                    if not(self.isEdgeHovered(self.engine.graph, self.hovered_Edge_id, self.hovered_Edge, x, y)):
                        self.hovered_Edge.kwargs["width"] = self.hovered_Edge_Back_width
                        self.hovered_Edge = None
                        self.update()

        QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        x = event.x()
        y = event.y()
        n = self.findNode(self.engine.graph, x, y)   
        if n is None:
            s = self.findSubNode(self.engine.graph, x,y)     
        if n is None:
            e, _ = self.findEdge(self.engine.graph, x,y)        
        else:
            e = None
        # Manipulating nodes
        if(self.manipulation_mode==QGraphVizManipulationMode.Nodes_Move_Mode):
            if self.selected_Node is not None and self.mouse_down:
                selected_Node = self.selected_Node
                s = self.findSubNode(self.engine.graph, x,y)
                if(s is not None and s!=selected_Node):
                    if(type(selected_Node)==Node):
                        del selected_Node.parent_graph.nodes[selected_Node.parent_graph.nodes.index(selected_Node)]
                        s.nodes.append(selected_Node)
                        selected_Node.parent_graph = s
                        self.build()
                        self.repaint()
                    if(type(selected_Node)==Graph):
                        del selected_Node.parent_graph.nodes[selected_Node.parent_graph.nodes.index(selected_Node)]
                        s.nodes.append(selected_Node)
                        selected_Node.parent_graph = s
                        self.build()
                        self.repaint()

        # Connecting edges
        if(self.manipulation_mode==QGraphVizManipulationMode.Edges_Connect_Mode):
            if self.selected_Node is not None and self.mouse_down:
                selected_Node = self.selected_Node
                d = n if n is not None else s
                if(d!=selected_Node and d is not None):
                    add_the_edge=True
                    if(self.new_edge_beingAdded_callback is not None):
                        add_the_edge, kwargs=self.new_edge_beingAdded_callback(selected_Node, d)
                    else:
                        kwargs={}
                    if add_the_edge:
                        edge = self.addEdge(selected_Node, d, kwargs)
                        if(add_the_edge):
                            if(self.new_edge_created_callback is not None):
                                self.new_edge_created_callback(edge)
                        self.build()
                self.selected_Node=None
        # Removing node
        elif(self.manipulation_mode==QGraphVizManipulationMode.Node_remove_Mode):
            if(n is not None):
                self.removeNode(n)
                self.build()
                self.repaint()

        #Removing edge
        elif(self.manipulation_mode==QGraphVizManipulationMode.Edge_remove_Mode):
            if(e is not None):
                self.removeEdge(e)
                self.build()
                self.repaint()
        # Remiving Subgraph
        elif(self.manipulation_mode==QGraphVizManipulationMode.Subgraph_remove_Mode):
            if(s is not None):
                self.removeSubgraph(s)
                self.build()
                self.repaint()

        # Inform application
        if(n is not None):
            if(self.node_selected_callback is not None):
                self.node_selected_callback(n)

        if( e is not None):
            if(self.edge_selected_callback is not None):
                self.edge_selected_callback(e)

        QWidget.mouseReleaseEvent(self, event)
        self.mouse_down=False
        self.repaint()

        
