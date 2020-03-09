import sys, os

try:
    from ete3 import NCBITaxa
except ImportError as exc:
    print(exc)
    sys.exit(1)

def main():
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('taxid', metavar='taxid', type=str,
                        help='A comma-separated list of TaxIDs and/or taxon names. (e.g. 561,2172)')
    parser.add_argument('-d', '--db', dest="db", type=str, default=None,
                        help='NCBI taxonomy database file path.')
    parser.add_argument('-u', '--update', action='store_true', default=False,
                        help='Update taxon database before querying.')
    parser.add_argument('-i', '--taxon-info', action='store_true', default=False,
                        help='Just write out rank & lineage info on the provided taxids (default: %(default)s)')

    args = parser.parse_args(sys.argv[1:])

    ncbi = NCBITaxa(dbfile=args.db)

    #ncbi.update_taxonomy_database()



if __name__ == '__main__':
    main()
