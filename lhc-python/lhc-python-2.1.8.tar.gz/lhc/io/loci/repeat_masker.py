from abc import ABC
from collections import Counter
from .loci_file import GenomicInterval, LociFile


class RepeatMaskerFile(LociFile):

    EXTENSION = ('.out', '.out.gz')
    FORMAT = 'repeat_masker'

    def __init__(self, file: str, mode: str = 'r', encoding: str = 'utf-8', index=1):
        super().__init__(file, mode, encoding, index)
        self.transcript_ids = Counter()
        self.unknown_genes = 0
        next(self.file)
        next(self.file)
        next(self.file)

    def parse(self, line: str, index=1) -> GenomicInterval:
        parts = line.rstrip('\r\n').split()
        class_, *family = parts[10].split('/', 1)
        try:
            gene_id = parts[14]
        except IndexError:
            self.unknown_genes += 1
            gene_id = 'unknown_{}'.format(self.unknown_genes)
        transcript_id = '{}.1'.format(gene_id)
        self.transcript_ids[transcript_id] += 1
        exon_number = self.transcript_ids[transcript_id]
        exon_id = '{}.{}'.format(transcript_id, exon_number)
        return GenomicInterval(
            int(parts[5]) - index,
            int(parts[6]),
            chromosome=parts[4],
            strand='+' if parts[8] == '+' else '-',
            data={'score': parts[0], 'divergence': parts[1], 'deletion': parts[2], 'insertion': parts[3],
                  'subfamily_id': parts[9], 'class_id': class_, 'family_id': ''.join(family), 'gene_id': gene_id,
                  'transcript_id': transcript_id, 'source': 'RepeatMasker', 'feature': 'repeat_element', 'frame': '0',
                  'exon_id': exon_id, 'exon_number': exon_number})
