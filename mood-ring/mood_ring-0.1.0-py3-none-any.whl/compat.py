"""Adding backwards compatibility for python3.5 - Adding the random choices method"""

import bisect
import itertools
import random


def choices(population, weights=None, *, cum_weights=None, k=1):
    """Return a k sized list of population elements chosen with replacement.

    If the relative weights or cumulative weights are not specified,
    the selections are made with equal probability.

    """
    random_random = random.random
    if cum_weights is None:
        if weights is None:
            _int = int
            total = len(population)
            return [population[_int(random_random() * total)] for i in range(k)]
        cum_weights = list(itertools.accumulate(weights))
    elif weights is not None:
        raise TypeError('Cannot specify both weights and cumulative weights')
    if len(cum_weights) != len(population):
        raise ValueError('The number of weights does not match the population')
    bisect_bisect = bisect.bisect
    total = cum_weights[-1]
    return [population[bisect_bisect(cum_weights, random_random() * total)] for i in range(k)]
