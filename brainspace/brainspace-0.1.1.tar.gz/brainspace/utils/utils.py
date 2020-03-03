import numpy as np
from scipy.stats import mode
from sklearn.utils.extmath import weighted_mode


def _get_redop(red_op, weights=None, axis=None):
    if red_op in ['mean', 'average']:
        if weights is None:
            def fred(x, w): return np.mean(x, axis=axis)
        else:
            def fred(x, w): return np.average(x, weights=w, axis=axis)
    elif red_op == 'median':
        def fred(x, w): return np.median(x, axis=axis)
    elif red_op == 'mode':
        if weights is None:
            def fred(x, w): return mode(x, axis=axis)[0].ravel()
        else:
            def fred(x, w): return weighted_mode(x, w, axis=axis)
    elif red_op == 'sum':
        def fred(x, w): return np.sum(x if w is None else w * x, axis=axis)
    elif red_op == 'max':
        def fred(x, w): return np.max(x, axis=axis)
    elif red_op == 'min':
        def fred(x, w): return np.min(x, axis=axis)
    else:
        raise ValueError("Unknown reduction operation '{0}'".format(red_op))
    return fred