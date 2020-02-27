"""Utilities for measuring the performance of a model."""

import torch

from mlbench_core.utils import AverageMeter
from mlbench_core.utils.pytorch.distributed import global_average
from abc import abstractmethod


class MLBenchMetric(object):

    def __init__(self):
        self.average_meter = AverageMeter()

    @abstractmethod
    def __call__(self, loss, output, target):
        pass

    def reset(self):
        self.average_meter = AverageMeter()

    def update(self, perc, size):
        self.average_meter.update(perc, size)

    def average(self):
        return global_average(self.average_meter.sum, self.average_meter.count)


class TopKAccuracy(MLBenchMetric):
    r"""Top K accuracy of an output.

    Counts a prediction as correct if the target value is in the top ``k``
    predictions, false otherwise, and returns the number of correct
    instances relative to total instances (0.0 to 100.0).

    Args:
        topk (int, optional): The number of top predictions to consider.
            Default: ``1``

    """

    def __init__(self, topk=1):
        super(TopKAccuracy, self).__init__()
        self.topk = topk

    def __call__(self, loss, output, target):
        """Computes the precision@k for the specified values of k

        Args:
            loss (:obj:`torch.Tensor`): Not used for accuracy
            output (:obj:`torch.Tensor`): Predictions of a model
            target (:obj:`torch.Tensor`): Target labels

        Example:
                >>> m = nn.Softmax()
                >>> input = torch.randn(10, 50)
                >>> preds = m(input)
                >>> targets = torch.randint(0, 1, (10,50))
                >>> topk = TopKAccuracy(5)
                >>> precision = topk(preds, targets)

        Returns:
            float
        """
        batch_size = target.size(0)

        _, pred = output.topk(self.topk, 1, True, True)
        pred = pred.t()
        correct = pred.eq(target.view(1, -1).expand_as(pred))
        correct_k = correct[:self.topk].view(-1).float().sum(0, keepdim=True)
        return correct_k.mul_(100.0 / batch_size)

    @property
    def name(self):
        """str: Name of this metric."""
        return "Prec@{}".format(self.topk)


class Perplexity(MLBenchMetric):
    """Language Model Perplexity score."""

    @property
    def name(self):
        """str: Name of this metric."""
        return "Perplexity"

    def __call__(self, loss, output, target):
        """Computes the perplexity

        Args:
            loss (:obj:`torch.Tensor`): The loss of a language model.
            output (:obj:`torch.Tensor`): Not Used
            target (:obj:`torch.Tensor`): Not Used

        Returns:
            float
        """
        return torch.exp(loss)


class DiceCoefficient(MLBenchMetric):

    def __call__(self, loss, output, target):
        """ Computes the Dice Coefficient of a Binary classification problem

        Args:
            loss (:obj:`torch.Tensor`): Not Used
            output (:obj:`torch.Tensor`): Output of model
            target (:obj:`torch.Tensor`): Target labels

        Returns:
            float: Dice Coefficient in [0,1]
        """
        eps = 0.0001
        self.inter = torch.dot(output.view(-1), target.view(-1))
        self.union = torch.sum(output) + torch.sum(target) + eps

        t = (2 * self.inter.float() + eps) / self.union.float()
        return t

    @property
    def name(self):
        """str: Name of this metric"""
        return "Dice Coefficient"


class F1Score(MLBenchMetric):
    def __init__(self, threshold=0.5, eps=1e-9):
        """ F1-Score metric

        Args:
            threshold (float): Threshold for prediction probability
        """
        super(F1Score, self).__init__()
        self.threshold = threshold
        self.eps = eps

    def __call__(self, loss, output, target):
        """ Computes the F1-Score of a Binary classification problem

        Args:
            loss (:obj:`torch.Tensor`): Not Used
            output (:obj:`torch.Tensor`): Output of model
            target (:obj:`torch.Tensor`): Target labels

        Returns:
            float: F1-Score in [0,1]
        """

        y_pred = torch.ge(output.float(), self.threshold).float()
        y_true = target.float()

        true_positive = (y_pred * y_true).sum(dim=0)
        precision = true_positive.div(y_pred.sum(dim=0).add(self.eps))
        recall = true_positive.div(y_true.sum(dim=0).add(self.eps))

        return torch.mean(
            (precision * recall).div(precision + recall + self.eps).mul(2))

    @property
    def name(self):
        return "F1-Score"
