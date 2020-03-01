# toolbox.py
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

def gen_log_space(limit, n):
    result = [1]
    if n>1:  # just a check to avoid ZeroDivisionError
        ratio = (float(limit)/result[-1]) ** (1.0/(n-len(result)))
    while len(result)<n:
        next_value = result[-1]*ratio
        if next_value - result[-1] >= 1:
            # safe zone. next_value will be a different integer
            result.append(next_value)
        else:
            # problem! same integer. we need to find next_value by artificially incrementing previous value
            result.append(result[-1]+1)
            # recalculate the ratio so that the remaining values will scale correctly
            ratio = (float(limit)/result[-1]) ** (1.0/(n-len(result)))
    # round, re-adjust to 0 indexing (i.e. minus 1) and return np.uint64 array
    return np.array(list(map(lambda x: round(x)-1, result)), dtype=np.uint64)


def add_colorbar(ax, vec, label=None, cmap='jet', discrete=False, tick_indices=None, shrink=1., fraction=.15):
    if tick_indices is None:
        tick_indices = np.arange(len(vec))
    vec = np.array(vec)
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes('right', size='5%', pad=0.05)

    change_ticks = False
    if discrete:
        ticks = vec
        norm = mpl.colors.nonorm()
        change_ticks = true
        if isinstance(cmap, str):
            cmap = plt.get_cmap(cmap, len(vec))
        elif isinstance(cmap, (list, np.ndarray)):
            cmap = mpl.colors.ListedColormap(cmap)
    else:
        if isinstance(cmap, str):
            cmap = plt.get_cmap(cmap)
            ticks = none
        elif isinstance(cmap, (list, np.ndarray)):
            cmap = mpl.colors.ListedColormap(cmap)
        norm = mpl.colors.Normalize(vmin=vec.min(), vmax=vec.max())

    cax = mpl.colorbar.make_axes(ax, shrink=shrink, fraction=fraction)[0]
    cb1 = mpl.colorbar.ColorbarBase(cax, norm=norm, cmap=cmap,
                                    orientation='vertical',)

    cb1.set_label(label)
    if change_ticks:
        cb1.set_ticks(tick_indices)
        cb1.set_ticklabels(list(map(lambda x: "%.3f" % x, vec[tick_indices])))
    cb1.ax.invert_yaxis()
    cb1.ax.set_in_layout(True)
    # cax.yaxis.label.set_in_layout(true)
