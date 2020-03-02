"""
_utilities.py
=============
written in Python3

author: C. Lockhart

This file exists because all models require some utilities. These utility functions need to be housed in a neutral
location to prevent circular imports.
"""

from izzy.misc import ArrayLike

import numpy as np


# Coerce sample weights
def _coerce_sample_weights(sample_weights, n_samples):
    """
    Coerce sample weights into a suitable form

    Parameters
    ----------
    sample_weights : ArrayLike
        Weight of observations
    n_samples : int
        Number of samples expected

    Returns
    -------
    numpy.ndarray
        Coerced ``sample_weights``
    """

    # If sample weights is None, set to ones
    if sample_weights is None:
        sample_weights = np.ones(n_samples)

    # Return
    return sample_weights


# Coerce y_prob
def _coerce_y_prob(y_prob, assert_binomial=False):
    """
    Coerces ``y_prob`` into a suitable form

    Parameters
    ----------
    y_prob : ArrayLike
        Predicted outcomes expressed as probabilities

    Returns
    -------
    numpy.ndarray
        Coerced ``y_prob``
    """

    # Convert y_prob to numpy array for convenience
    y_prob = np.array(y_prob)

    # If y_prob only has 1 dimensions, assume that this is a binomial problem and coerce it into [1 - y_prob, y_prob]
    if y_prob.ndim == 1:
        Warning('coercing into binomial form [1 - y_prob, y_prob]')
        y_prob = np.vstack([1. - y_prob, y_prob]).T

    # Otherwise if ndim > 2, fail
    elif y_prob.ndim > 2 :
        raise AttributeError('y_prob can be at maximum 2 dimensions')

    # Finally, if assert_binomial is true, we are expecting y_prob to have 2 columns
    if assert_binomial and y_prob.shape[1] != 2:
        raise AttributeError('y_prob expected to be suitable for binomial classification')

    # Return y_prob
    return y_prob
