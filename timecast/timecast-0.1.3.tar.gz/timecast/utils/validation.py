from typing import Callable

from jax import grad
from jax import jit


# TODO: Imperfect test. Need to be able to call grad_func on some default values
# (e.g., lambda x: onp.random.rand(x) won't error here, but should)
def differentiable(func: Callable, *args, **kwargs) -> bool:
    if not callable(func):
        return False

    try:
        grad_func = grad(func)
        result = grad_func(*args)
        jit(grad_func)
        result
    except Exception as e:
        print(e)
        # TODO: What is actual jax exception?
        return False

    return True
