"""
We want the project to start with...
* base directory
* project name

create the following directories
* models
* references
* data
* results
@todo: add a clean_up method to get rid of any unreferenced data files
"""
import json
import pickle
import os
import sys
import secrets
from pathlib import Path
from time import time
import boto3
from datetime import datetime
import numpy as np
import pandas as pd
from functools import lru_cache

hm = str(Path.home())

run_attributes = {
"X_train": "",
"y_train": "",
"X_test": "", 
"y_test": "",
"X_validate": "",
"y_validate": "",
"X_infer": "",
"references": {},
"param_grid": {},
"prep": "",
"algorithm": "",
"training_report": "",
"test_report": "",
"comments": "",
"seed": "",
"date": ""
}

line_attr = {
"id": 8,
"algorithm": 16,
"gold": 6,
"date": 14,
"comments": 36
}

set_types = ['X_train', 'y_train', 'X_test', 'y_test', 'X_validate', 'y_validate', 'X_infer']

s3 = boto3.resource('s3')
CACHE_SIZE = 8

def are_you_sure(name):
    """
    @doc: Get user input about whether or not to delete a project
    @args: name is a str for the project name (corresponds to a directory)
    @return: user input str ('yes' | 'no')
    """
    message = """Enter 'yes' (no quotes) to proceed with deleting the {} project
    and starting over, and 'no' to keep the existing project:   
    """.format(name)

    ret = input(message)
    return ret

def print_line(line):
    """
    @doc: print information about a particular model run
    @args: line is a dict with {'id', 'algorithm', 'gold', 'date', 'comments'} information
    @return: a line ready to print in the table (for Project.print_runs() method)
    """
    ret = "|"
    for key in line.keys():
        key_len = len(line[key])
        col_len = line_attr[key]
        if key_len > (col_len - 2):
            line[key] = line[key][:col_len - 2]

        spaces = " " * (col_len - key_len)
        ret = ret + spaces + line[key] + " |"

    return ret

def store_object(serializer, model_object, filename, remote, bucket):
    """
    @doc: a generalization of the object storage; works for pickle and json... maybe others
    @args: serializer is a serialization method that like `pickle.dump`
           model_object is the Python object to be stored
           filename is the desired name of the file either locally (full path) or on S3 (i.e. 'Key')
           remote is a boolean for whether or not to store it on S3
           bucket is the bucket object to use for remote storage
    @return: None
    """
    tmp_dir = filename[:filename.find("/")]
    json_object = filename[-4:].lower() == 'json'
    if remote:
        if json_object:
            serializer(model_object, open("{0}/{1}/tmp_object".format(hm, tmp_dir), "w"), indent = 4)
        else:
            try:
                serializer(model_object, open("{0}/{1}/tmp_object".format(hm, tmp_dir), "wb"))
            except:
                serializer(model_object, open("{0}/{1}/tmp_object".format(hm, tmp_dir), "w"))
        bucket.upload_file(Key = filename, Filename = "{0}/{1}/tmp_object".format(hm, tmp_dir))
        os.remove("{0}/{1}/tmp_object".format(hm, tmp_dir))
    else:
        if json_object:
            serializer(model_object, open(filename, "w"), indent = 4)
        else:
            try:
                serializer(model_object, open(filename, "wb"))
            except:
                serializer(model_object, open(filename, "w"))
    return

