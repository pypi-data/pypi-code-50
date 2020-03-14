import pandas as pd


def generate_virtual_pop(size, population_name, distribution_func, *para):

    """
    Create a virtual population

    Parameters
    ----------
    size : int
        The size of the virtual population
    population_name : str
        The population_name of the virtual population
    distribution_func : func
        The function that came from numpy.random
    *para : int
        The parameters the distribution_func is using

    Returns
    -------
    pd.DataFrame
        The virtual population as a dataframe

    Raises
    -------
    ValueError
        size input is greater than 0
    TypeError
        size input is an integer
    TypeError
        *para number of parameters for the distribution function

    Examples
    --------
    >>> from samplingsimulatorpy import generate_virtual_pop
    >>> pop = generate_virtual_pop(100, "Height", np.random.normal, 0, 1)
    """

    if (size <= 0):
        raise ValueError("Size of population must be a positive integer")

    if (not isinstance(size, int)):
        raise TypeError("Size of population must be a positive integer")

    try:
        distribution_func(*para, size)
    except TypeError:
        print('Please enter a valid distribution function'
              'with correct number of parameters for'
              'the distribution function')
        raise TypeError

    pop = pd.DataFrame(distribution_func(*para, size=size),
                       columns=[population_name])

    return pop
