from __future__ import annotations
from typing import Any, Callable, Iterable, Optional, Tuple, Union

import collections
import contextlib
import dlib
import functools
import math
import numpy as np
import os
import pathlib
import tempfile
import scipy.interpolate, scipy.linalg, scipy.optimize, scipy.spatial


__all__ = [
    "closest_trio",
    "expand",
    "extrapolate",
    "GoldenSectionSearch",
    "interpolate",
    "IOParams",
    "lcm",
    "linearly_independent",
    "MaxLIPOTR",
    "memoize",
    "mkdir_safe",
    "NestedDictionary",
    "nontrivial_vector",
    "normalize",
    "orthogonal_complement",
    "periodicity",
    "perpendicular_vector",
    "rotation_matrix",
    "rotation_matrix_m_to_n",
    "sample_spherical_triangle",
    "Settings",
    "spherical_excess",
    "temporary_seed",
    "work_dir",
]


def closest_trio(points):
    """
    Finds the three closest points from a given list of points.

    Parameters
    ----------
    points : numpy.ndarray
        3xNp Numpy array whose columns represent points on the unit sphere, where Np is the number of points.

    Returns
    -------
    numpy.ndarray:
        3x3 Numpy array whose columns are the three closest points from the given list of points.
    """
    tree = scipy.spatial.KDTree(points.T)
    pair = points.T[min(zip(*tree.query(points.T, k=2)), key=lambda t: t[0][1])[1]].T
    return points.T[
        min(zip(*tree.query(pair[:, 0, None].T, k=3)), key=lambda t: t[0][1])[1]
    ].T


def expand(path: str, dir: Optional[str] = None) -> str:
    p = pathlib.Path(path).expanduser()
    if dir is not None:
        p = pathlib.Path(dir).joinpath(p)
    return str(p.expanduser().resolve())


def extrapolate(x, y, x_extrap_to):
    # simple linear extrapolation
    x_lb, x_nlb, *_, x_nub, x_ub = x
    y_lb, y_nlb, *_, y_nub, y_ub = y

    # extrapolate down
    m_lb = (y_nlb - y_lb) / (x_nlb - x_lb)
    x_down = x_extrap_to[np.where(x_extrap_to < x_lb)]
    y_down = y_lb + m_lb * (x_down - x_lb)

    # extrapolate up
    m_ub = (y_ub - y_nub) / (x_ub - x_nub)
    x_up = x_extrap_to[np.where(x_extrap_to > x_ub)]
    y_up = y_ub + m_ub * (x_up - x_ub)

    return np.hstack((x_down, x, x_up)), np.hstack((y_down, y, y_up))


def interpolate(x, y, x_interp_to, method="cubic_spline"):
    if method == "sprague":
        return interpolate_sprague(x=x, y=y, x_interp_to=x_interp_to)
    elif method == "cubic_spline":
        return interpolate_cubic_spline(x=x, y=y, x_interp_to=x_interp_to)
    elif method == "linear_spline":
        return interpolate_linear_spline(x=x, y=y, x_interp_to=x_interp_to)
    else:
        raise ValueError(f"Interpolation method {method} not recognized.")


def interpolate_cubic_spline(x, y, x_interp_to):
    x_lb, *_, x_ub = x
    x_interp = x_interp_to[(x_interp_to >= x_lb) & (x_interp_to <= x_ub)]
    y_interp = scipy.interpolate.CubicSpline(x=x, y=y)(x_interp)

    return x_interp, y_interp


def interpolate_linear_spline(x, y, x_interp_to):
    x_lb, *_, x_ub = x
    x_interp = x_interp_to[(x_interp_to >= x_lb) & (x_interp_to <= x_ub)]
    y_interp = np.interp(x=x_interp, xp=x, fp=y)

    return x_interp, y_interp


