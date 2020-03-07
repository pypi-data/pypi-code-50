import numpy as np
import pandas as pd


__version__ = '0.2020.03.07'


def solve_n_bins(x):
    """
    Uses the Freedman Diaconis Rule for generating the number of bins required
    https://en.wikipedia.org/wiki/Freedman%E2%80%93Diaconis_rule
    Bin Size = 2 IQR(x) / (n)^(1/3)
    """
    from scipy.stats import iqr

    x = np.asarray(x)
    hat = 2 * iqr(x) / (len(x) ** (1 / 3))

    if hat == 0:
        return int(np.sqrt(len(x)))
    else:
        return int(np.ceil((x.max() - x.min()) / hat))


def neg_log_p(p):
    """
    Negative Log P value
    """
    return np.nan_to_num(-np.log10(p))


def most_common(iterable):
    """
    >>> most_common([1, 2, 2, 3, 4, 4, 4, 4])
    4
    >>> most_common(list('Anthony'))
    'n'
    >>> most_common('Stephen')
    'e'
    Exceptionally quick! Benchmark at 12.1 us
    :param iterable:
    :return:
    """
    from collections import Counter

    data = Counter(iterable)
    return data.most_common(1)[0][0]


def lambda_test(p_values, df=1):
    """
    Test for p-value inflation for hinting at population stratification or cryptic species.
    Paper: https://neurogenetics.qimrberghofer.edu.au/papers/Yang2011EJHG.pdf

    :param p_values: array of p-values
    :param df: Degrees of freedom for the Chi sq distribution
    :return: lambda gc
    """
    from scipy.stats import chi2
    assert np.max(p_values) <= 1 and np.min(p_values) >= 0, 'These do not appear to be p-values'

    chi_sq_scores = chi2.ppf(1 - p_values, df)
    return np.median(chi_sq_scores) / chi2.ppf(0.5, df)


def p_value_inflation_test(p_values):
    """
    Test for p-value inflation using the Kolmogorov-Smirnov test.
    However there are no assumptions to fail for this test.

    :param p_values: array of p-values
    :return: p-value (significant is bad)
    """
    from scipy.stats import ks_2samp
    h_null = np.random.uniform(0, 1, size=int(1e6))
    d, p_value = ks_2samp(p_values, h_null)
    return p_value, d


def bonferroni(p_values, alpha=0.05):
    """
    Bonferroni Correction

    :param p_values:
    :param alpha:
    :return:
    """
    return alpha / len(p_values)


def bh_procedure(p_values: pd.Series, alpha=0.05):
    """
    Benjamini–Hochberg procedure
    https://en.wikipedia.org/wiki/False_discovery_rate#BH_procedure
    http://www.math.tau.ac.il/~ybenja/MyPapers/benjamini_hochberg1995.pdf
    """
    assert len(p_values) > 0, 'p-value list in empty'
    assert sum(np.isnan(p_values)) == 0, 'You cannot have nans in the p-value list'

    p_values, m = sorted(p_values), len(p_values)

    max_condition = 0
    for i, p in enumerate(p_values):
        rank = i + 1
        if p <= (rank * alpha) / m:
            max_condition = p
        else:
            break

    return max_condition


def ecdf(data):
    """
    Empirical CDF (x, y) generator
    """
    x = np.sort(data)
    cdf = np.linspace(0, 1, len(x))
    return cdf, x


def elbow_detection(data, threshold=1, tune=0.01, get_index=False):
    cdf, ordered = ecdf(data)
    data_2nd_deriv = np.diff(np.diff(ordered))
    elbow_point = np.argmax(data_2nd_deriv > threshold) - int(len(cdf) * tune)
    return elbow_point if get_index else ordered[elbow_point]


def normalise_percents(x: np.ndarray or pd.Series, should_impute=False) -> np.ndarray or pd.Series:
    """
    If the vector contains numbers whose numbers are [0, 1] then this is transformation that properly handles the
    difference in how the variance of the kind of a feature is computed.
    x_norm = (x - mu) / sqrt(mu * (1 - mu))
    :param should_impute: If True then nans are imputed with the mean of x
    :param x:
    :return:
    """
    # NOTE Currently python doesn't allow you to write this as 0 <= x <= 1
    assert (0 <= x[~np.isnan(x)]).all() and (x[~np.isnan(x)] <= 1).all(), 'Values must be [0, 1]'
    mu = np.nanmean(x)
    if should_impute:
        x[np.isnan(x)] = mu
    return (x - mu) / np.sqrt(mu * (1 - mu))


def is_positive_definite(x):
    """
    If all eigenvalues are greater than 0 then the matrix is positive definite!
    """
    return np.all(np.linalg.eigvals(x) > 0)


def is_positive_semi_definite(x):
    return np.all(np.linalg.eigvals(x) >= 0)
