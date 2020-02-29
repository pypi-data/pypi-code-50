
from . import generic
from . import logistic
from . import metrics
from . import tree

from .generic import *
from .logistic import *
from .metrics import *
from .tree import *

# Module contents
__all__ = ['create_engine_from_string']
__all__ += generic.__all__
__all__ += logistic.__all__
__all__ += metrics.__all__
__all__ += tree.__all__


# Create machine learning model engine from string
# TODO find a home for this. It does not belong in __init__
def create_engine_from_string(identifier):
    """
    Create a machine learning model engine from a string

    Parameters
    ----------
    identifier : str
        String identifier of engine

    Returns
    -------
    engine : object
        An instance of an izzy model class.
    """

    # Type check
    assert isinstance(identifier, str), 'identifier must be string'

    # Convert to lowercase for simplicity and strip and white space
    identifier = identifier.lower().replace(' ', '')

    # Create engine (There needs to be a default; what should this be?)
    engine = None
    if identifier in ('lr', 'logisticregression', 'logit'):
        engine = LogisticRegression(penalty='none', solver='lbfgs', class_weight='balanced', warm_start=False)
    elif identifier in ('rf', 'randomforest'):
        engine = RandomForest()

    # Return
    return engine
