import pickle
import sys
import os

from sklearn.base import BaseEstimator
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.manifold import TSNE
from sklearn.pipeline import Pipeline

import rdflib
import pandas as pd
import numpy as np

import random

from graph import rdflib_to_kg
from rdf2vec import RDF2VecTransformer

from walkers import (RandomWalker, WeisfeilerLehmanWalker,
                     AnonymousWalker, WalkletWalker, NGramWalker,
                     CommunityWalker, HalkWalker)

files = {"AIFB": "aifb.n3",
         "AM": "rdf_am-data.ttl",
         "BGS": "BGS.nt",
         "MUTAG": "mutag.xml"}

labels = {"AIFB" : (["http://swrc.ontoware.org/ontology#affiliation",
                     "http://swrc.ontoware.org/ontology#employs",
                     "http://swrc.ontoware.org/ontology#carriedOutBy"], "person", "label_affiliation"),
          "AM" : (["http://purl.org/collections/nl/am/objectCategory",
                   "http://purl.org/collections/nl/am/material"], "proxy", "label_cateogory"),
          "BGS": (["http://data.bgs.ac.uk/ref/Lexicon/hasLithogenesis",
                   "http://data.bgs.ac.uk/ref/Lexicon/hasLithogenesisDescription",
                   "http://data.bgs.ac.uk/ref/Lexicon/hasTheme"], "rock", "label_lithogenesis"),
          "MUTAG": (["http://dl-learner.org/carcinogenesis#isMutagenic"], "bond", "label_mutagenic")}

# Load the data with rdflib
dataset = sys.argv[1]
print(end='Loading data... ', flush=True)
g = rdflib.Graph()
g.parse(os.path.join('..', 'data', dataset, files[dataset]), format=files[dataset].split('.')[-1])
print('OK')

# Load our train & test instances and labels
test_data = pd.read_csv(os.path.join('..', 'data', dataset, dataset + '_test.tsv'), sep='\t')
train_data = pd.read_csv(os.path.join('..', 'data', dataset, dataset + '_train.tsv'), sep='\t')

train_entities = [rdflib.URIRef(x) for x in train_data[labels[dataset][1]]]
train_labels = train_data[labels[dataset][2]]

test_entities = [rdflib.URIRef(x) for x in test_data[labels[dataset][1]]]
test_labels = test_data[labels[dataset][2]]

all_labels = list(train_labels) + list(test_labels)

# Define the label predicates, all triples with these predicates
# will be excluded from the graph
label_predicates = []
for pred in labels[dataset][0]:
    label_predicates.append(rdflib.term.URIRef(pred))

# Convert the rdflib to our KnowledgeGraph object
kg = rdflib_to_kg(g, label_predicates=label_predicates)


##############EMBEDDINGS###############

class RDF2VecEstimator(BaseEstimator):
    def __init__(self, depth=4, lb_freq_threshold=0.001, ub_freq_threshold=0.1):
        """Initialize with relevant parameters (these can be tuned using cv)."""
        self.depth = depth
        self.lb_freq_threshold = lb_freq_threshold
        self.ub_freq_threshold = ub_freq_threshold

    def fit(self, X, y=None):
        """Fit estimator to training data."""
        halk_walker = HalkWalker(self.depth, float('inf'),
                                 lb_freq_threshold=self.lb_freq_threshold,
                                 ub_freq_threshold=self.ub_freq_threshold)
        self.transformer = RDF2VecTransformer(walkers=[halk_walker], sg=1)
        # IMPORTANT: fit is performed on ALL training data, not X,
        # which is only the training data for a given split;
        # if fit is performed on X alone, the vocab will not contain
        # the entities in the valid set for the respective split
        self.transformer.fit(kg, train_entities)

    def transform(self, X):
        """Return the learned embeddings."""
        return self.transformer.transform(kg, X)

    def fit_transform(self, X, y=None):
        """Combine fit and transform."""
        self.fit(X, y)
        return self.transform(X)


##############EXPERIMENTS##############

logfile = open(os.path.join("results", "log_" + dataset + "_" + sys.argv[2] + "_halk.txt"), "a")
resfile = open(os.path.join("results", "experiments_" + dataset + "_" + sys.argv[2] + "_halk.txt"), "a")

def print_results(myDict, colList=None):
   """ Pretty print a list of dictionaries (myDict) as a dynamically sized table.
   If column names (colList) aren't specified, they will show in random order.
   Author: Thierry Husson
   Edited by: Michael Weyns
   """
   if not colList: colList = list(myDict.keys() if myDict else [])
   myList = [colList] # 1st row = header
   for i in range(len(myDict[colList[0]])):
       myList.append([str(myDict[col][i] if myDict[col][i] is not None else '') for col in colList])
   colSize = [max(map(len,col)) for col in zip(*myList)]
   formatStr = ' | '.join(["{{:<{}}}".format(i) for i in colSize])
   myList.insert(1, ['-' * i for i in colSize]) # Separating line
   for item in myList: logfile.write(formatStr.format(*item) + "\n")
   logfile.write("\n")


