import random
import os
import numpy as np

os.environ['PYTHONHASHSEED'] = '42'
random.seed(42)
np.random.seed(42)

import rdflib
import pandas as pd

from graph import rdflib_to_kg
from walkers import (RandomWalker, WeisfeilerLehmanWalker, 
					 AnonymousWalker, WalkletWalker, NGramWalker,
					 CommunityWalker, HalkWalker)

import warnings
warnings.filterwarnings('ignore')

WALK_DEPTH = 2
MAX_WALKS = float('inf')

# Load the data with rdflib
print(end='Loading data... ', flush=True)
g = rdflib.Graph()
g.parse('../data/mutag.owl')
print('OK')

# Load our train & test instances and labels
test_data = pd.read_csv('../data/MUTAG_test.tsv', sep='\t')
train_data = pd.read_csv('../data/MUTAG_train.tsv', sep='\t')

train_entities = [rdflib.URIRef(x) for x in train_data['bond']]
train_labels = train_data['label_mutagenic']

test_entities = [rdflib.URIRef(x) for x in test_data['bond']]
test_labels = test_data['label_mutagenic']

all_labels = list(train_labels) + list(test_labels)
all_entities = train_entities + test_entities

# Define the label predicates, all triples with these predicates
# will be excluded from the graph
label_predicates = [
    rdflib.term.URIRef('http://dl-learner.org/carcinogenesis#isMutagenic')
]

# Convert the rdflib to our KnowledgeGraph object
kg = rdflib_to_kg(g, label_predicates=label_predicates)

# Define our walking strategies
random_walker = RandomWalker(WALK_DEPTH, MAX_WALKS)
ano_walker = AnonymousWalker(WALK_DEPTH, MAX_WALKS)
walklet_walker = WalkletWalker(WALK_DEPTH, MAX_WALKS)
ngram_walker = NGramWalker(WALK_DEPTH, MAX_WALKS, n_wildcards=1)
wl_walker = WeisfeilerLehmanWalker(WALK_DEPTH, MAX_WALKS)
com_walker = CommunityWalker(WALK_DEPTH, MAX_WALKS)
halk_walker = HalkWalker(WALK_DEPTH, MAX_WALKS, freq_threshold=0.1)

walkers = [
	('random', random_walker),
	('anon', ano_walker),
	('walklet', walklet_walker),
	('ngram', ngram_walker),
	('wl', wl_walker),
	('com', com_walker),
	('halk', halk_walker),
]

# Generate the corpus for each strategy
for name, walker in walkers:
	file_name = 'walks_{}.txt'.format(name)
	walker.print_walks(kg, all_entities, file_name)