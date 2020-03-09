"""
Implements pseudorandomness in our program
"""
from random import randint

import jax.random

import strange

# NOTE: We use numpy because the jax RNG is deterministic


def set_key(key=None):
    """
    Description: Fix global random key to ensure reproducibility of results.

    Args:
        key (int): key that determines reproducible output
    """
    if key is None:
        key = randint(1, 9223372036854775807 + 1)
    assert type(key) == int
    strange.GLOBAL_RANDOM_KEY = jax.random.PRNGKey(key)


def generate_key():
    """
    Description: Generate random key.

    Returns:
        Random random key
    """
    key, subkey = jax.random.split(strange.GLOBAL_RANDOM_KEY)
    strange.GLOBAL_RANDOM_KEY = key
    return subkey


def get_global_key():
    """
    Description: Get current global random key.

    Returns:
        Current global random key
    """

    return strange.GLOBAL_RANDOM_KEY
