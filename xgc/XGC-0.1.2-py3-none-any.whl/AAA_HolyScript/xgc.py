import json,inspect,pathlib,os
from pathlib import Path,PurePath
import sys
import numpy as np

input_values = {}

#This json encoder will convert all "numpy" values stored in a df or list (that cannot be converted into json)  into json-able objects.
class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)

def init():
    #Init will look for the inputs of the scripts being called by XGC and will save them into a global variable for subsequent use.
    #Init WILL always return values and paths of the calling script.
    #The identification of the inputs will be as shown below:
    
    #For command line values where the code is runned along with the input,
    # 1.Init will look at the first argument of the line    
    if len(sys.argv) > 1:
        input_file = str(PurePath(sys.argv[1]))
    
    #For all other cases,  
    #2. Init will first try to idenitify a json with the same filename in the same folder.
    else:
        #Path from this (XGC) script
        path= PurePath(inspect.stack()[1].filename)
        
        try:
            p1=str((path.parent/path.stem).with_suffix('.json'))
            f = open(p1)
            f.close()
            input_file = p1
            
        #3. If it doesn't find it, Init will look for file called main.json on the same folder.    
        except FileNotFoundError:
            
            #3.1 Starting on the folder of the script calling xgc
            try:
                input_file = str(path.parent/'main.json')
            #3.2 And ending on the script where XGC is in
            except:
                input_file = str(PurePath(sys.argv[1]).parent/'main.json')
    
    
    # Checks if the file exists and if it doesn't it displays an error.
    global input_values
    try:
        with open(input_file) as f:
            f2=f.read()
            input_values = json.loads(f2)
    except IOError :   
        print("File not accessible")
        raise IOError


#This fucntion will return a dict with all the requested input data.
def get_input_file(input_name):
    return input_values[input_name]

def get_input_values(input_name):
    return input_values[input_name]

#This function will create/update a json with a specified name (Which should be the name of a script) and it will be filled with information provided in a dict format (inputs)
def update_file(inputs,update_script_name,update_variable_name,update_variable_values):
    path= PurePath(inspect.stack()[1].filename)
    
    with open(str((path.parent/update_script_name).with_suffix(".json")),'w') as f:
        inputs[update_variable_name]=update_variable_values
        json.dump({update_script_name:inputs},f,cls=NpEncoder)
    return

def get_output_file(output_name):
    return input_values[output_name]


def error(err):
    print("ERROR: " + err)


def log(msg):
    print("LOG: " + msg)


def success(msg):
    print("SUCCESS: " + msg)


def progress(portion):
    print("PROGRESS: " + str(portion * 100) + "%")

