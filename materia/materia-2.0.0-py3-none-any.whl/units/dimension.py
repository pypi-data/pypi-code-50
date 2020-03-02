from __future__ import annotations
from typing import Optional

__all__ = ["Dimension"]


class Dimension:
    def __init__(
        self,
        length: Optional[int] = 0,
        time: Optional[int] = 0,
        mass: Optional[int] = 0,
        electric_current: Optional[int] = 0,
        absolute_temperature: Optional[int] = 0,
        number: Optional[int] = 0,
        luminous_intensity: Optional[int] = 0,
    ) -> None:

        self.dimension_dict = {
            "length": length,
            "time": time,
            "mass": mass,
            "electric_current": electric_current,
            "absolute_temperature": absolute_temperature,
            "number": number,
            "luminous_intensity": luminous_intensity,
        }

    # MULTIPLICATION

    def __mul__(self, other: Dimension) -> Dimension:
        return Dimension(
            **{
                k: self.dimension_dict[k] + other.dimension_dict[k]
                for k in self.dimension_dict
            }
        )

    def __rmul__(self, other: Dimension) -> Dimension:
        return Dimension(
            **{
                k: self.dimension_dict[k] + other.dimension_dict[k]
                for k in self.dimension_dict
            }
        )

    def __imul__(self, other: Dimension) -> Dimension:
        for k, v in other.dimension_dict.items():
            self.dimension_dict[k] += v

        return self

    # DIVISION

    def __truediv__(self, other: Dimension) -> Dimension:
        return Dimension(
            **{
                k: self.dimension_dict[k] - other.dimension_dict[k]
                for k in self.dimension_dict
            }
        )

    def __rtruediv__(self, other: Dimension) -> Dimension:
        return Dimension(
            **{
                k: other.dimension_dict[k] - self.dimension_dict[k]
                for k in self.dimension_dict
            }
        )

    def __itruediv__(self, other: Dimension) -> Dimension:
        for k, v in other.dimension_dict.items():
            self.dimension_dict[k] -= v

        return self

    # EXPONENTIATION

    def __pow__(self, other: Dimension) -> Dimension:
        return Dimension(**{k: v * other for k, v in self.dimension_dict.items()})

    def __ipow__(self, other: Dimension) -> Dimension:
        for k in self.dimension_dict:
            self.dimension_dict[k] *= other

        return self

    # COMPARISON

    def __eq__(self, other: Dimension) -> bool:
        return self.dimension_dict == other.dimension_dict

    def __hash__(self) -> int:
        return hash(tuple(sorted(self.dimension_dict.items())))

    def __str__(self) -> str:
        lookup_dict = {
            "length": "L",
            "mass": "M",
            "time": "T",
            "electric_current": "I",
            "absolute_temperature": "\u03B8",
            "number": "N",
            "luminous_intensity": "J",
        }
        positive_power_strings = (
            f"{lookup_dict[dim]}^{pow}"
            for dim, pow in self.dimension_dict.items()
            if pow > 0
        )
        negative_power_strings = (
            f"{lookup_dict[dim]}^{-pow}"
            for dim, pow in self.dimension_dict.items()
            if pow < 0
        )

        numerator_string = "*".join(sorted(positive_power_strings))
        denominator_string = "*".join(sorted(negative_power_strings))

        if numerator_string == "" and denominator_string == "":
            return ""
        elif numerator_string != "" and denominator_string == "":
            return numerator_string.replace("^1", "")
        elif numerator_string == "" and denominator_string == "":
            return f"1/({denominator_string})".replace("^1", "")
        else:
            return f"({numerator_string})/({denominator_string})".replace("^1", "")

    def __repr__(self) -> str:
        kwargs_str = ",".join(f"{k}={v}" for k, v in self.dimension_dict.items())
        return f"Dimension({kwargs_str})"
