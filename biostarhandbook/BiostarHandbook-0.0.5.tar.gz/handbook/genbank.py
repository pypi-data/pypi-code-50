import re
import sys
from pprint import pprint
from itertools import count
import plac
import textwrap
from . import mydecs
from . import version

def parse_genbank(stream):

    try:
        from Bio import SeqIO
    except ImportError as exc:
        print(f"*** {exc}")
        print(f"*** This software requires biopython.")
        print(f"*** Try: conda install biopython")
        sys.exit(1)

    recs = SeqIO.parse(stream, "genbank")

    return recs


def hr(sep="-", size=80):
    print(sep * size)


def wrap(text):
    return "\n".join(textwrap.wrap(text))


def print_data(stream):
    # Parse the genbank stream.
    recs = parse_genbank(stream)
    for rec in recs:
        # print(dir(rec))
        rid = get_attr(rec, "id")
        name = get_attr(rec, "name")
        description = get_attr(rec, "description")
        dbxrefs=get_attr(rec, "dbxrefs")
        print(f"id={rid}")
        print(f"name={name}")
        print(f"description={description}")
        print(f"dbxrefs={dbxrefs}")
        pprint(rec.annotations)
        hr(sep="=")
        for feat in rec.features:
            print(feat)
            hr()
        hr(sep="=")


def escape(text):
    text = text.replace(";", "%3B")
    text = text.replace("=", "%3D")
    text = text.replace("&", "%26")
    text = text.replace("\t", "%09")
    text = text.replace(",", "%2C")
    return text


def format_attrs(feat, fields, sep="; "):
    """
    Formats field annotations on a record.
    """
    def func(field):
        value = get_attr(feat, field)
        value = escape(value)
        return field, value

    pairs = map(func, fields)
    pairs = filter(lambda x: x[1], pairs)
    pairs = list(pairs)
    vals = ["{}={}".format(*pair) for pair in pairs]
    line = sep.join(vals)
    return line


def flat_value(value):
    """
    Flattens values that may be lists.
    """
    if isinstance(value, list):
        return "|".join(value)
    else:
        return str(value)


def get_attr(feat, name):
    """
    Gets an attribute of a record.
    """
    if isinstance(feat, dict):
        value = feat.get(name)
    elif hasattr(feat, name):
        value = getattr(feat, name)
    elif hasattr(feat, "qualifiers"):
        value = feat.qualifiers.get(name, '')
    else:
        value = ''

    return flat_value(value or  '')


FIELDS = ["gene", "product", "type", "location", "locus_tag", "product"]


def get_seqid(feat, sep="; "):
    """
    Makes a sequence id for a Biopython feature.
    """
    prot = get_attr(feat, "protein_id") or get_attr(feat, 'gene')
    start = f">{prot} "
    rest = format_attrs(feat, fields=FIELDS)
    name = start + rest
    return name


def feat_type(word):
    def func(feat):
        return (word == feat.type) if word else True

    return func


def feat_overlap(coord):
    def func(feat):
        return feat.location.start <= coord <= feat.location.end if coord else True

    return func

@mydecs.nobreak
def print_genome(stream):
    # Parse the genbank stream.
    recs = parse_genbank(stream)

    for rec in recs:
        print(rec.format("fasta"))

@mydecs.nobreak
def print_gff(stream, ftype, match, coord=0):
    patt = re.compile(match, re.IGNORECASE)

    recs = parse_genbank(stream)

    print ("##gff-version 3")
    for rec in recs:
        # Filter the features.
        feats = filter(feat_type(ftype), rec.features)
        feats = filter(feat_overlap(coord), feats)
        recid = rec.name
        for index, feat in zip(count(1), feats):

            strand = '+' if feat.strand == 1 else '-'
            feat.ID = f'{recid}_{index}'

            attr = format_attrs(feat, feat.qualifiers.keys(), sep=";")

            data = [rec.id, ".", feat.type, int(feat.location.start)+1, int(feat.location.end), '0', strand, 0, attr]

            data = map(str, data)
            line = "\t".join(data)
            if patt.search(line):
                print (line)

@mydecs.nobreak
def print_seq(stream, ftype, match, coord=0):
    pass

@mydecs.nobreak
def print_translation(stream, ftype, match, coord=0):
    """
    Print the translation for each feature
    """
    patt = re.compile(match, re.IGNORECASE)

    recs = parse_genbank(stream)

    for rec in recs:

        # Filter the features.
        feats = filter(feat_type(ftype), rec.features)
        feats = filter(feat_overlap(coord), feats)

        for feat in feats:

            # print (dir(feat.location), feat.strand)

            seq_id = get_seqid(feat)

            if patt.search(seq_id):
                print(seq_id)
                seq = get_attr(feat, "translation")
                print(wrap(seq))


GENOME, PROTEIN, GFF, DNA = "genome", "protein", "gff", "dna"

choices = (GENOME, PROTEIN, GFF, DNA)


# Plac annotations:
#
# (help, kind, abbrev, type, choices, metavar)
#
@plac.annotations(
    t=("feature type (exact match)", "option", None, None, None, None),
    m=("sequence id match (regexp)", "option", None, None, None, None),
    c=("overlap with genomic coordinate (0=ignore)", "option", None, int, None, None),

    seq=(f"prints original sequences", "flag", "s"),
    gff=(f"prints GFF intervals", "flag", "i"),
    protein=(f"prints protein translations", "flag", "p"),
    genome=(f"prints the genome", "flag", "g"),
    report=(f"prints the GenBank data structure", "flag", "r"),
)
def run(seq=False, gff=False,  protein=False, genome=False, report=False, t='', m='.', c=0):
    "Reformats a GenBank file into Fasta or GFF"

    stream = sys.stdin

    if report:
        print_data(stream)
        return

    if (genome + protein + gff + seq) > 1:
        print(f"*** Only one output may be set: genome={genome} protein={protein} gff={gff} seq={seq} ")
        sys.exit(1)

    if genome:
        print_genome(stream)

    if protein:
        print_translation(stream, ftype='CDS', match=m, coord=c)
        return

    if gff:
        print_gff(stream=stream, ftype=t, match=m, coord=c)
        return

    if seq:
        print_seq(stream)
        return

def main():
    plac.call(run)


if __name__ == '__main__':
    main()
