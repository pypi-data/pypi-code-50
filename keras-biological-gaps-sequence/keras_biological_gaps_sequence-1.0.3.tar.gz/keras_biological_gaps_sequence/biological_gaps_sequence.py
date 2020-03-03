from tensorflow.keras.utils import Sequence
from ucsc_genomes_downloader.utils import expand_bed_regions
from keras_bed_sequence import BedSequence
import os
import pandas as pd
import numpy as np
from typing import Tuple


class BiologicalGapsSequence(Sequence):

    def __init__(
        self,
        source: str,
        target: str,
        source_window_size: int,
        target_window_size: int,
        batch_size: int,
        verbose: bool = True,
        seed: int = 42,
        elapsed_epochs: int = 0
    ):
        """Create new BiologicalGapsSequence.

        Parameters
        ----------------------------------
        source: str,
            Assembly from which to extract the input sequences.
            These sequences are centered upon the single nucleotide gaps.
        target: str,
            Assembly from which to extract the output sequences.
            These sequences are centered upon the nucleotides corresponding to the gaps.
        source_window_size: int,
            Window size to use for the input.
        target_window_size: int,
            Window size to use for the output.
        batch_size: int,
            Training batch size.
        verbose: bool = True,
            Wethever to show or not the loading bars.
        seed: int = 42,
            The seed to use for shuffling the data on training epoch end.
        elapsed_epochs: int = 0,
            The number of elapsed epochs.

        Raises
        ---------------------------------
        ValueError,
            If the dataset with given combination of source and target
            is not currently available.

        Returns
        ----------------------------------
        New BiologicalGapsSequence.
        """
        path = "{pwd}/datasets/{source}_{target}.bed".format(
            pwd=os.path.dirname(os.path.abspath(__file__)),
            source=source,
            target=target
        )
        if not os.path.exists(path):
            raise ValueError("Given combination of source '{source}' and target '{target}' is not currently available.".format(
                source=source,
                target=target
            ))
        bed = pd.read_csv(path, sep="\t")
        source_bed = expand_bed_regions(pd.DataFrame({
            "chrom": bed.chrom,
            "chromStart": bed[source],
            "chromEnd": bed[source]+1,
        }), source_window_size)
        target_bed = expand_bed_regions(pd.DataFrame({
            "chrom": bed.chrom,
            "chromStart": bed[target],
            "chromEnd": bed[target]+1,
        }), target_window_size)
        self._source_sequence = BedSequence(
            source,
            source_bed,
            batch_size=batch_size,
            verbose=verbose,
            seed=seed,
            nucleotides="actgn",
            elapsed_epochs=elapsed_epochs
        )
        self._target_sequence = BedSequence(
            target,
            target_bed,
            batch_size=batch_size,
            verbose=verbose,
            seed=seed,
            nucleotides="actgn",
            elapsed_epochs=elapsed_epochs
        )

    def on_epoch_end(self):
        """Shuffle private bed objects on every epoch end."""
        self._source_sequence.on_epoch_end()
        self._target_sequence.on_epoch_end()

    def __len__(self) -> int:
        """Return length of bed generator."""
        return len(self._source_sequence)

    @property
    def steps_per_epoch(self) -> int:
        """Return length of bed generator."""
        return self._source_sequence.steps_per_epoch

    @property
    def batch_size(self) -> int:
        """Return batch size to be rendered."""
        return self._source_sequence.batch_size

    @batch_size.setter
    def batch_size(self, batch_size: int):
        """Set batch size to given value."""
        self._source_sequence.batch_size = batch_size
        self._target_sequence.batch_size = batch_size

    @property
    def samples_number(self) -> int:
        """Return number of available samples."""
        return self._source_sequence.samples_number

    def __getitem__(self, idx: int) -> Tuple[np.ndarray, np.ndarray]:
        """Return batch corresponding to given index.

        Parameters
        ---------------
        idx: int,
            Index corresponding to batch to be rendered.

        Returns
        ---------------
        Return Tuple containing X and Y numpy arrays corresponding to given batch index.
        """
        # Get the input sequence
        x = self._source_sequence[idx]
        # Get the output sequence
        y = self._target_sequence[idx]
        # Get the values corresponding to gaps
        nx = x[:, :, -1].astype(bool)
        ny = y[:, :, -1].astype(bool)
        # Filter out the 5th nucleotide (the gaps)
        x = x[:, :, :4]
        y = y[:, :, :4]
        # Apply uniform value where the nucleotide is a gap
        x[nx] = 0.25
        y[ny] = 0.25
        return x, y
