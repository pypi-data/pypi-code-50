#!/usr/bin/env python

import argparse
import codecs
import gc
import logging
import math
import os
import time
from typing import Dict, Collection, Iterator, Optional, Set, Tuple

import psutil

from . import explanation_evaluation
from . import local_hdt
from . import path_evaluation
from . import path_pruner
from . import urishortener
from .blacklist import Blacklist
from .example import Examples
from .explanation import Explanation
from .knowledge_graph import Predicate, Vertex
from .memory_profiler import MemoryProfiler, profiler
from .path import Path
from .path_evaluation import SearchHeuristic, HEURISTIC_NAMES
from .path_pruner import PathPruner, PATH_PRUNER_NAMES


def strict_handler(exception):
    return u"", exception.end


codecs.register_error("strict", strict_handler)
LOG = logging.getLogger('dedalov2.ddl')


def print_examples(examples: Examples) -> None:
    LOG.debug("Using examples:")
    for e in examples:
        LOG.debug(e)


def mem_limit_exceeded(process: psutil.Process, memlimit: float) -> Tuple[bool, float]:
    membytes = process.memory_info().rss
    if membytes >= memlimit:
        gc.collect()
        membytes = process.memory_info().rss
        if membytes > memlimit:
            return (True, membytes)
    return (False, membytes)


def explain(hdt_file: str, example_file: str, heuristic: str = "entropy", groupid: int = None, prefix: str = None,
            blacklist: str = None, truncate: int = 0, balance: bool = True, prune: str = "gle",
            mem_profile: bool = False, runtime: float = math.inf, rounds: float = math.inf,
            complete: int = 0, minimum_score: float = math.inf, memlimit: float = math.inf) -> Iterator[Explanation]:
    """Explain why a group of URIs belong together using Semantic Web technology.
    
    :param hdt_file: The location of the HDT file to search for explanations. Instead of traversing the LOD-cloud, Dedadov2 offers increased performance in \
        exchange for using a preconstructed file containing the linked data. HDT is a space-efficiant storage format for linked data.
    :type hdt_file: str
    :param example_file: The location of the text file with input examples and their groups.
    :type example_file: str
    :param heuristic: The search heuristic that determines which path should be explored next, defaults to "entropy"
    :type heuristic: str, optional
    :param groupid: The id of the group that should be explained, defaults to None
    :type groupid: int, optional
    :param prefix: The location of a tsv-file with URI prefixes. This makes printed URIs easier to read, defaults to None
    :type prefix: str, optional
    :param blacklist: The location of a text file with predicate URIs (one per line) that Dedalov2 must ignore, defaults to None
    :type blacklist: str, optional
    :param truncate: If this value is larger than 0, both the number of positive examples (URIs from the given group id) and the number of negative examples \
        (URIs from all other groups) are truncated to this amount, defaults to 0
    :type truncate: int, optional
    :param balance: Discard examples such that that the number of positive and negative examples are equal, defaults to True
    :type balance: bool, optional
    :param prune: The path pruning policy to use, defaults to "gle"
    :type prune: str, optional
    :param mem_profile: If set to True, occassionaly log memory usage data, defaults to False
    :type mem_profile: bool, optional
    :param runtime: The mamimum allowed runtime. Stop searching after this time, defaults to math.inf
    :type runtime: float, optional
    :param rounds: Stop searching after this number of rounds. Every round, one path is explored, defaults to math.inf
    :type rounds: float, optional
    :param complete: If larger than 0, stop searching after all explanations with the given path length have been found. \
        an be used to implement complete search to limited depth, defaults to 0
    :type complete: int, optional
    :param minimum_score: If equal or greater to zero, only return explanations with a score greater or equal to the given value, defaults to -1
    :type minimum_score: float, optional
    :param memlimit: Stop searching if the program uses more than the given amount of memory in bytes. Can help prevent MemoryErrors, defaults to math.inf
    :type memlimit: float, optional
    :return: All explanations that meet the given requirements
    :rtype: Iterator[Explanation]
    """
    local_hdt.init(hdt_file)

    urishortener.setPrefixMapFromFile(prefix)
    bl = Blacklist.fromFile(blacklist)
    heur: SearchHeuristic = HEURISTIC_NAMES[heuristic]

    examples = Examples.fromCSV(example_file, groupid=groupid, truncate=truncate, balance=balance)
    print_examples(examples)

    pruner = PATH_PRUNER_NAMES[prune](explanation_evaluation.max_fuzzy_f_measure, examples)
    mp: MemoryProfiler = profiler(mem_profile)
    for explanation in _explain(examples, pruner, heuristic=heur, mp=mp, blacklist=bl, runtime=runtime, rounds=rounds,
                                complete=complete, minimum_score=minimum_score, memlimit=memlimit):
        yield explanation


