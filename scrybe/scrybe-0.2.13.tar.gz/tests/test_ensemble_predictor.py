from __future__ import print_function
import scrybe
import json
from scrybe.internal.depgraph import TrackingGraph
from sklearn.metrics import accuracy_score
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin
from sklearn.pipeline import Pipeline
from tests.test_mnist_model import get_untrained_model, get_dataset


scrybe.init("scrybe e2e client testing")
(x_train, y_train), (x_test, y_test), (x_val, y_val), input_shape = get_dataset()
batch_size = 128
epochs = 2

model1 = get_untrained_model(num_filter_1=4, input_shape=input_shape)
model1.fit(x_train, y_train,
           batch_size=batch_size,
           epochs=epochs,
           verbose=1
           )

model2 = get_untrained_model(num_filter_1=8, input_shape=input_shape)
model2.fit(x_train, y_train,
           batch_size=batch_size,
           epochs=epochs,
           verbose=1
           )


class Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, model1, model2):
        self.model1 = model1
        self.model2 = model2

    def fit(self, X, y=None):
        print("Transformer.fit: ", X.shape)
        return self

    def transform(self, X, copy=None):
        print("Transformer.transform: ", X.shape)
        X1 = self.model1.predict(X)
        X2 = self.model2.predict(X)
        return X1, X2


class Classifier(BaseEstimator, ClassifierMixin):
    def __init__(self, weight1, weight2):
        self.weight1 = weight1
        self.weight2 = weight2

    def fit(self, X, y=None):
        print("Classifier.fit: ", X[0].shape, X[1].shape)
        assert (type(self.weight1) == float), "weight1 parameter must be float"
        assert (type(self.weight2) == float), "weight2 parameter must be float"
        self.weight_1 = self.weight1
        self.weight_2 = self.weight2
        return self

    def predict(self, X, y=None):
        X1, X2 = X
        print("Classifier.predict: %s %s" % (X1.shape, X2.shape))
        try:
            getattr(self, "weight_1")
            getattr(self, "weight_2")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")
        print(X1[0])
        print(X2[0])
        Y = (self.weight_1 * X1 + self.weight_2 * X2) / (self.weight_1 + self.weight_2)
        print(Y[0])
        return Y

    def fit_predict(self, X, y=None):
        self.fit(X, y)
        return self.predict(X, y)

    def score(self, X, y=None, sample_weight=None):
        # counts number of values bigger than mean
        return accuracy_score(y, self.predict(X))


def get_ensemble_prob(model1, model2, weight1, weight2):
    steps = [('transformer',
              Transformer(model1=model1, model2=model2)),
             ('classifier', Classifier(weight1=weight1, weight2=weight2))]
    pipeline = Pipeline(steps)
    return pipeline.fit_predict(x_test)


y_pred = get_ensemble_prob(model1=model1, model2=model2, weight1=0.75, weight2=0.25)
print("Output Shape: ", y_pred.shape)
print(json.dumps(TrackingGraph.get_node_for_tracked_object(obj=y_pred).get_lineage().to_json(), indent=2))
