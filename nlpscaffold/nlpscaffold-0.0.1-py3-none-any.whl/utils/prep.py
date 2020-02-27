import torch
import argparse
import random
import importlib
import numpy as np
from torch import nn


def manual_seed(seed):
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)


def get_parser():
    return argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)


def pad_sequence(inds, pad=0, device=None):
    out = nn.utils.rnn.pad_sequence(inds, batch_first=True, padding_value=pad)
    return out if device is None else out.to(device)


def load_module(root, fname):
    return importlib.import_module('{}.{}'.format(root, fname))


def run_rnn(rnn, inp, lens, state0=None):
    pack = nn.utils.rnn.pack_padded_sequence(inp, lens, batch_first=True, enforce_sorted=False)
    out, state = rnn.forward(pack, state0)
    unpack, _ = nn.utils.rnn.pad_packed_sequence(out, batch_first=True, padding_value=0, total_length=inp.size(1))
    return unpack, state
