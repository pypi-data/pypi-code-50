"""simple_cliffworld_v0."""
from __future__ import annotations

from typing import Dict, List

from gym.envs.toy_text import discrete  # type: ignore
import numpy as np  # type: ignore

LEFT = 0
RIGHT = 1


class SimpleCliffworldEnv(discrete.DiscreteEnv):
    """A simplified version of Cliffworld in an OpenAI Gym Environment.

    This environment is intended for testing. It is so simple you can
    reason about the expected values, which helps you debug your new
    algorithm implementation.

    State:
        Imagine six boxes side by side. Box 0 and 5 are terminal states.
        You start in box 1. The goal is to reach the right hand side.

    Actions:
        0 = Left, 1 = Right.

    Reward:
        +5 for box 5. 0 otherwise.
    """

    metadata = {"render.modes": ["human"]}

    def __init__(self: SimpleCliffworldEnv) -> None:
        """Init function."""
        num_states = 6
        num_actions = 2
        P: Dict[int, Dict[int, List]] = {}
        for s in range(num_states):
            P[s] = {a: [] for a in range(num_actions)}
            if s == 1:
                P[s][LEFT] = [(1.0, s - 1, 0, True)]
            else:
                P[s][LEFT] = [(1.0, s - 1, 0, False)]
            if s >= 4:
                P[s][RIGHT] = [(1.0, s + 1, 5, True)]
            else:
                P[s][RIGHT] = [(1.0, s + 1, 0, False)]

        isd = np.zeros(num_states)
        isd[1] = 1.0
        super(SimpleCliffworldEnv, self).__init__(num_states, num_actions, P, isd)
