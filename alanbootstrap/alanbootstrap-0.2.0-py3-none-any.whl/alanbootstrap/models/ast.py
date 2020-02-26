import torch
import torch.nn as nn
from torch import optim
import torchnlp.encoders as tencoder
import torchnlp.encoders.text.text_encoder as ttencoder
import torch.utils.data as tdata
import numpy as np
import sklearn.metrics as sm

from alanbootstrap.models import layers, encoder
from alanbootstrap.components import ast as ast_module

import typing
import json


class ASTRegressionModel(nn.Module):

    def __init__(self,
                 vocab: typing.List[typing.AnyStr],
                 steps: int, emb_dims: int, rnn_dims: int, rnn_layers: int, parent_feeding: bool,
                 mlp_dims: typing.List, mlp_activation: nn.Module,
                 output_dims: int, dropout=0.3, bidirectional=False
                 ):
        super().__init__()

        self.steps = steps
        self.rnn_layers = rnn_layers
        self.emb_dims = emb_dims
        self.rnn_dims = rnn_dims
        self.parent_feeding = parent_feeding

        self.mlp_dims = mlp_dims
        self.mlp_activation = mlp_activation
        self.output_dims = output_dims
        self.dropout = dropout
        self.bidirectional = bidirectional

        self.ast_encoder = encoder.ASTEncoder(
            vocab, steps, emb_dims, rnn_dims, rnn_dropout=dropout, rnn_layer=rnn_layers, parent_feeding=parent_feeding,
            bidirectional=bidirectional
        )
        self.vocab_size = self.ast_encoder.vocab_size

        self.mlp = layers.FeedForward(
            2 * rnn_dims if bidirectional else rnn_dims, len(mlp_dims), mlp_dims, mlp_activation, dropout
        )

        self.scorer = layers.FeedForward(
            mlp_dims[-1], 1, output_dims, nn.ReLU(), 0
        )

    def forward(self, ast_batch: typing.List[ast_module.AST]):

        if self.parent_feeding:
            raise NotImplementedError
        else:
            hs = self.ast_encoder(ast_batch)
            return self.scorer(self.mlp(hs))

    def batch_train(self, train_dataset, batch_size=30, shuffle=True, epochs=100, dev_dataset=None):
        data_loader = tdata.DataLoader(
            train_dataset, batch_size=batch_size, shuffle=shuffle, collate_fn=collate_wrapper_for_list)

        loss_func = nn.MSELoss()
        optimizer = optim.SGD(self.parameters(), lr=0.01, momentum=0.3, nesterov=True)

        for epoch in range(epochs):
            losses = []

            for batch_index, samples in enumerate(data_loader):
                x = samples
                y = [float(sample.complexity) for sample in samples]

                self.train(True)
                y_p = self.forward(x)
                loss = loss_func(y_p, torch.tensor(y))
                losses.append(loss.data.tolist())

                loss.backward()
                optimizer.step()

                if batch_index % 50 == 0:
                    y_p = y_p.data.tolist()
                    mae = sm.mean_absolute_error(y, y_p)
                    evs = sm.explained_variance_score(y, y_p)
                    print('[%d/%d] mean_loss: %.4f; mean absolute error: %.4f; explained variance score: %.4f' %
                          (epoch, epochs, np.mean(losses), mae, evs)
                          )
                    losses = list()

                batch_index += 1

            if dev_dataset is not None:
                dev_ast = list(dev_dataset)
                dev_y = [float(ast_.complexity) for ast_ in dev_ast]

                self.train(False)
                dev_y_p = self.forward(dev_ast)
                dev_y_p = dev_y_p.data.tolist()

                mae = sm.mean_absolute_error(dev_y, dev_y_p)
                evs = sm.explained_variance_score(dev_y, dev_y_p)

                print('[%d/%d] mean absolute error: %.4f; explained variance score: %.4f\n' %
                      (epoch, epochs, mae, evs)
                      )


