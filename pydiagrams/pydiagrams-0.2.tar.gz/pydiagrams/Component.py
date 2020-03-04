# Component diagram

# Standard python libraries
from contextlib import contextmanager #required for the cond function

# Local python libraries
#from Diagram import DiagramBase, Item, Context
import pydiagrams.Diagram
from pydiagrams.helpers.PUML import Helper

from helpers.constants import *

##########################################################################
# Constants

# component shape keys
Component = 'Component'
Interface = 'Interface'


# group shapes
Cloud = 'Cloud'
Database = 'Database'
Folder = 'Folder'
Frame = 'Frame'
Node = 'Node'
Package = 'Package'
Rectangle = 'Rectangle'

##########################################################################
# Item Classes

class ComponentDiagramItem(Diagram.Item):
    """ Base class for all Items in a component Diagram """
    def __init__(self, label, shape, **attrs):
        Diagram.Item.__init__(self, label, **attrs)
        self.attrs['shape'] = shape


    # Override operators

    # >>  ==  vertical link
    def __rshift__(self, i2):
        """ Override the >> operator to mean to add an edge between this item and the i2 """
        return self.link_edge(i2, 'vertical')

    # ^  == up link
    def __xor__(self, i2):
        """ Override the ^ operator to mean to add an 'up' edge """
        return self.link_edge(i2, 'up')

    # | == down link
    def __or__(self, i2):
        """ Override the ^ operator to mean to add an 'up' edge """
        return self.link_edge(i2, 'down')

    # >= == right link
    def __ge__(self, i2):
        """ Override the >= operator to mean to add an 'right' edge """
        return self.link_edge(i2, 'right')

    # <= == left link
    def __le__(self, i2):
        """ Override the <= operator to mean to add an 'left' edge """
        return self.link_edge(i2, 'left')

    # -  == horizontal line
    def __sub__(self, i2):
        """ Override the - operator to add a horizontal line """
        return self.link_edge(i2, 'hline')

    # =  == vertical line
    def __eq__(self, i2):
        return self.link_edge(i2, 'vline')

    # >>=  == vertical dotted arrow
    def __irshift__(self, i2):
        return self.link_edge(i2,'vdotted')

##########################################################################
# Diagram Classes
class ComponentDiagram(Diagram.DiagramBase):
    def __init__(self, helper, filename=None, **attrs):
        Diagram.DiagramBase.__init__(self, helper, filename, **attrs)


    def Group(self, shape, label, **attrs):
        g=ComponentSubDiagram(parent=self, id=None, shape=shape, label=label, **attrs)
        self.collection.add_item(g)
        return g
    
    def add_new_item(self, shape, label, **kwargs):
        #kwargs.update({'shape':shape})
        #return self.collection.add_new_item(Item, label, **kwargs)
        i = ComponentDiagramItem(label, shape, **kwargs)
        return self.collection.add_item(i)

    # Item functions: Component, Interface, Actor
    def Component(self, label, **attrs):
        return self.add_new_item(Component, label, **attrs)

    def Interface(self, label, **attrs):
        return self.add_new_item(Interface, label, **attrs)

    def Actor(self, label, **attrs):
        return self.add_new_item('actor', label, **attrs)

    # Group functions: Cloud, Database, Folder, Frame, Node, Package
    def Cloud(self, label=None, **attrs):
        return self.Group(Cloud, label, **attrs)

    def Database(self, label=None, **attrs):
        return self.Group(Database, label, **attrs)

    def Folder(self, label=None, **attrs):
        return self.Group(Folder, label, **attrs)

    def Frame(self, label=None, **attrs):
        return self.Group(Frame, label, **attrs)

    def Node(self, label=None, **attrs):
        return self.Group(Node, label, **attrs)

    def Package(self, label=None, **attrs):
        return self.Group(Package, label, **attrs)

    def Rectangle(self, label=None, **attrs):
        return self.Group(Rectangle, label, **attrs)

#-------------------------------------------------------------------------
class ComponentSubDiagram(ComponentDiagram, Diagram.Item):
    def __init__(self, parent, id, shape, label, **attrs):
        ComponentDiagram.__init__(self, helper=parent.helper, **attrs)
        Diagram.Item.__init__(self, label, **attrs)
        self.attrs['shape'] = shape

        self.parent = parent
        self.id = id
        self.level = self.parent.level + 1

        self.node_attrs = parent.node_attrs.copy()
        self.edge_attrs = parent.edge_attrs.copy()

        # Denotes that this is to be treated as a group
        self.is_group = False

    # Renders this diagram
    def __str__(self):
        if self.is_group:
            a = self.helper.startSubdiagram(self.id, self.label, **self.attrs)
            a += '\n'.join([str(v) for v in self.collection.values()])
            a += self.helper.endSubdiagram(self.id, self.label, **self.attrs)
            return a
        else:
            return Diagram.Item.__str__(self)

    def __enter__(self):
        self.is_group = True
        #print 'subdiagram entered',self.id,self.label
        return self

    def __exit__(*args):
        pass        

##########################################################################
# Context Classes
class ComponentContextPUML(Diagram.Context):
    def __init__(self, filename=None):
        print 'Generating:',filename
        self.diagram = ComponentDiagram(Helper, filename)

class ComponentContext(Diagram.Context):
    def __init__(self, helper, filename=None):
        print 'Generating:',filename
        self.diagram = ComponentDiagram(helper, filename)
