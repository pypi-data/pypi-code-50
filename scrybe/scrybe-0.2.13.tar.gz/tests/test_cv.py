import scrybe
import pandas
from sklearn.base import BaseEstimator, TransformerMixin, ClassifierMixin
from sklearn.pipeline import Pipeline

from sklearn import model_selection
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier


scrybe.init("scrybe e2e client testing")
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names=names)
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,
                                                                                random_state=seed)


class Transformer(BaseEstimator, TransformerMixin):
    def __init__(self, model):
        self.model = model

    def fit(self, X, y=None):
        print("Transformer.fit: ", X.shape)
        self.model.fit(X, y)
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

    def score(self, X, y=None, sample_weight=None):
        # counts number of values bigger than mean
        return self.predict(X)


steps = [('transformer', Transformer(model=KNeighborsClassifier())), ('classifier', Classifier(threshold=0.8))]
pipeline = Pipeline(steps)

models = [
    ('KNN_Pipeline', pipeline),
    ('LR', LogisticRegression(solver='liblinear', multi_class='ovr')),
    ('LDA', LinearDiscriminantAnalysis()),
    ('KNN', KNeighborsClassifier()),
    ('CART', DecisionTreeClassifier()),
    ('NB', GaussianNB()),
    ('SVM', SVC(gamma='auto'))
]

# evaluate each model in turn
results = []
names = []

scoring = 'accuracy'
for name, model in models:
    kfold = model_selection.KFold(n_splits=5, random_state=7)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    # print(cv_results)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