def interpolate_sprague(x, y, x_interp_to):
    # FIXME: this implementation of Sprague interpolation is broken somehow!
    # data taken from https://link.springer.com/content/pdf/10.1007/978-3-642-27851-8_366-1.pdf
    # FIXME: we have to convert spec to wavelength spec with nanometer units first
    interp_coeffs = np.array(
        [
            [0, 0, 24, 0, 0, 0],
            [2, -16, 0, 16, -2, 0],
            [-1, -16, -30, 16, -1, 0],
            [-9, 39, 70, 66, -33, 7],
            [13, -64, 126, -124, 61, -12],
            [-5, 25, -50, 50, -25, 5],
        ]
    )
    # Sprague boundary points
    sbp1 = np.dot([884, -1960, 3033, -2648, 1080, 180], y[:6]) / 209
    sbp2 = np.dot([508, -540, 488, -367, 144, -24], y[:6]) / 209
    sbp3 = np.dot([-24, 144, -367, 488, -540, 508], y[-6:]) / 209
    sbp4 = np.dot([-180, 1080, -2648, 3033, -1960, 884], y[-6:]) / 209

    sprague_y = np.hstack([[sbp1, sbp2], y, [sbp3, sbp4]])[:, None]

    poly_c_mat = np.hstack(
        [
            (interp_coeffs @ np.roll(sprague_y, -i)[:6])
            for i in range(len(sprague_y) - 5)
        ]
    )  # [::-1]

    def interp(x_to):
        lower_bound_indices = np.searchsorted(x, x_to) - 1
        scaled_x = (x_to - x[lower_bound_indices]) / (
            x[lower_bound_indices + 1] - x[lower_bound_indices]
        )
        scaled_x_powers = np.vander(x=scaled_x, N=6)
        poly_coeffs = poly_c_mat[:, lower_bound_indices]
        # print(poly_coeffs.shape)
        # print(scaled_x.shape)
        return np.array(
            [
                np.polyval(p=coeffs[::-1], x=X)
                for coeffs, X in zip(poly_coeffs.T, scaled_x)
            ]
        )
        return (scaled_x_powers * poly_coeffs.T).sum(axis=1)

    y_interp = interp(x=x_interp_to)

    return x_interp_to, y_interp


_IO = collections.namedtuple("IO", ["work_dir", "inp", "out"])


class IOParams:
    def __init__(
        self,
        inp: Optional[str] = None,
        out: Optional[str] = None,
        work_dir: Optional[str] = ".",
        keep_logs: Optional[bool] = True,
    ) -> None:
        self._inp = inp
        self._out = out
        self._work_dir = expand(work_dir)
        self.keep_logs = keep_logs

    @contextlib.contextmanager
    def __call__(self):
        with contextlib.nullcontext(
            self._work_dir
        ) if self.keep_logs else tempfile.TemporaryDirectory(dir=self._work_dir) as wd:
            try:
                mkdir_safe(wd)
                yield _IO(
                    wd,
                    expand(self._inp, wd) if self._inp is not None else None,
                    expand(self._out, wd) if self._out is not None else None,
                )
            finally:
                pass


def lcm(numbers: Iterable[int]) -> int:
    a, *b = numbers
    if len(b) > 1:
        return lcm(numbers=(a, lcm(numbers=b)))
    else:
        [b] = b
        return a * b // math.gcd(a, b)


def linearly_independent(vectors, indep=None):
    # vectors is kxNv array where Nv is number of vectors
    # indep is kxNi array where Ni is number of linearly independent vectors

    if indep is None:
        indep = np.array([])

    k, *_ = vectors.shape  # dimension of vectors
    *_, n = indep.shape  # number of independent vectors

    if n == k:
        return indep
    else:
        array_generator = (np.vstack([*indep.T, v]) for v in vectors.T)
        try:
            indep = next(
                a
                for a in array_generator
                if scipy.linalg.null_space(a).shape[-1] == k - n - 1
            ).T
            return linearly_independent(vectors=vectors, indep=indep)
        except StopIteration:
            return indep


class _Cache(collections.OrderedDict):
    def last_result(self, n=1):
        return tuple(self.values())[-n]

    def last_args(self, n=1):
        args, kwarg_items = tuple(self.keys())[-n]
        return args, dict(kwarg_items)


