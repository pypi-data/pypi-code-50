import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def find_fruits_veg(df, type_of_out='categ'):
    '''
    This function will drop row with NAs and find the index of columns with all
    numeric value or categorical value based on the specification.

    Parameters
    -----------
    df: pandas.core.frame.DataFrame
        Data frame that need to be proceed
    type_of_out: string
        Type of columns that we want to know index of
    list_of_index: list
        list of index value

    Returns
    -------
    list_of_categ: list
        list of index of categorical value
    list_of_num: list
        list of index of numerical value

    Example
    --------
    >>> df = pd.DataFrame({'col1': [1, 2], 'col2': ['a', 'b']})
    >>> find_fruits_veg(df, type_of_out = 'categ')
    [1]
    '''
    list_of_categ = []
    list_of_num = []
    df_clean = df.dropna()
    if df_clean.shape[0] == 0:
        return "It is a empty data frame or too many missing data"
    for i in np.arange(df_clean.shape[1]):
        if isinstance(df_clean.iloc[0, i], str):
            list_of_categ += [i]
        elif not isinstance(df_clean.iloc[0, i], str):
            list_of_num += [i]
    if type_of_out == 'categ':
        return list_of_categ
    elif type_of_out == 'num':
        return list_of_num


def find_missing_ingredients(data):
    """
    For each column with missing values,
    this function will create a reference list of row indices,
    sum the number and calculate proportion of missing values

    Parameters
    -----------
    data: pandas.core.frame.DataFrame
        A dataframe that need to be processed

    Returns
    -------
    pandas.core.frame.DataFrame
        Data frame summarizing the indexes,
        count and proportion of missing values in each column

    Example
    --------
    >>> df = data.frame("letters" = c("a","b","c"),
                        "numbers" = c(1,2,3))
    >>> find_missing_ingredients(df)
    'There are no missing values'

    """
    assert isinstance(data, pd.core.frame.DataFrame), \
        "Input path should be a pandas data frame"
    assert data.shape[0] >= 1, "The input data frame has no rows"

    if np.sum(np.sum(data.isna(), axis=0)) == 0:
        return "There are no missing values"

    counts = np.sum(data.isna(), axis=0)
    counts = counts[counts > 0]
    indices = []

    for column in data.columns:
        if np.sum(data[column].isna()):
            indices.append(data[column][data[column].isna()].index.values)

    else:
        report = pd.DataFrame({'NaN count': counts,
                               'NaN proportion': counts / data.shape[0],
                               'NaN indices': indices}).reset_index()

        report['NaN proportion'] = pd.Series(
            ["{0:.1f}%".format(val * 100) for val in report['NaN proportion']])
        report = report.rename(columns={"index": 'Column name'})

        return report


def find_bad_apples(df):
    '''
    This function uses a univariate approach to outlier detection.
    For each column with outliers (values that are 2 or more
    standard deviations from the mean),
    this function will create a reference list of row indices with
    outliers, and the total number of outliers in that column.
    Note:
    This function works best for small datasets with
    unimodal variable distributions.
    Note:
    If your dataframe has duplicate column names,
    only the last of the duplicated columns will be checked.

    Parameters
    -----------
    df : pandas.core.frame.DataFrame
        A dataframe containing numeric data

    Returns
    -------
    bad_apples : pandas.DataFrame
        A dataframe showing 3 columns:
        Variable (column name),
        Indices (list of row indices with outliers), and
        Total Outliers (number of outliers in the column)

    Examples
    --------
    >>> df = pd.DataFrame({'A' : ['test', 1, 1, 1, 1])
    >>> find_bad_apples(df)
    AssertionError: Every column in your dataframe must be numeric.
    >>> df = pd.DataFrame({'A' : [1, 1, 1, 1, 1],
    ...                    'B' : [10000, 1, 1, 1, 1]})
    >>> find_bad_apples(df)
    AssertionError: Sorry, you don't have enough data.
    The dataframe needs to have at least 30 rows.
    >>> df = pd.DataFrame({'A' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    ...                             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ...                    'B' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-100,
    ...                             1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,100],
    ...                    'C' : [1,1,1,1,1,19,1,1,1,1,1,1,1,1,19,1,1,1,1,
    ...                             1,1,1,1,1,1,1,19,1,1,1,1,1,1,1,1]})
    >>> find_bad_apples(df)
    Variable      Indices     Total Outliers
        B         [17, 34]          2
        C      [5, 14, 26]          3
    >>> df = pd.DataFrame({'A' : [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    ...                             1,1,1,1,1,1,1,1,1,1,1,1,1],
    ...                    'B' : [1.000001, 1.000001, 1.000001, 1.000001,
    ...                           1.000001, 1.000001, 1.000001, 1.000001,
    ...                           1.000001, 1.000001, 1.000001, 1.000001,
    ...                           1.000001, 1.000001, 1.000001,
    ...                           1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]})
    >>> find_bad_apples(df))
    Variable                Indices     Total Outliers
    No outliers detected        []              0
    '''

    # Checks that every column in the dataframe is numeric
    assert df.select_dtypes(include=['float', 'int']).shape[1] == df.shape[1],\
        'Every column in your dataframe must be numeric.'

    # Checks that there are at least 30 rows in the dataframe
    assert df.shape[0] >= 30, \
        'Sorry, you don\'t have enough data. \
        The dataframe needs to have at least 30 rows.'

    columns = list(df)

    # Initializes empty dataframe
    output = pd.DataFrame(columns=['Variable', 'Indices', 'Total Outliers'])

    c = 0

    for column in columns:
        mean = round(df.mean(axis=0)[c], 3)
        sd = round(np.std(df.iloc[:, c]), 3)

        col = column
        ind = []
        tot = 0
        r = 0

        values = df.values[:, c]
        for value in values:
            if bool((mean - 2*sd) <= value & value <= (mean + 2*sd)) is True:
                r += 1
            elif bool((mean - 2 * sd) <= value &
                      value <= (mean + 2 * sd)) is False:
                ind.append(r)
                tot += 1
                r += 1
        c += 1

        if tot == 0:
            continue
        else:
            output = output.append({'Variable': col,
                                    'Indices': ind,
                                    'Total Outliers': tot},
                                   ignore_index=True)

    if len(output) == 0:
        output = output.append({'Variable': 'No outliers detected',
                                'Indices': 'x',
                                'Total Outliers': tot},
                               ignore_index=True)
        return output
    else:
        return output


