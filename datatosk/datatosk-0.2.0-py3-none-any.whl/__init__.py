import pathlib

from .main import *

pyproject_path: pathlib.Path = pathlib.Path(__file__).parents[1].joinpath(
    "./pyproject.toml"
)

with pyproject_path.open() as f:
    for line in f.readlines():
        if line.startswith("version"):
            __version__ = line.strip().replace('version = "', "").replace('"', "")
            break
