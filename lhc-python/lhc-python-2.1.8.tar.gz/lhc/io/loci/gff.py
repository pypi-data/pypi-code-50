from .loci_file import GenomicInterval, LociFile


class GffFile(LociFile):

    EXTENSION = ('.gff', '.gff.gz')
    FORMAT = 'gff'

    def parse(self, line: str, index=1) -> GenomicInterval:
        parts = line.rstrip('\r\n').split('\t')
        attributes = self.parse_attributes(parts[8])
        attributes['source'] = parts[1],
        attributes['feature'] = parts[2]
        attributes['score'] = parts[5]
        attributes['frame'] = parts[7]
        return GenomicInterval(int(parts[3]) - index, int(parts[4]),
                              chromosome=parts[0],
                              strand=parts[6],
                              data=attributes)

    def format(self, interval: GenomicInterval, index=1) -> str:
        attrs = {key: value for key, value in interval.data.items() if key not in {'source', 'feature', 'score', 'frame'}}
        return '{chr}\t{data[source]}\t{data[feature]}\t{start}\t{stop}\t{data[score]}\t{strand}\t{data[frame]}\t{attrs}'.format(
            chr=interval.chromosome,
            start=interval.start.position + index,
            stop=interval.stop.position,
            strand=interval.strand,
            data=interval.data,
            attrs=';'.join('{}={}'.format(key, value) for key, value in attrs.items()))

    @staticmethod
    def parse_attributes(line):
        attributes = {}
        for part in line.split(';'):
            if part:
                key, value = part.split('=', 1) if '=' in part else part
                attributes[key] = value.split(',')
        return attributes
