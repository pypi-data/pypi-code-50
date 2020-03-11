import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pytest
import seaborn as sbn
import time

from matplotlib.pyplot import Figure, Axes
from numpy import ndarray
from sklearn.cluster import KMeans
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Literal


from empyricalRMT.construct import correlated_eigs, generate_eigs
from empyricalRMT.eigenvalues import Eigenvalues
from empyricalRMT.ensemble import Poisson, GOE
from empyricalRMT.construct import goe_unfolded
from empyricalRMT.correlater import correlate_fast
from empyricalRMT.observables.step import _step_function_fast
from empyricalRMT.plot import _configure_sbn_style
from empyricalRMT.utils import make_parent_directories


def get_eigs(arr: ndarray) -> ndarray:
    print(f"\n{time.strftime('%H:%M:%S (%b%d)')} -- computing eigenvalues...")
    eigs = np.linalg.eigvalsh(arr)
    print(f"\n{time.strftime('%H:%M:%S (%b%d)')} -- computed eigenvalues...")
    return eigs


def test_outlier_find() -> None:
    _configure_sbn_style()
    eigs = correlated_eigs(percent=25)
    steps = np.arange(0, len(eigs))
    weights = None
    fit = np.polyval(np.polyfit(eigs, steps, deg=11, w=weights), eigs)
    fig, axes = plt.subplots()
    axes.scatter(steps, fit)
    axes.plot(steps, steps, color="red", alpha=0.3, linewidth=10)
    plt.show()


def relabel(km: KMeans) -> ndarray:
    k = 0
    labs: Dict[int, str] = {}
    cluster = km.labels_
    for label in cluster:
        if label in labs:
            continue
        labs[label] = f"c{k}"
        k += 1

    # we can just sort cluster means because 1D KMeans / Voronoi
    return (
        np.array(list(map(lambda lab: labs[lab], cluster))),
        np.sort(km.cluster_centers_),
    )


def test_k_means() -> None:
    eigs, eig_min, eig_max = correlated_eigs(90, log=False)
    # eigs = generate_eigs(1000)
    steps = np.arange(1, len(eigs) + 1)
    # init = np.array([eigs.min(), np.median(eigs), eigs.max()]).reshape(-1, 1)
    km = KMeans(n_clusters=11, n_jobs=-1).fit(eigs.reshape(-1, 1))
    cluster, centers = relabel(km)
    df = pd.DataFrame({"eigs": eigs, "steps": steps, "cluster": cluster})
    _configure_sbn_style()
    fig, axes = plt.subplots()
    print(centers)
    sbn.scatterplot(
        data=df, x="steps", y="eigs", hue="cluster", ax=axes, edgecolor=None
    )
    axes.set(title="K-means clusters", ylabel="Eigenvalues")
    axes.legend().set_visible(True)
    plt.show()

