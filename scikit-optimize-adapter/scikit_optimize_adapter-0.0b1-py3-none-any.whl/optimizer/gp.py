from sklearn.utils import check_random_state
from .base_optimizer import base_computation_graph
from ..utils import normalize_dimensions
from ..utils import cook_estimator
import numpy as np


def gp_computation_graph(estimator=None, cross_validator=None, group_key=None,
                         dimensions=None, base_estimator=None,
                         n_calls=100, n_initial_points=10,
                         initial_point_generator="random", acq_func="gp_hedge", 
                         acq_optimizer="auto", x0=None, y0=None, random_state=None, 
                         verbose=False, callback=None, n_points=25000, 
                         n_restarts_optimizer=5, xi=0.01, kappa=1.96, noise="gaussian", 
                         n_jobs=1, model_queue_size=None):
    
    rng = check_random_state(random_state)
    space = normalize_dimensions(dimensions)
    
    if base_estimator is None:
        base_estimator = cook_estimator(
            "GP", space=space, random_state=rng.randint(0, np.iinfo(np.int32).max),
            noise=noise)
        
    return base_computation_graph(
        estimator, cross_validator, group_key,
        dimensions=space, base_estimator=base_estimator,
        acq_func=acq_func,
        xi=xi, kappa=kappa, acq_optimizer=acq_optimizer, n_calls=n_calls,
        n_points=n_points, 
        n_initial_points=n_initial_points,
        initial_point_generator=initial_point_generator,
        n_restarts_optimizer=n_restarts_optimizer,
        x0=x0, y0=y0, random_state=rng, verbose=verbose,
        callback=callback, n_jobs=n_jobs, model_queue_size=model_queue_size)
    
    