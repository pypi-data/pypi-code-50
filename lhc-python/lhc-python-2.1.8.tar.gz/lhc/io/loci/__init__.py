from contextlib import contextmanager
from typing import Optional
from .loci_file import LociFile
from .bed import BedFile
from .gff import GffFile
from .gtf import GtfFile
from .region import RegionFile
from .repeat_masker import RepeatMaskerFile


@contextmanager
def open_loci_file(filename: Optional[str], mode='r', *, encoding='utf-8', format: Optional[str] = None, index=1):
    file = LociFile.open_loci_file(filename, mode, encoding=encoding, format=format, index=index)
    yield file
    file.close()


LociFile.register_loci_file(BedFile)
LociFile.register_loci_file(GffFile)
LociFile.register_loci_file(GtfFile)
LociFile.register_loci_file(RegionFile)
LociFile.register_loci_file(RepeatMaskerFile)
