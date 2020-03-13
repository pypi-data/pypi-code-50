import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from hic3defdr import HiC3DeFDR
from hic3defdr.lowess import lowess_fit


def main():
    # load data
    h = HiC3DeFDR.load('output-fast')
    ys = h.load_data('disp_per_dist')[:, 0]
    old_fn = h.load_disp_fn('ES')

    # weighted lowess, depends on xs, ys, and window size w
    n = len(ys)
    xs = np.arange(n)
    idx = np.isfinite(ys)
    w = 20

    # compute rolling var
    var = np.zeros_like(ys)
    var[idx] = pd.Series(ys[idx]).rolling(window=w, center=True).var()

    # convert to precision
    prec = 1 / var

    # scale to make smallest precision 1
    min_prec = np.nanmin(prec)
    scaled_prec = prec * (1 / min_prec)

    # fill left and right side nan's
    # get the first non-nan precision (for filling left side)
    max_prec = scaled_prec[np.argmax(np.isfinite(scaled_prec))]
    max_fill_idx = np.isnan(scaled_prec) & (xs < n/2)
    min_fill_idx = np.isnan(scaled_prec) & (xs > n/2)
    scaled_prec[max_fill_idx] = max_prec
    # fill right side with 1s
    scaled_prec[min_fill_idx] = 1

    # floor and convert to int
    floored_prec = np.floor(scaled_prec).astype(int)

    # print the sum of the weights - needs to be reasonably small
    print(np.nansum(floored_prec))

    # create duplicated data
    expanded_xs = []
    expanded_ys = []
    for i in range(n):
        m = floored_prec[i]
        if not np.isfinite(m):
            continue
        expanded_xs.extend([xs[i]] * m)
        expanded_ys.extend([ys[i]] * m)

    # lowess fit duplicated data
    fn = lowess_fit(np.array(expanded_xs), np.array(expanded_ys), frac=0.2)

    # plots
    ax = plt.gca()
    ax2 = ax.twinx()
    ax.scatter(xs[idx], ys[idx], label='raw dispersion', color='C0')
    ax.plot(xs[idx], fn(xs[idx]), label='smoothed dispersion', color='C1', linewidth=3)
    ax2.plot(xs[idx], floored_prec[idx], label='precision', color='C2')
    ax.set_xlabel('distance')
    ax.set_ylabel('dispersion')
    ax2.set_ylabel('precision')
    ax.legend()
    plt.savefig('var_test.png')

    ax.plot(xs[idx], old_fn(xs[idx]), label='old dispersion', color='C3', linewidth=3)
    ax.set_xlim((0, 35))
    ax.set_ylim((0, 0.01))
    ax.legend()
    plt.savefig('var_test_zoomed.png')


if __name__ == '__main__':
    main()
