import sciunit
import sciunit.utils as utils
import quantities as pq

import numpy as np
from scipy.stats import power_divergence
from collections import namedtuple

PearsonResult = namedtuple('PearsonResult', ('statistic_n', 'pvalue'))
class PearsonChiSquaredScore(sciunit.Score):
    """
    A Pearson score. A float giving the result of
    a Pearson's chi-squared goodness-of-fit test
    """

    _allowed_types = (float,tuple,)

    _description = ('A Pearson score. A float giving the result'
                    'of a Pearson''s chi-squared goodness-of-fit test')

    @classmethod
    def compute(cls, observation, prediction):
        """
        Computes a Pearson's chi-squared score from an observation and a prediction.
        """

        obs_values = observation[~np.isnan(observation)]
        pred_values = prediction[~np.isnan(prediction)]

        assert(all(x<=1.00 for x in obs_values) and all(x<=1.00 for x in pred_values)), \
            "Probabiltity values should not be larger than 1.0"

        obs_values *= 100
        pred_values *= 100

        if type(obs_values) is pq.quantity.Quantity:
            obs_values = obs_values.magnitude
        if type(pred_values) is pq.quantity.Quantity:
            pred_values = pred_values.magnitude

        Pearson_Result = power_divergence(f_obs=obs_values, f_exp=pred_values, lambda_='pearson')

        utils.assert_dimensionless(Pearson_Result.statistic)
        utils.assert_dimensionless(Pearson_Result.pvalue)

        # Obtaining a score value normalized respect to the mean and std of the Chi-squared distribution
        dof = len(obs_values)-1  # degrees of freedom for the Chi-squared distribution
        stat = Pearson_Result.statistic
        chisq_mean = dof
        chisq_std = np.sqrt(2*dof)
        stat_n = abs(stat-chisq_mean)/chisq_std
        Pearson_result = PearsonResult(stat_n, Pearson_Result.pvalue)

        return PearsonChiSquaredScore(Pearson_result)

    @property
    def sort_key(self):
        return self.score

    def __str__(self):
        return 'Pearson''s chi-squared-score = %.5f' % self.score.statistic_n
