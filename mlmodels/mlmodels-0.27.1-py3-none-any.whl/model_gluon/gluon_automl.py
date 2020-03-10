# -*- coding: utf-8 -*-
"""
AutoGluon : Automatic ML using gluon platform.
# First install package from terminal:  pip install mxnet autogluon
https://autogluon.mxnet.io/tutorials/tabular_prediction/tabular-quickstart.html



"""
import json
import os
from pathlib import Path

import autogluon as ag
from autogluon import TabularPrediction as tabular_task

# from mlmodels.model_gluon.util_autogluon import (
#    fit, get_dataset, fit_metrics, load, log, os_package_root_path, predict, save)


#######################################################################################################
######## Helper functions
def os_package_root_path(filepath, sublevel=0, path_add=""):
    """
       get the module package root folder
    """
    from pathlib import Path
    path = Path(os.path.realpath(filepath)).parent
    for i in range(1, sublevel + 1):
        path = path.parent

    path = os.path.join(path.absolute(), path_add)
    return path


def log(*s, n=0, m=1):
    sspace = "#" * n
    sjump = "\n" * m
    print(sjump, sspace, s, sspace, flush=True)




######################################################################################################
#### Model defintion
class Model(object):
    def __init__(self, model_pars=None, compute_pars=None):
        ## Empty model for Seaialization
        if model_pars is None and compute_pars is None:
            self.model = None

        else:
            if model_pars['model_type'] == 'tabular':
                self.model = tabular_task



################ Dataset   #########################################################################
def _get_dataset_from_aws(**kw):
    URL_INC_TRAIN = 'https://autogluon.s3.amazonaws.com/datasets/Inc/train.csv'
    URL_INC_TEST = 'https://autogluon.s3.amazonaws.com/datasets/Inc/test.csv'

    dt_name = kw['dt_name']
    if dt_name == 'Inc':
        if kw['train']:
            data = tabular_task.Dataset(file_path=URL_INC_TRAIN)
        else:
            data = tabular_task.Dataset(file_path=URL_INC_TEST)
        label = 'occupation'
        if kw.get('label'):
            label = kw.get('label')

        return data, label
    else:
        print(f"Not support {dt_name} yet!")


def get_dataset(**kw):
    data = None
    if kw['uri_type'] == 'amazon_aws':
        data, label = _get_dataset_from_aws(**kw)
        return data, label

    ##check whether dataset is of kind train or test
    # data_path = kw['train_data_path'] if kw['train'] else kw['test_data_path']
    df = data.import_data_fromfile(**kw)

    col_target = kw.get('col_target') if kw.get('col_target') else 'y'
    colX = list(df.columns)
    colX.remove(col_target)

    label = df[col_target].values
    train = df[colX].values
    return data, label


####################################################################################################
# Model fit
def fit(model, data_pars=None, model_pars=None, compute_pars=None, out_pars=None, session=None,
        **kwargs):
    ##loading dataset
    """
      Classe Model --> model,   model.model contains thte sub-model

    """
    data = get_dataset(**data_pars)
    if data is None or not isinstance(data, (list, tuple)):
        raise Exception("Missing data or invalid data format for fitting!")

    train_ds, label = data
    nn_options = {
        'num_epochs': compute_pars['num_epochs'],
        'learning_rate': model_pars['learning_rate'],
        'activation': model_pars['activation'],
        'layers': model_pars['layers'],
        'dropout_prob': model_pars['dropout_prob'],
    }

    gbm_options = {
        'num_boost_round': model_pars['num_boost_round'],
        'num_leaves': model_pars['num_leaves'],
    }

    ## Attribut model has the model
    predictor = model.model.fit(train_data=train_ds, label=label,
                                output_directory=out_pars['out_path'],
                                time_limits=compute_pars['time_limits'],
                                num_trials=compute_pars['num_trials'],
                                hyperparameter_tune=compute_pars['hp_tune'],
                                hyperparameters={'NN': nn_options, 'GBM': gbm_options},
                                search_strategy=compute_pars['search_strategy'])
    model.model = predictor
    return model


# Model p redict
def predict(model, data_pars, compute_pars=None, out_pars=None, **kwargs):
    ##  Model is class
    ## load test dataset
    data_pars['train'] = False
    test_ds, label = get_dataset(**data_pars)
    # remove label in test data if have
    if label in test_ds.columns:
        test_ds = test_ds.drop(labels=[label], axis=1)

    y_pred = model.model.predict(test_ds)

    ### output stats for prediction
    if VERBOSE:
        pass
    return y_pred


def fit_metrics(model, ypred, ytrue, data_pars, compute_pars=None, out_pars=None, **kwargs):
    ## load test dataset
    # data_pars['train'] = False
    # test_ds, label = get_dataset(**data_pars)
    # y_test = test_ds[label]

    ## evaluate
    acc = model.model.evaluate_predictions(y_true=ytrue, y_pred=ypred, auxiliary_metrics=False)
    metrics_dict = {"ACC": acc}
    return metrics_dict


