from .loci_file import GenomicInterval, LociFile


class BedFile(LociFile):

    EXTENSION = ('.bed', '.bed.gz')
    FORMAT = 'bed'

    def parse(self, line: str, index=1) -> GenomicInterval:
        parts = line.rstrip('\r\n').split('\t')
        name = parts[3] if len(parts) > 3 else ''
        score = parts[4] if len(parts) > 4 else ''
        strand = parts[5] if len(parts) > 5 else '+'
        return GenomicInterval(int(parts[1]) - index, int(parts[2]),
                               chromosome=parts[0],
                               strand=strand,
                               data={'gene_id': name, 'score': score})

    def format(self, interval: GenomicInterval, index=1) -> str:
        return '{chr}\t{start}\t{stop}\t{data[gene_id]}\t{data[score]}\t{strand}'.format(
            chr=interval.chromosome,
            start=interval.start.position + index,
            stop=interval.stop.position,
            data=interval.data,
            strand=interval.strand)
