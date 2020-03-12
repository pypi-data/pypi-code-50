"""Python template."""
from gym.envs.registration import register  # type: ignore

register(
    id="SimpleCliffworld-v0",
    entry_point="gym_simple_cliffworld.envs:SimpleCliffworldEnv",
)
