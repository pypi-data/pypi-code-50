from typing import Any, Optional, List, Mapping, Tuple

import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

from .utils import add_identity, get_circle_coordinates


def annotate_correlation(
    x: pd.Series, y: pd.Series,
    method: str,
    hue_positions: Optional[Mapping[str, Tuple[float, float]]] = None,
    **kwargs: Any
) -> None:
    """Plot correlation.

    Adapted from https://github.com/mwaskom/seaborn/issues/1444
    """
    # compute correlation
    corr_r = x.corr(y, method)
    corr_text = f'{corr_r:2.2f}'.replace('0.', '.')

    # visualize correlation
    ax = plt.gca()
    ax.set_axis_off()

    hue_color = kwargs.pop('color', 'face')
    x_jitter, y_jitter = hue_positions.get(kwargs.get('label'), (0, 0)) if hue_positions is not None else (0, 0)

    marker_size = abs(corr_r) * 10000  # TODO: points might overlap
    ax.scatter(
        [.5 + x_jitter], [.5 + y_jitter], marker_size, [corr_r], alpha=0.6,
        linewidths=[4], edgecolors=[hue_color],
        cmap='vlag_r', vmin=-1, vmax=1,  # bwr_r
        transform=ax.transAxes)

    ax.annotate(
        corr_text,
        [.5 + x_jitter, .5 + y_jitter], xycoords='axes fraction',
        ha='center', va='center', fontsize=20)


def custom_distplot(x, **kwargs):
    """Automatically remove NaN values."""
    sns.distplot(pd.Series(x).dropna(), **kwargs)
    # print(pd.Series(x).dropna())
    # sns.distplot(pd.Series(x).dropna(), **kwargs)
    # plt.hist(x, **kwargs)


def custom_scatterplot(*args, **kwargs):
    """Enhance default scatterplot with identity line."""
    ax = sns.scatterplot(*args, **kwargs)  # regplot
    add_identity(ax, color='grey', ls='--', alpha=.5)


def corrplot(
    df: pd.DataFrame,
    corr_method: str = 'spearman',
    upper_kws: Mapping[str, Any] = None,
    diag_kws: Mapping[str, Any] = None,
    lower_kws: Mapping[str, Any] = None,
    **kwargs: Any
) -> sns.PairGrid:
    """Implement an improved version of `sns.pairplot`."""
    # setup
    upper_kws = upper_kws or {}
    diag_kws = diag_kws or {}
    lower_kws = lower_kws or {}

    # plotting
    g = sns.PairGrid(df, **kwargs)

    hue_positions = None
    if 'hue' in kwargs:
        hue_list = df[kwargs['hue']].unique()
        hue_positions = {hue: coords
                         for hue, coords in zip(
                             hue_list,
                             get_circle_coordinates(0, 0, .25, len(hue_list))
                         )}

    g.map_upper(
        annotate_correlation,
        method=corr_method, hue_positions=hue_positions,
        **upper_kws)
    g.map_diag(custom_distplot, **diag_kws)
    g.map_lower(custom_scatterplot, **lower_kws)

    return g


if __name__ == '__main__':
    import numpy as np
    import pandas as pd

    # generate data
    np.random.seed(1)

    N = 200
    xs = np.sort(np.random.normal(size=N))

    df = pd.DataFrame({
        'A': xs,
        'B': np.random.normal(size=N),
        'C': xs + np.random.normal(0.01, size=N),
        'D': xs[::-1] + np.random.normal(0.01, size=N),
        'group': ['G1'] * (N//2) + ['G2'] * (N//2)
    })
    print(df.head())

    # plot
    corrplot(df, hue='group')
    plt.show()
