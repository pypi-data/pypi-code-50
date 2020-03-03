import scrybe
import json

import pandas
from sklearn import model_selection
from sklearn.base import BaseEstimator, ClassifierMixin, TransformerMixin
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from scrybe.internal.depgraph import TrackingGraph

scrybe.init("scrybe e2e client testing")



# Load dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)

# Split-out validation dataset
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)

knn = KNeighborsClassifier()
scrybe.log_custom_hyperparameter(model=knn, param_name="custom_param", param_value=10)
knn.fit(X_train, Y_train)

class Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, model):
        self.model = model

    def fit(self, X, y=None):
        print("Transformer.fit: ", X.shape)
        return self

    def transform(self, X, copy=None):
        print("Transformer.transform: ", X.shape)
        return self.model.predict(X)


class Classifier(BaseEstimator, ClassifierMixin):
    def __init__(self, threshold):
        self.threshold = threshold

    def fit(self, X, y=None):
        print("Classifier.fit: ", X.shape)
        assert (type(self.threshold) == float), "threshold parameter must be float"
        self._threshold = self.threshold
        return self

    def predict(self, X, y=None):
        print("Classifier.predict: ", X.shape)
        try:
            getattr(self, "_threshold")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")
        # X[X < self._threshold] = 0
        return X

    def transform(self, X, y=None):
        return self.predict(X)

    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.predict(X)

    def score(self, X, y=None, sample_weight=None):
        # counts number of values bigger than mean
        return self.predict(X)


# def get_conditional_prob(model, threshold):
def fit_pipeline():
    steps = [('transformer', Transformer(model=knn)),
             ('classifier', Classifier(threshold=0.8))]
    pipeline = Pipeline(steps)
    x = pipeline.fit_transform(X_train, Y_train)
    print(x.shape)
    x = pipeline.transform(X_train)
    print(x.shape)
    accuracy_score(Y_validation, pipeline.predict(X_validation))


fit_pipeline()

