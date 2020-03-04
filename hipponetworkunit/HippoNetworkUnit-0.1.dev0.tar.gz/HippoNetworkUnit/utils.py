import sciunit
import os
import json


class CA1_laminar_distribution_synapses(sciunit.Model):

    def __init__(self, name="CA1_laminar_distribution_synapses", CA1_laminar_distribution_synapses_model=None):

        sciunit.Model.__init__(self, name=name)
        self.name = name
        self.description = "HBP Hippocampus CA1's output to test synapses distribution across CA1 layers"
        self.CA1_laminar_distribution_synapses_info = CA1_laminar_distribution_synapses_model

    def get_CA1_laminar_distribution_synapses_info(self):
        return self.CA1_laminar_distribution_synapses_info

# ==============================================================================

class CA1Layers_NeuritePathDistance(sciunit.Model):

    def __init__(self, name='CA1Layers_NeuritePathDistance', CA1LayersNeuritePathDistance_info={}):
        self.CA1LayersNeuritePathDistance_info = CA1LayersNeuritePathDistance_info
        sciunit.Model.__init__(self, name=name)
        self.name = name
        self.description = "Dummy model to test neurite path-distances across CA1 layers"
        self.set_CA1LayersNeuritePathDistance_info_default()

    def set_CA1LayersNeuritePathDistance_info_default(self):
        self.CA1LayersNeuritePathDistance_info = {"SLM": {'PathDistance': {'value':'120 um'}},
                                                  "SR": {'PathDistance': {'value':'280 um'}},
                                                  "SP": {'PathDistance': {'value':'40 um'}},
                                                  "SO": {'PathDistance': {'value':'100 um'}}
                                                 }

    def get_CA1LayersNeuritePathDistance_info(self):
        return self.CA1LayersNeuritePathDistance_info