def _explain(examples: Examples, pruner: PathPruner, heuristic: SearchHeuristic = path_evaluation.entropy,
             mp: MemoryProfiler = profiler(False), runtime: float = math.inf,
             rounds: float = math.inf, blacklist: Blacklist = None, complete: int = 0,
             minimum_score: float = -1, memlimit: float = math.inf) -> Iterator[Explanation]:
    nodes: Collection[Vertex] = [example.vertex for example in examples]

    paths: Dict[Path, Path] = dict()
    explanations: int = 0

    best_path: Optional[Path] = Path.from_examples(examples)
    end_time = time.time() + runtime
    round_number = 1
    shortest_path: int = 0
    process = psutil.Process(os.getpid())
    try:
        while best_path is not None and time.time() < end_time and round_number <= rounds and (complete == 0 or shortest_path < complete):
            mp()
            new_explanations: Set[Explanation] = set()
            LOG.debug("ROUND: {}".format(round_number))
            LOG.debug("PATH: {} NUMVERTICES: {}".format(best_path, len(nodes)))
            round_start = time.time()
            for i, node in enumerate(nodes):
                _print_progress(len(nodes), i, round_number)
                e = follow_outgoing_links(node, best_path, paths, end_time, examples, blacklist=blacklist)
                new_explanations.update(e)
                explanations += len(e)
                curtime = time.time()
                if curtime > end_time:
                    LOG.debug("RUNTIME LIMIT EXCEEDED: {} > {}. EXITING".format(curtime, end_time))
                    break
            if len(new_explanations) > 0:
                explanation_evaluation.find_best_explanation(new_explanations, examples)
                for exp in new_explanations:
                    if exp.record is not None and exp.record.score >= minimum_score:
                        yield exp
            paths.pop(best_path, None)

            round_duration = time.time() - round_start
            exceeded, num_bytes = mem_limit_exceeded(process, memlimit)
            LOG.debug("ROUND: {} TIME: {} MEMBYTES: {}".format(round_number, round_duration, num_bytes))
            mp()
            round_number += 1
            if exceeded:
                LOG.debug("MEMLIMIT EXCEEDED: {} > {}. EXITING".format(num_bytes, memlimit))
                break

            if len(paths) > 0:
                if complete > 0:
                    shortest_path = min(map(lambda x: len(x), paths))
                best_path = path_evaluation.find_best_path(heuristic, paths, examples, pruner, max_length=complete - 1)
                if best_path is None:
                    break
                nodes = set(v for v in best_path.get_end_points() if v.is_subject())
            else:
                break
    except KeyboardInterrupt as ki:
        raise ki
    LOG.debug("Exiting...")
    LOG.debug("Num explanations created: {}".format(explanations))


def _print_progress(number_of_nodes: int, current_node_index: int, round_number: int) -> None:
    if number_of_nodes > 10000 and current_node_index % 1000 == 0:
        LOG.debug("Round {} at {}%".format(round_number, int(current_node_index/number_of_nodes*100)))


def follow_outgoing_links(node: Vertex, best_path: Path, paths: Dict[Path, Path], end_time: float,
                          examples: Examples, blacklist: Blacklist = None) -> Set[Explanation]:
    new_explanations: Set[Explanation] = set()
    triples, k = local_hdt.document().search_triples_ids(node.s_id, 0, 0)
    for s_id, p_id, o_id in triples:
        s = Vertex.fromSubjectId(s_id)
        p = Predicate(p_id)
        o = Vertex.fromObjectId(o_id)
        # Create new path.
        if blacklist is not None and blacklist.isBlacklisted(p):
            continue
        path = best_path.extend(paths, s, p, o)
        exp = Explanation(path, o)
        new_explanations.add(exp)
        if time.time() > end_time:
            break
    return new_explanations


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("example_file")
    parser.add_argument("--hdt-file", type=str, default="/scratch/wbeek/data/LOD-a-lot/data.hdt", help="Location of HDT file to use.")
    parser.add_argument("--groupid", type=int, help="The positive examples group number.")
    parser.add_argument("--truncate", "-t", type=int, help="Selects the first x positive and negative examples. The resulting input has size 2x.")
    parser.add_argument("--balance", "-b", action="store_true", help="Makes sure that the number of positive examples equals the number of negative examples. \
        This is performed after truncate.")

    parser.add_argument("--heuristic", type=str, choices=HEURISTIC_NAMES, default="entropy", help="The search heuristic to use.")

    parser.add_argument("--complete", "-c", type=int, default=0, help="Perform a complete search of all paths up to given length.")
    parser.add_argument("--runtime", type=float, default=math.inf, help="Number of seconds the program is allowed to run.")
    parser.add_argument("--rounds", default=math.inf, help="Number of rounds the program is allowed to run.")
    parser.add_argument("--memlimit", type=int, default=2**35, help="Stops the program once it uses more than the given amount of RAM in bytes.")

    parser.add_argument("--prefix", type=str, help="File containing URI prefixes. Two columns [abbrv prefix] separated by whitespace.")
    parser.add_argument("--blacklist", type=str, help="File containing blacklisted URIs. The program does not follow these links.")

    parser.add_argument("--prune", "-p", type=str, choices=PATH_PRUNER_NAMES, default="gle", help="Selects path-prune policy.")
    parser.add_argument("--minimum_score", type=float, default=-1, help="Explanations with scores less or equal to given value are not printed.")

    parser.add_argument("--mem-profile", action="store_true", help="Occassionally log memory usage. Can help with finding memory leaks.")
    args = parser.parse_args()

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(logging.Formatter('%(asctime)s %(levelname)-8s %(message)s', '%Y-%m-%d %H:%M:%S'))
    logging.getLogger('').addHandler(ch)
    logging.getLogger().setLevel(logging.DEBUG)

    args_dict = vars(args)
    for k, v in args_dict.items():
        logging.info("USING {}: {}.".format(k.upper(), v))
    for explanation in explain(**args_dict):
        logging.info(explanation)
