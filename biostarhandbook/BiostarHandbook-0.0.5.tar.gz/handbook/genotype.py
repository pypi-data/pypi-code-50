"""
Iterates over a BAM file and prints reads that match a genotype at a location.

Works for matches and mistmatching bases only.
"""
import csv
import os
import sys
import plac
from pprint import pprint
import argparse

def group_variations(fasta, fname, chrom, pos, meta="metadata.txt", long=False):

    try:
        # Don't make pysam a universal dependency.
        import pysam
    except ImportError as exc:
        print("*** This program requires pysam: conda install pysam", file=sys.stderr)
        sys.exit(1)

    if os.path.isfile(meta):
        stream = csv.reader(open(meta, 'rt'), delimiter="\t")
        pairs = [(p[0], p[1:]) for p in stream]
        data = dict(pairs)
    else:
        data = dict()

    bam = pysam.AlignmentFile(fname, 'rb')

    fasta = pysam.FastaFile(fasta)

    store = dict()

    def update(pos):
        stream = bam.pileup(chrom, start=pos, end=pos+1)
        stream = filter(lambda c: c.pos == pos, stream)
        for col in stream:
            names = col.get_query_names()
            seqs = col.get_query_sequences(add_indels=True)

            base = fasta.fetch(chrom, col.reference_pos,col.reference_pos+1).upper()


            for name, alt in zip(names, seqs):
                alt = alt.upper()
                gtp = f"{base}/{alt}"
                store.setdefault(name, []).append(gtp)

    # The position is zero based.
    values = list(map(int, pos.split(",")))
    for val in values:
        update(val-1)

    #pprint(store)

    # Reformat the collected information
    group = dict()
    for name, values in store.items():
        newkey = ",".join(values)
        group.setdefault(newkey, []).append(name)

    #pprint(group)

    def short_report(group, header):
        print("\t".join(header))
        for index, (base, values) in enumerate(group.items()):
            gname = f"{base}"
            data = [ pos, len(values), gname,]
            data = map(str, data)
            print("\t".join(data))


    def long_report(group, header):
        print("\t".join(header))
        for index, (base, values) in enumerate(group.items()):
            # Making a group number
            gname = f"{base}"
            for name in values:
                name = name.split(".")[0]
                fields = data.get(name, [])
                attr = "\t".join(fields)
                elems = [pos, len(values), gname,  name, attr]
                elems = map(str, elems)
                print("\t".join(elems))

    if long:
        header = ["pos","count",  "gtype", "sample"]
        long_report(group, header=header)
    else:
        header =  [ "pos", "count", "gtype" ]
        short_report(group, header=header)

@plac.annotations(
    bam=("input BAM file (sorted, indexed)", "option", "b", str),
    f=("reference genome file (samtools indexed)", "option", None, None, None, "FASTA"),
    chr=("chromosome name", "option", "c", str),
    pos=("genomic coordinate(s), comma separated if more than one", "option", "p", str),
    m=("metadata matching read names", "option",),
    long= ("long form of report", "flag","L")
)
def run(f, bam, chr, pos, long=False, m="metadata.txt", ):
    "Groups reads in a BAM file by their genotype at a position"
    group_variations(fasta=f, fname=bam, chrom=chr, pos=pos, meta=m, long=long)


def main():
    plac.call(run)


if __name__ == '__main__':
    main()
