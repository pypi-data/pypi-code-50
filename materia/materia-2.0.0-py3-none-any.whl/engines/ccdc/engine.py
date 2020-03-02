from __future__ import annotations
import os
import materia
import subprocess
from typing import Optional

__all__ = ["CCDCEngine"]


class CCDCEngine:
    def __init__(
        self,
        log: Optional[str] = "ccdc.log",
        ccdc_root: Optional[str] = "fragit",
        work_dir: Optional[str] = ".",
        cleanup: Optional[bool] = False,
    ) -> None:

        self.executable = executable
        self.work_dir = materia.expand(work_dir)

        self.log = os.path.join(work_dir, log)

        self.cleanup = cleanup

        self.ccdc_root = materia.expand(ccdc_root)
        # FIXME: generalize past 2019 version of CCDC code
        self.executable = os.path.join(
            self.ccdc_root, "Python_API_2019", "miniconda", "bin", "python"
        )

    def execute(self, input_path: str) -> None:
        try:
            os.makedirs(materia.expand(self.work_dir))
        except FileExistsError:
            pass

        # FIXME: generalize past 2019 version of CCDC code
        os.environ["CSDHOME"] = os.path.join(self.ccdc_root, "CSD_2019")

        with open(self.output_path, "w") as f:
            subprocess.call((self.executable, input_path), stdout=f)
