from . import sources


def source(engine, **kwargs):
    try:
        src = sources.ENGINES[engine]
    except KeyError:
        raise NotImplementedError(f"{engine} engine is not supported")

    return src(**kwargs)
