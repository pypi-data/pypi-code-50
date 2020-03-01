from typing import List
import numpy as np


def sequence_length(sequence: List, batch_size: int) -> int:
    """Return number of batch sizes contained in sequence.

    Parameters
    -----------
    sequence: List,
        Iterable to split into batches.
    batch_size: int,
        Size of the batches.

    Returns
    -----------
    Return number of batch size contained in given sequence, by excess.
    """
    return int(np.ceil(len(sequence) / float(batch_size)))
