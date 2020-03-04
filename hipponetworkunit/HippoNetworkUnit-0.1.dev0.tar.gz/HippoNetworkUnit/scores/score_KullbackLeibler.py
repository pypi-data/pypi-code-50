import sciunit
import sciunit.utils as utils
import quantities as pq

import numpy as np
from scipy.stats import entropy

class KLdivScore(sciunit.Score):
    """
    A Kullback-Leibler divergence score. A float giving the Kullback-Leibler divergence (KLdiv),
    a measure indicating how much a predicted (model's) probability distribution P_mod
    diverges from an experimental one (observation's) P_obs. In the simple case, a KLdiv with value of 0
    indicates that almost similar behavior of both probabilities can be expected.
    The contrary holds when the divergence's value is 1.
    """

    _allowed_types = (float,)

    _description = ('The divergence from the probability P_mod to the probability P_obs, being computed '
                    'as the expectation of the logarithmic difference between P_mod and P_obs, '
                    'where the expectation is taken using the probabilities P_obs.')

    @classmethod
    def compute(cls, observation, prediction):
        """
        Computes a KLdiv-score from an observation and a prediction.
        """

        obs_values = observation[~np.isnan(observation)]
        pred_values = prediction[~np.isnan(prediction)]

        value = entropy(pk=obs_values, qk=pred_values)
        value = utils.assert_dimensionless(value)
        return KLdivScore(value)

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return '%.5f' % self.score
