import os

import torch

__all__ = ["load_models"]

# https://pytorch.org/tutorials/beginner/saving_loading_models.html#saving-loading-model-across-devices

from model_loads.utils import load_param, loads_state_dict, LoadException


def load_models(model_path, model, use_gpu=True):
    try:
        state_dict, other_param = loads_state_dict(model_path)
        model = load_param(state_dict, model)
    except LoadException as e:
        print("error in loading models! Please check load methods.")
        print(e.args)
    else:
        print("Success load model to {}!".
              format("GPU" if use_gpu and torch.cuda.is_available() else "CPU"))

    return model


if __name__ == "__main__":
    from tests.mnist import Net
    model = Net()
    print(os.getcwd())
    model = load_models("/Users/cw-mac/model_loads/tests/cpu_models/mnist_cnn.pth.tar", model)
    model = load_models("/Users/cw-mac/model_loads/tests/cpu_models/mnist_cnn_model.pt", model)
    model = load_models("/Users/cw-mac/model_loads/tests/cpu_models/mnist_cnn_state_dict.pt", model)

    model = load_models("/Users/cw-mac/model_loads/tests/gpu_models/mnist_cnn.pth.tar", model)
    model = load_models("/Users/cw-mac/model_loads/tests/gpu_models/mnist_cnn_model.pt", model)
    model = load_models("/Users/cw-mac/model_loads/tests/gpu_models/mnist_cnn_state_dict.pt", model)
