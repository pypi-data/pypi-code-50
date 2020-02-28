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

from functools import lru_cache
import numpy as np
import scipy.sparse as sp

from .utils import DimensionError
from .bd import SymmetricBlockDiagonal


class LowRankBlockDiag(object):

    def __init__(self, V, S, D_blocks):
        """Represent the matrix V.T @ S @ V + block_diag(D_blocks).

        - V: a numpy 2d array
        - S: a numpy 2d array
        - D_blocks: an iterator of numpy 2d arrays
        """

        self._V = np.array(V)
        self._k, self._n = self._V.shape

        self._S = np.array(S)
        if not ((self._S.shape[0] == self._S.shape[1])
                and (self._S.shape[0] == self._k)):
            raise DimensionError

        self._D = SymmetricBlockDiagonal(D_blocks)

        if not self._D.shape[0] == self._n:
            raise DimensionError

    @property
    def shape(self):
        return (self._n, self._n)

    @property
    def V(self):
        return self._V

    @property
    def S(self):
        return self._S

    @property
    def D(self):
        return self._D

    def todense(self):
        return np.array(self._V.T @ self._S @ self._V +
                        self._D.todense())

    def __matmul__(self, value):
        """self @ value"""

        result = self._V.T @ (self._S @ (self._V @ value))

        result += self._D @ value

        return result

    def masked_matmul(self, left_mask, right_mask, value):

        result = self._V[:, left_mask].T @ \
            (self._S @ (self._V[:, right_mask] @ value))

        sliced_D = self._D.slice(left_mask, right_mask)

        return result + sliced_D @ value

    # def __rmatmul__(self, value):
    #     return self.__matmul__(value)

    # def inverse(self):
    #     """self^(-1) as a LowRankBlockDiag"""
    #     block_inverses = [np.linalg.inv(D)
    #                       for D in self._D_blocks]
    #     #block_inverses_dense = sp.block_diag()
    #     S_inverse = np.linalg.inv(self._S)

    #     # internal = S_inverse +
    #     raise NotImplemented

    def symmetric_submatrix(self, mask):
        return self._symmetric_submatrix(tuple(mask))

    @lru_cache(maxsize=2)  # used to cache last solver
    def _symmetric_submatrix(self, mask):
        """self[mask][:,mask]"""

        mask = np.array(mask)
        return LowRankBlockDiag(self._V[:, mask],
                                self._S,
                                self._D.symmetric_slice(mask)._blocks)

    def regularized_solve(self, value, lambd=0.):
        """(self + lamb * I)^(-1) @ value"""
        #print('inverting A')

        if not hasattr(self, 'D_inv'):
            self.D_inv = self._D.regularized_inverse(lambd)

        if not hasattr(self, '_internal'):
            # print('inverting S')
            self._internal = np.linalg.inv(self._S)
            # print('computing  V@A^(-1)@V.T')
            # temp = np.zeros(self._V.T.shape)
            temp = self.D_inv @ self._V.T
            self._internal += self._V @ temp
            # print('inverting internal')
            self._internal = np.linalg.inv(self._internal)

        result = self.D_inv @ value

        second_part = np.array(result)
        second_part = (self._V.T @ (self._internal @ (self._V @ second_part)))

        result -= self.D_inv @ second_part

        return result

    def regularized_schur(self, left_mask, right_mask, value, lambd=0.):
        """self[out_mask,in_mask] @ \
            (self[in_mask,in_mask] + lambd * I )^(-1) @ value """

        submatrix = self.symmetric_submatrix(right_mask)

        result = submatrix.regularized_solve(value, lambd=lambd)

        return self.masked_matmul(left_mask, right_mask, result)

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

    #     result = self._V[:, entrance_mask] @ vector
    #     result = self._S @ result
    #     result = self._V[exit_mask] @ result

    #     # spacing
    #     # spacing
    #     # spacing
    #     # spacing        # spacing
    #     # spacing