# random forest experiment

logfile.write('-----------RANDOM FOREST-----------\n\n')

rf_scores = []
for i in range(int(sys.argv[2])):
    logfile.write("ITERATION " + str(i) + "...\n\n")
    init = random.randint(0, 100000)
    est = RDF2VecEstimator()
    rf =  RandomForestClassifier(random_state=init)

    rf_pipe = Pipeline([('est', est), ('rf', rf)])
    clf =  GridSearchCV(rf_pipe, {'est__depth': [2, 4, 8],
                                  'est__lb_freq_threshold': [0.001, 0.005, 0.01, 0.05, 0.1, 0.15, 0.25],
                                  'est__ub_freq_threshold': [0.1, 0.25, 0.5, 0.75, 0.9],
                                  'rf__n_estimators': [50, 100, 150, 200]}, cv=3)
    clf.fit(train_entities, train_labels)

    params = clf.best_params_
    logfile.write("best results found for" + str(params) + "\n\n")
    results = clf.cv_results_
    # print("results:", results)
    print_results(results)

    halk_walker = HalkWalker(params['est__depth'], float('inf'),
                             lb_freq_threshold=params['est__lb_freq_threshold'],
                             ub_freq_threshold=params['est__ub_freq_threshold'])
    transformer = RDF2VecTransformer(walkers=[halk_walker], sg=1)
    embeddings = transformer.fit_transform(kg, train_entities + test_entities)
    train_embeddings = embeddings[:len(train_entities)]
    test_embeddings = embeddings[len(train_entities):]

    rf = RandomForestClassifier(random_state=init, n_estimators=params['rf__n_estimators'])
    rf.fit(train_embeddings, train_labels)
    rf_scores.append(accuracy_score(test_labels, rf.predict(test_embeddings)))
    logfile.write("confusion matrix:\n" + str(confusion_matrix(test_labels, rf.predict(test_embeddings))) + "\n\n")
    logfile.write("test accuracy: " + str(rf_scores[-1]) + "\n\n")


logfile.write("AVG test scores: " + str(np.average(rf_scores)) + ", " + str(np.std(rf_scores)) + "\n\n")
resfile.write(dataset + "," + "halk" + "," + sys.argv[2] + "," + "RF" + "," +
              str(np.average(rf_scores)) + "," + str(np.std(rf_scores)) + "\n")

# support vector machine experiment

logfile.write('\n\n-----------SVM-----------\n')

svc_scores = []
for i in range(int(sys.argv[2])):
    logfile.write("ITERATION " + str(i) + "...\n")
    init = random.randint(0, 100000)
    est = RDF2VecEstimator()
    svc = SVC(random_state=init)
    rf_pipe = Pipeline([('est', est), ('svc', svc)])
    clf =  GridSearchCV(rf_pipe, {'est__depth': [2, 4, 8],
                                  'est__lb_freq_threshold': [0.001, 0.005, 0.01, 0.05, 0.1, 0.15, 0.25],
                                  'est__ub_freq_threshold': [0.1, 0.25, 0.5, 0.75, 0.9],
                                  'svc__kernel': ['linear', 'poly', 'rbf'],
                                  'svc__C': [10 ** i for i in range(-3, 4)]}, cv=3)
    clf.fit(train_entities, train_labels)

    params = clf.best_params_
    logfile.write("best results found for" + str(params)+ "\n\n")
    results = clf.cv_results_
    # print("results:", results)
    print_results(results)

    halk_walker = HalkWalker(params['est__depth'], float('inf'),
                             lb_freq_threshold=params['est__lb_freq_threshold'],
                             ub_freq_threshold=params['est__ub_freq_threshold'])
    transformer = RDF2VecTransformer(walkers=[halk_walker], sg=1)
    embeddings = transformer.fit_transform(kg, train_entities + test_entities)
    train_embeddings = embeddings[:len(train_entities)]
    test_embeddings = embeddings[len(train_entities):]

    svc = SVC(random_state=init, kernel=params['svc__kernel'], C=params['svc__C'])
    svc.fit(train_embeddings, train_labels)
    svc_scores.append(accuracy_score(test_labels, clf.predict(test_embeddings)))
    logfile.write("confusion matrix:\n" + str(confusion_matrix(test_labels, clf.predict(test_embeddings))) + "\n\n")
    logfile.write("test accuracy: " + str(svc_scores[-1]) + "\n\n")

logfile.write("AVG test scores: " + str(np.average(rf_scores)) + ", " + str(np.std(rf_scores)) + "\n\n")
resfile.write(dataset + "," + "halk" + "," + sys.argv[2] + "," + "SVC" + "," +
              str(np.average(rf_scores)) + "," + str(np.std(rf_scores)) + "\n")
logfile.close()
resfile.close()