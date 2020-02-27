"""Compute mean and variance."""
import math


class RunningStats:
    """Compute mean and variance.
    """
    def __init__(self):
        self.n = 0
        self.M1 = 0.0
        self.M2 = 0.0

    def push(self, value):
        """Add a value."""
        self.n += 1
        delta = value - self.M1
        self.M1 += delta/self.n
        # print(f"{delta=}, value-M1={value-self.M1}")
        self.M2 += delta * (value - self.M1)

    def push_iter(self, values):
        """Add values from an Iterable."""
        for value in values:
            self.push(value)
            # print(self)

    def mean(self):
        """Compute mean."""
        return self.M1

    def variance(self):
        """Compute the sample variance."""
        return self.M2/(self.n - 1) if self.n > 1 else 0.0

    def standard_deviation(self):
        """Compute the sample standard deviation."""
        return math.sqrt(self.variance())

    def __add__(self, other):
        combined = RunningStats()
        combined.n = self.n + other.n

        delta = other.M1 - self.M1
        delta2 = delta * delta

        combined.M1 = (self.M1 * self.n + other.M1 * other.n)/combined.n
        combined.M2 = self.M2 + other.M2 + delta2 * self.n * other.n / combined.n

        return combined

    def __str__(self):
        return f"RunningStats(n={self.n}, M1={self.M1}, M2={self.M2})"
