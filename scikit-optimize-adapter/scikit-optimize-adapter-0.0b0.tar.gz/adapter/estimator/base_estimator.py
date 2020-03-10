from abc import ABCMeta, abstractmethod

class BaseEstimator(object, metaclass=ABCMeta):
    """
    Base class for all Algorithm classes.

    comment on similarity with scikit learn
    """

    @abstractmethod
    def __init__(self, **kwargs):
        pass
     
    @abstractmethod
    def fit(self, X, y, params):
        pass

    @abstractmethod
    def score(self, X, y):
        pass

    @abstractmethod
    def predict(self, X):
        pass 
       
