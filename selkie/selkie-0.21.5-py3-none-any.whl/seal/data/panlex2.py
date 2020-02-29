
import csv
from os.path import join
from seal.core.config import get

panlex_dir = get('data.panlex') or \
             raise Exception("Configuration key not set: 'data.panlex'")

def topen (name):
    return open(join(panlex_dir, name + '.csv'))

rdr = csv.reader

def print_header (name):
    with topen(name) as f:
        print(next(rdr(f)))
