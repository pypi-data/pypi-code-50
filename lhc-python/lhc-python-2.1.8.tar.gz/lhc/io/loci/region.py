from .loci_file import GenomicInterval, LociFile


class RegionFile(LociFile):

    EXTENSION = ('.txt', '.txt.gz')
    FORMAT = 'region'

    def parse(self, line: str, index=1) -> GenomicInterval:
        chromosome, interval = line.split(':', 1)
        start, stop = interval.split('-')
        return GenomicInterval(int(start) - index, int(stop), chromosome=chromosome)

    def format(self, interval: GenomicInterval, index=1) -> str:
        return '{chr}:{start}-{stop}'.format(
            chr=interval.chromosome,
            start=interval.start.position + index,
            stop=interval.stop.position)
