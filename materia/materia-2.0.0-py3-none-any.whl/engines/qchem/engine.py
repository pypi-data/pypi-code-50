from __future__ import annotations
from typing import Iterable, Optional

import ast
import os
import materia
import re
import shlex
import subprocess

__all__ = ["QChemEngine"]


class QChemEngine:
    def __init__(
        self,
        scratch_dir: Optional[str] = None,
        qcenv: Optional[str] = None,
        num_processors: Optional[int] = None,
        num_threads: Optional[int] = None,
        executable: Optional[str] = "qchem",
        arguments: Optional[Iterable[str]] = None,
    ) -> None:
        self.scratch_dir = (
            materia.expand(scratch_dir) if scratch_dir is not None else None
        )
        self.qcenv = shlex.quote(materia.expand(qcenv)) if qcenv is not None else None
        self.executable = executable
        self.num_processors = num_processors
        self.num_threads = num_threads
        self.arguments = arguments

    def execute(self, input_filepath: str, log_filepath: str) -> str:
        if self.scratch_dir is not None:
            os.environ["QCSCRATCH"] = materia.expand(self.scratch_dir)
        if self.qcenv is not None:
            qcenv_environ = ast.literal_eval(
                re.match(
                    r"environ\((.*)\)",
                    subprocess.check_output(
                        f". {self.qcenv}; python -c 'import os; print(os.environ)'",
                        shell=True,
                    )  # FIXME: shell=True needs to be avoided!!
                    .decode()
                    .strip(),
                ).group(1)
            )
            # os.environ.update(qcenv_environ)
        else:
            qcenv_environ = None
        cmd = [self.executable]
        if self.arguments is not None:
            cmd.extend(self.arguments)
        if self.num_processors is not None:
            cmd.append(f"-np {self.num_processors}")
        if self.num_threads is not None:
            cmd.append(f"-nt {self.num_threads}")
        cmd.extend([materia.expand(input_filepath), materia.expand(log_filepath)])

        if qcenv_environ is not None:
            return subprocess.check_output(
                shlex.split(" ".join(cmd)), env=qcenv_environ
            ).decode()
        return subprocess.check_output(shlex.split(" ".join(cmd))).decode()
