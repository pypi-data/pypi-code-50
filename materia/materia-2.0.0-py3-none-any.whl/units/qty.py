from __future__ import annotations
import copy
import collections
import numpy as np
from typing import Any, Optional

from .unit import Unit

__all__ = ["Qty"]


class Qty(collections.abc.Sequence):
    def __init__(self, value, unit: Unit) -> None:
        self.value = copy.deepcopy(np.array(value))
        self.unit = copy.deepcopy(unit)

    def is_dimensionless(self) -> bool:
        return self.unit.is_dimensionless()

    def convert(self, new_unit: Unit, in_place: Optional[bool] = True) -> Qty:
        if in_place:
            self.value = (
                self.value * (self.unit / new_unit).prefactor
            )  # FIXME: can't write this as 'self.value *= (self.unit / new_unit).prefactor' without causing numpy unsafe casting error in some cases
            self.unit = copy.deepcopy(new_unit)
            return self
        else:
            return Qty(
                value=self.value * (self.unit / new_unit).prefactor,
                unit=copy.deepcopy(new_unit),
            )

    def __getattr__(self, name: str) -> Any:
        if name.startswith("__") and name.endswith("__"):
            raise AttributeError
        return getattr(self.value, name)

    # ADDITION

    def __add__(self, other) -> Qty:
        # FIXME: type hinting annotation is confusing for this one...
        if not isinstance(other, Qty):
            if self.is_dimensionless():
                return Qty(value=self.value + other, unit=self.unit)
            else:
                raise ValueError(f"Cannot add {type(other)} to Qty.")
        if self.unit != other.unit:
            raise ValueError("Cannot add quantities with different dimensions.")

        return Qty(value=self.value + other.value, unit=self.unit)

    def __radd__(self, other) -> Qty:
        if not isinstance(other, Qty):
            if self.is_dimensionless():
                return Qty(value=other + self.value, unit=self.unit)
            else:
                raise ValueError(f"Cannot add Qty to {type(other)}.")
        if self.unit != other.unit:
            raise ValueError("Cannot add quantities with different dimensions.")

        return Qty(value=other.value + self.value, unit=self.unit)

    def __iadd__(self, other) -> Qty:
        if not isinstance(other, Qty):
            if self.is_dimensionless():
                self.value += other
                return self
            else:
                raise ValueError(f"Cannot add {type(other)} to Qty.")
        if self.unit != other.unit:
            raise ValueError("Cannot add quantities with different dimensions.")

        self.value = self.value + other.value
        return self

    # SUBTRACTION

    def __sub__(self, other):
        if not isinstance(other, Qty):
            if self.is_dimensionless():
                return Qty(value=self.value - other, unit=self.unit)
            else:
                raise ValueError(f"Cannot subtract {type(other)} from Qty.")
        if self.unit != other.unit:
            raise ValueError("Cannot subtract quantities with different dimensions.")

        return Qty(value=self.value - other.value, unit=self.unit)

    def __rsub__(self, other):
        if not isinstance(other, Qty):
            if self.is_dimensionless():
                return Qty(value=other - self.value, unit=self.unit)
            else:
                raise ValueError(f"Cannot subtract Qty from {type(other)}.")
        if self.unit != other.unit:
            raise ValueError("Cannot subtract quantities with different dimensions.")

        return Qty(value=other.value - self.value, unit=self.unit)

    def __isub__(self, other):
        if not isinstance(other, Qty):
            if self.is_dimensionless():
                self.value -= other
                return self
            else:
                raise ValueError(f"Cannot subtract {type(other)} from Qty.")
        if self.unit != other.unit:
            raise ValueError("Cannot subtract quantities with different dimensions.")

        self.value = self.value - other.value
        return self

    # MULTIPLICATION

    def __mul__(self, other):
        if isinstance(other, Qty):
            return Qty(value=self.value * other.value, unit=self.unit * other.unit)
        else:
            return Qty(value=self.value * other, unit=self.unit)

    def __rmul__(self, other):
        if isinstance(other, Qty):
            return Qty(value=self.value * other.value, unit=self.unit * other.unit)
        else:
            return Qty(value=self.value * other, unit=self.unit)

    def __imul__(self, other):
        if isinstance(other, Qty):
            self.value = self.value * other.value
            self.unit = self.unit * other.unit
        else:
            self.value = self.value * other

        return self

    # DIVISION

    def __truediv__(self, other):
        if isinstance(other, Qty):
            return Qty(value=self.value / other.value, unit=self.unit / other.unit)
        else:
            return Qty(value=self.value / other, unit=self.unit)

    def __rtruediv__(self, other):
        if isinstance(other, Qty):
            return Qty(value=other.value / self.value, unit=other.unit / self.unit)
        else:
            return Qty(value=other / self.value, unit=1 / self.unit)

    def __itruediv__(self, other):
        if isinstance(other, Qty):
            self.value = self.value / other.value
            self.unit = self.unit / other.unit
        else:
            self.value /= other

        return self

    # EXPONENTIATION

    def __pow__(self, other):
        return Qty(value=self.value ** other, unit=self.unit ** other)

    def __ipow__(self, other):
        self.value = self.value ** other
        self.unit = self.unit * other

        return self

    # COMPARISON

    def __eq__(self, other):
        if isinstance(other, Qty):
            # np.array_equal works on any array_like and also single values, which should cover all reasonable types for self.value
            return np.array_equal(self.value, other.value) and self.unit == other.unit
        else:
            return self.is_dimensionless() and np.array_equal(self.value, other)

    def __lt__(self, other):
        if isinstance(other, Qty):
            if self.unit != other.unit:
                raise ValueError("Cannot compare quantities with different units.")

            return self.value < other.value
        else:
            return self.is_dimensionless() and self.value < other

    def __le__(self, other):
        if isinstance(other, Qty):
            if self.unit != other.unit:
                raise ValueError("Cannot compare quantities with different units.")

            return self.value <= other.value
        else:
            return self.is_dimensionless() and self.value <= other

    def __gt__(self, other):
        if isinstance(other, Qty):
            if self.unit != other.unit:
                raise ValueError("Cannot compare quantities with different units.")

            return self.value > other.value
        else:
            return self.is_dimensionless() and self.value > other

    def __ge__(self, other):
        if isinstance(other, Qty):
            if self.unit != other.unit:
                raise ValueError("Cannot compare quantities with different units.")

            return self.value >= other.value
        else:
            return self.is_dimensionless() and self.value >= other

    # OTHER

    def __getitem__(self, index):
        return self.value[index]

    def __len__(self):
        return len(self.value)

    def __hash__(self):
        return hash((self.value, self.unit))

    def __str__(self):
        return f"{self.value} ({self.unit})"

    def __repr__(self):
        return f"Qty(value={self.value},unit={repr(self.unit)})"
