# -*- coding: utf-8 -*-
"""
Lightweight Functional interface to wrap access to Deep Learning, RLearning models.
Logic follows Scikit Learn API and simple for easy extentions logic.
Goal to facilitate Jupyter to Prod. models.


Models are stored in model_XX/  or in folder XXXXX
    module :  folder/mymodel.py, contains the methods, operations.
    model  :  Class in mymodel.py containing the model definition, compilation
   

models.py   #### Generic Interface
   module_load(model_uri)
   model_create(module)
   fit(model, module, session, data_pars, out_pars   )
   metrics(model, module, session, data_pars, out_pars)
   predict(model, module, session, data_pars, out_pars)
   save()
   load()
 

####################################################################################################
######### Code sample  #############################################################################
https://github.com/arita37/mlmodels/blob/dev/README_model_list.md



######### Command line sample  #####################################################################
#### generate config file
python mlmodels/models.py  --do generate_config  --model_uri model_tf.1_lstm.py  --save_folder "c:\myconfig\" 

#### Cusomt Directory Models
python mlmodels/models.py --do test  --model_uri "D:\_devs\Python01\gitdev\mlmodels\mlmodels\model_tf\1_lstm.py"


### RL model
python  models.py  --model_uri model_tf.rl.4_policygradient  --do test

### TF DNN model
python  models.py  --model_uri model_tf.1_lstm.py  --do test

## PyTorch models
python  models.py  --model_uri model_tch.mlp.py  --do test


"""
import argparse
import glob
import inspect
import json
import os
import re
import sys
from importlib import import_module
from pathlib import Path
from warnings import simplefilter

####################################################################################################
from mlmodels.util import (get_recursive_files, load_config, log, os_package_root_path )


from mlmodels.util import (env_build, env_conda_build, env_pip_requirement)


simplefilter(action='ignore', category=FutureWarning)
simplefilter(action='ignore', category=DeprecationWarning)








####################################################################################################
def module_env_build(model_uri="", verbose=0, env_build=0):
    """
      Load the file which contains the model description
      model_uri:  model_tf.1_lstm.py  or ABSOLUTE PATH
    """
    # print(os_file_current_path())
    model_uri = model_uri.replace("/", ".")
    module = None
    if verbose : 
      print(model_uri)

    #### Dynamic ENV Build based on requirements.txt
    if env_build :
      env_pars = {"python_version" : '3.6.5'}
      env_build(model_uri, env_pars)



def module_load(model_uri="", verbose=0, env_build=0):
    """
      Load the file which contains the model description
      model_uri:  model_tf.1_lstm.py  or ABSOLUTE PATH
    """
    # print(os_file_current_path())
    model_uri = model_uri.replace("/", ".")
    module = None
    if verbose : 
      print(model_uri)

    try :
      #### Import from package mlmodels sub-folder
      model_name = model_uri.replace(".py", "")
      module     = import_module( f"mlmodels.{model_name}")
      #module    = import_module("mlmodels.model_tf.1_lstm")

    except Exception as e1 :
      try :
        ### Add Folder to Path and Load absoluate path model
        path_parent = str( Path( model_uri).parent.absolute())
        sys.path.append( path_parent )
        # print(path_parent, sys.path)
        
        #### import Absilute Path model_tf.1_lstm
        model_name = Path(model_uri).stem  # remove .py
        model_name = str(Path(model_uri).parts[-2]) +"."+ str(model_name )
        #print(model_name)
        module     = import_module(model_name)
        
      except Exception as e2:
        raise NameError( f"Module {model_name} notfound, {e1}, {e2}")
        
    if verbose: print(module)
    return module



def module_load_full(model_uri="", model_pars=None, data_pars=None, compute_pars=None, choice=None,  **kwarg):
  """
    Create Instance of the model, module
    model_uri:  model_tf.1_lstm.py
  """
  module = module_load(model_uri=model_uri)
  model  = module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars, **kwarg)
  return module, model


def model_create(module, model_pars=None, data_pars=None, compute_pars=None, **kwarg):
    """
      Create Instance of the model from loaded module
      model_pars : dict params
    """
    if model_pars is None :
      model_pars = module.get_params()

    model = module.Model(model_pars=model_pars, data_pars=data_pars, compute_pars=compute_pars, **kwarg)
    return model



def fit(module, model, sess=None, data_pars=None, compute_pars=None, out_pars=None,  **kwarg):
    """
    Wrap fit generic method
    :type model: object
    """
    return module.fit(model, sess,  data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)


def predict(module, model, sess=None, data_pars=None, compute_pars=None,  out_pars=None,  **kwarg):
    """
       predict  using a pre-trained model and some data
    :return:
    """
    return module.predict(model, sess, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars, **kwarg)


def fit_metrics(module, model, sess=None, data_pars=None, compute_pars=None,  out_pars=None, **kwarg):
  return module.fit_metrics(model, sess, data_pars, compute_pars, out_pars, **kwarg)



def metrics(module, model, sess=None, data_pars=None, compute_pars=None,  out_pars=None, **kwarg):
  return module.metrics(model, sess, data_pars, compute_pars, out_pars, **kwarg)