def memoize(func):
    func.cache = _Cache()

    @functools.wraps(func)
    def memoized(*args, **kwargs):
        k = (args, frozenset(kwargs.items()))
        if k not in func.cache:
            func.cache[k] = func(*args, **kwargs)

        return func.cache[k]

    return memoized


def mkdir_safe(dir: str) -> None:
    with contextlib.suppress(FileExistsError):
        os.makedirs(dir)


def nontrivial_vector(R, seed: Optional[int] = None):
    """
    Generates a vector which is acted upon nontrivially (i.e. is sent to a linearly independent vector) by the given rotation matrix.

    Parameters
    ----------
    R: numpy.ndarray
        3x3 numpy array representing a rotation matrix.

    Returns
    -------
    numpy.ndarray:
        3x1 numpy array representing a vector which is acted upon nontrivially by R.
    """
    if (
        np.allclose(R, np.eye(R.shape[0]))
        or np.allclose(R, -np.eye(R.shape[0]))
        or np.allclose(R, np.zeros(R.shape[0]))
    ):
        return None

    # get the eigenvectors with real (i.e. 1 or -1) eigenvalues, since these are mapped to colinear vectors by R
    # each column of evecs is an eigenvector of R
    evals, evecs = scipy.linalg.eig(R)

    # FIXME: why np.real(evec) instead of simply evec?
    real_eigenbasis = np.real(evecs.T[np.isclose(np.imag(evals), 0)].T)

    # form the linear combination of the "trivial" eigenvectors
    # get random coefficients between 1 and 2 so that 0 is never chosen
    # the result is guaranteed to be mapped to a linearly independent vector
    # by R because the "trivial" eigenvectors do not all have the same eigenvalues #all have different eigenvalues
    # this is true because R is not proportional to the identity matrix
    with temporary_seed(seed=seed):
        coeffs = np.random.uniform(low=1, high=2, size=(real_eigenbasis.shape[1], 1))

    return normalize(v=real_eigenbasis @ coeffs)


def normalize(v):
    norm = scipy.linalg.norm(v)

    return v / norm if norm > 0 else v


def orthogonal_complement(v, l):
    return normalize(v - np.dot(v.T, l) * l)


def periodicity(matrix) -> int:
    # if A is periodic, then its eigenvalues are roots of unity, and its periodicity is the lcm of the periodicities of these roots of unity
    # kth roots of unity form the vertices of a regular k-gon with internal angles 2*pi/k
    # the angle between two such vertices z1=a+jb and z2=c+jd is given by cos(theta) = a*c + b*d = Re(z1*conj(z2))
    # choose z2 = z1**2 (clearly z2 is still a root of unity); then z1*conj(z2) = exp(2*pi*j/k)*exp(-4*pi*j/k) = exp(-2*pi*j/k)
    # then Re(z1*conj(z2)) = Re(exp(-2*pi*j/k)) = cos(2*pi*j/k) = Re(z1)
    # so 2*pi*j/k = arccos(Re(z1)) -> j/k = arccos(Re(z1))/(2*pi), and k = lcm(k/j1, k/j2,...)
    evals = scipy.linalg.eigvals(matrix)
    angles = (max(min(z.real, 1), -1) for z in evals if not np.isclose(z, 1))
    # if z is close to 1, then it contributes a period of 1, which doesn't impact the lcm and therefore the final period
    periods = (int((2 * np.pi / np.arccos(angle)).round()) for angle in angles)

    try:
        return lcm(numbers=periods)
    except ValueError:
        # `periods` must not have any values in it, so all evals must have been close to 1
        return 1


