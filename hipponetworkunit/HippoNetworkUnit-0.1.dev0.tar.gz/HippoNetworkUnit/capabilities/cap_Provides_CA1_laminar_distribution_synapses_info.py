import sciunit

#==============================================================================

class Provides_CA1_laminar_distribution_synapses_info(sciunit.Capability):
    """
    Indicates that the model returns structural information, namely:
    the synapses distribution of different digitally reconstructed m-types neurons (AA, BP, BS, CCKBC, Ivy, OLM, PC, PPA, SCA, Tri) 
    across the four layers of CA1 subregion of Hippocampus (SO, SP, SR, SLM) and what is OUT
    """

    def get_CA1_laminar_distribution_synapses_info(self):
        """ Must return a dictionary of the form:
        {
        "AA":{
                "SO": {"value": "X0"},
                "SP": {"value": "X1"},
                "SR": {"value": "X2"},
                "SLM":{"value": "X3"},
                "OUT":{"value": "X4"}
                },
        "BP": {...},
        "BS": {...},
        "CCKBC":{...},
        "Ivy":{...},
        "OLM":{...},
        "PC":{...},
        "PPA":{...},
        "SCA":{...},
        "Tri":{...}
        }
        """
        raise NotImplementedError()

    def get_CA1_laminar_distribution_synapses(self):
        """ Returns a nested dictionary with the synapses distribution of different digitally reconstructed m-types neurons
            (AA, BP, BS, CCKBC, Ivy, OLM, PC, PPA, SCA, Tri)
            across the four layers of CA1 subregion of Hippocampus (SO, SP, SR, SLM) and what is OUT
        """
        CA1_laminar_distribution_synapses_info = self.get_CA1_laminar_distribution_synapses_info()

        return CA1_laminar_distribution_synapses_info

