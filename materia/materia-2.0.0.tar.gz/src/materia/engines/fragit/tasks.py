from __future__ import annotations
import contextlib
import materia
import os
import re
import tempfile
from typing import Iterable, Optional, Tuple, Union
import uuid

from ...workflow.tasks.task import Task

__all__ = ["FragItFragmentStructure"]


class FragItFragmentStructure(Task):
    """
    Task to fragment a structure using FragIt.

    Attributes:
        engine (materia.FragItEngine): Engine which will be used to fragment structure.
    """

    def __init__(
        self,
        engine: materia.FragItEngine,
        log_name: str = "fragit.log",
        work_dir: str = ".",
        keep_logs: bool = True,
        handlers: Optional[Iterable[materia.Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__(handlers=handlers, name=name)
        self.engine = engine
        self.log_name = log_name
        self.work_dir = materia.expand(work_dir)
        self.keep_logs = keep_logs

    def run(
        self, structure: Union[str, materia.Structure]
    ) -> Tuple[str, Iterable[materia.Structure]]:
        with contextlib.nullcontext(
            self.work_dir
        ) if self.keep_logs else tempfile.TemporaryDirectory(dir=self.work_dir) as wd:
            try:
                os.makedirs(wd)
            except FileExistsError:
                pass

            if isinstance(structure, str):
                filepath = materia.expand(structure)
            else:
                while isinstance(structure, materia.Structure):
                    filepath = materia.expand(
                        os.path.join(wd, f"{uuid.uuid4().hex}.xyz")
                    )
                    try:
                        structure.write(filepath)
                        break
                    except FileExistsError:
                        continue

            self.engine.execute(
                structure_filepath=filepath,
                log_filepath=materia.expand(os.path.join(wd, self.log_name)),
                work_dir=wd,
            )

            name, _ = os.path.splitext(os.path.basename(filepath))
            pat = re.compile(rf"(?P<file_name>{name}_fragment_\d*\.xyz)")
            matches = (pat.match(s) for s in os.listdir(wd))

            return tuple(
                materia.Structure.read(os.path.join(wd, m.group("file_name")))
                for m in matches
                if m is not None
            )
