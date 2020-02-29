##  \package seal
#   The seal package.
#
#   \mainpage Seal API Documentation
#   The main divisions of Seal are:
#    - \ref seal.core
#    - \ref seal.script
#    - \ref seal.nlp
#    - \ref seal.ml
#    - \ref seal.data
#    - \ref seal.app
#    - \ref seal.cld

import sys, imp
from sys import stdin, stdout, stderr
from math import log, exp
from itertools import islice, chain

try:
    from numpy import matrix, array
    from numpy.linalg import svd
    from seal.data.wn import sense, sense_names, word_senses, words_expressing
except ImportError:
    pass

from seal.core.misc import hello, intersect, union, difference, call, launch, as_list, \
    concat, nth, head, tail, more, \
    count, counts, mean, Index, as_ascii

from seal.core.io import \
    Fn, ex, root, tmp, here, home, tmpfile, \
    infile, outfile, close, \
    load_string, save_string, load_lines, iter_lines, save_lines, \
    load_records, iter_records, save_records, \
    load_dict, save_dict, \
    load_paragraphs, iter_paragraphs, save_paragraphs, \
    load_tokens, iter_tokens, \
    Indenter, tabular, wget

from seal.ml.prob import lg, entropy, dotprod, cross_entropy, divergence, \
    f_measure, Dist

from seal.nlp.tree import \
    getcat, getchildren, getword, getnld, getrole, getid, getsem, getparent, \
    iter_trees, load_trees, save_trees, \
    set_parents, \
    getroot, \
    copy_tree, \
    delete_child, \
    draw_tree, \
    eliminate_epsilons, \
    expansion, \
    head_child, \
    head_index, \
    left_dependents, \
    is_dependency_tree, \
    is_efree_tree, \
    is_empty, \
    is_governor, \
    is_headed_phrase, \
    is_headed_tree, \
    is_interior, \
    is_leaf, \
    is_empty_leaf, \
    is_phrase, \
    is_leaf_word, \
    is_unary, \
    is_unaryfree_tree, \
    is_unheaded_phrase, \
    leaves, \
    Tree, \
    nodes, \
    nodetype, \
    preorder, \
    parse_tree, \
    paths, \
    right_dependents, \
    subtrees, \
    subtree, \
    tagged_words, \
    terminal_string, \
    textorder, \
    tree_to_dot, \
    TreeBuilder, \
    iter_tabular_trees, load_tabular_trees, save_tabular_trees, \
    treetype, \
    words

from seal.nlp.head import \
    decoordinate_node, decoordinate, HeadRules, find_head, mark_heads

from seal.nlp.dep import dependency_tree, stemma, governor_array

from seal.nlp.xml import load_xml, getvalue

#import seal.cld.rom
#seal.cld.rom.register()
