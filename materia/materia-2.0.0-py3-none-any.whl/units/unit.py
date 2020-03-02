from __future__ import annotations
from .dimension import Dimension
from typing import Optional, Union

__all__ = ["Unit"]


class Unit:
    def __init__(
        self,
        length: Optional[int] = 0,
        mass: Optional[int] = 0,
        time: Optional[int] = 0,
        electric_current: Optional[int] = 0,
        absolute_temperature: Optional[int] = 0,
        number: Optional[int] = 0,
        luminous_intensity: Optional[int] = 0,
        prefactor: Optional[float] = 1.0,
    ) -> None:
        self.dimension = Dimension(
            length=length,
            mass=mass,
            time=time,
            electric_current=electric_current,
            absolute_temperature=absolute_temperature,
            number=number,
            luminous_intensity=luminous_intensity,
        )

        self.prefactor = prefactor

    def is_dimensionless(self) -> bool:
        return all(v == 0 for v in self.dimension.dimension_dict.values())

    # MULTIPLICATION

    def __mul__(self, other: Union[Unit, float]) -> Unit:
        if hasattr(other, "dimension") and hasattr(other, "prefactor"):
            return Unit(
                **(self.dimension * other.dimension).dimension_dict,
                prefactor=self.prefactor * other.prefactor,
            )
        else:
            return Unit(
                **self.dimension.dimension_dict, prefactor=self.prefactor * other
            )

    def __rmul__(self, other: Union[Unit, float]) -> Unit:
        if hasattr(other, "dimension") and hasattr(other, "prefactor"):
            return Unit(
                **(self.dimension * other.dimension).dimension_dict,
                prefactor=self.prefactor * other.prefactor,
            )
        else:
            return Unit(
                **self.dimension.dimension_dict, prefactor=self.prefactor * other
            )

    def __imul__(self, other: Union[Unit, float]) -> Unit:
        if hasattr(other, "dimension") and hasattr(other, "prefactor"):
            self.dimension *= other.dimension
            self.prefactor *= other.prefactor
        else:
            self.prefactor *= other

        return self

    # DIVISION

    def __truediv__(self, other: Union[Unit, float]) -> Unit:
        if hasattr(other, "dimension") and hasattr(other, "prefactor"):
            return Unit(
                **(self.dimension / other.dimension).dimension_dict,
                prefactor=self.prefactor / other.prefactor,
            )
        else:
            return Unit(
                **self.dimension.dimension_dict, prefactor=self.prefactor / other
            )

    def __rtruediv__(self, other: Union[Unit, float]) -> Unit:
        if hasattr(other, "dimension") and hasattr(other, "prefactor"):
            return Unit(
                **(other.dimension / self.dimension).dimension_dict,
                prefactor=other.prefactor / self.prefactor,
            )
        else:
            return Unit(
                **{k: -v for k, v in self.dimension.dimension_dict.items()},
                prefactor=other / self.prefactor,
            )

    def __itruediv__(self, other: Union[Unit, float]) -> Unit:
        if hasattr(other, "dimension") and hasattr(other, "prefactor"):
            self.dimension /= other.dimension
            self.prefactor /= other.prefactor
        else:
            self.prefactor /= other

        return self

    # EXPONENTIATION

    def __pow__(self, other: float) -> Unit:
        return Unit(
            **(self.dimension ** other).dimension_dict,
            prefactor=self.prefactor ** other,
        )

    def __ipow__(self, other: float) -> Unit:
        self.dimension **= other
        self.prefactor **= other

    # COMPARISON

    def __eq__(self, other: Unit) -> bool:
        return self.prefactor == other.prefactor and self.dimension == other.dimension

    def __lt__(self, other: Unit) -> bool:
        if self.dimension != other.dimension:
            raise ValueError("Cannot compare units with different dimensions.")

        return self.prefactor < other.prefactor

    def __le__(self, other: Unit) -> bool:
        if self.dimension != other.dimension:
            raise ValueError("Cannot compare units with different dimensions.")

        return self.prefactor <= other.prefactor

    def __gt__(self, other: Unit) -> bool:
        if self.dimension != other.dimension:
            raise ValueError("Cannot compare units with different dimensions.")

        return self.dimension > other.dimension

    def __ge__(self, other: Unit) -> bool:
        if self.dimension != other.dimension:
            raise ValueError("Cannot compare units with different dimensions.")

        return self.dimension >= other.dimension

    def __hash__(self) -> int:
        return hash((self.prefactor, self.dimension))

    def __str__(self) -> str:
        # FIXME: make this pretty by printing the unit name, not its composition (which should go in __repr__)
        dimension_string = (
            str(self.dimension)
            .replace("L", "m")
            .replace("M", "kg")
            .replace("T", "s")
            .replace("I", "A")
            .replace("\u03B8", "K")
            .replace("N", "mol")
            .replace("J", "cd")
        )

        return (
            f"{self.prefactor} {dimension_string}"
            if self.prefactor != 1
            else dimension_string
        )

    def __repr__(self) -> str:
        kwargs_str = (
            ",".join(f"{k}={v}" for k, v in self.dimension.dimension_dict.items())
            + f",prefactor={self.prefactor}"
        )
        return f"Unit({kwargs_str})"
