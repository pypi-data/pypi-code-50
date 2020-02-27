from mlbench_core.evaluation.pytorch.metrics import *
import torch


def test_f1_score():
    output = torch.tensor([1, 1, 1, 1, 1]).reshape(5, 1)
    target = torch.tensor([0, 0, 0, 0, 0]).reshape(5, 1)

    f1 = F1Score()
    score = f1(0, output, target)

    assert score.item() == 0


    output = torch.tensor([1, 1, 1, 0, 1]).reshape(5, 1)
    target = torch.tensor([1, 0, 1, 1, 0]).reshape(5, 1)

    precision = 2 / (2 + 2)
    recall = 2 / (2 + 1)