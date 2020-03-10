
from .generic import *
from .logistic import *
from .metrics import *
from .tree import *

# Module contents
__all__ = [
    'accuracy',  # has unit tests
    'aic',  # has unit tests
    'bic',  # has unit tests
    'confusion_matrix',  # has unit tests
    'create_engine_from_string',
    'f1',  # has unit tests
    'false_negatives',  # has unit tests
    'false_positives',  # has unit tests
    'GenericModel',
    'gini',  # has unit tests
    'ks',  # has unit tests
    'LogisticRegression',
    'performance_report',
    'precision',
    'recall',
    'roc',  # has unit tests
    'roc_auc',  # has unit tests
    'roc_plot',
    'sensitivity',
    'specificity',
    'true_negatives',  # has unit tests
    'true_positives',  # has unit tests
    'weight_of_evidence'
]


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
