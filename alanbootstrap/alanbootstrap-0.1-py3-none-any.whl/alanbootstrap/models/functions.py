import torch
import torch.functional as F


def variable_recurrent_factory(batch_sizes):
    def fac(inner, reverse=False):
        if reverse:
            return VariableRecurrentReverse(batch_sizes, inner)
        else:
            return VariableRecurrent(batch_sizes, inner)
    return fac


def VariableRecurrent(batch_sizes, inner):

    def forward(input_, hidden, weight):
        output = []
        input_offset = 0
        last_batch_size = batch_sizes[0]
        hiddens = []
        flat_hidden = not isinstance(hidden, tuple)
        if flat_hidden:
            hidden = (hidden,)
        for batch_size in batch_sizes:
            step_input = input_[input_offset:input_offset + batch_size]
            input_offset += batch_size

            dec = last_batch_size - batch_size
            if dec > 0:
                hiddens.append(tuple(h[-dec:] for h in hidden))
                hidden = tuple(h[:-dec] for h in hidden)
            last_batch_size = batch_size

            if flat_hidden:
                hidden = (inner(step_input, hidden[0], *weight),)
            else:
                hidden = inner(step_input, hidden, *weight)

            output.append(hidden[0])
        hiddens.append(hidden)
        hiddens.reverse()

        hidden = tuple(torch.cat(h, 0) for h in zip(*hiddens))
        assert hidden[0].size(0) == batch_sizes[0]
        if flat_hidden:
            hidden = hidden[0]
        output = torch.cat(output, 0)

        return hidden, output

    return forward


def VariableRecurrentReverse(batch_sizes, inner):

    def forward(input_, hidden, weight):
        output = []
        input_offset = input_.size(0)
        last_batch_size = batch_sizes[-1]
        initial_hidden = hidden
        flat_hidden = not isinstance(hidden, tuple)
        if flat_hidden:
            hidden = (hidden,)
            initial_hidden = (initial_hidden,)
        hidden = tuple(h[:batch_sizes[-1]] for h in hidden)
        for batch_size in reversed(batch_sizes):
            inc = batch_size - last_batch_size
            if inc > 0:
                hidden = tuple(torch.cat((h, ih[last_batch_size:batch_size]), 0)
                               for h, ih in zip(hidden, initial_hidden))
            last_batch_size = batch_size
            step_input = input_[input_offset - batch_size:input_offset]
            input_offset -= batch_size

            if flat_hidden:
                hidden = (inner(step_input, hidden[0], *weight),)
            else:
                hidden = inner(step_input, hidden, *weight)
            output.append(hidden[0])

        output.reverse()
        output = torch.cat(output, 0)
        if flat_hidden:
            hidden = hidden[0]
        return hidden, output

    return forward


def StackedRNN(inners, num_layers, lstm=False, dropout=0, train=True):

    num_directions = len(inners)
    total_layers = num_layers * num_directions

    def forward(input_, hidden, weight):
        assert(len(weight) == total_layers)
        next_hidden = []

        if lstm:
            hidden = list(zip(*hidden))

        for i in range(num_layers):
            all_output = []
            for j, inner in enumerate(inners):
                l = i * num_directions + j

                hy, output = inner(input_, hidden[l], weight[l])
                next_hidden.append(hy)
                all_output.append(output)

            input_ = torch.cat(all_output, input_.dim() - 1)

            if dropout != 0 and i < num_layers - 1:
                input_ = F.dropout(input_, p=dropout, training=train, inplace=False)

        if lstm:
            next_h, next_c = zip(*next_hidden)
            next_hidden = (
                torch.cat(next_h, 0).view(total_layers, *next_h[0].size()),
                torch.cat(next_c, 0).view(total_layers, *next_c[0].size())
            )
        else:
            next_hidden = torch.cat(next_hidden, 0).view(
                total_layers, *next_hidden[0].size())

        return next_hidden, input_

    return forward