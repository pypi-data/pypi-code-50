import pysam

from typing import ClassVar, Iterator, Optional
from lhc.binf.genomic_coordinate import GenomicInterval
from lhc.io import open_file


class LociFile:

    REGISTERED_EXTENSIONS = {}
    REGISTERED_FORMATS = {}

    def __init__(self, file: str, mode: str = 'r', encoding: str = 'utf-8', index=1):
        self.generator = None
        if mode in 'rw':
            self.generator = open_file(file, mode, encoding)
            self.file = self.generator.__enter__()
        elif mode == 'q':
            self.file = pysam.TabixFile(file)
        else:
            raise ValueError('Unrecognised open mode: {}'.format(mode))
        self.mode = mode
        self.encoding = encoding
        self.index = index

    def __iter__(self) -> Iterator[GenomicInterval]:
        if self.mode == 'w':
            raise ValueError('Loci file opened for writing, not reading.')
        for line in self.file:
            if not line or line.startswith('#'):
                continue
            yield self.parse(line, self.index)

    def fetch(self, loci: GenomicInterval) -> Iterator[GenomicInterval]:
        if self.mode in 'rw':
            raise ValueError('Loci file opened for reading or writing, not querying.')
        return (self.parse(line, self.index) for line in
                self.file.fetch(str(loci.chromosome), loci.start.position, loci.stop.position))

    def write(self, loci: GenomicInterval):
        if self.mode in 'rq':
            raise ValueError('Loci file opened for reading or querying, not writing.')
        self.file.write(self.format(loci, self.index))
        self.file.write('\n')

    def close(self):
        if self.mode in 'rw':
            self.file.close()

    def parse(self, line: str) -> GenomicInterval:
        raise NotImplementedError('This function must be implemented by the subclass.')

    def format(self, loci: GenomicInterval) -> str:
        raise NotImplementedError('This function must be implemented by the subclass.')

    @classmethod
    def register_loci_file(cls, loci_file: ClassVar['LociFile']):
        for extension in loci_file.EXTENSION:
            cls.REGISTERED_EXTENSIONS[extension] = loci_file.FORMAT
        cls.REGISTERED_FORMATS[loci_file.FORMAT] = loci_file

    @classmethod
    def open_loci_file(cls, filename: Optional[str], mode='r', *,
                       encoding='utf-8', format: Optional[str] = None, index=1) -> 'LociFile':
        if filename is None and format is None:
            raise ValueError('When reading from stdin or writing to stdout, the file format must be specified.'
                             ' Valid formats are {}'.format(', '.join(cls.REGISTERED_FORMATS)))
        if not format:
            for extension, format in cls.REGISTERED_EXTENSIONS.items():
                if filename.endswith(extension):
                    break
        if format not in cls.REGISTERED_FORMATS:
            raise ValueError('Unknown loci file format: {}.'.format(format))
        return cls.REGISTERED_FORMATS[format](filename, mode, encoding, index)