def perpendicular_vector(a, b=None):
    """
    Generates a unit vector which is perpendicular to one or two given nonzero vector(s).

    Parameters
    ----------
    a: numpy.ndarray
        3x1 Numpy array representing a nonzero vector.
    b: numpy.ndarray
        3x1 Numpy array representing a nonzero vector.

    Returns
    -------
    numpy.ndarray:
        3x1 Numpy array representing a unit vector which is perpendicular to a (and b, if applicable).
    """
    if b is None:
        m = np.zeros(a.shape)

        # storing in variable for reuse
        ravel_a = np.ravel(a)

        # index of the first nonzero element of a
        i = (ravel_a != 0).argmax()
        # first index of a which is not i
        j = next(ind for ind in range(len(ravel_a)) if ind != i)
        # unravel indices for 3x1 arrays m and a
        i, j = (
            np.unravel_index(i, a.shape),
            np.unravel_index(j, a.shape),
        )

        # make m = np.array([[-ay,ax,0]]).T so np.dot(m.T,a) = -ax*ay + ax*ay = 0
        m[j] = a[i]
        m[i] = -a[j]
    else:
        m = np.cross(a.T, b.T).T

    return normalize(v=m)


def rotation_matrix(axis, cos_theta):
    """
    Generates a matrix which rotates a vector a given angle about a given axis.

    Parameters
    ----------
    axis: numpy.ndarray
        3x1 Numpy array representing the vector whose direction is the axis of rotation.
    cos_theta: float
        Cosine of angle of rotation about the axis of rotation.

    Returns
    -------
    numpy.ndarray:
        3x3 Numpy array representing the rotation matrix which rotates a vector by the given angle about the given axis.
    """
    u1, u2, u3 = np.ravel(normalize(v=axis))

    K = np.array([[0, -u3, u2], [u3, 0, -u1], [-u2, u1, 0]])

    sin_theta = np.sqrt(1 - cos_theta ** 2)

    return (np.eye(3) + sin_theta * K + (1 - cos_theta) * (K @ K)).astype("float64")


def rotation_matrix_m_to_n(m, n):
    """
    Generates a matrix which rotates one given vector to another.

    Parameters
    ----------
    m: numpy.ndarray
        3x1 Numpy array representing the vector to be rotated.
    n: numpy.ndarray
        3x1 Numpy array representing the vector after rotation, i.e. the target vector.

    Returns
    -------
    numpy.ndarray:
        3x3 Numpy array representing the rotation matrix which maps m to n.
    """
    # make rotation axis, which is perpendicular to both m and n
    # no need to normalize, since rotation_matrix will do that for us
    u = np.cross(m.T, n.T).T

    # cosine of the angle between m and n
    c = np.dot(normalize(v=m).T, normalize(v=n))

    return rotation_matrix(axis=u, cos_theta=c)


def sample_spherical_triangle(A, B, C, sin_alpha, sin_beta, sin_gamma, seed=None):
    # see https://www.graphics.cornell.edu/pubs/1995/Arv95c.pdf
    # a, b, and c are cross products of normal vectors, so their magnitudes
    # are the sine of the angles between these normal vectors; these angles
    # are also the angles between planes and therefore the great arcs which
    # define the legs of the triangle; therefore, these angles are also
    # the internal angles of the triangle
    eps = np.finfo(float).eps  # machine precision

    with temporary_seed(seed=seed):
        fraction, cos_theta = np.random.uniform(low=eps, high=1, size=2)

    cos_alpha, cos_beta, cos_gamma = np.sqrt(
        (1 - sin_alpha ** 2, 1 - sin_beta ** 2, 1 - sin_gamma ** 2)
    )

    area = fraction * spherical_excess(
        cos_alpha=cos_alpha, cos_beta=cos_beta, cos_gamma=cos_gamma
    )
    cos_area, sin_area = np.cos(area), np.sin(area)

    s = sin_area * cos_alpha - cos_area * sin_alpha  # sin(area - alpha)
    t = cos_area * cos_alpha + sin_area * sin_alpha  # cos(area - alpha)
    u = t - cos_alpha
    v = s + (cos_gamma + cos_beta * cos_alpha) / sin_beta  # spherical law of cosines

    q = ((v * t - u * s) * cos_alpha - v) / ((v * s + u * t) * sin_alpha)
    C_prime = q * A + np.sqrt(1 - q ** 2) * orthogonal_complement(v=C, l=A)

    z = 1 - cos_theta * (1 - np.dot(C_prime.T, B))
    return z * B + np.sqrt(1 - z ** 2) * orthogonal_complement(v=C_prime, l=B)


