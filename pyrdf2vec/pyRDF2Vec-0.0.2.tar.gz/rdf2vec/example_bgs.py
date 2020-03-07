import random
import os
import numpy as np

os.environ['PYTHONHASHSEED'] = '42'
random.seed(42)
np.random.seed(42)

import rdflib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.manifold import TSNE

from graph import rdflib_to_kg
from rdf2vec import RDF2VecTransformer

from walkers import (RandomWalker, WeisfeilerLehmanWalker, 
					 AnonymousWalker, WalkletWalker, NGramWalker,
					 CommunityWalker)

import warnings
warnings.filterwarnings('ignore')

# Load the data with rdflib
print(end='Loading data... ', flush=True)
g = rdflib.Graph()
g.parse('../data/BGS/BGS.nt', format='nt')
print('OK')

# Load our train & test instances and labels
test_data = pd.read_csv('../data/BGS/BGS_test.tsv', sep='\t')
train_data = pd.read_csv('../data/BGS/BGS_train.tsv', sep='\t')

train_people = [rdflib.URIRef(x) for x in train_data['rock']]
train_labels = train_data['label_lithogenesis']

test_people = [rdflib.URIRef(x) for x in test_data['rock']]
test_labels = test_data['label_lithogenesis']

all_labels = list(train_labels) + list(test_labels)

# Define the label predicates, all triples with these predicates
# will be excluded from the graph
label_predicates = [
        rdflib.term.URIRef('http://data.bgs.ac.uk/ref/Lexicon/hasLithogenesis'),
        rdflib.term.URIRef('http://data.bgs.ac.uk/ref/Lexicon/hasLithogenesisDescription'),
        rdflib.term.URIRef('http://data.bgs.ac.uk/ref/Lexicon/hasTheme')
]

# Convert the rdflib to our KnowledgeGraph object
kg = rdflib_to_kg(g, label_predicates=label_predicates)

com_walker = CommunityWalker(2, float('inf'))

# Create embeddings with random walks
transformer = RDF2VecTransformer(walkers=[com_walker], sg=1)
walk_embeddings = transformer.fit_transform(kg, train_people + test_people)

# Fit model on the walk embeddings
train_embeddings = walk_embeddings[:len(train_people)]
test_embeddings = walk_embeddings[len(train_people):]

rf =  RandomForestClassifier(random_state=42, n_estimators=100)
rf.fit(train_embeddings, train_labels)

print('Random Forest:')
print(accuracy_score(test_labels, rf.predict(test_embeddings)))
print(confusion_matrix(test_labels, rf.predict(test_embeddings)))

clf =  GridSearchCV(SVC(random_state=42), {'kernel': ['linear', 'poly', 'rbf'], 'C': [10**i for i in range(-3, 4)]})
clf.fit(train_embeddings, train_labels)

print('Support Vector Machine:')
print(accuracy_score(test_labels, clf.predict(test_embeddings)))
print(confusion_matrix(test_labels, clf.predict(test_embeddings)))