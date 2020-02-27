import pytest
import shutil
import torch

from mlbench_core.dataset.linearmodels.pytorch.dataloader import \
    load_and_download_lmdb


def test_lmdb_loader():
    dataset = load_and_download_lmdb("duke", "train", "./datasets-test")

    assert len(dataset) == 44

    feats, label = dataset[0]

    assert feats.shape[1] == 7129

    shutil.rmtree("./datasets-test")
