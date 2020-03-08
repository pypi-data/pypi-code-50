import jax.random

from proust.learners import blackbox, boost
from proust.utils.random import set_key

# Initialize global random key by seeding the jax random number generator
GLOBAL_RANDOM_KEY = jax.random.PRNGKey(0)
set_key()

__all__ = ["blackbox", "boost"]
