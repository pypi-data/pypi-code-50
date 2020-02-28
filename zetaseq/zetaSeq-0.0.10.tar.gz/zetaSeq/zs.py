#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 10:36:47 2018

Coders who love to comment their code are unlikely to have bad luck.

@author: Zewei Song
@email: songzewei@genomics.cn
"""
#%
from __future__ import print_function
from __future__ import division
import zetaSeq.util
import sys

def main():
    import argparse
    import textwrap
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, \
                                     description=textwrap.dedent('''\
                                    ZetaSeq is a versatile toolbox for handling sequencing data.
                                                                 '''),
                                     epilog=textwrap.dedent('''\
                                    ------------------------
                                    By Zewei Song
                                    BGI Research
                                    Shenzhen China
                                    songzewei@outlook.com
                                    ------------------------'''), prog='zseq', usage='%(prog)s [options]')
    subparsers = parser.add_subparsers(help='commands', dest='subparser_name')
    # count aligned reads
    countAlnReads_parser = subparsers.add_parser('countAlnReads', help='Count the number of reads aligned to the reference.', \
                                                 description='Count the number of alignments in the data file.')
    countAlnReads_parser.add_argument('-i', '--input', help='The alignment output to count.')
    countAlnReads_parser.set_defaults(func=countAlnReads)
  
    # keep paired alignments
    keepPairAln_parser = subparsers.add_parser('keepPairAln', help='Keep only the pair alignment of a read.', \
                                               description='Keep alignments contain both reads (R1 and R2).')
    keepPairAln_parser.add_argument('-i', '--input', type=argparse.FileType('r'), nargs='+', \
                                    default=sys.stdin, help='The alignment to be checked.')
    keepPairAln_parser.add_argument('-o', '--output', help='The paired alignment.')
    keepPairAln_parser.set_defaults(func=keepPairAln)
    
    # concat multiple biome files into one biom file, using JSON format
    concatBioms_parser = subparsers.add_parser('concatBioms', help='Concat multiple biome files into one biom file, using JSON format.', \
                                               description='Join all biom profiles into one.')
    concatBioms_parser.add_argument('-i', '--input', type=argparse.FileType('r'), nargs='+', \
                                    default=sys.stdin, help='The biom files to be concat.')
    concatBioms_parser.add_argument('-o', '--output', help='The paired alignment.')
    concatBioms_parser.set_defaults(func=concatBioms)    
    
    # winner-take-all profile
    winnerTakeAll_parser = subparsers.add_parser('winnerTakeAll', help='Calculate the winner-take-all profile from alignments.', \
                                                 description='Calculate the winner-take-all profile.')
    winnerTakeAll_parser.add_argument('-i', '--input', type=argparse.FileType('r'), nargs='+', \
                                    default=sys.stdin, help='The alignment to be calculated.')
    winnerTakeAll_parser.add_argument('-o', '--output', help='The tab-delimited profile.')
    winnerTakeAll_parser.add_argument('-sn', '--sample_name', help='Sample name.')
    method = winnerTakeAll_parser.add_mutually_exclusive_group(required=True)
    method.add_argument('-g', '--greedy', action='store_true', default=True, \
                        help='Option to enable greedy method. [Default is greedy capitalists]')
    method.add_argument('-l', '--less_greedy', action='store_true', default=False, \
                        help='Option to enable less greedy method, equally greedy is nTargets = 1. [Enable me to disable the greedy capitalists]')
    score = winnerTakeAll_parser.add_mutually_exclusive_group()
    score.add_argument('-ec', action='store_true', default=True, \
                       help='Specify to score using Effective Count [Default]')
    score.add_argument('-median', action='store_true', default=False, \
                       help='Specify to score using median of abundance.')
    score.add_argument('-ave', action='store_true', default=False, \
                       help='Specify to score using average of abundance.')
    winnerTakeAll_parser.set_defaults(func=winnerTakeAll)
    
    # Rarefy a profile array
    rarefy_parser = subparsers.add_parser('rarefy', help='Rarefy a profile array.', \
                                          description='Perform a random sampling on an OTU table.')
    rarefy_parser.add_argument('-i', '--input', help='Input OTU table.')
    rarefy_parser.add_argument('-o', '--output', help='Output OTU table.')
    rarefy_parser.add_argument('-d', '--depth', type=int, help='Subsampling depth.')
    rarefy_parser.add_argument('-n', '--iteration', type=int, default=1000, help='Number of rarefying iteration for an array.')
    rarefy_parser.add_argument('-t', '--threads', type=int, default=8, help='Number of threads.')
    rarefy_parser.add_argument('-k', '--keep_all', action='store_true', \
                               help='Switch to keep all samples, including ones lower than the depth.')
    rarefy_parser.add_argument('-meta_column', default='taxonomy', help='Name of the first meta data')
    
    args = parser.parse_args()
    args.func(args)

def test_me(args):    
    import zetaSeq.util
    zetaSeq.util.test_me(args)

# count the number of aligned reads
def countAlnReads(args):
    zetaSeq.util.countAlnReads(args)
    return None

# keep paired alignments
def keepPairAln(args):
    zetaSeq.util.keepPairAln(args)
    return None

# concat multiple biome files into one biom file, using JSON format
def concatBioms(args):
    zetaSeq.util.concatBioms(args)
    return None

# calculate the winner take all profile
def winnerTakeAll(args):
    zetaSeq.util.winnerTakeAll(args)
    return None

# Randomly sample a profile array into lower depth
def rarefy(args):
    zetaSeq.util.rarefy(args)
    return None

if __name__ == '__main__':
    main()