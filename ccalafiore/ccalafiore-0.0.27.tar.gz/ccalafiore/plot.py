"""
===========================
Creating annotated heatmaps
===========================

It is often desirable to show data which depends on two independent
variables as a color coded image plot. This is often referred to as a
heatmap. If the data is categorical, this would be called a categorical
heatmap.
Matplotlib's :meth:`imshow <matplotlib.axes.Axes.imshow>` function makes
production of such plots particularly easy.

The following examples show how to create a heatmap with annotations.
We will start with an easy example and expand it to be usable as a
universal function.
"""


##############################################################################
#
# A simple categorical heatmap
# ----------------------------
#
# We may start by defining some data. What we need is a 2D list or array
# which defines the data to color code. We then also need two lists or arrays
# of categories; of course the number of elements in those lists
# need to match the data along the respective axes.
# The heatmap itself is an :meth:`imshow <matplotlib.axes.Axes.imshow>` plot
# with the labels set to the categories we have.
# Note that it is important to set both, the tick locations
# (:meth:`set_xticks<matplotlib.axes.Axes.set_xticks>`) as well as the
# tick labels (:meth:`set_xticklabels<matplotlib.axes.Axes.set_xticklabels>`),
# otherwise they would become out of sync. The locations are just
# the ascending integer numbers, while the ticklabels are the labels to show.
# Finally we can label the data itself by creating a
# :class:`~matplotlib.text.Text` within each cell showing the value of
# that cell.


# import numpy as np
from matplotlib import pyplot as plt, ticker as ticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
# sphinx_gallery_thumbnail_number = 2


#############################################################################
# Using the helper function code style
# ------------------------------------
#
# As discussed in the :ref:`Coding styles <coding_styles>`
# one might want to reuse such code to create some kind of heatmap
# for different input data and/or on different axes.
# We create a function that takes the data and the row and column labels as
# input, and allows arguments that are used to customize the plot
#
# Here, in addition to the above we also want to create a colorbar and
# position the labels above of the heatmap instead of below it.
# The annotations shall get different colors depending on a threshold
# for better contrast against the pixel color.
# Finally, we turn the surrounding axes spines off and create
# a grid of white lines to separate the cells.


def heatmap(data, cmap=None, ax=None,
            title=None, x_label=None, y_label=None,
            annot=False, fmt_annot='.2f', fontsize_annot=None, textcolors="black",
            xticklabels='auto', yticklabels='auto',
            fontsize_title=None, rotation_title=None,
            fontsize_x_label=None, rotation_x_label=None,
            fontsize_y_label=None, rotation_y_label=None,
            fontsize_xticklabels=None, rotation_xticklabels=None,
            fontsize_yticklabels=None, rotation_yticklabels=None,
            fontsize_cbar_ticklabels=None, cbarlabel="", fontsize_cbarlabel=None):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    y_labels
        A list or array of length N with the labels for the rows.
    x_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if ax is None:
        figures_existing = plt.get_fignums()
        n_figures_new = 1
        i = 0
        f = 0
        while f < n_figures_new:
            if i in figures_existing:
                pass
            else:
                id_figures = i
                f += 1
            i += 1
        if data.shape[1] > data.shape[0]:
            ratio_x = 1
            ratio_y = data.shape[0] / data.shape[1]
        elif data.shape[1] < data.shape[0]:
            ratio_x = data.shape[1] / data.shape[0]
            ratio_y = 1
        else:
            ratio_x = 1
            ratio_y = 1

        plt.figure(id_figures, figsize=(10 * ratio_x, 10 * ratio_y))
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, cmap=cmap)

    # Create colorbar
    # divider = make_axes_locatable(ax)
    # cax = divider.append_axes("right", size="5%", pad=0.05)
    cbar = plt.colorbar(im, ax=ax)
    ax.set_aspect('auto')
    cbar.ax.tick_params(labelsize=fontsize_cbar_ticklabels)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom", fontsize=fontsize_cbarlabel)
    # if fontsize_cbar_ticklabels != 'auto':
    #     # fontsize_cbar_ticklabels = 8
    #     # use matplotlib.colorbar.Colorbar object
    #     cbar = ax.collections[0].colorbar
    #     # here set the labelsize
    #     cbar.ax.tick_params(labelsize=fontsize_cbar_ticklabels)

    plt.title(title, fontsize=fontsize_title, rotation=rotation_title)
    if x_label is not None:
        plt.xlabel(x_label, fontsize=fontsize_x_label, rotation=rotation_x_label)
    if y_label is not None:
        plt.ylabel(y_label, fontsize=fontsize_y_label, rotation=rotation_y_label)

    # # We want to show all ticks...
    ax.set_xticks(list(range(data.shape[1])))
    ax.set_yticks(list(range(data.shape[0])))
    if xticklabels != 'auto':
        # ... and label them with the respective list entries.
        ax.set_xticklabels(xticklabels, fontsize=fontsize_xticklabels, rotation=rotation_xticklabels)

    if yticklabels != 'auto':
        ax.set_yticklabels(yticklabels, fontsize=fontsize_yticklabels, rotation=rotation_yticklabels)


    if annot:
        """"
        A function to annotate a heatmap.
    
        Parameters
        ----------
        im
            The AxesImage to be labeled.
        data
            Data used to annotate.  If None, the image's data is used.  Optional.
        valfmt
            The format of the annotations inside the heatmap.  This should either
            use the string format method, e.g. "$ {x:.2f}", or be a
            `matplotlib.ticker.Formatter`.  Optional.
        textcolors
            A list or array of two color specifications.  The first is used for
            values below a threshold, the second for those above.  Optional.
        threshold
            Value in data units according to which the colors from textcolors are
            applied.  If None (the default) uses the middle of the colormap as
            separation.  Optional.
        **kwargs
            All other arguments are forwarded to each call to `text` used to create
            the text labels.
        """

        # Set default alignment to center, but allow it to be
        # overwritten by textkw.
        kw = dict(horizontalalignment="center",
                  verticalalignment="center",
                  color=textcolors,
                  fontsize=fontsize_annot)

        # Get the formatter in case a string is supplied
        # if isinstance(fmt_annot, str):
        #     fmt_annot = ticker.StrMethodFormatter(fmt_annot)

        # Loop over the data and create a `Text` for each "pixel".
        # Change the text's color depending on the data.
        # texts = []
        # print()
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                # kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
                text = im.axes.text(j, i, fmt_annot.format( data[0, 0]),**kw)
                # texts.append(text)

        # return texts
    plt.tight_layout()
    plt.show()


