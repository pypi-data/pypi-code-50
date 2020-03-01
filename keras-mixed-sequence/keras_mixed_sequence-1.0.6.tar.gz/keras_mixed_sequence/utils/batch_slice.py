def batch_slice(index: int, batch_size: int) -> slice:
    """Return slice corresponding to given index for given batch_size.

    Parameters
    ---------------
    index: int,
        Index corresponding to batch to be rendered.
    batch_size: int
        Batch size for the current Sequence.

    Returns
    ---------------
    Return slice corresponding to given index for given batch_size.
    """
    return slice(index * batch_size, (index + 1) * batch_size)
