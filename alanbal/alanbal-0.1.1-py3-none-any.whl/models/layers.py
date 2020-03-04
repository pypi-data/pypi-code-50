import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.utils
from torch.nn import Parameter, init

import numpy as np


class FeedForward(nn.Module):
    """Feed forward neural network adapted from AllenNLP"""

    def __init__(self, input_dim, num_layers, hidden_dims, activations, dropout):
        super(FeedForward, self).__init__()

        if not isinstance(hidden_dims, list):
            hidden_dims = [hidden_dims] * num_layers  # type: ignore
        if not isinstance(activations, list):
            activations = [activations] * num_layers  # type: ignore
        if not isinstance(dropout, list):
            dropout = [dropout] * num_layers  # type: ignore

        self.activations = activations
        input_dims = [input_dim] + hidden_dims[:-1]
        linear_layers = [
            nn.Linear(layer_input_dim, layer_output_dim)
            for layer_input_dim, layer_output_dim in zip(input_dims, hidden_dims)
        ]
        self.linear_layers = nn.ModuleList(linear_layers)
        dropout_layers = [nn.Dropout(p=value) for value in dropout]
        self.dropout = nn.ModuleList(dropout_layers)
        self.output_dim = hidden_dims[-1]
        self.input_dim = input_dim

    def forward(self, x):
        output = x
        for layer, activation, dropout in zip(self.linear_layers, self.activations, self.dropout):
            output = dropout(activation(layer(output)))
        return output


class Attention(nn.Module):
    def __init__(self, hidden_size, batch_first=False):
        super(Attention, self).__init__()

        self.hidden_size = hidden_size

        self.attention_weights = nn.Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.context_weights = nn.Parameter(torch.randn(1, hidden_size, requires_grad=True))

        self.reset_parameters()

    def forward(self, inputs):
        batch_size, max_len = inputs.size()[:2]

        x = torch.bmm(inputs, self.attention_weights.unsqueeze(0).repeat(batch_size, 1, 1))
        # (batch_size, max_len, hidden_size) * (batch_size, hidden_size, 1) --> (batch_size, max_len, 1)
        x = torch.bmm(x, self.context_weights.permute(1, 0).unsqueeze(0).repeat(batch_size, 1, 1))

        # (batch_size, max_len, 1) --> (batch_size, max_len)
        attentions = torch.softmax(F.relu(x.squeeze()), dim=-1)

        # # create mask based on the sentence lengths
        # mask = torch.ones(attentions.size(), requires_grad=True).cuda()
        # for i, l in enumerate(lengths):  # skip the first sentence
        #     if l < max_len:
        #         mask[i, l:] = 0
        #
        # # apply mask and renormalize attention scores (weights)
        # masked = attentions * mask
        # _sums = masked.sum(-1).unsqueeze(-1)  # sums per row
        #
        # attentions = masked.div(_sums)

        # apply attention weights
        weighted = torch.mul(inputs, attentions.unsqueeze(-1).expand_as(inputs))

        # get the final fixed vector representations of the sentences
        representations = weighted.sum(1).squeeze()

        return representations, attentions

    def reset_parameters(self):
        stdv = 1.0 / np.sqrt(self.hidden_size)
        init.uniform_(self.attention_weights, -stdv, stdv)
        init.uniform_(self.context_weights, -stdv, stdv)



