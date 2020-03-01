from typing import Dict, Union, Tuple
from tensorflow.keras.utils import Sequence
import numpy as np
from .utils import NumpySequence


class MixedSequence(Sequence):
    """Handles Mixed type input / output Sequences.

    Usage examples
    -----------------------------
    """

    def __init__(
        self,
        x: Union[Dict[str, Union[np.ndarray, Sequence]], np.ndarray, Sequence],
        y: Union[Dict[str, Union[np.ndarray, Sequence]], np.ndarray, Sequence],
        batch_size: int
    ):
        """Return new MixedSequence object.

        Parameters
        -------------
        x: Union[Dict[str, Union[np.ndarray, Sequence]], np.ndarray, Sequence],
            Either an numpy array, a keras Sequence or a dictionary of either of them
            to be returned as the input.
        y: Union[Dict[str, Union[np.ndarray, Sequence]], np.ndarray, Sequence],
            Either an numpy array, a keras Sequence or a dictionary of either of them
            to be returned as the output.
        batch_size: int,
            Batch size for the batches.

        Returns
        -------------
        Return new MixedSequence object.
        """
        # Casting to dictionary if not one already
        x, y = [
            e if isinstance(e, Dict) else {0: e}
            for e in (x, y)
        ]

        # Retrieving sequence length
        self._sequence_length = None
        self._batch_size = batch_size
        for candidate in (*x.values(), *y.values()):
            if isinstance(candidate, Sequence):
                self._sequence_length = len(candidate)
                break

        # Veryfing that at least a sequence was provided
        if self._sequence_length is None:
            raise ValueError("No Sequence was provided.")

        # Converting numpy arrays to Numpy Sequences
        x, y = [
            {
                key: NumpySequence(candidate, batch_size) if isinstance(
                    candidate, np.ndarray) else candidate
                for key, candidate in dictionary.items()
            }
            for dictionary in (x, y)
        ]

        # Checking that every value within the dictionaries
        # is now a sequence with the same length.
        for dictionary in (x, y):
            for _, value in dictionary.items():
                if len(self) != len(value):
                    raise ValueError(
                        "One or given sub-Sequence does not match length of other Sequences."
                    )

        self._x, self._y = x, y

    def on_epoch_end(self):
        """Call on_epoch_end callback on every sub-sequence."""
        for dictionary in (self._x, self._y):
            for _, value in dictionary.items():
                value.on_epoch_end()

    def __len__(self) -> int:
        """Return length of Sequence."""
        return self._sequence_length

    @property
    def steps_per_epoch(self) -> int:
        """Return length of Sequence."""
        return len(self)

    def __getitem__(self, idx: int) -> Tuple[
        Union[np.ndarray, Dict],
        Union[np.ndarray, Dict]
    ]:
        """Return batch corresponding to given index.

        Parameters
        ---------------
        idx: int,
            Index corresponding to batch to be rendered.

        Returns
        ---------------
        Return Tuple containing input and output batches.
        """
        return tuple([
            {
                key: sequence[idx]
                for key, sequence in dictionary.items()
            } if len(dictionary) > 1 else next(iter(dictionary.values()))[idx]
            for dictionary in (self._x, self._y)
        ])
