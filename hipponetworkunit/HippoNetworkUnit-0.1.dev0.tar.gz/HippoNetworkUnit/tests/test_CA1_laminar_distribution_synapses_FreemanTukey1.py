import sciunit

import sciunit.scores
import HippoNetworkUnit.scores as hpn_scores
import HippoNetworkUnit.capabilities as hpn_cap

import quantities
import os

# For data manipulation
import numpy as np
import pandas as pd

# Force matplotlib to not use any Xwindows backend.
import matplotlib
# matplotlib.use('Agg')
from matplotlib import pyplot as plt
import seaborn as sns


# ==============================================================================
score_str = 'FreemanTukey1Score'
"""An approach closely related to Cressie-Read power divergence method implemented in scipy.stats is used here.
Accordingly, this test is invalid when the predicted and observed outcomes (number of boutons) in each
layer are too small. A typical rule is that all of those outcome values should be at least 5.
It is also possible that the asymptotic distribution is not a chisquare, in which case this test is not appropriate.
(comment addapted from the one in 'power_divergence' method of scipy.stats"""

class CA1_laminar_distribution_synapses_FreemanTukey1Test(sciunit.Test):
    """Tests a synapses distribution of different m-types (AA, BP, BS, CCKBC, Ivy, OLM, PC, PPA, SCA, Tri)
       across the layers of Hippocampus CA1 (SO, SP, SR, SLM)"""

    score_type = eval('hpn_scores.' + score_str)

    def __init__(self, observation={}, name="CA1 laminar_distribution_synapses Test"):

        description = "Tests the synapses distribution of different m-types across the Hippocampus CA1 layers"
        require_capabilities = (hpn_cap.Provides_CA1_laminar_distribution_synapses_info,)

        self.units = quantities.dimensionless
        self.figures = []
        observation = self.format_data(observation)
        sciunit.Test.__init__(self, observation, name)
        self.directory_output = './output/'

    # ----------------------------------------------------------------------

    def format_data(self, data):
        """
        This accepts data input in the form:
        ***** (observation) *****
        {   "AA":{
                "SO": {"mean": "X0"},
                "SP": {"mean": "X1"},
                "SR": {"mean": "X2"},
                "SLM":{"mean": "X3"}
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
        ***** (prediction) *****
        {   "AA":{
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
        Returns a new dictionary of the form
        { "AA":[X0, X1, X2, X3, X4], "BP":[...] , "BS":[...], "CCKBC":[...], "Ivy":[...], "OLM":[...],
        "PC":[...], "PPA":[...], "SCA":[...], "Tri":[...] }
        """

        data_new_dict = dict()
        for key0, dict0 in data.items():  # dict0: a dictionary containing the synapses fraction in each of the
                                    # Hippocampus CA1 layers (SO, SP, SR, SLM) and OUT (for prediction data only)
                                    # for each m-type cell (AA, BP, BS, CCKBC, Ivy, OLM, PC, PPA, SCA, Tri)
            data_list_1 = list()
            for dict1 in dict0.values():  # dict1: a dictionary of the form
                                        # {"mean": "X0"} (observation) or {"value": "X"} (prediction)
                try:
                    synapses_fraction = float(dict1.values()[0])
                    assert(synapses_fraction <= 1.0)
                    data_list_1.extend([synapses_fraction])
                except:
                    raise sciunit.Error("Values not in appropriate format. Synapses fraction of an m-type cell"
                                        "must be dimensionless and not larger than 1.0")

            if "out" not in [x.lower() for x in dict0.keys()]: data_list_1.extend([0.0])  # observation data
            data_list_1_q = quantities.Quantity(data_list_1, self.units)
            data_new_dict[key0] = data_list_1_q

        return data_new_dict

    # ----------------------------------------------------------------------

    def validate_observation(self, observation):

        for val in observation.values():  # val0: a list with synapses fraction in each of the
                                            # Hippocampus CA1 layers (SO, SP, SR, SLM) and OUT (=0.0 by default)
                                            # for each m-type cell (AA, BP, BS, CCKBC, Ivy, OLM, PC, PPA, SCA, Tri)
            assert type(val) is quantities.Quantity, \
                sciunit.ObservationError("Observation about synapses fraction in each CA1-layer"
                                         "must be of the form {'mean': XX}")

    # ----------------------------------------------------------------------

    def generate_prediction(self, model, verbose=False):
        """Implementation of sciunit.Test.generate_prediction"""

        self.model_name = model.name
        prediction = model.get_CA1_laminar_distribution_synapses_info()
        prediction = self.format_data(prediction)

        return prediction

    # ----------------------------------------------------------------------

    def compute_score(self, observation, prediction, verbose=True):
        """Implementation of sciunit.Test.score_prediction"""

        assert len(observation) == len(prediction), \
            sciunit.InvalidScoreError(("Difference in # of m-type cells. Cannot continue test"
                                        "for laminar distribution of synapses across CA1 layers"))

        # print "observation = ", observation, "\n"
        # print "prediction = ", prediction, "\n"

        # Computing the score
        scores_cell = dict.fromkeys(observation.keys(),[])
        for key0 in scores_cell.keys():  # m-type cell (AA, BP, BS, CCKBC, Ivy, OLM, PC, PPA, SCA, Tri)
            scores_cell[key0] = getattr(hpn_scores, score_str).compute(observation[key0], prediction[key0])

        # create output directory
        path_test_output = self.directory_output + self.model_name + '/'
        if not os.path.exists(path_test_output):
            os.makedirs(path_test_output)

        # save figure with score data
        scores_cell_floats = dict.fromkeys(observation.keys(), [])
        for key0, score_cell in scores_cell.items():
            scores_cell_floats[key0] = [score_cell.score.statistic_n, score_cell.score.pvalue]

        score_label = score_str[:-5] + '-score'
        scores_cell_df = pd.DataFrame(scores_cell_floats, index=[score_label, 'p-value'])
        scores_cell_df = scores_cell_df.transpose()
        print scores_cell_df, '\n'

        # pal = sns.cubehelix_palette(len(observation))
        pal = sns.color_palette('Reds', len(observation))
        rank = [int(value)-1 for value in scores_cell_df[score_label].rank()]
        axis_obj = sns.barplot(x=scores_cell_df[score_label], y=scores_cell_df.index, palette=np.array(pal)[rank])
        axis_obj.set(xlabel=score_label, ylabel='Cell')
        sns.despine()

        for i, p in enumerate(axis_obj.patches):
                axis_obj.annotate("p = %.2f" % scores_cell_df['p-value'].values[i],
                xy=(p.get_x() + p.get_width(), p.get_y() + 0.5),
                xytext=(3, 0), textcoords='offset points')

        filename = path_test_output + score_str + '_plot' + '.png'
        plt.savefig(filename, dpi=600,)
        self.figures.append(filename)

        scores_array = scores_cell_df[score_label].array
        self.score = sum(map(abs,scores_array)) / len(scores_array)

        return hpn_scores.FreemanTukey1Score(self.score)

    # ----------------------------------------------------------------------

    def bind_score(self, score, model, observation, prediction):
        score.related_data["figures"] = self.figures
        return score
