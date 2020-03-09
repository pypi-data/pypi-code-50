import jax.random

from strange.learners import blackbox
from strange.learners import boost
from strange.utils.random import set_key

# Initialize global random key by seeding the jax random number generator
GLOBAL_RANDOM_KEY = jax.random.PRNGKey(0)
set_key()

__all__ = ["blackbox", "boost"]
