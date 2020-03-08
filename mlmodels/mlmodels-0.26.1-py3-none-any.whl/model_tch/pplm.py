

from transformers import GPT2Tokenizer, GPT2LMHeadModel
from pplm.pplm_classification_head import ClassificationHead

from nltk.tokenize.treebank import TreebankWordDetokenizer
from pplm.run_pplm import run_pplm_example
from pplm.run_pplm_discrim_train import train_discriminator as test_case_1


VERBOSE = False

####################################################################################################
def os_module_path():
  current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
  parent_dir = os.path.dirname(current_dir)
  # sys.path.insert(0, parent_dir)
  return parent_dir


def os_file_path(data_path):
  from pathlib import Path
  data_path = os.path.join(Path(__file__).parent.parent.absolute(), data_path)
  print(data_path)
  return data_path


def os_package_root_path(filepath, sublevel=0, path_add=""):
  """
     get the module package root folder
  """
  from pathlib import Path
  path = Path(filepath).parent
  for i in range(1, sublevel + 1):
    path = path.parent
  
  path = os.path.join(path.absolute(), path_add)
  return path
# print("check", os_package_root_path(__file__, sublevel=1) )


def log(*s, n=0, m=1):
  sspace = "#" * n
  sjump = "\n" * m
  print(sjump, sspace, s, sspace, flush=True)


class to_namespace(object):
  def __init__(self, adict):
    self.__dict__.update(adict)

  def get(self, key):
    return self.__dict__.get(key)


def path_setup(out_folder="", sublevel=1, data_path="dataset/"):
    data_path = os_package_root_path(__file__, sublevel=sublevel, path_add=data_path)
    out_path = os.getcwd() + "/" + out_folder
    os.makedirs(out_path, exist_ok=True)
    model_path = out_path + "/model/"
    os.makedirs(model_path, exist_ok=True)

    log(data_path, out_path, model_path)
    return data_path, out_path, model_path
####################################################################################################




def generate(cond_text,bag_of_words,discrim=None,class_label=-1):
    print(" Generating text ... ")
    unpert_gen_text, pert_gen_text = run_pplm_example(
                        cond_text=cond_text,
                        num_samples=3,
                        bag_of_words=bag_of_words,
                        length=50,
                        discrim=discrim,
                        class_label=class_label,
                        stepsize=0.03,
                        sample=True,
                        num_iterations=3,
                        window_length=5,
                        gamma=1.5,
                        gm_scale=0.95,
                        kl_scale=0.01,
                        verbosity="quiet"
                    )
    print(" Unperturbed generated text :\n")
    print(unpert_gen_text)
    print()
    print(" Perturbed generated text :\n")
    print(pert_gen_text)
    print()
                    

    

####################################################################################################
class Model:
  def __init__(self, model_pars=None, data_pars=None
               ):
    ### Model Structure        ################################
    self.model = None   #ex Keras model
    
    





def fit(model, data_pars={}, compute_pars={}, out_pars={}, out_pars={},  **kw):
  """

  :param model:    Class model
  :param data_pars:  dict of
  :param out_pars:
  :param compute_pars:
  :param kwargs:
  :return:
  """

  sess = None # Session type for compute
  Xtrain, Xtest, ytrain, ytest = None, None, None, None  # data for training.
  o = 0
  

  return model, sess



    

def predict(model, sess=None, data_pars={}, out_pars={}, compute_pars={}, **kw):
  ##### Get Data ###############################################
  Xpred, ypred = None, None

  #### Do prediction
  ypred = model.model.fit(Xpred)

  ### Save Results
  
  
  ### Return val
  if compute_pars.get("return_pred_not") is not None :
    return ypred




####################################################################################################
def get_dataset(data_pars=None, **kw):
  """
    JSON data_pars to get dataset
    "data_pars":    { "data_path": "dataset/GOOG-year.csv", "data_type": "pandas",
    "size": [0, 0, 6], "output_size": [0, 6] },
  """

  if data_pars['train'] :
    Xtrain, Xtest, ytrain, ytest = None, None, None, None  # data for training.
    return Xtrain, Xtest, ytrain, ytest 

  else :
    Xtest, ytest = None, None  # data for training.
    return Xtest, ytest 







def get_params(choice="", data_path="dataset/", config_mode="test", **kw):
    if choice == "json":
        with open(data_path, encoding='utf-8') as config_f:
            config = json.load(config_f)
            c      = config[config_mode]

        model_pars, data_pars  = c[ "model_pars" ], c[ "data_pars" ]
        compute_pars, out_pars = c[ "compute_pars" ], c[ "out_pars" ]
        return model_pars, data_pars, compute_pars, out_pars


    if choice == "test01":
        log("#### Path params   ##########################################")
        data_path, out_path, model_path = path_setup(out_folder="", sublevel=1,
                                                     data_path="dataset/")
        data_pars    = {}
        model_pars   = {}
        compute_pars = {}
        out_pars     = {}

    return model_pars, data_pars, compute_pars, out_pars



        
#################################################################################        
#################################################################################
if __name__ == '__main__':
    # initializing the model
    # model = Model()
    # generating teh text
    generate(cond_text="The potato",bag_of_words='military')
    # for training classification model give the datset and datset path
    #test_case_1(dataset, dataset_fp=None)

        
    """    
    VERBOSE = True
    test_path = os.getcwd() + "/mytest/"
    
    ### Local
    test(pars_choice="json")
    test(pars_choice="test01")

    ### Global mlmodels
    test_global(pars_choice="json", out_path= test_path,  reset=True)
    """
