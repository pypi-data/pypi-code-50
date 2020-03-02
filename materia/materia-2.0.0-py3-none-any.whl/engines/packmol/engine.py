from __future__ import annotations
import os
import materia
import subprocess
from typing import Optional

__all__ = ["PackmolEngine"]


class PackmolEngine:
    def __init__(self, executable: Optional[str] = "packmol") -> None:

        self.executable = executable

    def execute(self, input_filepath: str, log_filepath: str) -> str:
        with open(input_filepath, "r") as f_in:
            with open(log_filepath, "w") as f_out:
                subprocess.call([self.executable], stdin=f_in, stdout=f_out)

        with open(log_filepath, "r") as f:
            output = "".join(f.readlines())

        return output
