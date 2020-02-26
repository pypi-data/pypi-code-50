import torch
import torch.nn as nn
import torchnlp.encoders as tencoder
import torchnlp.encoders.text.text_encoder as ttencoder

from alanbootstrap.models import layers
from alanbootstrap.components import ast as ast_module

import typing


class ASTEncoder(nn.Module):
    PAD_TOKEN = '<PAD>'
    """
    Encode Abstract Syntax Tree by pre-order transversal.
    """
    def __init__(self,
                 vocab: typing.List[typing.AnyStr],
                 steps: int, emb_dims: int, rnn_dims: int, rnn_layer=1, rnn_dropout=0.3,
                 parent_feeding=False, bidirectional=False
                 ):
        super().__init__()

        self.label_encoder = tencoder.LabelEncoder(vocab, reserved_labels=[ASTEncoder.PAD_TOKEN])
        vocab_size = self.label_encoder.vocab_size
        self.vocab_size = vocab_size
        self.steps = steps
        self.rnn_layers = rnn_layer
        self.emb_dims = emb_dims
        self.rnn_dims = rnn_dims
        self.rnn_dropout = rnn_dropout
        self.parent_feeding = parent_feeding
        self.bidirectional = bidirectional

        self.embed = nn.Embedding(vocab_size, emb_dims)
        self.rnn = nn.LSTM(
            emb_dims, rnn_dims, num_layers=int(rnn_layer), bidirectional=bidirectional, dropout=rnn_dropout
        )
        self.attention = layers.Attention(rnn_dims if not bidirectional else rnn_dims*2)

        self.reset_parameters()

    def forward(self, ast_batch: typing.List[ast_module.AST]):
        if self.parent_feeding:
            raise NotImplementedError
        else:
            self_input = self.batch_encode_and_pad_ast(ast_batch, parent=False)

            xs = self.embed(self_input.tensor)
            xs = xs.transpose(0, 1)
            hss, (_, _) = self.rnn(xs)
            hs, _ = self.attention(hss.transpose(0, 1))

            return hs

    def batch_encode_and_pad_ast(self, ast_batch: typing.List[ast_module.AST], parent=False):

        if parent:
            # ASTs to strings
            self_batch, head_batch = [self.ast_to_seq(ast_, parent=parent) for ast_ in ast_batch]
            # encode: string list to index tensor
            self_tensor = self.label_encoder.batch_encode(self_batch)
            head_tensor = self.label_encoder.batch_encode(head_batch)
            # padding
            self_tensor = ttencoder.pad_tensor(self_tensor, self.steps, padding_index=0)
            head_tensor = ttencoder.pad_tensor(head_tensor, self.steps, padding_index=0)
            return self_tensor, head_tensor
        else:
            # ASTs to strings
            self_batch = [self.ast_to_seq(ast_, parent=parent) for ast_ in ast_batch]
            # encode: string list to index tensor
            self_batch = [self.label_encoder.batch_encode(ast_types) for ast_types in self_batch]
            self_batch[0] = ttencoder.pad_tensor(self_batch[0], self.steps, padding_index=0)
            # padding
            self_tensor = ttencoder.stack_and_pad_tensors(self_batch, padding_index=0, dim=0)

            return self_tensor

    def ast_to_seq(self, ast: ast_module.AST, parent=False):
        flat_ast = ast.preorder(parent=parent, max_len=self.steps)

        if not parent:
            ast_type = [ast_.get_type() for ast_ in flat_ast]
            return ast_type
        else:
            flat_ast, flat_head = list(zip(*flat_ast))

            self_type = [ast_.get_type() for ast_ in flat_ast]
            head_type = [ast_.get_type() if ast_ is not None else 'None' for ast_ in flat_head]

            return self_type, head_type

    def reset_parameters(self):
        nn.init.xavier_normal(self.embed.weight)