def spherical_excess(cos_alpha: float, cos_beta: float, cos_gamma: float) -> float:
    # Girard's formula for spherical excess
    return np.arccos((cos_alpha, cos_beta, cos_gamma)).sum() - np.pi


@contextlib.contextmanager
def temporary_seed(seed: int) -> None:
    # adapted from https://stackoverflow.com/a/49557127
    state = np.random.get_state()
    if seed is not None:
        np.random.seed(seed)
    try:
        yield
    finally:
        np.random.set_state(state)


@contextlib.contextmanager
def work_dir(dir: Optional[str] = None):
    # FIXME: learn how to type annotation yields
    with contextlib.nullcontext(
        expand(dir)
    ) if dir is not None else tempfile.TemporaryDirectory(dir=dir) as wd:
        try:
            mkdir_safe(dir=wd)
            yield wd
        finally:
            pass


# -------------------------------------------------------------------- #


class GoldenSectionSearch:
    def __init__(self, objective_function):
        self.objective_function = objective_function

    @memoize
    def evaluate_objective(self, x):
        return self.objective_function(x)

    def optimize(self, delta, tolerance):
        bracket = self._find_gss_bracket(delta=delta)

        return scipy.optimize.minimize_scalar(
            fun=self.evaluate_objective, bracket=bracket, method="Golden", tol=tolerance
        )

    def _find_gss_bracket(self, delta):
        # FIXME: ugly but it works...
        phi = (1 + math.sqrt(5)) / 2

        self.evaluate_objective(x=0.0)
        self.evaluate_objective(x=delta)

        while self.evaluate_objective.cache.last_result(
            n=1
        ) <= self.evaluate_objective.cache.last_result(n=2):
            _, last1 = self.evaluate_objective.cache.last_args(n=1)
            _, last2 = self.evaluate_objective.cache.last_args(n=2)

            self.evaluate_objective(x=last1["x"] + phi * (last1["x"] - last2["x"]))

        if len(self.evaluate_objective.cache) > 2:
            _, last3 = self.evaluate_objective.cache.last_args(n=3)
            _, last1 = self.evaluate_objective.cache.last_args(n=1)
            return (last3["x"], last1["x"])
        else:
            _, last2 = self.evaluate_objective.cache.last_args(n=2)
            _, last1 = self.evaluate_objective.cache.last_args(n=1)
            return (last2["x"], last1["x"])

        return bracket

    # def plot_results(self):
    #     x, y = zip(*sorted(self.evaluate_objective.cache.items()))
    #     plt.plot(x, y)
    #     plt.show()


T = Union[int, float]


class MaxLIPOTR:
    def __init__(self, objective_function: Callable[T, T]) -> None:
        self.objective_function = objective_function

    @memoize
    def evaluate_objective(self, *args):
        return self.objective_function(*args)

    def optimize(
        self, x_min: T, x_max: T, num_evals: int, epsilon: Optional[float] = 0
    ) -> Tuple[T, Union[int, float]]:

        return dlib.find_min_global(
            self.evaluate_objective,
            x_min if isinstance(x_min, list) else [x_min],
            x_max if isinstance(x_max, list) else [x_max],
            num_evals,
            solver_epsilon=epsilon,
        )

    # def plot_results(self):
    #     x, y = zip(*sorted(self.evaluate_objective.cache.items()))
    #     plt.plot(x, y)
    #     plt.show()


# FIXME: remove this before pushing
# def f(x):
#     return 2*(x-0.74249)**2 + 3

