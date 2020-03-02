from __future__ import annotations
import cclib
import os
import materia
import subprocess
from typing import Any, Iterable, Optional

from ...workflow.tasks.task import Task

__all__ = ["ExecuteVASP"]


class ExecuteVASP(Task):
    def __init__(
        self,
        output_name: str,
        executable: str = "vasp_std",
        work_directory: str = ".",
        num_cores: int = 1,
        parallel: bool = False,
        handlers: Optional[Iterable[materia.Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__()
        self.settings["executable"] = executable
        self.settings["output_path"] = os.path.join(
            work_directory, materia.expand(output_name)
        )
        self.settings["work_directory"] = materia.expand(work_directory)

        self.settings["num_cores"] = num_cores
        self.settings["parallel"] = parallel

        try:
            os.makedirs(self.settings["work_directory"])
        except FileExistsError:
            pass

    def run(self, **kwargs: Any) -> Any:
        with open(self.settings["output_path"], "w") as f:
            if self.settings["parallel"]:
                subprocess.call(
                    [
                        "mpirun",
                        "np",
                        str(self.settings["num_cores"]),
                        self.settings["executable"],
                    ],
                    stdout=f,
                    stderr=subprocess.STDOUT,
                )
            else:
                subprocess.call([self.settings["executable"]], stdout=f)