def load(load_pars, **kwarg):
    """
       Load model/session from files
    :param folder_name:
    :return:
    """
    from mlmodels.util import (load_pkl, load_gluon, load_keras,
                               load_tch, load_tf)

    path = load_pars['path']
    model_type = load_pars['model_type']
    filename = load_pars['filename']


    if model_type == "model_tf" :
        return load_tf(path, filename)

    if model_type == "model_tch" :
        return load_tch(path)

    if model_type == "model_gluon" :
        return load_gluon(path)

    if model_type == "model_keras" :
        return load_keras(path)

    else :
        return load_pkl(path)


def save(model, session, save_pars , **kwarg):
    """
       Save model/session on disk
    (path, modelname="model_default", model_type="tf",  model_session=None, ** kwarg)
    :return:
    """
    from mlmodels.util import (save_pkl, save_gluon, save_keras,
                               save_tch, save_tf)

    d = save_pars
    path = d['path']
    model_type  = d['model_type']
    model_uri   = d['model_uri'].replace(".", "_")


    if model_type == "model_tf" :
      os.makedirs(path, exist_ok = True)
      file_path = f"{path}/{model_uri}.ckpt"
      save_tf(session, file_path)
      print(file_path)
      return 1      


    if  model_type == "model_tch"  :
       save_tch(model, session, path)


    if  model_type == "model_keras"  :
       save_keras(model,  path)


    if  model_type == "model_gluon"  :
       save_gluon(model,  path)


    else :
       save_pkl(model,  path)





####################################################################################################
####################################################################################################
def test_all(folder=None):
    if folder is None :
       folder =  os_package_root_path() +  "/model_tf/"
            
    # module_names = get_recursive_files(folder, r"[0-9]+_.+\.py$")
    module_names  = config_model_list()
    module_names.sort()
    print(module_names)
    failed_scripts = []

    for module_name in module_names:
        print("#######################")
        print(module_name)
        test(module_name)



def test(modelname):
    print(modelname)
    try :
      module = module_load( modelname , verbose=1)
      print(module)
      module.test()
      del module
    except Exception as e:
      print("Failed", e)


def test_global(modelname):
    print(modelname)
    try :
      module = module_load( modelname , verbose=1)
      print(module)
      module.test_global()
      del module
    except Exception as e:
      print("Failed", e)


def test_api(model_uri, model_pars, data_pars, compute_pars, out_pars, save_pars=None) :
    log("############ Model preparation   ##################################")
    from mlmodels.models import module_load_full
    from mlmodels.models import fit as fit_global
    from mlmodels.models import predict as predict_global
    from mlmodels.models import save as save_global, load as load_global

    module, model = module_load_full(model_uri, model_pars, data_pars, compute_pars)
    print(module, model)


    log("############ Model fit   ##########################################")
    model, sess = fit_global(module, model, data_pars=data_pars, compute_pars=compute_pars, out_pars=out_pars )
    print("fit success", sess)


    log("############ Prediction############################################")
    preds = predict_global(module, model, sess, data_pars=data_pars,
                           compute_pars=compute_pars, out_pars=out_pars)
    print(preds)


    log("############ Save/ Load ############################################")
    #save_global( save_pars, model, sess)

    #load_global(save_pars)


def test_module(model_uri, model_pars, data_pars, compute_pars, out_pars, save_pars=None) :
    ###loading the command line arguments
    #model_uri = "model_xxxx/yyyy.py"

    log("#### Module init   ############################################")
    from mlmodels.models import module_load
    module = module_load(model_uri)
    log(module)


    log("#### Loading params   ##############################################")
    #model_pars, data_pars, compute_pars, out_pars = module.get_params(choice=pars_choice,
    #                                                                  data_path=data_path)


    log("#### Model init   ############################################")
    from mlmodels.models import model_create 
    model = model_create(module, model_pars)
    log(model)


    log("#### Fit   ########################################################")
    model, sess = module.fit(model, data_pars, model_pars, compute_pars, out_pars )


    log("#### Predict   ####################################################")
    ypred = module.predict(model, sess, data_pars, compute_pars, out_pars)
    print(ypred)


    log("#### Get  metrics   ################################################")
    metrics_val = module.fit_metrics(model, data_pars, compute_pars, out_pars)


    log("#### Save/Load   ###################################################")
    # save_pars = {}
    # load_pars = {}
    # module.save( save_pars,  model, sess)
    # model2, sess2 = module.load(load_pars)
    #     ypred = predict(model2, data_pars, compute_pars, out_pars)
    #     metrics_val = metrics(model2, ypred, data_pars, compute_pars, out_pars)
    # print(model2)



####################################################################################################
############ JSON template #########################################################################
def config_get_pars(config_file, config_mode="test") :
   """ 
     load JSON and output the params
   """
   js        = json.load(open(config_file, 'r'))  #Config
   js        = js[config_mode]  #test /uat /prod
   model_p   = js.get("model_pars")
   data_p    = js.get("data_pars")
   compute_p = js.get("compute_pars")
   out_p     = js.get("out_pars")

   return model_p, data_p, compute_p, out_p
                                 
   
