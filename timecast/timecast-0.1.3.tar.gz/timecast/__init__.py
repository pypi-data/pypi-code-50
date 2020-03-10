import jax.random

from timecast.learners import blackbox
from timecast.learners import boost
from timecast.utils.random import set_key

# Initialize global random key by seeding the jax random number generator
GLOBAL_RANDOM_KEY = jax.random.PRNGKey(0)
set_key()

__all__ = ["blackbox", "boost"]
