import dask
from skopt.optimizer import Optimizer
import time


def stateful_object_mutator(obj, method_str, **kwargs):
    getattr(obj, method_str)(**kwargs)
    return obj

def base_computation_graph(estimator, cross_validator, group_key=None,
                           dimensions=None, base_estimator=None,
                           n_calls=100, n_initial_points=10, 
                           initial_point_generator="random",
                           acq_func="EI", acq_optimizer="lbfgs",
                           x0=None, y0=None, random_state=None, verbose=False,
                           callback=None, n_points=10000, n_restarts_optimizer=5,
                           xi=0.01, kappa=1.96, n_jobs=1, model_queue_size=None):
    
    acq_optimizer_kwargs = {
        "n_points": n_points, "n_restarts_optimizer": n_restarts_optimizer,
        "n_jobs": n_jobs}
    acq_func_kwargs = {"xi": xi, "kappa": kappa}
    
    optimizer = Optimizer(dimensions, base_estimator,
                          n_initial_points=n_initial_points,
                          #initial_point_generator=initial_point_generator,
                          #n_jobs=n_jobs,
                          acq_func=acq_func, acq_optimizer=acq_optimizer,
                          random_state=random_state,
                          model_queue_size=model_queue_size,
                          acq_optimizer_kwargs=acq_optimizer_kwargs,
                          acq_func_kwargs=acq_func_kwargs)
    
    K = cross_validator.K

    for n in range(n_calls):
        
        next_x = dask.delayed(optimizer.ask)()
        
        evaluation_results = []
        
        for k in range(K):
            
            evaluation_result = dask.delayed(cross_validator.evaluate_fold)(estimator, 
                                                                             k, next_x, 
                                                                             group_key)
            evaluation_results.append(evaluation_result)
            
        avg_evaluation_result = dask.delayed(lambda *args: sum(args)/k)(*evaluation_results)
        optimizer = dask.delayed(stateful_object_mutator)(optimizer, "tell", x=next_x, 
                                                          y=avg_evaluation_result)
        
    return optimizer

