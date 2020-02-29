"""
datasets.py
-----------

Datasets for testing / analysis.
"""


import numpy as np
import pandas as pd


# Random dataset
def random_dataset(n_rows=100000, n_columns=2, null_proportion=0.25):
    """
    Generates a dataset full of random numbers between 0 and 1

    Parameters
    ----------
    n_rows : int
        Number of observations
    n_columns : int
        Number of features
    null_proportion : float
        Percent (per column) of observations that will be randomly converted to null values

    Returns
    -------
    pandas.DataFrame
        Random dataset
    """

    # Generate random data
    df = pd.DataFrame(np.random.rand(n_rows, n_columns))

    # Insert nulls?
    if null_proportion > 0.:
        # Number of nulls
        n_nulls = int(n_rows * null_proportion)

        # Nullify on a per column basis
        for j in range(n_columns):
            # Rows to nullify
            i = np.random.randint(low=0, high=n_rows, size=n_nulls)

            # Nullify
            df.iloc[i, j] = np.nan

    # Return
    return df


class RandomModelingDataset:
    """
    Create a random dataset with a binary outcome for modeling tests
    """

    # Initialize class instance
    def __init__(self, n_observations=100000, n_predictors=5, class_balance=0.5):
        """

        Initialize instance of `RandomModelingDataset`

        Parameters
        ----------
        n_observations : int
            Number of observations in dataset.
        n_predictors : int
            Number of predictors to the outcome. (Default: 5)
        class_balance : float
            Percentage to skew the outcome (Default: 0.5, i.e., not skewed).
        """

        # Save parameters
        self.n_observations = n_observations
        self.n_predictors = None
        self.class_balance = class_balance

        # Define outcome
        outcome = np.random.rand(n_observations)
        self._data = pd.DataFrame({'outcome': outcome < class_balance})

        # Add predictors
        for i in range(n_predictors):
            self.add_predictor(scale=np.random.randint(1, 5))

    # Get item
    def __getitem__(self, item):
        return self._data[item]

    # Add predictor
    def add_predictor(self, scale=1., size=1000000):
        """
        Add a predictor to the random modeling dataset

        Parameters
        ----------
        scale : Number
            Variance
        size : Number


        Returns
        -------

        """

        # Outcomes
        outcomes = self._data['outcome'].values

        # Create two histograms that contain possible values for this new feature
        values_0 = np.random.normal(loc=0., scale=scale, size=size)
        values_1 = np.random.normal(loc=1., scale=scale, size=size)

        # Sample from the histograms because on the known outcome
        result = np.zeros(outcomes.shape)
        condition = outcomes == 0
        result[condition] = np.random.choice(a=values_0, size=np.sum(condition))
        condition = outcomes == 1
        result[condition] = np.random.choice(a=values_1, size=np.sum(condition))

        # Save
        if self.n_predictors is None:
            self.n_predictors = -1
        self.n_predictors += 1
        self._data['feature' + str(self.n_predictors)] = result


# Wrapper function for RandomModelingDataset
def random_modeling_dataset(n_observations=1000000, n_predictors=5, class_balance=0.5):
    """
    Wrapper function to initialize an instance of :class:`izzy.datasets.RandomModelingDataset`

    Parameters
    ----------
    n_observations : int
        Number of observations (Default: 1000000).
    n_predictors : int
        Number of predictors (Default: 5).
    class_balance : float
        How should the class be balanced? (Default: 0.5)

    Returns
    -------
    pandas.DataFrame
        Random modeling dataset
    """

    return RandomModelingDataset(n_observations, n_predictors, class_balance)[:]
