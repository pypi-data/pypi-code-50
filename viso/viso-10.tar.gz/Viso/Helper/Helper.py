import numpy as np
import math

def quartiles(d):
    data = np.array(d).astype(float)
    return [np.quantile(data, .25), np.quantile(data, .5), np.quantile(data, .75)]


def whiskers(d, q, Settings):
    iqr = (q[2] - q[0]) * Settings.boxIQR
    i = 0
    j = len(d) - 1

    while d[i] < q[0] - iqr:
        i += 1
    while d[j] > q[2] + iqr:
        j -= 1

    return [d[i], d[j]]


def outliers(d, w):
    o = [a < w[0] or a > w[1] for a in d]
    r = []
    for i in range(len(o)):
        if o[i] != (-math.inf if i == 0 else o[i - 1]):
            r.append(o[i])
    return r
