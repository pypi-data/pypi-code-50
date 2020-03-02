from __future__ import annotations
import materia
import subprocess
from typing import Iterable, Optional, Tuple, Union

__all__ = ["FragItEngine"]


class FragItEngine:
    def __init__(self, executable: Optional[str] = "fragit") -> None:

        self.executable = executable

    def execute(
        self, structure_filepath: str, log_filepath: str, work_dir: Optional[str] = "."
    ) -> Tuple[str, Iterable[materia.Structure]]:
        with open(materia.expand(log_filepath), "w") as log:
            subprocess.call(
                [self.executable, structure_filepath],
                stdout=log,
                stderr=subprocess.STDOUT,
                cwd=work_dir,
            )

        with open(materia.expand(log_filepath), "r") as f:
            output = "".join(f.readlines())

        return output
