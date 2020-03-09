from .loci_file import GenomicInterval, LociFile


class GtfFile(LociFile):

    EXTENSION = ('.gtf', '.gtf.gz')
    FORMAT = 'gtf'

    def parse(self, line: str, index=1) -> GenomicInterval:
        parts = line.rstrip('\r\n').split('\t')
        attributes = self.parse_attributes(parts[8])
        attributes['source'] = parts[1]
        attributes['feature'] = parts[2]
        attributes['score'] = parts[5]
        attributes['frame'] = parts[7]
        return GenomicInterval(int(parts[3]) - index, int(parts[4]),
                               chromosome=parts[0],
                               strand=parts[6],
                               data=attributes)

    def format(self, interval: GenomicInterval, index=1) -> str:
        attrs = {key: value for key, value in interval.data.items() if key not in {'source', 'feature', 'score', 'frame'}}
        source = interval.data.get('source', 'unknown')
        feature = interval.data.get('feature', 'exon')
        score = interval.data.get('score', 0)
        frame = interval.data.get('frame', 0)
        return '{chr}\t{source}\t{feature}\t{start}\t{stop}\t{score}\t{strand}\t{frame}\t{attrs}'.format(
            chr=interval.chromosome,
            source=source,
            feature=feature,
            start=interval.start.position + index,
            stop=interval.stop.position,
            score=score,
            strand=interval.strand,
            frame=frame,
            data=interval.data,
            attrs='; '.join('{} "{}"'.format(key, value) if isinstance(value, str) else '{} {}'.format(key, value) for key, value in attrs.items()))

    @staticmethod
    def parse_attributes(line):
        parts = (part.strip() for part in line.split(';'))
        parts = [part.split(' ', 1) for part in parts if part != '']
        for part in parts:
            part[1] = part[1][1:-1] if part[1].startswith('"') else int(part[1])
        return dict(parts)
