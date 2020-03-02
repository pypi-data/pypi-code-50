from __future__ import annotations
import contextlib
import numpy as np
import os
import materia
import subprocess
from typing import Iterable, Optional, Tuple, Union
from ...workflow.tasks.task import Task

__all__ = ["PackmolSolvate"]


class PackmolSolvate(Task):
    def __init__(
        self,
        shells: int,
        tolerance: float,
        engine: materia.PackmolEngine,
        number_density: Optional[materia.Qty] = None,
        mass_density: Optional[materia.Qty] = None,
        input_name: str = "packmol.inp",
        log_name: str = "packmol.log",
        work_dir: str = ".",
        keep_logs: bool = True,
        handlers: Optional[Iterable[materia.Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__(handlers=handlers, name=name)

        self.shells = shells
        self.number_density = number_density
        self.mass_density = mass_density

        self.tolerance = tolerance

        self.input_name = input_name
        self.log_name = log_name
        self.work_dir = work_dir
        self.keep_logs = keep_logs

        self.engine = engine

    def _packing_params(self, solvent: materia.Structure) -> Tuple[int, materia.Qty]:
        if self.number_density is None:
            if self.mass_density is None:
                raise ValueError(
                    "Either mass density or number density required to pack shells."
                )
            if isinstance(solvent, str):
                solvent = materia.Structure.read(solvent)
            number_density = self.mass_density / solvent.mass
        else:
            number_density = self.number_density

        # these are the ideal gas packing values:
        n = int((2 / 3) * self.shells ** 3)
        sphere_radius = self.shells * (2 * np.pi * number_density) ** (-1 / 3)

        return n, sphere_radius

    def run(
        self,
        solute: Union[materia.Structure, str],
        solvent: Union[materia.Structure, str],
    ) -> materia.Structure:
        n, sphere_radius = self._packing_params(solvent=solvent)

        with materia.work_dir(self.work_dir) as wd:
            inp = materia.PackmolInput(
                tolerance=self.tolerance,
                filetype="xyz",
                output_name=materia.expand(path="packed", dir=wd),
            )

            if isinstance(solute, str):
                solute_cm = contextlib.nullcontext(solute)
            else:
                solute_cm = solute.tempfile(suffix=".xyz", dir=wd)

            if isinstance(solvent, str):
                solvent_cm = contextlib.nullcontext(solvent)
            else:
                solvent_cm = solvent.tempfile(suffix=".xyz", dir=wd)

            with solute_cm as f, solvent_cm as g:
                inp.add_structure(
                    structure_filepath=materia.expand(
                        path=f.name if hasattr(f, "name") else f, dir=wd
                    ),
                    number=1,
                    instructions=["fixed 0. 0. 0. 0. 0. 0."],
                )

                inp.add_structure(
                    structure_filepath=materia.expand(
                        path=g.name if hasattr(g, "name") else g, dir=wd
                    ),
                    number=n - 1,
                    instructions=[
                        f"inside sphere 0. 0. 0. {sphere_radius.convert(materia.angstrom).value}"
                    ],
                )

                input_filepath = materia.expand(path=self.input_name, dir=wd)

                inp.write(input_filepath)

                self.engine.execute(
                    input_filepath=input_filepath,
                    log_filepath=materia.expand(path=self.log_name, dir=wd),
                )

                return materia.Structure.read(materia.expand(path="packed.xyz", dir=wd))
