import scrybe
import keras
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin
from sklearn.pipeline import Pipeline

from tests.test_mnist_model import get_untrained_model, get_dataset

scrybe.init("scrybe e2e client testing")
(x_train, y_train), (x_test, y_test), (x_val, y_val), input_shape = get_dataset()
batch_size = 1024
epochs = 2

model = get_untrained_model(num_filter_1=4, input_shape=input_shape)
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1
          )


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
        X[X < self._threshold] = 0
        return X

    def score(self, X, y=None, sample_weight=None):
        # counts number of values bigger than mean
        return self.predict(X)


def get_conditional_prob(model, threshold):
    steps = [('transformer', Transformer(model=model)),
             ('classifier', Classifier(threshold=threshold))]
    pipeline = Pipeline(steps)
    scrybe.log_custom_hyperparameter(model=pipeline, param_name="Threshold", param_value=threshold)
    pipeline.fit(x_train, y_train)
    scrybe.log_custom_model_evaluation_metric(model=pipeline, x_test=x_test, y_test=y_test, param_name="custom_metric",
                                              param_value=0.6)
    return pipeline.predict(x_test)


predictions = get_conditional_prob(model=model, threshold=0.80)
print("Output Shape: ", predictions.shape)
predictions = predictions.argmax(axis=-1)
predictions_one_hot = keras.utils.to_categorical(predictions, 10)
y_test_one_hot = y_test
y_test = y_test.argmax(axis=-1)

from sklearn.metrics import jaccard_score, classification_report

print("Classification Report")
print(classification_report(y_test, predictions))
print("Jaccard Score")
print(jaccard_score(y_test, predictions, average=None))

