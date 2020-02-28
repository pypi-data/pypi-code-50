"""
Copyright 2020 Enzo Busseti.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import numpy as np

from .utils import DimensionError


def get_block_cumul_dims(blocks):

    block_cumul_dim_0 = np.zeros(len(blocks) + 1,
                                 dtype=int)
    block_cumul_dim_1 = np.zeros(len(blocks) + 1,
                                 dtype=int)

    for i, D in enumerate(blocks):
        block_cumul_dim_0[i + 1] = block_cumul_dim_0[i] + D.shape[0]
        block_cumul_dim_1[i + 1] = block_cumul_dim_1[i] + D.shape[1]

    return block_cumul_dim_0, block_cumul_dim_1


def block_diag_multiply(result, value, blocks,
                        block_cumul_dim_0,
                        block_cumul_dim_1):
    """result = result + block_diag(blocks)@value"""

    for i in range(len(blocks)):

        start_0 = block_cumul_dim_0[i]
        end_0 = block_cumul_dim_0[i + 1]

        start_1 = block_cumul_dim_1[i]
        end_1 = block_cumul_dim_1[i + 1]

        # if block_start == block_end:
        #     continue

        result[start_0:end_0] +=\
            blocks[i] @ value[start_1:end_1]


def slice_blocks(blocks,
                 block_cumul_dim_0,
                 block_cumul_dim_1,
                 left_mask,
                 right_mask):

    sliced_blocks = []

    for i, D in enumerate(blocks):

        block_start_0 = block_cumul_dim_0[i]
        block_end_0 = block_cumul_dim_0[i + 1]

        block_start_1 = block_cumul_dim_1[i]
        block_end_1 = block_cumul_dim_1[i + 1]

        left_mask_slice = left_mask[block_start_0:block_end_0]
        right_mask_slice = right_mask[block_start_1:block_end_1]

        sliced_D = D[left_mask_slice][:, right_mask_slice]

        sliced_blocks.append(sliced_D)

    return sliced_blocks


class BlockDiagonal(object):

    def __init__(self, blocks):

        self._blocks = blocks

        self._block_cumul_dim_0, \
            self._block_cumul_dim_1 = \
            get_block_cumul_dims(blocks)

    @property
    def shape(self):
        return (self._block_cumul_dim_0[-1],
                self._block_cumul_dim_1[-1])

    def __matmul__(self, value):

        if len(value.shape) == 2:
            result = np.zeros((self.shape[0], value.shape[1]))
        elif len(value.shape) == 1:
            result = np.zeros(self.shape[0])
        else:
            raise NotImplementedError

        block_diag_multiply(result, value, self._blocks,
                            self._block_cumul_dim_0,
                            self._block_cumul_dim_1)

        return result

    @property
    def T(self):
        return BlockDiagonal([D.T for D in self._blocks])

    def todense(self):
        result = np.zeros(self.shape)
        for i, D in enumerate(self._blocks):
            start_0 = self._block_cumul_dim_0[i]
            end_0 = self._block_cumul_dim_0[i + 1]

            start_1 = self._block_cumul_dim_1[i]
            end_1 = self._block_cumul_dim_1[i + 1]

            result[start_0:end_0, start_1:end_1] = D
        return result

    def slice(self, left_mask, right_mask):
        return BlockDiagonal(
            slice_blocks(self._blocks,
                         self._block_cumul_dim_0,
                         self._block_cumul_dim_1,
                         left_mask,
                         right_mask))


class SymmetricBlockDiagonal(BlockDiagonal):

    def __init__(self, blocks):
        super().__init__(blocks)

        for D in self._blocks:
            if not (D.shape[0] == D.shape[1]):
                raise DimensionError

    def symmetric_slice(self, mask):
        return SymmetricBlockDiagonal(
            slice_blocks(self._blocks,
                         self._block_cumul_dim_0,
                         self._block_cumul_dim_0,
                         mask,
                         mask))

    def regularized_inverse(self, lambd=0.):
        return SymmetricBlockDiagonal(
            [np.linalg.inv(D + np.eye(D.shape[0]) * lambd)
             for D in self._blocks])
