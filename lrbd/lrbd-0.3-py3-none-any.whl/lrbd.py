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
import scipy.sparse as sp


class DimensionError(Exception):
    pass


class LowRankBlockDiag(object):

    def __init__(self, V, S, D_blocks):
        """Represent the matrix V.T @ S @ V + block_diag(D_blocks).

        - V: a sparse or dense matrix
        - S: a dense matrix
        - D_blocks: an iterator of dense matrices
        """

        self.V = V
        self.k, self.n = self.V.shape

        self._S = S
        if not ((self._S.shape[0] == self._S.shape[1])
                and (self._S.shape[0] == self.k)):
            raise DimensionError

        self.D_blocks = D_blocks
        self.num_blocks = len(self.D_blocks)
        self.block_cumul_dim = np.zeros(self.num_blocks + 1, dtype=int)

        for i, D in enumerate(self.D_blocks):

            if not (D.shape[0] == D.shape[1]):
                raise DimensionError

            self.block_cumul_dim[i + 1] = \
                self.block_cumul_dim[i] + D.shape[0]

        if not self.block_cumul_dim[-1] == self.n:
            raise DimensionError

    @property
    def shape(self):
        return (self.n, self.n)

    def todense(self):
        return np.array(self.V.T @ self._S @ self.V +
                        sp.block_diag(self.D_blocks))

    def __matmul__(self, value):
        """self @ value"""

        result = self.V.T @ (self._S @ (self.V @ value))

        for i in range(self.num_blocks):
            block_start = self.block_cumul_dim[i]
            block_end = self.block_cumul_dim[i + 1]
            result[block_start:block_end] +=\
                self.D_blocks[i] @ value[block_start:block_end]
        return result

    def __rmatmul__(self, value):
        return self.__matmul__(value)

    def inverse(self):
        """self^(-1) as a LowRankBlockDiag"""
        raise NotImplemented

    def regularized_solve(self, value, lambd=0.):
        """(self + lamb * I)^(-1) @ value"""
        raise NotImplemented

    # def masked_matmul(self, entrance_mask, exit_mask, vector):
    #     """Compute self[exit_mask:entrance_mask] @ vector

    #     - entrance_mask: a boolean array
    #     - exit_mask: a boolean array
    #     - vector: a numeric array

    #     Note: If the matrix V is sparse, slicing it might
    #     be an expensive operation. If it is dense
    #     """

    #     if not sum(entrance_mask) == len(vector):
    #         raise DimensionError

    #     result = self.V[:, entrance_mask] @ vector
    #     result = self._S @ result
    #     result = self.V[exit_mask] @ result

    #     # spacing
    #     # spacing
    #     # spacing
    #     # spacing        # spacing
    #     # spacing
