import sys
from collections import OrderedDict

# Get access to the running scripts variables
module_globals = sys.modules['__main__'].__dict__

class BaseItem(object):
    """ Defines a base item, eg: a Component in a Component Diagram """
    def __init__(self,  label, **attrs):
        self.owner = None
        self.label = label
        self.attrs = attrs
        self.id = None

    def __repr__(self):
        return 'BaseItem.label = "{}"'.format(self.label)

    @property
    def Diagram(self):
        if self.owner:
            return self.owner.diagram
        else:
            raise ValueError, '%s has no owner' % (self.__repr__())

    @property
    def Helper(self):
        return self.Diagram.helper


class BaseItemCollection(object):
    """ Represents an Object that owns base items, eg: a Diagram """
    def __init__(self, diagram):
        self.collection = OrderedDict()
        self.diagram = diagram

    def add_item(self, i):
        """ Add BaseItem i to the collection """
        i.owner = self
        self.collection[hash(i)] = i
        return i

    def add_new_item(self, itemType, label, **attrs):
        i = itemType(self, label, **attrs)
        return self.add_item(i)

    def items(self):
        return [(k,v) for (k,v) in module_globals.items() if (isinstance(v, BaseItem))]
        
    def values(self):
        for v in self.collection.values():
            yield v

    def set_ids(self):
        #print 'set_ids()'
        for (k,v) in self.items():
            #print k,v.label
            v.id = k

    def get_first_item(self):
        return self.collection.values()[0]