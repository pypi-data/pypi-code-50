from __future__ import annotations
import os
import materia
import subprocess
from typing import Iterable, Optional

from ...workflow.tasks.task import Task
from ...workflow.handlers.handler import Handler

__all__ = ["ExecuteMultiwfn", "MultiwfnVolume", "WriteMultiwfnInput"]


class ExecuteMultiwfn(Task):
    def __init__(
        self,
        input_path: str,
        engine: materia.MultiwfnEngine,
        handlers: Optional[Iterable[materia.Handler]] = None,
        name: Optional[str] = None,
    ) -> None:
        super().__init__(handlers=handlers, name=name)
        self.input_path = input_path
        self.engine = engine

    def run(self) -> None:
        self.engine.execute(input_path=self.input_path)


class MultiwfnVolume(Task):
    def __init__(
        self,
        input_name: str,
        output_name: str,
        executable: str = "Multiwfn",
        work_directory: str = ".",
        num_cores: int = 1,
        parallel: bool = False,
        handlers: Iterable[Handler] = None,
        name: str = None,
    ):
        super().__init__(handlers=handlers, name=name)
        self.input_path = materia.expand(os.path.join(work_directory, input_name))
        self.output_path = materia.expand(os.path.join(work_directory, output_name))

        self.executable = executable

        self.num_cores = num_cores
        self.parallel = parallel

        try:
            os.makedirs(materia.expand(work_directory))
        except FileExistsError:
            pass

    def run(
        self,
        molden_filepath: str,
        integration_mesh_exp: int = 9,
        density_isosurface: float = 0.001,
        box_size_factor: float = 1.7,
    ):
        materia.MultiwfnInput(
            materia.expand(molden_filepath),
            100,
            3,
            f"{integration_mesh_exp},{density_isosurface},{box_size_factor}",
            "0,0,0",
            0,
            -10,
        ).write(input_path=self.input_path)

        # For Multiwfn 3.6
        with open(self.input_path, "r") as f:
            input_lines = f.readlines()

        if self.parallel:
            for s in reversed("\n".join(("1000", "10", str(self.num_cores), ""))):
                input_lines.insert(1, s)

        with open(self.output_path, "w") as f:
            # FIXME: printf is system-specific - is there any other way to pipe in input_lines?
            pipe_command_string = subprocess.Popen(
                args=("printf", "".join(input_lines)),
                stdout=subprocess.PIPE,
                encoding="utf-8",
            )
            multiwfn = subprocess.Popen(
                (self.executable,),
                stdin=pipe_command_string.stdout,
                stdout=f,
                encoding="utf-8",
            )
            pipe_command_string.stdout.close()
            multiwfn.communicate()

        return materia.MultiwfnOutput(filepath=self.output_path).get("volume")


class WriteMultiwfnInput(Task):
    def __init__(
        self,
        input_name: str,
        in_filepath: str,  # FIXME: awful name for this variable, fix here and analogous issues throughout this file
        commands: Iterable[str],
        work_directory: str = ".",
        handlers: Iterable[Handler] = None,
        name: str = None,
    ):
        super().__init__(handlers=handlers, name=name)
        self.input_path = materia.expand(os.path.join(work_directory, input_name))
        self.in_filepath = materia.expand(in_filepath)
        self.commands = commands

        try:
            os.makedirs(materia.expand(work_directory))
        except FileExistsError:
            pass

    def run(self):
        materia.MultiwfnInput(self.in_filepath, *self.commands).write(self.input_path)
