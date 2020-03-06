import requests
import gzip
import json
import csv
from collections import OrderedDict
import os

def ontology_csv(ontology):
    custom_header = {'Accept-Encoding': 'gzip'}
    r = requests.get(f'http://data.bioontology.org/ontologies/{ontology}/download?apikey=8b5b7825-538d-40e0-9e9e-5ab9274a9aeb&download_format=csv', headers = custom_header, stream=True)
    #r.raw.decode_content = True
    f = gzip.GzipFile(fileobj = r.raw)
    reader = csv.DictReader(line.decode('UTF-8') for line in f)
    reader.fieldnames = list([n.lower().replace(' ','_') for n in reader.fieldnames])
    for row in reader:
        row['synonyms'] = row['synonyms'].split('|')
        row['semantic_types'] = row['semantic_types'].split('|')
        row['parents'] = row['parents'].split('|')
        x = dict()
        for idx, key in enumerate(row.keys()):
            x['ontology'] = ontology
            if 0 <= idx < 8:
                if(row[key]==''):
                    x[key] = None
                else:
                    x[key] = row[key]
                if(row[key]==['']):
                    x[key] = []
        yield(x)

def get_all_ontology_short_ids():
    import yaml
    yaml_string = requests.get('https://raw.githubusercontent.com/OBOFoundry/OBOFoundry.github.io/master/_config.yml')
    val = yaml.load(yaml_string.content)
    x = []
    for onto in val['ontologies']:
        x.append(onto['id'].upper())
    return(x)

        
if __name__ == '__main__':
    for onto in sorted(get_all_ontology_short_ids()):
        print(onto)
        with open(onto + '.json', 'w') as outfile:
            try:
                for line in ontology_csv(onto):
                    outfile.write(json.dumps(line) + "\n")
            except KeyboardInterrupt:
                exit(0)
            except:
                os.unlink(onto + '.json')
                print(f'error with {onto}')
                continue

