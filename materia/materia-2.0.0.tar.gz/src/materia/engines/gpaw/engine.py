from __future__ import annotations
import contextlib
import os
import materia
import tempfile
from typing import Optional

__all__ = ["GPAWEngine"]


class GPAWEngine:
    def __init__(
        self,
        log: Optional[str] = "fragit.log",
        executable: Optional[str] = "fragit",
        work_dir: Optional[str] = ".",
        cleanup: Optional[bool] = False,
        num_cores=1,
        parallel=False,
    ) -> None:

        self.executable = executable
        self.work_dir = materia.expand(work_dir)

        self.log = os.path.join(work_dir, log)

        self.cleanup = cleanup
        self.num_cores = num_cores
        self.parallel = parallel

    def execute(self, structure_file):
        raise NotImplementedError
        with tempfile.TemporaryDirectory(
            dir=self.work_dir
        ) if self.cleanup else contextlib.nullcontext(self.work_dir) as wd:
            try:
                os.makedirs(wd)
            except FileExistsError:
                pass

            os.chdir(wd)

            with open(self.log, "w") as log:
                subprocess.call(
                    [self.executable, structure_file],
                    stdout=log,
                    stderr=subprocess.STDOUT,
                )
