from __future__ import annotations
import materia
import subprocess
from typing import Iterable, Optional

__all__ = ["OpenbabelEngine"]


class OpenbabelEngine:
    def __init__(self, executable: Optional[str] = "obabel") -> None:

        self.executable = executable

    def execute(
        self,
        input_filepath: str,
        log_filepath: str,
        arguments: Optional[Iterable[str]] = None,
    ) -> str:
        with open(materia.expand(log_filepath), "w") as log:
            subprocess.call(
                [self.executable, materia.expand(input_filepath)] + arguments,
                stdout=log,
                stderr=subprocess.STDOUT,
            )

        with open(materia.expand(log_filepath), "r") as log:
            return "".join(log.readlines())