class ASTClassificationModel(nn.Module):

    def __init__(self,
                 vocab: typing.List[typing.AnyStr],
                 steps: int, emb_dims: int, rnn_dims: int, rnn_layers: int, parent_feeding: bool,
                 mlp_dims: typing.List, mlp_activation: nn.Module,
                 output_dims: int, dropout=0.3, bidirectional=False
                 ):
        super().__init__()

        self.steps = steps
        self.rnn_layers = rnn_layers
        self.emb_dims = emb_dims
        self.rnn_dims = rnn_dims
        self.parent_feeding = parent_feeding

        self.mlp_dims = mlp_dims
        self.mlp_activation = mlp_activation
        self.output_dims = output_dims
        self.dropout = dropout
        self.bidirectional = bidirectional

        self.ast_encoder = encoder.ASTEncoder(
            vocab, steps, emb_dims, rnn_dims, rnn_dropout=dropout, rnn_layer=rnn_layers, parent_feeding=parent_feeding,
            bidirectional=bidirectional
        )
        self.vocab_size = self.ast_encoder.vocab_size

        self.mlp = layers.FeedForward(
            2 * rnn_dims if bidirectional else rnn_dims, len(mlp_dims), mlp_dims, mlp_activation, dropout
        )

        self.scorer = layers.FeedForward(
            mlp_dims[-1], 1, output_dims, nn.Softmax(), 0
        )

    def forward(self, ast_batch: typing.List[ast_module.AST]):

        if self.parent_feeding:
            raise NotImplementedError
        else:
            hs = self.ast_encoder(ast_batch)
            return self.scorer(self.mlp(hs))

    def batch_train(self, train_dataset, batch_size=30, shuffle=True, epochs=100, dev_dataset=None):

        weights = inverse_frequency_weights(train_dataset)
        sampler = tdata.WeightedRandomSampler(weights, len(weights))

        data_loader = tdata.DataLoader(
            train_dataset, batch_size=batch_size, shuffle=False,
            collate_fn=collate_wrapper_for_list, sampler=sampler
        )

        loss_func = nn.CrossEntropyLoss()
        optimizer = optim.Adam(self.parameters())

        for epoch in range(epochs):
            losses = []

            for batch_index, samples in enumerate(data_loader):
                x = samples
                y = [sample.complexity for sample in samples]

                self.train(True)
                y_p = self.forward(x)
                loss = loss_func(y_p, torch.tensor(y))
                losses.append(loss.data.tolist())

                loss.backward()
                optimizer.step()

                if batch_index % 50 == 0:
                    preds, labels = y_p.argmax(1).data.tolist(), y
                    prec_score = sm.precision_score(labels, preds, average='weighted')
                    reca_score = sm.recall_score(labels, preds, average='weighted')
                    print('[%d/%d] mean_loss: %.4f; weighted_precision: %.4f; weighted_recall: %.4f' % (
                        epoch, epochs, np.mean(losses), prec_score, reca_score))
                    losses = list()

                batch_index += 1

            if dev_dataset is not None:
                dev_ast = list(dev_dataset)
                dev_y = [ast_.complexity for ast_ in dev_ast]

                self.train(False)
                dev_y_p = self.forward(dev_ast)

                preds, labels = dev_y_p.argmax(1).data.tolist(), dev_y
                print(sm.classification_report(labels, preds))


class SharedASTJsonDataset(tdata.dataset.Dataset):

    def __init__(self, shared_ast_json_path):
        self.path = shared_ast_json_path

        worker_info = tdata.get_worker_info()
        if worker_info is None:  # single-process data loading, return the full iterator
            self.ast_list = ast_module.AST.from_shared_ast_json_file(self.path)

        super(SharedASTJsonDataset, self).__init__()

    def __iter__(self):
        worker_info = tdata.get_worker_info()
        if worker_info is None:  # single-process data loading, return the full iterator

            return iter(self.ast_list)
        else:
            raise NotImplementedError

    def __len__(self):
        return len(self.ast_list)

    def __getitem__(self, index):
        return self.ast_list[index]


def collate_wrapper_for_list(batch):
    return batch


def inverse_frequency_weights(ast_dataset):
    target = np.array([
        ast_.complexity for ast_ in ast_dataset
    ])
    class_sample_count = np.array(
        [len(np.where(target == t)[0]) for t in np.unique(target)]
    )
    print(class_sample_count)
    weight = 1. / class_sample_count
    samples_weight = np.array([weight[t] for t in target])

    return samples_weight
