import pandas as pd
import altair as alt
import numpy as np


def plot_sample_hist(pop, samples):
    """
    Creates a facetted plot of sample histograms from a population

    Parameters
    ----------
    pop : pd.DataFrame
        The virtual population as a dataframe
    samples : pd.DataFrame
        The samples as a dataframe

    Returns
    -------
    altair.vegalite.v3.api.Chart
        A grid of the sample distribution plots

    Raises
    -------
    TypeError
        if pop input is not a valid data frame
    TypeError
        if pop input is an empty data frame
    ValueError
        pop input should only contain numeric values
    TypeError
        if samples input is not a valid data frame
    ValueError
        samples input should only contain numeric values

    Examples
    --------
    >>> pop = generate_virtual_pop(100, "variable", normal, 0, 1)
    >>> samples = draw_samples(pop, 3, [5, 10, 15, 20])
    >>> plot_sample_hist(pop, samples)
    """
    # START CHECKS
    # check pop df input
    if not isinstance(pop, pd.DataFrame):
        raise TypeError("'pop' should be input as a dataframe")

    if not pop.shape[0] >= 1:
        raise TypeError("'pop' appears to be an empty dataframe")

    if not np.issubdtype(pop.to_numpy().dtype, np.number):
        raise ValueError("'pop' should only contain numeric values")

    # check samples df input
    if not isinstance(samples, pd.DataFrame):
        raise TypeError("'samples' should be input as a dataframe")

    if not np.issubdtype(samples.to_numpy().dtype, np.number):
        raise ValueError("'samples' should only contain numeric values")

    # only look at one sample (ignore replicates)
    s_df = samples.query('replicate == 1')
    s_df.loc[:, 'Sample Distribution Histograms'] = \
        'Sample Size=' + s_df['size'].astype(str)
    pop_copy = pop.copy()
    pop_copy.loc[:, 'Sample Distribution Histograms'] = "True Population"

    # combine into one df for plotting
    plot_data = pd.concat([s_df, pop_copy], ignore_index=True, sort=False)

    # create facetted chart
    return alt.Chart(plot_data).mark_bar().encode(
        alt.X(f"{plot_data.columns[1]}:Q", bin=True),
        alt.Y('count()', title="Count")
    ).properties(
        width=150,
        height=150
    ).facet(
        column='Sample Distribution Histograms:N'
    ).resolve_scale(
        y='independent'
    )
