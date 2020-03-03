"""

@author: maffettone
"""
import warnings
import numpy as np
from .constraints import Constraint
from .utils import ensure_rng

EPS = 1e-4


def _hashable(x):
    """ ensure that an point is hashable by a python dict """
    return tuple(map(float, x))


class SampledSpace:
    """
    Configures a space to track a MCMC sampling.
    Allows for constant-time appends, while assuring no duplicates are added
    """

    def __init__(self, path, random_state=None):
        self.constraint = Constraint(path)
        self.current = self.constraint.get_example()
        self.dim = self.constraint.get_ndim()
        self.step_size = np.array([1e-2/self.dim for _ in range(self.dim)])

        self.random_state = ensure_rng(random_state)

        # keep track of unique points we have seen so far
        self._cache = set()
        self.register(self.current)

        # track acceptance rate for analytics and scheduling
        self.n_proposed = np.zeros(self.dim)
        self.n_accepted = np.zeros(self.dim)

    def __contains__(self, x):
        return _hashable(x) in self._cache

    def __len__(self):
        return len(self._cache)

    @property
    def empty(self):
        return len(self) == 0

    def _as_array(self, x):
        x = np.asarray(x, dtype=float)
        x = x.ravel()
        try:
            assert x.size == self.dim
        except AssertionError:
            raise ValueError(
                "Size of array ({}) is different than the ".format(len(x)) +
                "expected number of parameters ({}).".format(self.dim)
            )
        return x

    def valid(self, point):
        """
        Tests all constraints and bounds of the unit hypercube
        Parameters
        ----------
        point: ndarray
            Point to test

        Returns
        -------
        Boolean, validity of point given constraints
        """
        if not self.constraint.apply(point):
            return False
        elif any([p > 1 for p in point]) or any([p < 0 for p in point]):
            return False
        else:
            return True

    def register(self, point):
        """
        Add a point to the running cache
        Parameters
        ----------
        point: ndarray
            a single point, with len(x) == self.dim

        """
        x = self._as_array(point)
        self._cache.add(_hashable(x))

    def reset_counts(self):
        self.n_proposed = np.zeros(self.dim)
        self.n_accepted = np.zeros(self.dim)

    def update_step_size(self, target_rate):
        """
        Updates step size of each dimension based on the ratio between the acceptance rate and target rate.
        Parameters
        ----------
        target_rate: float
            Desired acceptance rate.
            If the measure acceptance rate is below the desired, the stepsize is decreased.
            If the measure acceptance rate is above the desired, the stepsize is increased.

        """
        acceptance_rate = self.n_accepted / (self.n_proposed + EPS)
        for i in range(self.dim):
            if acceptance_rate[i] < target_rate:
                self.step_size[i] *= 0.1
            else:
                self.step_size[i] *= 1.1

    def propose_step(self):
        """
        Metropolis-Hastings proposal and acceptance criteria
        """
        idx = self.random_state.randint(0, self.dim)
        self.n_proposed[idx] += 1
        step = (self.random_state.rand() - 0.5) * self.step_size[idx]

        self.current[idx] += step
        # Acceptance criterion
        if self.valid(self.current):
            self.register(self.current)
            self.n_accepted[idx] += 1
        else:
            self.current[idx] -= step

    def random_walk(self, n_steps=1000):
        """
        Conduct a Markov Chain random walk for n_steps
        Parameters
        ----------
        n_steps : int
            Number of steps to continue the random walk

        """
        for i in range(n_steps):
            self.propose_step()

    def adaptive_displacement(self, target_rate=0.01, total_steps=100000, feedback_rate=1000, timeout=None):
        """
        Conducts a adaptive_displacement run, that schedules the step-size based on a desired acceptance rate

        Parameters
        ----------
        target_rate: float
            Desired acceptance rate.
            If the measure acceptance rate is below the desired, the stepsize is decreased.
            If the measure acceptance rate is above the desired, the stepsize is increased.
            This way, a MC explores as much as it can.
        total_steps: int
            Total number of steps in the Markov Chain
        feedback_rate:
            Number of steps for each iteration of the step scheduler.
        timeout: float
            Time in minutes to exit random walk
        """
        if timeout:
            import time
            max_s = timeout * 60
            start = time.time()

        for _ in range(total_steps // feedback_rate):
            self.reset_counts()
            self.random_walk(feedback_rate)
            self.update_step_size(target_rate)
            if timeout and time.time() - start > max_s:
                return
        self.reset_counts()
        self.random_walk(total_steps % feedback_rate)

    def sample_space(self, sample_size):
        """
        Takes a sub-sample of the space in the cache
        Should the cache not be large enough, a random walk will be initiated until it reaches a sufficient size.
        This is sub-optimal behavior, and the cache should always be much larger than the sample size.
        Parameters
        ----------
        sample_size: int
            Size of sub-sample of space

        """
        if sample_size > len(self._cache):
            warnings.warn("Desired sample size {} is larger than current cache size {}. Running simulated annealing "
                          "until sufficiently large.".format(sample_size, len(self._cache)), UserWarning)
        while sample_size > len(self._cache):
            # self.random_walk(sample_size - len(self._cache))
            self.adaptive_displacement(total_steps=sample_size, feedback_rate=self.dim * 10)

        arr = np.array(tuple(self._cache))
        idx = self.random_state.choice(len(arr), sample_size)
        return arr[idx]
