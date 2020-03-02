from __future__ import annotations
import inspect
import materia
import re
from typing import Iterable, TypeVar, Union

__all__ = ["MultiwfnOutput"]

T = TypeVar("T")


class MultiwfnOutput:
    def __init__(self, filepath: str) -> None:
        self.filepath = materia.expand(filepath)

    def get(self, *quantity_names: str) -> Union[T, Iterable[T]]:
        method_dict = dict(inspect.getmembers(self, predicate=inspect.isroutine))

        with open(self.filepath, "r") as f:
            lines = "".join(f.readlines())

        quantities = tuple(
            method_dict[name.lower()](lines=lines) for name in quantity_names
        )

        if len(quantities) == 1:
            return quantities[0]
        return quantities

    def volume(self, lines: str) -> materia.Qty:
        # read off the volume in atomic units (i.e. cubic Bohr)
        volume_pattern = re.compile(
            r"\s*Molecular\s*volume\s*:\s*(\d*\.\d*)\s*Bohr\^3,\s*\(\s*\d*\.\d*\s*Angstrom\^3\s*,\s*\d*\.\d*\s*cm\^3\/mol\)\s*"
        )
        # Molecular volume:    0.000 Bohr^3, (    0.000 Angstrom^3,    0.000 cm^3/mol)
        # the last match is the molecular volume (Multiwfn likes to spit out
        # other volumes earlier in the script as well)
        *_, volume_str = volume_pattern.search(lines).groups()

        return materia.Qty(value=float(volume_str), unit=materia.au_volume)
