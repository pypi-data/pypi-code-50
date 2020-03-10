import numpy as np
from sklearn.utils import check_random_state
import socket
import os
from scipy.optimize import OptimizeResult
# from sklearn.gaussian_process.kernels import ConstantKernel
# from sklearn.gaussian_process.kernels import Matern
# the sklearn kernels do not implement gradients!
from skopt.learning.gaussian_process.kernels import ConstantKernel
from skopt.learning.gaussian_process.kernels import HammingKernel
from skopt.learning.gaussian_process.kernels import Matern
from skopt.learning import GaussianProcessRegressor
from skopt.space import Space, Categorical, Integer, Real, Dimension
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm
plt.style.use('seaborn')


def normalize_dimensions(dimensions):
    """Create a ``Space`` where all dimensions are normalized to unit range.
    This is particularly useful for Gaussian process based regressors and is
    used internally by ``gp_minimize``.
    Parameters
    ----------
    dimensions : list, shape (n_dims,)
        List of search space dimensions.
        Each search dimension can be defined either as
        - a `(lower_bound, upper_bound)` tuple (for `Real` or `Integer`
          dimensions),
        - a `(lower_bound, upper_bound, "prior")` tuple (for `Real`
          dimensions),
        - as a list of categories (for `Categorical` dimensions), or
        - an instance of a `Dimension` object (`Real`, `Integer` or
          `Categorical`).
         NOTE: The upper and lower bounds are inclusive for `Integer`
         dimensions.
    """
    space = Space(dimensions)
    transformed_dimensions = []
    for dimension in space.dimensions:
        if isinstance(dimension, Categorical):
            transformed_dimensions.append(Categorical(dimension.categories,
                                                      dimension.prior,
                                                      name=dimension.name,
                                                      transform="normalize"))
        # To make sure that GP operates in the [0, 1] space
        elif isinstance(dimension, Real):
            transformed_dimensions.append(
                Real(dimension.low, dimension.high, dimension.prior,
                     name=dimension.name,
                     transform="normalize",
                     dtype=dimension.dtype)
                )
        elif isinstance(dimension, Integer):
            transformed_dimensions.append(
                Integer(dimension.low, dimension.high,
                        name=dimension.name,
                        transform="normalize",
                        dtype=dimension.dtype)
                )
        else:
            raise RuntimeError("Unknown dimension type "
                               "(%s)" % type(dimension))

    return Space(transformed_dimensions)

def cook_estimator(base_estimator, space=None, **kwargs):
    """Cook a default estimator.
    For the special base_estimator called "DUMMY" the return value is None.
    This corresponds to sampling points at random, hence there is no need
    for an estimator.
    Parameters
    ----------
    base_estimator : "GP", "RF", "ET", "GBRT", "DUMMY" or sklearn regressor
        Should inherit from `sklearn.base.RegressorMixin`.
        In addition the `predict` method should have an optional `return_std`
        argument, which returns `std(Y | x)`` along with `E[Y | x]`.
        If base_estimator is one of ["GP", "RF", "ET", "GBRT", "DUMMY"], a
        surrogate model corresponding to the relevant `X_minimize` function
        is created.
    space : Space instance
        Has to be provided if the base_estimator is a gaussian process.
        Ignored otherwise.
    kwargs : dict
        Extra parameters provided to the base_estimator at init time.
    """
    if isinstance(base_estimator, str):
        base_estimator = base_estimator.upper()
        if base_estimator not in ["GP", "ET", "RF", "GBRT", "DUMMY"]:
            raise ValueError("Valid strings for the base_estimator parameter "
                             " are: 'RF', 'ET', 'GP', 'GBRT' or 'DUMMY' not "
                             "%s." % base_estimator)
    elif not is_regressor(base_estimator):
        raise ValueError("base_estimator has to be a regressor.")

    if base_estimator == "GP":
        if space is not None:
            space = Space(space)
            space = Space(normalize_dimensions(space.dimensions))
            n_dims = space.transformed_n_dims
            is_cat = space.is_categorical

        else:
            raise ValueError("Expected a Space instance, not None.")

        cov_amplitude = ConstantKernel(1.0, (0.01, 1000.0))
        # only special if *all* dimensions are categorical
        if is_cat:
            other_kernel = HammingKernel(length_scale=np.ones(n_dims))
        else:
            other_kernel = Matern(
                length_scale=np.ones(n_dims),
                length_scale_bounds=[(0.01, 100)] * n_dims, nu=2.5)

        base_estimator = GaussianProcessRegressor(
            kernel=cov_amplitude * other_kernel,
            normalize_y=True, noise="gaussian",
            n_restarts_optimizer=2)
    
    if ('n_jobs' in kwargs.keys()) and not hasattr(base_estimator, 'n_jobs'):
        del kwargs['n_jobs']

    base_estimator.set_params(**kwargs)
    return base_estimator

