import heapq

from typing import Dict, Iterable, Iterator, List
from lhc.binf.genomic_coordinate import GenomicInterval, NestedGenomicInterval


def make_loci(loci: Iterable[GenomicInterval], *, tolerance: int = 100000) -> Iterator[NestedGenomicInterval]:
    tops = []  # type: List[NestedGenomicInterval]
    parents = {}  # type: Dict[str, NestedGenomicInterval]
    for locus in loci:
        gene_id = locus.data['gene_id']
        transcript_id = locus.data['transcript_id']
        nested_locus = NestedGenomicInterval(locus.start, locus.stop, strand=locus.strand, data=locus.data)

        if locus.data['feature'] == 'gene':
            heapq.heappush(tops, nested_locus)
            parents[gene_id] = nested_locus
        elif locus.data['feature'] == 'transcript':
            parents[transcript_id] = nested_locus
            parents[gene_id].add_child(nested_locus)
        else:
            if gene_id not in parents:
                top = NestedGenomicInterval(locus.start, locus.stop, strand=locus.strand, data=locus.data)
                heapq.heappush(tops, top)
                parents[gene_id] = top
            if transcript_id not in parents:
                parents[transcript_id] = NestedGenomicInterval(locus.start, locus.stop, strand=locus.strand, data=locus.data)
                parents[gene_id].add_child(parents[transcript_id])
            parents[transcript_id].add_child(nested_locus)

        while len(tops) > 0 and tops[0].data['gene_id'] != gene_id and tops[0].stop + tolerance < locus.start:
            gene = tops.pop(0)
            for transcript in gene.children:
                del parents[transcript.data['transcript_id']]
            del parents[gene.data['gene_id']]
            yield gene

    yield from tops
