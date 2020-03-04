import logging
import inspect
from scrybe.internal.util import get_default_params, get_hyperparams, is_patched_object


LOGGER = logging.getLogger(__name__)


def get_keras_hyperparameters(params, model, class_weights=None):
    hyperparameters = dict()
    if model.optimizer is not None:
        try:
            req_args, default_dict = get_default_params(model.optimizer)
            if hasattr(model.optimizer, 'get_config'):
                optimizer_name = model.optimizer.__class__.__name__
                optimizer_config = get_hyperparams(model.optimizer.get_config(), default_dict, req_args)
                hyperparameters['optimizer'] = {
                    'name': optimizer_name,
                    'config': optimizer_config
                }
            elif inspect.isfunction(model.optimizer) and hasattr(model.optimizer, '__name__'):
                optimizer_name = model.optimizer.__name__
                optimizer_config = {}
                hyperparameters['optimizer'] = {
                    'name': optimizer_name,
                    'config': optimizer_config
                }
        except Exception as e:
            LOGGER.warning("Exception occured while trying to extract optimizer info")

    hyperparameters['num_weights'] = model.count_params()
    if 'batch_size' in params.keys():
        hyperparameters['batch_size'] = params['batch_size']

    if 'epochs' in params.keys():
        hyperparameters['epochs'] = params['epochs']

    if 'samples' in params.keys():
        hyperparameters['samples'] = params['samples']

    if hasattr(model.loss, 'get_config'):
        hyperparameters['loss'] = model.loss.get_config()
    elif inspect.isfunction(model.loss) and hasattr(model.loss, '__name__'):
        hyperparameters['loss'] = model.loss.__name__

    if model.loss_weights is not None:
        hyperparameters['loss_weights'] = model.loss_weights
    if class_weights is not None and isinstance(class_weights, dict) and len(class_weights) > 0:
        hyperparameters['class_weights'] = class_weights
    return hyperparameters


def get_architecture(model):
    config = model.get_config()
    layer_iter = 0
    for layer in model.layers:
        req_args, default_dict = get_default_params(layer)
        if 'name' not in config['layers'][layer_iter].keys():
            config['layers'][layer_iter]['name'] = config['layers'][layer_iter]['class_name']
        layer_config = config['layers'][layer_iter]['config']
        config['layers'][layer_iter]['config'] = get_hyperparams(layer_config, default_dict, req_args)
        layer_iter += 1
    return config


def is_patched_keras_object(orig_object):
    return is_patched_object(orig_object,
                             [('keras.engine.sequential', 'Sequential.fit'), ('keras.engine.training', 'Model.fit')])
