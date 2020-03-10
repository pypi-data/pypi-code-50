
import json
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
def read_json(filename):
    with open(f'{dir_path}/../assets/json/{filename}.json', 'r') as json_file:

        data = json.load(json_file)
        
    return data

def write_json(filename, data):
    
    with open(f'{dir_path}/../assets/json/{filename}.json', 'w') as outfile:
        json.dump(data, outfile)
def append_json(filename, data):
    with open(f'{dir_path}/../assets/json/{filename}.json', 'w') as outfile:
        json.dump(data, outfile)
def json_parse(data):
    data = json.dumps(data)
    data = json.loads(data)
    return(data)
if __name__ == '__main__':
    print(read_json('previous'))