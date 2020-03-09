from simple_plotter.core.advanced_graph import AnnotatedLinePlot
import numpy as np


def func1(x):
    """Test function 1"""

    return x**2


def test_lin_lin():
    """Test x-y axis linear scaling"""

    graph = AnnotatedLinePlot()

    x_vals = np.linspace(-10., 10., 100)
    y_vals = func1(x_vals)

    graph.plot(x_values=x_vals, y_values=y_vals, color=None, label=None)
    assert graph.graph.xmin == -10.
    assert graph.graph.xmax == 10.


def test_log_log():
    """Test x-y axis with linear scaling"""

    graph = AnnotatedLinePlot(xlog=True, ylog=True)

    x_vals = np.linspace(-10., 10., 100)    # this will create negative x-values which the graph should ignore
    y_vals = func1(x_vals)

    graph.plot(x_values=x_vals, y_values=y_vals)

    assert graph.graph.xmin > 0
    assert graph.graph.xmax == 10.

    # test negative y-values
    y_vals = x_vals**2 - 10.
    graph.plot(x_values=x_vals, y_values=y_vals)

    assert graph.graph.ymin > 0

    # check if data sets are stored correctly
    assert len(graph.xy_datasets) == 2


def test_auto_colors():
    """Test if the automatic color assignment works"""

    graph = AnnotatedLinePlot()

    data_sets = 25

    x_vals = np.linspace(-10., 10., 100)
    set_params = np.linspace(1., 10., data_sets)    # more curve sets than standard colors

    for set_param in set_params:
        graph.plot(x_values=x_vals, y_values=x_vals**set_param, label=str(set_param))

    assert len(graph.xy_datasets) == data_sets