def config_generate_json(modelname, to_path="ztest/new_model/") :
  """
    Generate config file from code source
    config_generate_template("model_tf.1_lstm", to_folder="ztest/")

  """
  os.makedirs(to_path, exist_ok=True)
  ##### JSON file
  import inspect
  module = module_load(modelname)
  signature = inspect.signature( module.Model )
  args = {
        k: v.default if v.default is not inspect.Parameter.empty else None
        for k, v in signature.parameters.items()
        # if v.default is not inspect.Parameter.empty
  }
                                 
  # args = inspect.getargspec(module.Model)
  model_pars = {"model_pars" :     args,
                  "data_pars" :      {},
                  "compute_pars":    {},
                  "out_pars" :       {}
               }

  modelname = modelname.replace(".py", "").replace(".", "-" )
  fname = os.path.join(to_path, f"{modelname}_config.json")
  json.dump(model_pars, open( fname, mode="w"))
  print(fname)


def config_generate_template(template_type=None, to_path="ztest/new_model/"):
    """
      Generate template from code source
      config_generate_template("model_tf.1_lstm", to_folder="ztest/")

    if template_type is None :
       os_root = os_package_root_path()
       lfiles = get_recursive_files(os_root, ext='/*template*/*.py')
       for f in lfiles :
           print(f.replace(os_root, ""))
    """
    import shutil
    os_root = os_package_root_path()
    #os.makedirs(to_path, exist_ok=True)
    shutil.copytree(os_root+"/template/", to_path)


def config_model_list(folder=None) :
  # Get all the model.py into folder  
  folder = os_package_root_path() if folder is None else folder
  # print(folder)
  module_names = get_recursive_files(folder, r'/*model*/*.py' )     
  mlist = []                  
  for t in module_names :
     mlist.append( t.replace(folder, "").replace("\\", ".") )
     print(mlist[-1])

  return mlist  
    

  
####################################################################################################
############CLI Command ############################################################################
def cli_load_arguments(config_file= None):
    """
        Load CLI input, load config.toml , overwrite config.toml by CLI Input
    """
    if config_file is None  :
      cur_path = os.path.dirname(os.path.realpath(__file__))
      config_file = os.path.join(cur_path, "template/models_config.json")
    # print(config_file)

    p = argparse.ArgumentParser()
    def add(*w, **kw) :
       p.add_argument(*w, **kw)
    
    add("--config_file" , default=config_file          , help="Params File")
    add("--config_mode" , default="test"               , help="test/ prod /uat")
    add("--log_file"    , default="mlmodels_log.log"   ,help="log.log")
    add("--do"          , default="test"               , help="test")
    add("--folder"      , default=None                 , help="test")
    
    ##### model pars
    add("--model_uri"   , default="model_tf/1_lstm.py" , help=".")
    add("--load_folder" , default="ztest/"             , help=".")

    ##### data pars
    add("--dataname"    , default="dataset/google.csv" , help=".")

    ##### compute pars

    ##### out pars
    add("--save_folder" , default="ztest/"             , help=".")
    
    arg = p.parse_args()
    # arg = load_config(arg, arg.config_file, arg.config_mode, verbose=0)
    return arg





def main():
    arg = cli_load_arguments()
    print(arg.do)

    if arg.do == "model_list"  :  #list all models in the repo
       l = config_model_list( arg.folder )
                                                     
    if arg.do == "testall"  :
        # test_all() # tot test all te modules inside model_tf
        test_all(folder=None)
                                 
    if arg.do == "test"  :
        test(arg.model_uri)  # '1_lstm'
        test_global(arg.model_uri)  # '1_lstm'

    if arg.do == "fit"  :
        model_p, data_p, compute_p, out_p  = config_get_pars(arg.config_file, arg.config_mode)
        
        module = module_load(arg.model_uri)  # '1_lstm.py
        model  = model_create(module, model_p, data_p, compute_p)   # Exact map JSON and paramters

        log("Fit")
        model, sess = module.fit(model, data_pars=data_p, compute_pars= compute_p, out_pars = out_p)

        log("Save")
        save_pars = { "path" : f"{arg.save_folder}/{arg.model_uri}", "model_uri" : arg.model_uri }
        save(save_pars, model, sess )


    if arg.do == "predict"  :
        model_p, data_p, compute_p, out_p  = config_get_pars(arg.config_file, arg.config_mode)
        # module = module_load(arg.modelname)  # '1_lstm'
        load_pars = { "path" : f"{arg.save_folder}/{arg.model_uri}", "model_uri" : arg.model_uri }

        module = module_load( model_p[".model_uri"])  # '1_lstm.py
        model, session = load(load_pars)
        module.predict(model, session, data_pars= data_p, compute_pars= compute_p, out_pars=out_p )

        
    if arg.do == "generate_config"  :
        log( arg.save_folder)
        config_generate_json(arg.model_uri, to_path= arg.save_folder)

        
    if arg.do == "generate_template"  :
        log( arg.save_folder)
        config_generate_template(arg.model_uri, to_path= arg.save_folder)



if __name__ == "__main__":
    main()
