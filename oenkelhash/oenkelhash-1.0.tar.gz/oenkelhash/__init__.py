import os
import sys
from pathlib import Path


def hash_file(file_path: Path):
    """Calculates a 64 bit hash for the given file"""

    with file_path.open("rb") as file:

        oenkel_hash = 0

        # The size determines the space between samples
        file_size = os.path.getsize(str(file_path))

        # Sample the file at 32 evenly spaced intervals
        for i in range(0, file_size, int(file_size/32)):
            file.seek(i, 0)

            # Read 8 bytes and xor it with oenkel_hash
            h = h ^ int.from_bytes(file.read(8), sys.byteorder)

        return oenkel_hash
