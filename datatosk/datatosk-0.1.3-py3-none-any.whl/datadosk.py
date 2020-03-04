from pathlib import Path

from dotenv import load_dotenv

from . import sources

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


def source(engine, **kwargs):
    try:
        src = sources.ENGINES[engine]
    except KeyError:
        raise NotImplementedError(f"{engine} engine is not supported")

    return src(**kwargs)
