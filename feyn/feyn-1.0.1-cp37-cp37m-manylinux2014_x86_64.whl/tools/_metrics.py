import itertools

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix


def plot_confusion_matrix(y_true,
                          y_pred,
                          labels=None,
                          sample_weight=None,
                          title='Confusion matrix',
                          color_map=plt.cm.Blues):

    """ Plot a Confusion Matrix.

    Arguments:
        y_true {typing.Iterable} -- Expected values (Truth)
        y_pred {typing.Iterable} -- Estimated values (Guess form the Graph)

    Keyword Arguments:
        labels {typing.Iterable} -- List of labels to index the matrix (default: {None})
        sample_weight {typing.Iterable} -- Sample weights (default: {None})
        normalize {bool} -- Normalizes confusion matrix over the true (rows), predicted (columns) conditions or all the population. If None, confusion matrix will not be normalized. (default: {False})
        title {str} -- Title to show on top (default: {'Confusion matrix'})
        color_map {matplotlib.colors.LinearSegmentedColormap} -- Color map to use for the matrix (default: {plt.cm.Blues})

    Returns:
        [plot] -- matplotlib confusion matrix
    """

    if labels is None:
        labels = np.unique(y_true)

    cm = confusion_matrix(y_true, y_pred, labels, sample_weight)

    plt.title(title)
    tick_marks = range(len(labels))
    plt.xticks(tick_marks, labels, rotation=45)
    plt.yticks(tick_marks, labels)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], 'd'),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('Expected')
    plt.xlabel('Predicted')

    plt.imshow(cm, interpolation='nearest', cmap=color_map)
    plt.colorbar()
    plt.tight_layout()
    return plt.show()


def plot_regression_metrics(y_true, y_pred, side_notes, title="Regression metrics"):
    """Plot metrics for a regression problem.

    Arguments:
        y_true {typing.Iterable} -- Expected values (Truth).
        y_pred {typing.Iterable} -- Estimated values (Guess form the Graph).
        side_notes {typing.list[str]} -- A list of notes to add to the plot.

    Keyword Arguments:
        title {str} -- Title of the plot. (default: {"Regression metrics"})

    Raises:
        ValueError: When y_true and y_pred do not have same shape

    Returns:
        [type] -- [description]
    """
    if (len(y_true) != len(y_pred)):
        raise ValueError('Size of expected and predicted are different!')

    data = pd.DataFrame(np.array([y_true, y_pred]).T, columns=[
                        'Expected', 'Predicted'])
    ax = data.sort_values(data.columns[0]).reset_index(drop=True).plot()
    if side_notes is not None:
        for i, note in enumerate(side_notes):
            ax.text(data.index.size*1.2, 0.8 - i * .06, note, fontsize=14)
    return plt, ax.get_figure()
