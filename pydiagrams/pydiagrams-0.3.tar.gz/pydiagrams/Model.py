import pydiagrams.baseItems as bi

class Item(bi.BaseItem):
    @property 
    def Id(self):
        if self.id:
            return self.id
        else:
            return self.label.replace(' ', '_')

    @Id.setter
    def Id(self, value):
        self.id = value

# Model
class Model(bi.BaseItemCollection):
    pass

class Context():
    """ Represents a general data model. Implements as a context """
    def __init__(self, model):
        self.model = model

    def __enter__(self):
        return self.model

    def __exit__(self, *args):
        self.model.set_ids()