###############################################################################################################
### different plots and output metric


###############################################################################################################
# save and load model helper function
class Model_empty(object):
    def __init__(self, model_pars=None, compute_pars=None):
        ## Empty model for Seaialization
        self.model = tabular_task


def save(model, out_pars):
    if not model:
        print("model do not exist!")
    else:
        model.model.save()


def load(path):
    if not os.path.exists(path):
        print("model file do not exist!")
        return None
    else:
        model = Model_empty()
        model.model = tabular_task.load(path)

        #### Add back the model parameters...
        return model


########################################################################################################################
def path_setup(out_folder="", sublevel=1, data_path="dataset/"):
    data_path = os_package_root_path(__file__, sublevel=sublevel, path_add=data_path)
    out_path = os.getcwd() + "/" + out_folder
    os.makedirs(out_path, exist_ok=True)
    model_path = out_path + "/model_gluon_automl/"
    os.makedirs(model_path, exist_ok=True)

    log(data_path, out_path, model_path)
    return data_path, out_path, model_path


def _config_process(config):
    data_pars = config["data_pars"]

    log("#### Model params   ################################################")
    m = config["model_pars"]
    model_pars = {"model_type": m["model_type"],
                  "learning_rate": ag.space.Real(m["learning_rate_min"],
                                                 m["learning_rate_max"],
                                                 default=m["learning_rate_default"],
                                                 log=True),
                  
                  "activation": ag.space.Categorical(*tuple(m["activation"])),
                  "layers": ag.space.Categorical(*tuple(m["layers"])),
                  "dropout_prob": ag.space.Real(m["dropout_prob_min"],
                                                m["dropout_prob_max"],
                                                default=m["dropout_prob_default"]),
                  
                  "num_boost_round": m["num_boost_round"],
                  "num_leaves": ag.space.Int(lower=m["num_leaves_lower"],
                                             upper=m["num_leaves_upper"],
                                             default=m["num_leaves_default"])
                  }

    compute_pars = config["compute_pars"]
    out_pars = config["out_pars"]
    return model_pars, data_pars, compute_pars, out_pars


def get_params(choice="", data_path="dataset/", config_mode="test", **kw):
    if choice == "json":
        data_path = Path(os.path.realpath(
            __file__)).parent.parent / "model_gluon/gluon_automl.json" if data_path == "dataset/" else data_path

        config = json.load( open(data_path, encoding='utf-8', mode='r'))
        config = config[config_mode]

        model_pars, data_pars, compute_pars, out_pars = _config_process(config)
        return model_pars, data_pars, compute_pars, out_pars

    if choice == "test01":
        log("#### Path params   #################################################")
        data_path, out_path, model_path = path_setup(out_folder="", sublevel=1,
                                                     data_path="dataset/")

        data_pars = {"train": True, "uri_type": "amazon_aws", "dt_name": "Inc"}

        model_pars = {"model_type": "tabular",
                      "learning_rate": ag.space.Real(1e-4, 1e-2, default=5e-4, log=True),
                      "activation": ag.space.Categorical(*tuple(["relu", "softrelu", "tanh"])),
                      "layers": ag.space.Categorical(
                          *tuple([[100], [1000], [200, 100], [300, 200, 100]])),
                      'dropout_prob': ag.space.Real(0.0, 0.5, default=0.1),
                      'num_boost_round': 10,
                      'num_leaves': ag.space.Int(lower=26, upper=30, default=36)}

        compute_pars = {"hp_tune": True, "num_epochs": 1, "time_limits": 100, "num_trials": 2,
                        "search_strategy": "skopt"}

        out_pars = {"out_path": out_path}

    return model_pars, data_pars, compute_pars, out_pars


########################################################################################################################
def test(data_path="dataset/", pars_choice="json"):
    ### Local test
    log("#### Loading params   ##############################################")
    model_pars, data_pars, compute_pars, out_pars = get_params(choice=pars_choice,
                                                               data_path=data_path)

    log("#### Loading dataset   #############################################")
    gluon_ds = get_dataset(**data_pars)

    log("#### Model init, fit   #############################################")
    model = Model(model_pars, compute_pars)
    model = fit(model, data_pars, model_pars, compute_pars, out_pars)

    log("#### save the trained model  #######################################")
    # save(model, data_pars["modelpath"])


    log("#### Predict   ####################################################")
    ypred = predict(model, data_pars, compute_pars, out_pars)

    log("#### metrics   ####################################################")
    metrics_val = fit_metrics(model, ypred, data_pars, compute_pars, out_pars)
    print(metrics_val)

    log("#### Plot   #######################################################")

    log("#### Save/Load   ##################################################")
    save(model, out_pars)
    model2 = load(out_pars['out_path'])
    #     ypred = predict(model2, data_pars, compute_pars, out_pars)
    #     metrics_val = metrics(model2, ypred, data_pars, compute_pars, out_pars)
    print(model2)



if __name__ == '__main__':
    VERBOSE = True
    test(pars_choice="json")
    test(pars_choice="test01")