@lru_cache(maxsize = CACHE_SIZE)
def get_object(deserializer, filename, remote, bucket):
    """
    @doc: a generalization of the object fetching; works for pickle and json... maybe others
    @args: deserializer is a deserialization method that like `pickle.load`
           filename is the location of the file either locally (full path) or on S3 (i.e. 'Key')
           remote is a boolean for whether or not to fetch it from S3
           bucket is the bucket object to use for remote
    @return: the deserialized object
    @note: This implements a cache to save time for repeated calls to S3.  It can have some
           unintended consequences.  If you suspect that you're not getting the most recent
           object (either from S3 or locally) then run `project.clear_object_cache()` and try
           again.
    """
    tmp_dir = filename[:filename.find("/")]
    json_object = filename[-4:].lower() == 'json'
    
    if remote:
        dfname = "{0}/{1}/tmp_object".format(hm, tmp_dir)
        bucket.download_file(Key = filename, Filename = dfname)
        if json_object:
            model_object = deserializer(open(dfname, "r"))
        else:
            try:
                model_object = deserializer(open(dfname, "rb"))
            except:
                model_object = deserializer(open(dfname, "r"))
        os.remove(dfname)
    else:
        if json_object:
            model_object = deserializer(open(filename, "r"))
        elif os.path.isfile(filename):
            try:
                model_object = deserializer(open(filename, "rb"))
            except:
                model_object = deserializer(open(filename, "r"))
            
    return model_object

def s3_isdir(directory, bucket):
    """
    @doc: check a bucket for a directory... yes, we know that S3 doesn't actually have directories
    @args: directory is a str of the directory to check
           bucket is a boto3.resource.Bucket object
    @return boolean whether or not the directory exists
    """
    if bucket is None:
        return False
    
    if directory[-1] != "/":
        directory = "{}/".format(directory)
    objs = list(bucket.objects.filter(Prefix = directory))
    return len(objs) > 0

def s3_isfile(filepath, bucket):
    """
    @doc: check a file for existence in an S3 bucket
    @args: filepath is a str
           bucket is a boto3.resource.Bucket object
    @return: boolean whether or not the file exists
    """
    if bucket is None:
        return False
    
    objs = list(bucket.objects.filter(Prefix = filepath))
    return len(objs) > 0 and objs[0].key == filepath