def get_host_ip_address():
    """Get the host ip address of the machine where the executor is running. 

    Returns
    -------
    host_ip : String
    """
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name) 
        return host_ip
    except:
        try:
            host_ip = socket.gethostbyname('localhost') 
            return host_ip
        except:
            host_ip = 'ip_address_NA'
            return host_ip
        
def is_port_available(port):
    """Checks if the given port argument is available.
    
    Returns
    -------
    result : boolean
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        localhost_ip = socket.gethostbyname("localhost") 
        sock.bind((localhost_ip, port))
        result = True
    except:
        result = False
    sock.close()
    return result

def get_available_port(default_port=8787):
    """Returns an available port starting with the argument, 
    incrementing it by 1 in case it is unavailable.
    
    Returns
    -------
    default_port : int
    """
    while not is_port_available(default_port):
        
        default_port += 1
        
    return default_port

def create_result(Xi, yi, space=None, rng=None, specs=None, models=None):
    """
    Initialize an `OptimizeResult` object.
    Parameters
    ----------
    Xi : list of lists, shape (n_iters, n_features)
        Location of the minimum at every iteration.
    yi : array-like, shape (n_iters,)
        Minimum value obtained at every iteration.
    space : Space instance, optional
        Search space.
    rng : RandomState instance, optional
        State of the random state.
    specs : dict, optional
        Call specifications.
    models : list, optional
        List of fit surrogate models.
    Returns
    -------
    res : `OptimizeResult`, scipy object
        OptimizeResult instance with the required information.
    """
    res = OptimizeResult()
    yi = np.asarray(yi)
    if np.ndim(yi) == 2:
        res.log_time = np.ravel(yi[:, 1])
        yi = np.ravel(yi[:, 0])
    best = np.argmin(yi)
    res.x = Xi[best]
    res.fun = yi[best]
    res.func_vals = yi
    res.x_iters = Xi
    res.models = models
    res.space = space
    res.random_state = rng
    res.specs = specs
    return res

def plot_convergence(*args, **kwargs):
    """Plot one or several convergence traces.
    Parameters
    ----------
    args[i] :  `OptimizeResult`, list of `OptimizeResult`, or tuple
        The result(s) for which to plot the convergence trace.
        - if `OptimizeResult`, then draw the corresponding single trace;
        - if list of `OptimizeResult`, then draw the corresponding convergence
          traces in transparency, along with the average convergence trace;
        - if tuple, then `args[i][0]` should be a string label and `args[i][1]`
          an `OptimizeResult` or a list of `OptimizeResult`.
    ax : `Axes`, optional
        The matplotlib axes on which to draw the plot, or `None` to create
        a new one.
    true_minimum : float, optional
        The true minimum value of the function, if known.
    yscale : None or string, optional
        The scale for the y-axis.
    Returns
    -------
    ax : `Axes`
        The matplotlib axes.
    """
    # <3 legacy python
    ax = kwargs.get("ax", None)
    true_minimum = kwargs.get("true_minimum", None)
    yscale = kwargs.get("yscale", None)

    if ax is None:
        ax = plt.gca()

    ax.set_title("Convergence plot")
    ax.set_xlabel("Number of calls $n$")
    ax.set_ylabel(r"$\min f(x)$ after $n$ calls")
    ax.grid()

    if yscale is not None:
        ax.set_yscale(yscale)

    colors = cm.viridis(np.linspace(0.25, 1.0, len(args)))

    for results, color in zip(args, colors):
        if isinstance(results, tuple):
            name, results = results
        else:
            name = None

        if isinstance(results, OptimizeResult):
            n_calls = len(results.x_iters)
            mins = [np.min(results.func_vals[:i])
                    for i in range(1, n_calls + 1)]
            ax.plot(range(1, n_calls + 1), mins, c=color,
                    marker=".", markersize=12, lw=2, label=name)

        elif isinstance(results, list):
            n_calls = len(results[0].x_iters)
            iterations = range(1, n_calls + 1)
            mins = [[np.min(r.func_vals[:i]) for i in iterations]
                    for r in results]

            for m in mins:
                ax.plot(iterations, m, c=color, alpha=0.2)

            ax.plot(iterations, np.mean(mins, axis=0), c=color,
                    marker=".", markersize=12, lw=2, label=name)

    if true_minimum:
        ax.axhline(true_minimum, linestyle="--",
                   color="r", lw=1,
                   label="True minimum")

    if true_minimum or name:
        ax.legend(loc="best")

    ax.grid()
    return ax