# def g(f):
#     errors = {}
#     eps = float('inf')
#     m = mtr.MaxLIPOTRMinimizer(lambda x: errors[x])
#     while len(errors) < 10:
#         try:
#             m.optimize(0,1,len(errors)+1)
#         except KeyError as e:
#             try_next = float(str(e))
#             errors[try_next] = f(try_next)
#     return errors

# errors = g(f)
# x = np.array(list(errors.keys()))
# y = np.array(list(errors.values()))
# x[np.argmin(y)].round(3)

# class Net(torch.nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.conv1 = torch_geometric.nn.GCNConv(dataset.num_node_features,16)
#         self.conv2 = torch_geometric.nn.GCNConv(16,dataset.num_classes)
#     def forward(self, data):
#         x, edge_index = data.x,data.edge_index
#         x = self.conv1(x,edge_index)
#         x = torch.nn.functional.relu(x)
#         x = torch.nn.functional.dropout(x,training=self.training)
#         x = self.conv2(x,edge_index)
#         return torch.nn.functional.log_softmax(x,dim=1)

# -------------------------------------------------------------- #


class NestedDictionary(collections.abc.MutableMapping):
    def __init__(self, *args, **kwargs) -> None:
        self.d = dict(*args, **kwargs)

    def __getitem__(self, keys) -> NestedDictionary:
        if not isinstance(keys, tuple):
            keys = (keys,)

        branch = self.d
        for k in keys:
            branch = branch[k]

        return NestedDictionary(branch) if isinstance(branch, dict) else branch

    def __setitem__(self, keys, value) -> None:
        if not isinstance(keys, tuple):
            keys = (keys,)

        *most_keys, last_key = keys

        branch = self.d
        for k in most_keys:
            if k not in branch:
                branch[k] = {}
            branch = branch[k]

        branch[last_key] = value

    def __delitem__(self, keys) -> None:
        if not isinstance(keys, tuple):
            keys = (keys,)

        *most_keys, last_key = keys

        branch = self.d
        for k in most_keys:
            # FIXME: does this really need to be here? if we're deleting the item, we shouldn't ever need to make branches on the way to the item...
            if k not in branch:
                branch[k] = {}
            branch = branch[k]

        del branch[last_key]

    def __iter__(self, d=None, prepath=()):
        if d == None:
            d = self.d
        for k, v in d.items():
            if hasattr(v, "items"):
                for keys in self.__iter__(d=v, prepath=prepath + (k,)):
                    yield keys
            else:
                yield prepath + (k,)

    def __len__(self) -> int:
        return sum(1 for _ in self)

    def __str__(self) -> str:
        return str(self.d)

    def __repr__(self) -> str:
        return repr(self.d)


class Settings(NestedDictionary):
    def update(self, settings: Settings) -> None:
        for k, v in settings.items():
            self.__setitem__(keys=k, value=v)


# def plot_lune(self, samples):
#     import matplotlib.pyplot as plt
#     from mpl_toolkits.mplot3d import Axes3D
#     xs,ys,zs = samples
#     fig = plt.figure()
#     ax = Axes3D(fig)
#     phigrid,thetagrid = np.mgrid[0.0:np.pi:100j,0.0:2.0*np.pi:100j]
#     xgrid = np.sin(phigrid)*np.cos(thetagrid)
#     ygrid = np.sin(phigrid)*np.sin(thetagrid)
#     zgrid = np.cos(phigrid)
#     ax.plot_surface(xgrid,ygrid,zgrid,rstride=1,cstride=1,color='c',alpha=0.1,linewidth=0)
#     ax.scatter(xs,ys,zs)
#     ax.quiver([0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[1,0,0,-1,0,0],[0,1,0,0,-1,0],[0,0,1,0,0,-1],arrow_length_ratio=0.1,linewidths=[2,2,2,2,2,2])
#     #ax.set_aspect('equal')
#     ax.xaxis._axinfo['juggled'] = (0,0,0)
#     ax.yaxis._axinfo['juggled'] = (1,1,1)
#     ax.zaxis._axinfo['juggled'] = (2,2,2)
#     plt.show(block=True)