class Project():
    """
    @doc: Run the `create` method to start with
    """
    def __init__(self, name, base_dir = hm, verbose = False, remote = True):
        """
        @args: name is a str for the name of the project
               base_dir is a str for the base file path to start the project, if remote is True then
                   this is treated as an S3 location
               verbose is a boolean for whether or not to print some stuff
               remote is a boolean for whether or not to establish the project on S3 (instead of local)
        @note: when using remote, you should specify the `base_dir` as a bucket path (e.g. 'test-bucket/project/dir')
                   and NOT as an S3 URL (i.e. NOT like this 's3://test-bucket/project/dir')
               base_dir is intended to be a directory where many projects are stored, not specific to this project,
                   which will avoid unnecessary depth of directory when the projects is created.  
        @todo: need a `back_it_up` method that goes local -> s3 or s3 -> s3 or local/s3 -> zip
        """
        self.name = name
        self.base_dir = base_dir
        self.remote = remote
        self.run = None
        
        if remote:
            msg = """ 
Attempting to access or create a remote project...
If you notice memory issues set the CACHE_SIZE value to a lower number 
in your notebook with: `tracker.CACHE_SIZE = `
""".format("{0}/{1}".format(hm, name))
            print(msg)
            
            bucket_name = base_dir[:base_dir.find("/", 1)]
            
            sub_dir = base_dir[base_dir.find("/")+1:]
            if s3.Bucket(bucket_name) in s3.buckets.all():
                self.bucket = s3.Bucket(bucket_name)
                bucket = self.bucket
            else:
                msg = """`remote` is set to True, but the bucket name in the base_dir
that you specified ({0}) could not be created as a boto3.resource('s3').Bucket object.
It could be that the IAM configuration is not correct OR that the bucket name does not
exist.  The project is being created locally.  If this is in error, delete the project 
artifacts, fix the S3 issue, and start over.""".format(bucket_name)
                print(msg)
                self.remote = False
                self.bucket = None
                bucket = self.bucket
                remote = self.remote
                
            self.sub_dir = sub_dir
            self.project_dir = "{0}/{1}".format(sub_dir, name)
            
            if os.path.isdir("{0}/{1}".format(hm, name)):
                pass
            else:
                print("Making a directory ({}) to store temporary objects".format("{0}/{1}".format(hm, name)))
                os.mkdir("{0}/{1}".format(hm, name))
            
        if remote: # making a subsequent evaluation just in case it threw an error when creating the Bucket object
            if s3_isdir(sub_dir, bucket):
                filename = "{0}/{1}.json".format(self.project_dir, name)
                if s3_isfile(filename, bucket):
                    if verbose:
                        print("Found the project JSON file on S3... Loading it now")
                    self.load_it()
                else:
                    if verbose:
                        print("No project file found... Creating it on S3 and locally now.")
                    self.create_it()
            else:
                if verbose:
                    print("Creating the project on S3 and the blank JSON now")
                self.create_it()
        
        else:
            project_dir = "{0}/{1}".format(base_dir, name)
            json_name = name + ".json"
            self.project_dir = project_dir
            self.sub_dir = ""
            self.bucket = None
            
            if os.path.isdir(project_dir):
                if os.path.isfile(project_dir + json_name) or os.path.isfile(json_name):
                    if verbose:
                        print("Found the project JSON file... Loading it now")
                    self.load_it()
                else:
                    if verbose:
                        print("No project file found... Creating it now")
                    self.create_it()
            else:
                if verbose:
                    print("Creating the project directory and a blank project JSON.")
                self.create_it()
    
    def set_run(self, run):
        """
        """
        self.run = run
        return
    
    def create_it(self):
        """
        @doc: Create a project directory if necessary and set a project dictionary
        @args: None
        @return: None
        
        """
        base_dir = self.base_dir
        name = self.name
        project_dir = self.project_dir
        remote = self.remote
        bucket = self.bucket
        
        if remote:
            filename = "{0}/{1}.json".format(project_dir, name)
            self.project_dict = {
            "data": project_dir + "/data",
            "results": project_dir + "/results",
            "references": project_dir + "/references",
            "gold": "",
            "runs": [],
            "remote": remote
            }
            if s3_isfile(filename, bucket):
                msg = """
There is an existing project directory and project file on S3.  In order to avoid accidental 
overwrite the project will be reset.  You will need to EITHER recreate the project object
with a different name OR manually delete the existing stuff on S3.
            """
                print(msg)
                self.project_dict = None
        
        else:
            if not os.path.isdir(project_dir):
                os.mkdir(project_dir)
                os.mkdir(project_dir + "/models")
                os.mkdir(project_dir + "/references")
            if not os.path.isdir(project_dir + "/models"):
                os.mkdir(project_dir + "/models")
            if not os.path.isdir(project_dir + "/references"):
                os.mkdir(project_dir + "/references")
            if not os.path.isdir(project_dir + "/results"):
                os.mkdir(project_dir + "/results")
            if not os.path.isdir(project_dir + "/data"):
                os.mkdir(project_dir + "/data")

        self.project_dict = {
            "data": project_dir + "/data",
            "results": project_dir + "/results",
            "references": project_dir + "/references",
            "gold": "",
            "runs": [],
            "remote": remote
            }
        self.data_dir = self.project_dict['data']
        
        if os.path.isfile(project_dir + "/" + name + ".json"):
            msg = """
There is an existing project directory and project file.  In order to avoid accidental 
overwrite the project will be reset.  You will need to EITHER recreate the project object
with a different name OR manually delete the existing stuff locally.
            """
            print(msg)
            self.project_dict = None
            check = False
        else:
            self.save_it()
        return self

    def save_it(self, check = False):
        """
        @doc: Save a project JSON file to the base directory AND to the current working directory
        @args: check is a boolean for whether or not to backup and existing file... not used
        @return: None
        @note: the version saved to the current working directory is the one used with Git
        """
        base_dir = self.base_dir
        name = self.name
        project_dir = self.project_dir
        project_dict = self.project_dict
        remote = self.remote
        bucket = self.bucket
        
        if check:
            thetime  = datetime.now().strftime("%Y-%m-%d-%H:%M")
            filename = "{0}/{1}-{2}.json".format(project_dir, name, thetime)
            checker = json.load(open(project_dir + "/" + name + ".json", "r"))
            json.dump(checker, open(filename, "w"))
            
        if remote:
            json.dump(project_dict, open(name + ".json", "w"), indent = 4)
            bucket.upload_file(Key = "{0}/{1}.json".format(project_dir, name), Filename = "{}.json".format(name))
        else:
            filename = "{0}/{1}.json".format(project_dir, name)
            json.dump(project_dict, open(filename, "w"), indent = 4)
            json.dump(project_dict, open(name + ".json", "w"), indent = 4)
        return self

    def load_it(self):
        """
        @doc: Load a project_dict from its JSON file
        @args: None
        @return: None
        """
        base_dir = self.base_dir
        name = self.name
        project_dir = self.project_dir
        remote = self.remote
        bucket = self.bucket
        
        if remote:
            if os.path.isfile("./{}.json".format(name)):
                self.project_dict = json.load(open("./{}.json".format(name), "r"))
            else:
                bucket.download_file("./{}.json".format(name))
                self.project_dict = json.load(open("./{}.json".format(name), "r"))
        else:
            try:
                self.project_dict = json.load(open(name + ".json", "r"))
            except:
                filename= "{0}/{1}.json".format(project_dir, name)
                self.project_dict = json.load(filename, "r")
        self.data_dir = self.project_dict['data']
        return self

    def print_runs(self):
        """
        @doc: Print a table of some information about each run in the project
        @args: None
        @return: None
        """
        runs = self.project_dict['runs']
        gold = self.project_dict['gold']
        topline = ""
        for i in range(91):
            topline += "-"
        ret = topline + '\n'
        line = {'id': 'id', 'algorithm': 'algorithm', 'date': 'date', 'gold': 'gold', 'comments': 'comments'}
        ret = ret + print_line(line) + "\n"
        ret = ret + topline + '\n'

        for run in runs:
            the_run = self.get_run(run)
            the_id = run
            try:
                algorithm = the_run['algorithm']
            except:
                algorithm = ""
            date = the_run['date']
            the_gold = 'no'
            if run == gold:
                the_gold = 'yes'
            try:
                comments = the_run['comments'][:33]
            except:
                comments = ""
                
            line = {'id': the_id, 'algorithm': algorithm, 'date': date, 'gold': the_gold, 'comments': comments}
            ret = ret + print_line(line) + "\n"

        ret = ret + topline
        print(ret)
        return self

    def store_run(self, model_object = None, prep_object = None, gold = False, serializer = pickle.dump, **kwargs):
        """
        @doc: Pickle a model object and store some run attributes in a JSON file
        @args: model_object is a serializable-able model object
               gold is a Boolean for whether or not this is the Gold model run
               **kwargs according to acceptable run_attributes dictionary
        @return: run as a string
        @note: if working with an existing run, this will only update the 
                   parameters that you specify explicitly
        """
        remote = self.remote
        bucket = self.bucket
        run = self.run
        
        if run is None:
            run = secrets.token_hex(3)
        
        passed_attr = kwargs.keys()
        this_run = self.get_run(run = run, verbose = True)
        
        pops = []
        existing_references = {}
        
        if "references" in this_run.keys():
            existing_references = this_run['references']

        if "references" in passed_attr:
            new_references = kwargs['references']
            for key, val in new_references.items():
                filename = "{0}/references/{1}_{2}.json".format(self.project_dir, key, run)
                try:
                    store_object(json.dump, val, filename, remote, bucket)
                except:
                    print("Could not store the {} reference".format(key))
                existing_references.update({key: filename})
            
        for attr in passed_attr:
            if attr == 'references':
                this_run[attr] = existing_references
            elif attr in this_run.keys():
                this_run[attr] = kwargs[attr]

        for key, val in this_run.items():
            if len(val) == 0:
                pops.append(key)
        for pop in pops:
            hold = this_run.pop(pop, None)
        
        this_run['id'] = run
        this_run['date'] = datetime.today().strftime("%Y-%m-%d")
        
        if model_object is not None:
            filename = "{0}/models/{1}".format(self.project_dir, run)
            try:
                store_object(serializer, model_object, filename, remote, bucket)
            except:
                print("Could not serialize the model object")
        
        if prep_object is not None:
            filename = "{0}/models/prep_{1}".format(self.project_dir, run)
            try:
                store_object(serializer, prep_object, filename, remote, bucket)
            except:
                print("Could not serialize the prep object")
                
            this_run['prep'] = self.project_dir + "/models/prep_" + run
        
        update_run = self.get_run(run = run)
        
        update_run.update(this_run)
        
        filename = "{0}/{1}.json".format(self.project_dir, run)
        store_object(serializer = json.dump, 
                     model_object = update_run, 
                     filename = filename,
                     remote = remote, 
                     bucket = bucket)
        
        runs = self.project_dict['runs']
        if run not in runs:
            runs.append(run)
            runs = list(set(runs))
            self.project_dict['runs'] = runs
            _ = self.save_it()
        if gold:
            self.project_dict['gold'] = run
            _ = self.save_it()
            
        return run
    
    def clone_run(self, run):
        """
        @doc: allow the user to start from an existing run
        @args: run is a str of the modeling run that you want to clone
        @return: a string of the new run name
        @note: This will essentially copy new prep and model objects to the project_dir/models directory, 
               but will not create copies of the train/test/validate data. 
               This also sets the self.run to the new_run_name
        """
        new_run_name = secrets.token_hex(3)
        model_object, prep_object, old_run = self.load_run(run)
        self.run = new_run_name
        
        _ = self.store_run(model_object = model_object, 
                           prep_object = prep_object, 
                           **old_run)
        
        return new_run_name
    
    def load_run(self, run = None, deserializer = pickle.load, verbose = False):
        """
        @doc: Load a serialized model object and some run attributes from JSON
        @args: run is a 6 digit hex str
        @return: The un-pickled model objects and an attribute dictionary
        @note: this checks for a random seed and sets it using numpy
               this sets the self.run to the run specified, or the gold
               run if none is specified
        """
        remote = self.remote
        bucket = self.bucket
        
        if run is None:
            run = self.project_dict['gold']
        
        this_run = self.get_run(run = run, verbose = verbose)
        try:
            if len(this_run['seed']) > 0:
                seed = int(this_run['seed'])
                np.random.seed(seed)
        except:
            this_run['seed'] = 0
        
        filename = self.project_dir + "/models/" + run
        try:
            model_object = get_object(deserializer, filename, remote, bucket)
        except:
            if verbose:
                print("Couldn't find the {} model object".format(run))
            model_object = None
        
        filename = this_run['prep']
        
        try:
            prep_object = get_object(deserializer, 
                                     filename, 
                                     remote, 
                                     bucket)
        except:
            if verbose:
                print("Couldn't find a prep object... ignoring it.")
            prep_object = None
        
        this_run['references'] = self.load_references(run, verbose = True)
        
        self.run = run
        return model_object, prep_object, this_run
    
    def check_run(self, run):
        """
        @doc: check if a run is in the project's scope
        @args: run is a str run id
        @return: boolean for whether or not it's in there
        """
        runs = self.project_dict['runs']
        return run in runs
    
    def get_run(self, run = None, verbose = False):
        """
        @doc: get the run's dictionary wihtout loading model and prep objects
        @args: run is a 6 digit string identifier for the run
               verbose is a boolean for whether or not to print anything
        @return: a dict containing the run's information
        """
        remote = self.remote
        bucket = self.bucket
        if run is None:
            print("Using the gold run since no run was specified")
            run = self.project_dict['gold']
        if run == "":
            print("No run and no gold specified... nothing to get")
            this_run = {}
        else:
            filename = "{0}/{1}.json".format(self.project_dir, run)
            self.clear_object_cache()
            if remote:
                try:
                    run_dict = get_object(json.load, 
                                          filename = filename, 
                                          remote = remote, 
                                          bucket = bucket) 
                    this_run = run_attributes.copy()
                    this_run.update(run_dict)
                    
                except:
                    if verbose:
                        print("Could not find the run on S3... creating a new one")
                    this_run = run_attributes.copy()
                    store_object(json.dump, 
                                 this_run, 
                                 filename = filename, 
                                 remote = remote, 
                                 bucket = bucket)
            else:
                try:
                    this_run = json.load(open(filename, "r"))
                except:
                    if verbose:
                        print("Could not find the run specified... creating a new one")
                    this_run = run_attributes.copy()
                    store_object(json.dump, 
                                 this_run, 
                                 filename = filename, 
                                 remote = remote, 
                                 bucket = bucket)
        
        return this_run
    
    def load_references(self, run, verbose = False):
        """
        """
        remote = self.remote
        bucket = self.bucket
        name = self.name
        
        if run is None and self.run is None:
            print("You must specify a run since current run is not yet initialized")
            return None
        if run is None:
            run = self.run
        
        run_dict = self.get_run(run)
        references = run_dict["references"]
        ref_names = list(references.keys())
        ret = {}
        
        for key, val in references.items():
            ref = get_object(json.load, val, remote, bucket)
            ret[key] = ref
            if verbose:
                print("Loaded a {0} under the key {1}".format(type(ref), key))
        
        return ret
    
    def store_data(self, data, set_type = "X_train", index = False, verbose = False):
        """
        @doc: a convenience method for writing data to the local disk
        @args: data is either a text blob (probably representing some SQL) or
                   a pandas DataFrame or a numpy array
               
               set_type is one of the allowable set types (e.g. 'X_train'... see tracker.set_types)
               index is a boolean for whether or not to write the index to CSV 
                   (only used if data is a pandas DataFrame)
               verbose is a boolean for whether or not to print anything
        @return: a tuple of the run string and the data path string
        @note: if no run is specified it will initialize a new identifier... 
        """
        remote = self.remote
        bucket = self.bucket
        name = self.name
        run = self.run
        
        if set_type not in set_types:
            print("You supplied {0} for the set_type, but only one of {1} is allowed.".format(set_type, set_types))
            return
        
        if run is None:
            run = secrets.token_hex(3)
            print("No run set... run is {}".format(run))
            self.run = run
        
        if remote:
            if isinstance(data, str):
                filename = "{0}/{1}/temp_data.txt".format(hm, name)
                data_str = "{0}/data/{1}_{2}.txt".format(self.project_dir, set_type, run)
                with open(filename, "w") as file:
                    file.write(data)
                bucket.upload_file(Key = data_str, Filename = filename)
                os.remove(filename)

            else:
                filename = "{0}/{1}/temp_data.csv".format(hm, name)
                data_str = "{0}/data/{1}_{2}.csv".format(self.project_dir, set_type, run)
                try:
                    data.to_csv(filename, index = index, header = True)
                    bucket.upload_file(Key = data_str, Filename = filename)
                    os.remove(filename)
                    if verbose:
                        print("stored data using pandas")
                except:
                    try:
                        np.savetxt(X = data, fname = filename, delimiter = ",")
                        bucket.upload_file(Key = data_str, Filename = filename)
                        os.remove(filename)
                        if verbose:
                            print("stored data using numpy")
                    except:
                        print("Could not store the data to {} for some reason".format(data_str))
                        data_str = None

        else:
            
            if isinstance(data, str):
                data_str = "{0}/data/{1}_{2}.txt".format(self.project_dir, set_type, run)
                with open(data_str, "w") as file:
                    file.write(data)

            else:
                data_str = "{0}/data/{1}_{2}.csv".format(self.project_dir, set_type, run)
                try:
                    data.to_csv(data_str, index = index)
                    if self.verbose:
                        print("stored data using pandas")
                except:
                    try:
                        np.savetxt(X = data, fname = data_str, delimiter = ",")
                        if verbose:
                            print("stored data using numpy")
                    except:
                        print("Could not store the data to {} for some reason".format(data_str))
                        data_str = None

        kwarg = {}
        kwarg[set_type] = data_str
        
        _ = self.store_run(run = run, **kwarg)
        return run, data_str
    
    def load_data(self, run = None, set_type = "X_train", delim = ",", skiprows = 0, verbose = False):
        """
        @doc: get either an array of data OR a text blob (presumably a query of some kind)
        @args: run is a str of the 6 digit run identifier
               set_type is one of the allowable set types (e.g. 'X_train'... see tracker.set_types)
               delim is the delimiter used in the file
               skiprows is an int of the number of rows to skip (default: 0)
        @return: either a numpy array OR a text blob
        @note: if the set_type in the run dict is a CSV it will load a numpy array
               if the set_type in the run dict is TXT it will try a numpy array,
                   and then fail over to a text blob
               IF you want to load a pandas DataFrame, use pd.read_csv() directly on the 
                   file path stored in the run dictionary.
        """
        remote = self.remote
        bucket = self.bucket
        name = self.name
        
        if run is None and self.run is None:
            print("You must specify a run since current run is not yet initialized")
            return None
        if run is None:
            run = self.run
        
        run_dict = self.get_run(run)
        data_str = run_dict[set_type]
        
        if remote:
            if data_str[-3:].lower() == 'txt':
                filename = "{0}/{1}/temp_data.txt".format(hm, name)
                bucket.download_file(Key = data_str, Filename = filename)
                try:
                    ret = np.loadtxt(filename, delimiter = delim, skiprows = skiprows)
                    if verbose:
                        print("loaded a TXT file using numpy")
                except:
                    with open(filename, "r") as file:
                        ret = file.read()
                    if verbose:
                        print("loaded TXT file to a blob")
                os.remove(filename)
                
            elif data_str[-3:].lower() == 'csv':
                filename = "{0}/{1}/temp_data.csv".format(hm, name)
                
                bucket.download_file(Key = data_str, Filename = filename)
                try:
                    ret = np.loadtxt(filename, delimiter = delim, skiprows = skiprows)
                except:
                    ret = pd.read_csv(filename, sep = delim, skiprows = skiprows)
                if verbose:
                    print("loaded a CSV file using numpy")
                os.remove(filename)
            else:
                if verbose:
                    msg = """Not a TXT or CSV file extension... 
not sure what to do, but trying a numpy load with a '{}' delimiter.
Failing that, loading it as a text blob.""".format(delim)
                    print(msg)
                filename = "{0}/{1}/temp_data".format(hm, name)
                bucket.download_file(Key = data_str, Filename = filename)
                try:
                    ret = np.loadtxt(data_str, delimiter = delim, skiprows = skiprows)
                except:
                    with open(filename, "r") as file:
                        ret = file.read()
                os.remove(filename)
        else:
            if data_str[-3:].lower() == 'txt':
                try:
                    ret = np.loadtxt(data_str, delimiter = delim, skiprows = skiprows)
                    if verbose:
                        print("loaded a TXT file using numpy")
                except:
                    with open(data_str, "r") as file:
                        ret = file.read()
                    if verbose:
                        print("loaded TXT file to a blob")

            elif data_str[-3:].lower() == 'csv':

                ret = np.loadtxt(data_str, delimiter = delim, skiprows = skiprows)
                if verbose:
                    print("loaded a CSV file using numpy")
            else:
                if verbose:
                    msg = """Not a TXT or CSV file extension... 
                    not sure what to do, but trying a numpy load
                    with a '{}' delimiter""".format(delim)
                    print(msg)
                ret = np.loadtxt(data_str, delimiter = delim, skiprows = skiprows)
            
        return ret
    
    def remove_run(self, run, verbose = False):
        """
        @doc: a convenience method to remove a run from the project
        @args: run is a 6 digit str identifier to remove
        @return: just the project object
        @note: this will only remove things that are named according to the run identifier.
               (i.e. it will not remove data referred to by the run if that data is based on 
                a different run)
        """
        project_dir = self.project_dir
        run_dict = run_attributes.copy()
        run_dict.update(self.get_run(run))
        prep = run_dict['prep']
        remote = self.remote
        bucket = self.bucket
        references = run_dict['references']
        
        if remote:
            filename = "{0}/{1}.json".format(project_dir, run)
            if s3_isfile(filename, bucket):
                bucket.Object(key = filename).delete()
                if verbose: 
                    print("removed {}".format(filename))
                
            filename = "{0}/models/{1}".format(project_dir, run)
            if s3_isfile(filename, bucket):
                bucket.Object(key = filename).delete()
            
            filename = "{0}/models/prep_{1}".format(project_dir, run)
            if s3_isfile(filename, bucket):
                bucket.Object(key = filename).delete()

            for set_type in set_types:
                filename = run_dict[set_type]
                if len(filename) > 0 and s3_isfile(filename, bucket) and run in filename:
                    bucket.Object(key = filename).delete()
            
            for key, val in references.items():
                if len(val) > 0 and s3_isfile(val, bucket) and run in val:
                    bucket.Object(key = val).delete()
        
        else:
            filename = "{0}/{1}.json".format(project_dir, run)
            if os.path.isfile(filename):
                os.remove("{0}/{1}.json".format(project_dir, run))

            if os.path.isfile("{0}/models/{1}".format(project_dir, run)):
                os.remove("{0}/models/{1}".format(project_dir, run))

            if os.path.isfile("{0}/models/prep_{1}".format(project_dir, run)):
                os.remove("{0}/models/prep_{1}".format(project_dir, run))

            for set_type in set_types:
                filename = run_dict[set_type]
                if len(filename) > 0 and os.path.isfile(filename) and run in filename:
                    os.remove(filename)
                    
            for key, val in references.items():
                if len(val) > 0 and os.path.isfile(val, bucket) and run in val:
                    os.remove(val)
        
        _ = self.project_dict['runs'].remove(run)
        _ = self.save_it()
        return self
    
    def pprint_run(self, run = None):
        """
        @doc: print the modeling run information from the appropriate dictionary
        @args: run is a str of the model run id... if None then tries the current then the gold run
        @return: None
        """
        project_dict = self.project_dict
        gold = project_dict['gold']
        if run is not None:
            pass
        elif self.run is not None:
            run = self.run
        elif len(gold) == 6:
            run = gold
        else:
            print("You must either specify a run str as an argument, or have a gold or current run")
            return
        
        run_dict = self.get_run(run)
        msg = "The run information for run id {}".format(run_dict['id'])
        
        for key in run_attributes.keys():
            spaces = " " * (27 - len(key))
            if key == 'id':
                pass
            elif len(run_dict[key]) < 1:
                val = "{0}{1} : No value specified...".format(key, spaces)
            elif key == 'param_grid':
                val = "Hyperparameter Grid{}  : ".format(spaces)
                for pkey, pval in run_dict[key].items():
                    pkey = pkey[:18]
                    long_spaces = " " * (20 - len(pkey))
                    hold = "    {0}{1} -> {2}".format(pkey, long_spaces, pval)
                    val = "{0}\n{1}".format(val, hold)
            elif "report" in key:
                val = run_dict[key]
            elif key == 'references':
                val = "Reference Object Locations  : "
                for pkey, pval in run_dict[key].items():
                    pkey = pkey[:18]
                    long_spaces = " " * (20 - len(pkey))
                    hold = "    {0}{1} -> {2}".format(pkey, long_spaces, pval)
                    val = "{0}\n{1}".format(val, hold)
            else:
                val = "{0}{1} : {2}".format(key, spaces, run_dict[key])
            msg = "{0}\n{1}".format(msg, val)
        print(msg)
        
        return
    
    def clear_object_cache(self):
        """
        @doc: flushes the cache of the get_object function
        @args: None
        @return: None
        """
        get_object.cache_clear()
        return