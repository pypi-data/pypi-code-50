"""

@author: maffettone
"""
import numpy as np

def ensure_rng(random_state=None):
    """
    Creates a random number generator based on an optional seed.  This can be
    an integer or another random state for a seeded rng, or None for an
    unseeded rng.
    """
    if random_state is None:
        random_state = np.random.RandomState()
    elif isinstance(random_state, int):
        random_state = np.random.RandomState(random_state)
    else:
        assert isinstance(random_state, np.random.RandomState)
    return random_state


def get_rnd_simplex(dimension, random_state):
    """
    Uniform random point on a simplex, i.e. x_i >= 0 and sum of the coordinates is 1.
    Donald B. Rubin, The Bayesian bootstrap Ann. Statist. 9, 1981, 130-134.
    https://cs.stackexchange.com/questions/3227/uniform-sampling-from-a-simplex

    Parameters
    ----------
    dimension: int
        Dimensionality of the simplex
    random_state: optional, RandomState object

    Returns
    -------
    numpy array corresponding to random sample in dimension of space
    """
    t = random_state.uniform(0, 1, dimension - 1)
    t = np.append(t, [0, 1])
    t.sort()

    return np.array([(t[i + 1] - t[i]) for i in range(len(t) - 1)])
