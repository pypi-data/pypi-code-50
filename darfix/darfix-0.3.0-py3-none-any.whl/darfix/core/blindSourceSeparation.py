# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2016-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/


__authors__ = ["J. Garriga"]
__license__ = "MIT"
__date__ = "28/01/2020"


import cv2
from enum import Enum
import logging
import numpy
from sklearn.decomposition import PCA, NMF

_logger = logging.getLogger(__file__)


class Method(Enum):
    """
    Different shifts approaches that can be used for the shift detection and
    correction.
    """
    PCA = "PCA"
    NNICA = "NNICA"
    NMF = "NMF"
    NNICA_NMF = "NNICA+NMF"

    @staticmethod
    def values():
        return list(map(lambda c: c.value, Method))


class BSS():
    """
    Class that provides the methods to apply blind source separation to a set
    of frames.
    It uses the sklearn library from some of the methods.

    :param array_like data_frames: array of frames.
    """
    def __init__(self, data_frames):

        self._data_frames = data_frames

        self.X = self._X_from_images(self.data_frames)
        """input frames (flatten)"""

    @property
    def data_frames(self):
        return self._data_frames

    def _X_from_images(self, data_frames):
        _logger.info("Flattening data")
        shape = data_frames.shape
        return data_frames.reshape((shape[0], shape[1] * shape[2]))

    def PCA(self, num_components=None, max_components=None):
        """
        Applies Principal component analysis.

        :param num_components: number of components to find. Read more in
                               `sklearn.decomposition.PCA`.
        :type: Union[int, float, None, str]
        """
        if num_components is None:
            log = "Computing PCA with {} components".format(self.X.shape[0])
        else:
            log = "Computing PCA with {} components".format(num_components)
        _logger.info(log)
        if not num_components:
            if not max_components:
                PCA_data = cv2.PCACompute2(self.X, numpy.mean(self.X,
                                           axis=0).reshape(1, -1))
            else:
                if max_components < 1:
                    max_components *= self.X.shape[0]
                PCA_data = cv2.PCACompute2(self.X, numpy.mean(self.X,
                                           axis=0).reshape(1, -1),
                                           maxComponents=int(max_components))
            return PCA_data
        model = PCA(n_components=num_components)
        if self.X is not None:
            W = model.fit_transform(self.X)
        return model.components_, W

    def whiten(self, X=None, num_components=None, center=True, rowvar=True):
        """Whiten the data in matrix X using PCA decomposition.

        The data corresponds to n samples of a p-dimensional random vector.
        The shape of the matrix can be either (n, p) if each row is considered
        to be a sample or (p, n) if each column is considered to be a sample.
        How to read the matrix entries is specified by the rowvar parameter.
        Before whitening, a dimensionality reduction step can be applied to the
        data to reduce the p dimensions of each sample to num_components dimensions.
        If num_components is None, the number of dimensions kept is the maximum
        possible (nº of non-zero eigenvalues). For example, if X is full rank
        (rank(X) = min(n, p)), then num_components = p if p < n, and
        num_components = n-1 if p >= n.

        :param Union[numpy_array,None] X: Data matrix.
        :param num_components: Number of PCA dimensions of the whitened samples.
        :param center: Whether to center the samples or not (zero-mean whitened samples).
        :param rowvar: Whether each row of X corresponds to one of the p variables or not.
        :type num_components: Union[uint,None]
        :type center: bool
        :type rowvar: bool
        :return: (Z, V): The whitened data matrix and the whitening matrix.

        """
        r = num_components

        if X is None:
            X = self.X

        if rowvar:
            X = X.transpose()

        # Data matrix contains n observations of a p-dimensional vector
        # Each observation is a row of X
        n, p = X.shape

        # Arbitrary (but sensible) choice. In any case, we remove the eigenvectors of 0 eigenvalue later
        if r is None:
            r = min(n, p)

        # Compute the mean of the observations (p-dimensional vector)
        mu = numpy.mean(X, axis=0)

        # If p > n compute the eigenvectors efficiently
        if p > n:
            # n x n matrix
            M = numpy.matmul((X - mu), (X - mu).transpose())

            # Eigenvector decomposition
            vals, vecs = numpy.linalg.eig(M)
            vals, vecs = vals.real, vecs.real

            # Sort the eigenvectors by "importance" and get the first r
            pairs = sorted([(vals[i], vecs[:, i]) for i in range(len(vals))], key=lambda x: x[0], reverse=True)
            pairs = [p for p in pairs if abs(p[0]) > 1e-10]  # Remove the eigenvectors of 0 eigenvalue
            pairs = pairs[:r]

            # nxr matrix of eigenvectors (each column is an n-dimensional eigenvector)
            E = numpy.array([p[1] for p in pairs]).transpose()

            # pxr matrix of the first r eigenvectors of the covariance of X
            # Note that we normalize!
            E = numpy.matmul((X - mu).transpose(), E)
            E /= numpy.linalg.norm(E, axis=0)

            # Eigenvalues of cov(X) to the -1/2
            # Note that we rescale the eigenvalues of M to get the eigenvalues of cov(X)!
            diag = numpy.array([1 / numpy.sqrt(p[0] / (n - 1)) for p in pairs])

        else:
            # p x p matrix
            C = numpy.cov(X, rowvar=False)

            # Eigenvector decomposition
            vals, vecs = numpy.linalg.eig(C)
            vals, vecs = vals.real, vecs.real

            # Sort the eigenvectors by "importance" and get the first r
            pairs = sorted([(vals[i], vecs[:, i]) for i in range(len(vals))], key=lambda x: x[0], reverse=True)
            pairs = [p for p in pairs if abs(p[0]) > 1e-10]  # Remove the eigenvectors of 0 eigenvalue
            pairs = pairs[:r]

            # pxr matrix of the first r eigenvectors of the covariance of X
            E = numpy.array([p[1] for p in pairs]).transpose()

            # Eigenvalues of cov(X) to the -1/2
            diag = numpy.array([1 / numpy.sqrt(p[0]) for p in pairs])

        # Warn that the specified number of components is larger
        # than the number of non-zero eigenvalues.
        if num_components is not None:
            if num_components > len(pairs):
                _logger.warning(
                    'The desired number of components (%d) is larger than the actual dimension'
                    ' of the PCA subespace (%d)' % (num_components, len(pairs))
                )

        # Center and whiten the data
        if center:
            X = X - mu

        # Whitening matrix
        V = E * diag

        # White data
        Z = numpy.matmul(X, V)

        if rowvar:
            Z = Z.transpose()

        # Since X is assumed to be (n, p) through the computations, the current
        # whitening matrix V is in fact the transpose of the actual whitening matrix.
        # Observation: If z = V * x for random column vectors x, z, then Z = X * V
        # for the (n, p) and (n, r) matrices X, Z of observations of x, z.
        V = V.transpose()

        return Z, V

    def non_negative_ICA(self, num_components, lr=0.03, max_iter=5000, tol=1e-8,
                         rowvar=True):
        """Compute the non-negative independent components of the linear generative
        model x = A * s.

        Here, x is a p-dimensional observable random vector and s is the latent
        random vector of length num_components, whose components are statistically
        independent and non-negative. The matrix X is assumed to hold n samples
        of x, stacked in rows (shape(X) = (n, p)) or columns (shape(X) = (p, n)),
        which can be specified by the rowvar parameter. In practice, if
        shape(X) = (p, n) (resp. shape(X) = (n, p)) this function solves X = A * S
        (resp. X = S.T * A.T) both for S and A, where A is the so-called mixing
        matrix, with shape (p, num_components), and S is a (num_components, n)
        matrix which contains n samples of the latent source vector, stacked in
        columns.

        This function implements the method presented in:
        `Blind Separation of Positive Sources by Globally Convergent Gradient Search´
        (https://core.ac.uk/download/pdf/76988305.pdf)

        :param num_components: Dimension of s. Number of latent random variables.
        :param float lr: Learning rate of gradient descent.
        :param int max_iter: Maximum number of iterations of gradient descent.
        :param float tol: Tolerance on update at each iteration.
        :param bool rowvar: Whether each row of X corresponds to one of the p
            variables or not.
        :type num_components: Union[uint, None]

        :return: (S, A) if rowvar == True else (S.T, A)

        """
        # Whiten the data
        Z, V = self.whiten(self.X, num_components, center=False, rowvar=rowvar)

        if num_components > V.shape[0]:
            _logger.warning(
                'The desired number of sources (%d) is larger than the actual dimension'
                ' of the whitened observable random vector (%d). The number of sources'
                ' will be set to %d' % (num_components, V.shape[0], V.shape[0])
            )
            num_components = V.shape[0]

        # We assume rowvar is True throughout the algorithm
        if not rowvar:
            Z = Z.transpose()

        # Initialize W
        W = numpy.eye(num_components)

        for i in range(max_iter):
            W0 = W

            # Compute gradient
            Y = numpy.matmul(W, Z)
            f = numpy.minimum(0, Y)
            f_Y = numpy.matmul(f, Y.transpose())
            E = (f_Y - f_Y.transpose()) / Y.shape[1]

            # Gradient descent
            W -= lr * numpy.matmul(E, W)

            # Symmetric orthogonalization
            M = numpy.matmul(W, W.transpose())
            vals, vecs = numpy.linalg.eig(M)
            vals, vecs = vals.real, vecs.real

            W_sqrt = vecs / numpy.sqrt(vals)
            W_sqrt = numpy.matmul(W_sqrt, vecs.transpose())
            W = numpy.matmul(W_sqrt, W)

            if numpy.linalg.norm(W - W0) < tol:
                break

        # Independent sources (up to an unknown permutation y = Q * s)
        Y = numpy.matmul(W, Z)

        # Compute the mixing matrix A' = A * Q.T
        # (which is A up to a permutation of its columns)
        # from the identity y = Q * s = W * V * A * s.
        # It then holds x = A * s = A * Q.T * y = A' * y.
        # Note: A' is computed as the right Moore-Penrose
        # inverse of W * V, but A' may not be unique since
        # in general p != num_components and any right inverse
        # could be taken as A'.
        WV = numpy.matmul(W, V)
        WV_ = numpy.matmul(WV, WV.transpose())
        WV_ = numpy.linalg.inv(WV_)
        WV_ = numpy.matmul(WV.transpose(), WV_)

        if not rowvar:
            Y = Y.transpose()

        return Y, WV_

    def NMF(self, num_components, init='random', random_state=0):
        """
        Non-Negative Matrix Factorization.
        For more look at `sklearn.decomposition.NMF`

        :param num_components: number of components.
        :param init: method used to initialize the procedure.
        :param int random_state: seed used by the random number generator.
        """
        _logger.info("Computing NMF with {} components".format(num_components))
        model = NMF(n_components=num_components, init=init,
                    random_state=random_state)
        W = model.fit_transform(self.X)

        return model.components_, W

    def NNICA_NMF(self, num_components, lr=0.03, max_iter=5000, tol=1e-8,
                  rowvar=True):
        """Non-negative matrix factorization with non-negative ICA (NICA)
        initialization.

        Under the linear generative model x = A * s, where x is a p-dimensional
        observable random vector, s is the latent non-negative random vector of
        length num_components and A is a fixed (but unknown) non-negative matrix,
        this function tries to determine both s and A. The data matrix X is
        assumed to hold n samples of x, stacked in rows (shape(X) = (n, p)) or
        columns (shape(X) = (p, n)), which can be specified by the rowvar parameter.
        In practice, if shape(X) = (p, n) (resp. shape(X) = (n, p)) this function
        solves X = A * S (resp. X = S.T * A.T) both for S and A, where A is the
        so-called mixing matrix, with shape (p, num_components), and S is a
        (num_components, n) matrix which contains n samples of the latent source
        vector, stacked in columns.

        The non-uniqueness (non-convexity) property of NMF implies that the
        solution depends on the initial factor matrices.
        This function implements the idea presented in:
        `Efficient initialization for nonnegative matrix factorization based on
        nonnegative independent component analysis´
        (https://ieeexplore.ieee.org/document/7602947)
        which suggests that a good initialization is based on the factorization
        given by non-negative ICA.

        :param num_components: Dimension of s. Number of latent random variables.
        :param float lr: Learning rate of gradient descent.
        :param int max_iter: Maximum number of iterations of gradient descent.
        :param float tol: Tolerance on update at each iteration.
        :param bool rowvar: Whether each row of X corresponds to one of the p
            variables or not.
        :type num_components: Union[uint, None]

        :return: (S, A) if rowvar == True else (S.T, A)

        """
        S, A = self.non_negative_ICA(num_components, lr, max_iter, tol, rowvar)

        X = self.X
        # We assume rowvar is True throughout the algorithm
        if not rowvar:
            X = X.transpose()
            S = S.transpose()

        # Initial NMF factorization: X = F0 * G0
        F0 = numpy.abs(A)
        G0 = numpy.abs(S)

        W0 = G0.transpose().copy()  # Make array C-contiguous
        H0 = F0.transpose()

        nmf = NMF(n_components=min(num_components, S.shape[0]), init='custom')
        W = nmf.fit_transform(X.transpose(), W=W0, H=H0)
        H = nmf.components_

        A = H.transpose()
        W = W.copy()

        if rowvar:
            S = W.transpose()

        return S, A
