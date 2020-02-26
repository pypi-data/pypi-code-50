import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.nn.utils
from torch.nn import Parameter, init
from torch.nn.modules.rnn import RNNCellBase
from torch.nn.utils.rnn import PackedSequence

import numpy as np

from alanbootstrap.models import functions
#from torch.nn._functions.thnn import rnnFusedPointwise as fusedBackend
#from torch.nn._functions.rnn import variable_recurrent_factory, StackedRNN


class RecurrentDropoutLSTMCell(RNNCellBase):
    def __init__(self, input_size, hidden_size, dropout=0.):
        super(RecurrentDropoutLSTMCell, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.dropout = dropout

        self.W_i = Parameter(torch.randn(hidden_size, input_size, requires_grad=True))
        self.U_i = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        # self.b_i = Parameter(torch.randn(hidden_size))

        self.W_f = Parameter(torch.randn(hidden_size, input_size, requires_grad=True))
        self.U_f = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        # self.b_f = Parameter(torch.randn(hidden_size))

        self.W_c = Parameter(torch.randn(hidden_size, input_size, requires_grad=True))
        self.U_c = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        # self.b_c = Parameter(torch.randn(hidden_size))

        self.W_o = Parameter(torch.randn(hidden_size, input_size, requires_grad=True))
        self.U_o = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        # self.b_o = Parameter(torch.randn(hidden_size))

        self.bias_ih = Parameter(torch.randn(4 * hidden_size, requires_grad=True))
        self.bias_hh = Parameter(torch.randn(4 * hidden_size, requires_grad=True))

        self._input_dropout_mask = self._h_dropout_mask = None

        self.reset_parameters()

    def reset_parameters(self):
        init.orthogonal(self.W_i)
        init.orthogonal(self.U_i)
        init.orthogonal(self.W_f)
        init.orthogonal(self.U_f)
        init.orthogonal(self.W_c)
        init.orthogonal(self.U_c)
        init.orthogonal(self.W_o)
        init.orthogonal(self.U_o)
        self.bias_ih.data.fill_(0.)
        # forget gate set to 1.
        self.bias_ih.data[self.hidden_size:2 * self.hidden_size].fill_(1.)
        self.bias_hh.data.fill_(0.)

    def set_dropout_masks(self, batch_size):
        if self.dropout:
            if self.training:
                new_tensor = self.W_i.data.new
                self._input_dropout_mask = torch.tensor(
                    torch.bernoulli(new_tensor(4, batch_size, self.input_size).fill_(1 - self.dropout)),
                    requires_grad=False
                )
                self._h_dropout_mask = torch.tensor(
                    torch.bernoulli(new_tensor(4, batch_size, self.hidden_size).fill_(1 - self.dropout)),
                    requires_grad=False
                )
            else:
                self._input_dropout_mask = self._h_dropout_mask = [1. - self.dropout] * 4
        else:
            self._input_dropout_mask = self._h_dropout_mask = [1.] * 4

    def forward(self, input_, hidden_state):
        def get_mask_slice(mask, idx):
            if isinstance(mask, list):
                return mask[idx]
            else:
                return mask[idx][:input_.size(0)]

        h_tm1, c_tm1 = hidden_state

        # if self._input_dropout_mask is None:
        #     self.set_dropout_masks(input_.size(0))

        xi_t = F.linear(input_ * get_mask_slice(self._input_dropout_mask, 0), self.W_i)
        xf_t = F.linear(input_ * get_mask_slice(self._input_dropout_mask, 1), self.W_f)
        xc_t = F.linear(input_ * get_mask_slice(self._input_dropout_mask, 2), self.W_c)
        xo_t = F.linear(input_ * get_mask_slice(self._input_dropout_mask, 3), self.W_o)

        hi_t = F.linear(h_tm1 * get_mask_slice(self._h_dropout_mask, 0), self.U_i)
        hf_t = F.linear(h_tm1 * get_mask_slice(self._h_dropout_mask, 1), self.U_f)
        hc_t = F.linear(h_tm1 * get_mask_slice(self._h_dropout_mask, 2), self.U_c)
        ho_t = F.linear(h_tm1 * get_mask_slice(self._h_dropout_mask, 3), self.U_o)

        i_t = F.sigmoid(xi_t + self.bias_ih[:self.hidden_size] + hi_t + self.bias_hh[:self.hidden_size])
        f_t = F.sigmoid(
            xf_t + self.bias_ih[self.hidden_size:2 * self.hidden_size] +
            hf_t + self.bias_hh[self.hidden_size:2 * self.hidden_size]
        )
        c_t = f_t * c_tm1 + i_t * torch.tanh(
            xc_t + self.bias_ih[2 * self.hidden_size:3 * self.hidden_size] +
            hc_t + self.bias_hh[2 * self.hidden_size:3 * self.hidden_size]
        )
        o_t = F.sigmoid(
            xo_t + self.bias_ih[3 * self.hidden_size:4 * self.hidden_size] +
            ho_t + self.bias_hh[3 * self.hidden_size:4 * self.hidden_size]
        )
        h_t = o_t * torch.tanh(c_t)

        return h_t, c_t


class ParentFeedingLSTMCell(RNNCellBase):
    def __init__(self, input_size, hidden_size):
        super(ParentFeedingLSTMCell, self).__init__()

        self.input_size = input_size
        self.hidden_size = hidden_size

        self.W_i = Parameter(torch.randn(hidden_size, input_size, requires_grad=True))
        self.U_i = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.U_i_p = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.b_i = Parameter(torch.randn(hidden_size, requires_grad=True))

        self.W_f = Parameter(torch.randn(hidden_size, input_size, requires_grad=True))
        self.U_f = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.U_f_p = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.b_f = Parameter(torch.randn(hidden_size, requires_grad=True))
        self.b_f_p = Parameter(torch.randn(hidden_size, requires_grad=True))

        self.W_c = Parameter(torch.randn(hidden_size, input_size, requires_grad=True))
        self.U_c = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.U_c_p = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.b_c = Parameter(torch.randn(hidden_size, requires_grad=True))

        self.W_o = Parameter(torch.randn(hidden_size, input_size, requires_grad=True))
        self.U_o = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.U_o_p = Parameter(torch.randn(hidden_size, hidden_size, requires_grad=True))
        self.b_o = Parameter(torch.randn(hidden_size, requires_grad=True))

        self.reset_parameters()

    def reset_parameters(self):
        init.orthogonal(self.W_i)
        init.orthogonal(self.U_i)
        init.orthogonal(self.U_i_p)

        init.orthogonal(self.W_f)
        init.orthogonal(self.U_f)
        init.orthogonal(self.U_f_p)

        init.orthogonal(self.W_c)
        init.orthogonal(self.U_c)
        init.orthogonal(self.U_c_p)

        init.orthogonal(self.W_o)
        init.orthogonal(self.U_o)
        init.orthogonal(self.U_o_p)

        self.b_i.data.fill_(0.)
        self.b_c.data.fill_(0.)
        self.b_o.data.fill_(0.)
        # forget bias set to 1.
        self.b_f.data.fill_(1.)
        self.b_f_p.data.fill_(1.)

    def forward(self, input_, hidden_states):
        h_tm1, c_tm1, h_tm1_p, c_tm1_p = hidden_states
        i_t = F.sigmoid(
            F.linear(input_, self.W_i) + F.linear(h_tm1, self.U_i) + F.linear(h_tm1_p, self.U_i_p) + self.b_i)

        xf_t = F.linear(input_, self.W_f)
        f_t = F.sigmoid(xf_t + F.linear(h_tm1, self.U_f) + self.b_f)
        f_t_p = F.sigmoid(xf_t + F.linear(h_tm1_p, self.U_f_p) + self.b_f_p)

        xc_t = F.linear(input_, self.W_c) + F.linear(h_tm1, self.U_c) + F.linear(h_tm1_p, self.U_c_p) + self.b_c
        c_t = f_t * c_tm1 + f_t_p * c_tm1_p + i_t * torch.tanh(xc_t)

        o_t = F.sigmoid(
            F.linear(input_, self.W_o) + F.linear(h_tm1, self.U_o) + F.linear(h_tm1_p, self.U_o_p) + self.b_o)
        h_t = o_t * torch.tanh(c_t)

        return h_t, c_t


class LSTM(nn.Module):
    def __init__(self, input_size, hidden_size, bidirectional=False, dropout=0., cell_factory=RecurrentDropoutLSTMCell):
        super(LSTM, self).__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.bidirectional = bidirectional
        self.dropout = dropout
        self.cell_factory = cell_factory
        num_directions = 2 if bidirectional else 1
        self.lstm_cells = []

        for direction in range(num_directions):
            cell = cell_factory(input_size, hidden_size, dropout=dropout)
            self.lstm_cells.append(cell)

            suffix = '_reverse' if direction == 1 else ''
            cell_name = 'cell{}'.format(suffix)
            self.add_module(cell_name, cell)

    def forward(self, input_, hidden_state=None):
        is_packed = isinstance(input_, PackedSequence)
        if is_packed:
            input_, batch_sizes = input_
            max_batch_size = batch_sizes[0]
        else:
            raise NotImplementedError()

        for cell in self.lstm_cells:
            cell.set_dropout_masks(max_batch_size)

        if hidden_state is None:
            num_directions = 2 if self.bidirectional else 1
            hx = torch.tensor(
                input_.data.new(num_directions, max_batch_size, self.hidden_size).zero_()
            )

            hidden_state = (hx, hx)

        rec_factory = functions.variable_recurrent_factory(batch_sizes)
        if self.bidirectional:
            layer = (rec_factory(lambda x, h: self.cell(x, h)),
                     rec_factory(lambda x, h: self.cell_reverse(x, h), reverse=True))
        else:
            layer = (rec_factory(lambda x, h: self.cell(x, h)),)

        func = functions.StackedRNN(layer, num_layers=1, lstm=True, dropout=0., train=self.training)
        next_hidden, output = func(input_, hidden_state, weight=[[], []])

        if is_packed:
            output = PackedSequence(output, batch_sizes)
        return output, next_hidden


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



