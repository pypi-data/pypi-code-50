import collections
import logging

import torch


def model_type(ckpt):
    '''
    :param ckpt: torch.load(model_path)
    :return:
    '''
    if isinstance(ckpt, collections.OrderedDict):
        _type = "state_dict_pth"

    elif isinstance(ckpt, dict):
        _type = "pth_tar"

    else:
        # fixme
        # Pytorch recommend not use this methods to save models
        # torch.save(model.state_dict()) is recommended

        _type = "self_contained_model_pth"

    return _type


if __name__ == "__main__":
    print(model_type("../../tests/mnist_cnn.pth.tar"))
    print(model_type("../../tests/mnist_cnn_state_dict.pt"))
    print(model_type("../../tests/mnist_cnn_model.pt"))
