from __future__ import annotations
import os
import materia
import subprocess
from typing import Optional

__all__ = ["MultiwfnEngine"]


class MultiwfnEngine:
    def __init__(
        self,
        log: Optional[str] = "multiwfn.log",
        executable: Optional[str] = "Multiwfn",
        work_dir: Optional[str] = ".",
        cleanup: Optional[bool] = False,
        num_cores: Optional[int] = 1,
        parallel: Optional[bool] = False,
    ) -> None:

        self.executable = executable
        self.work_dir = materia.expand(work_dir)

        self.log = os.path.join(work_dir, log)

        self.cleanup = cleanup

        self.num_cores = num_cores
        self.parallel = parallel

    def execute(self, input_path: str) -> None:
        with tempfile.TemporaryDirectory(
            dir=self.work_dir
        ) if self.cleanup else contextlib.nullcontext(self.work_dir) as wd:
            try:
                os.makedirs(wd)
            except FileExistsError:
                pass

            os.chdir(wd)

            with open(input_path, "r") as f:
                input_lines = f.readlines()

            if self.parallel:
                for s in reversed("\n".join(("1000", "10", str(self.num_cores), ""))):
                    input_lines.insert(1, s)

            with open(self.log, "w") as log:
                # For Multiwfn 3.6
                # FIXME: printf is system-specific - is there any other way to pipe in input_lines?
                pipe_command_string = subprocess.Popen(
                    args=("printf", "".join(input_lines)),
                    stdout=subprocess.PIPE,
                    encoding="utf-8",
                )
                multiwfn = subprocess.Popen(
                    (self.executable,),
                    stdin=pipe_command_string.stdout,
                    stdout=log,
                    stderr=subprocess.STDOUT,
                    encoding="utf-8",
                )
                pipe_command_string.stdout.close()
                multiwfn.communicate()
