from collections import OrderedDict

import torch
import logging

from model_loads.utils import model_type


def loads_state_dict(model_path, use_gpu=True):
    # to load
    if use_gpu and torch.cuda.is_available():
        checkpoint = torch.load(model_path, map_location=lambda storage, loc: storage)
    else:
        checkpoint = torch.load(model_path, map_location=lambda storage, loc: storage)

    _type = model_type(ckpt=checkpoint)
    other_param = None

    if _type == "self_contained_model_pth":

        logging.warning(
            """
            torch.save(the_model, PATH) methods not recommended:

            the serialized data is bound to the specific classes and the exact directory structure used, 
            so it can break in various ways when used in other projects, or after some serious refactors.

            Recommended approach for saving only the model parameters:
            torch.save(the_model.state_dict(), PATH)

            see: https://pytorch.org/docs/master/notes/serialization.html
            """)
        state_dict = checkpoint.state_dict()

    elif _type == "state_dict_pth":
        state_dict = checkpoint

    elif _type == "pth_tar":
        state_dict = checkpoint["state_dict"]
        other_param = checkpoint.pop("state_dict")

    else:
        raise Exception("Not support this type model yet!")

    # multi_gpus_models trained model
    # create new OrderedDict that does not contain `module.`
    new_state_dict = OrderedDict()

    if "module." in list(state_dict.keys())[0]:
        for k, v in state_dict.items():
            name = k[7:]  # remove `module.`
            new_state_dict[name] = v
        state_dict = new_state_dict

    return state_dict, other_param


def load_param(state_dict, model=None, use_gpu=True):
    model.load_state_dict(state_dict)
    if use_gpu and torch.cuda.is_available():
        model.cuda()
    else:
        model.cpu()
    return model


if __name__ == "__main__":
    from tests.mnist import Net

    state_dict, other_param = loads_state_dict("../../tests/mnist_cnn_model.pt")
    m = Net()
    model = load_param(state_dict, m)