def make_recipe(
        X,
        y,
        recipe,
        splits_to_return="train_test",
        random_seed=None,
        train_valid_prop=0.8):
    """
    The `make_recipe()` function is used to quickly apply common data
    preprocessing techniques

    Parameters
    ----------
    X : pandas.DataFrame
        A dataframe containing training, validation, and testing features.
    y : pandas.DataFrame
        A dataframe containing training, validation, and testing response.
    recipe : str
        A string specifying which recipe to apply to the data. The only recipe
        currently available is "ohe_and_standard_scaler". More recipes are
        under development.
    splits_to_return : str, optional
        "train_test" to return train and test splits, "train_test_valid" to
        return train, test, and validation data, "train" to return all data
        without splits. By default "train_test".
    random_seed : int, optional
        The random seed to set for splitting data to create reproducible
        results. By default None.
    train_valid_prop : float, optional
        The proportion to split the data by. Should range between 0 to 1. By
        default = 0.8

    Returns
    -------
    Tuple of pandas.DataFrame
        A tuple of dataframes: (X_train, X_valid, X_test, y_train, y_valid,
        y_test)

    Example
    --------
    >>> from vega_datasets import data
    >>> from mealprep.mealprep import make recipe
    >>> df = pd.read_json(data.cars.url).drop(columns=["Year"])
    >>> X = df.drop(columns=["Name"])
    >>> y = df[["Name"]]
    >>> X_tr X_va, X_te, y_tr, y_va, y_te = mealprep.make_recipe(
    ...        X=X, y=y, recipe="ohe_and_standard_scaler",
    ...        splits_to_return="train_test")
    """

    # validate inputs
    assert (
        X.shape[0] == y.shape[0]
    ), "X and y should have the same number of observations."
    assert recipe in [
        "ohe_and_standard_scaler"
    ], "Please select a valid string option for recipe."
    assert splits_to_return in [
        "train_test",
        "train_test_valid",
    ], "Please enter a valid string for splits_to_return."

    # clean input data
    y = y.to_numpy().ravel()

    # split data
    if splits_to_return == "train_test":
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=train_valid_prop, random_state=random_seed
        )
        X_valid = None
        y_valid = None
    elif splits_to_return == "train_test_valid":
        X_train_valid, X_test, y_train_valid, y_test = train_test_split(
            X, y, test_size=train_valid_prop, random_state=random_seed
        )
        X_train, X_valid, y_train, y_valid = train_test_split(
            X_train_valid,
            y_train_valid,
            test_size=train_valid_prop,
            random_state=random_seed,
        )

    # determine column type
    numerics = ["int16", "int32", "int64", "float16", "float32", "float64"]
    categorics = ["object"]
    numeric_features = list(X_train.select_dtypes(include=numerics).columns)
    categorical_features = list(
        X_train.select_dtypes(
            include=categorics).columns)

    # preprocess data
    if recipe == "ohe_and_standard_scaler":
        numeric_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder(handle_unknown="ignore")

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features),
        ]
    )

    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)
    if splits_to_return == "train_test_valid":
        X_valid = preprocessor.transform(X_valid)

    # get column names back and convert back to a DataFrame
    categorical_features_transformed = preprocessor.transformers_[1][
        1
    ].get_feature_names()
    features_transformed = list(numeric_features) + list(
        categorical_features_transformed
    )
    X_train = pd.DataFrame(data=X_train, columns=features_transformed)
    X_test = pd.DataFrame(data=X_test, columns=features_transformed)
    if splits_to_return == "train_test_valid":
        X_valid = pd.DataFrame(data=X_valid, columns=features_transformed)

    return (X_train, X_valid, X_test, y_train, y_valid, y_test)
