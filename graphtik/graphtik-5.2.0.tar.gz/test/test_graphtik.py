# Copyright 2016, Yahoo Inc.
# Licensed under the terms of the Apache License, Version 2.0. See the LICENSE file associated with the project for terms.

import logging
import math
import os
import re
import sys
import time
import types
from functools import partial
from multiprocessing import Pool, cpu_count
from multiprocessing import dummy as mp_dummy
from multiprocessing import get_context
from operator import add, floordiv, mul, sub
from pprint import pprint
from unittest.mock import MagicMock

import pytest

from graphtik import (
    NO_RESULT,
    AbortedException,
    IncompleteExecutionError,
    abort_run,
    compose,
    evictions_skipped,
    execution_pool,
    get_execution_pool,
    is_marshal_tasks,
    network,
    operation,
    operations_endured,
    operations_reschedullled,
    optional,
    sideffect,
    tasks_marshalled,
    vararg,
)
from graphtik.netop import NetworkOperation
from graphtik.network import Solution
from graphtik.op import Operation

log = logging.getLogger(__name__)


_slow = pytest.mark.slow
_proc = pytest.mark.proc
_thread = pytest.mark.thread
_parallel = pytest.mark.parallel
_marshal = pytest.mark.marshal


@pytest.fixture(
    params=[
        # PARALLEL?, Proc/Thread?, Marshalled?
        (None, None, None),
        pytest.param((1, 0, 0), marks=(_parallel, _thread)),
        pytest.param((1, 0, 1), marks=(_parallel, _thread, _marshal)),
        pytest.param((1, 1, 1), marks=(_parallel, _proc, _marshal, _slow)),
        pytest.param(
            (1, 1, 0),
            marks=(
                _parallel,
                _proc,
                _slow,
                pytest.mark.xfail(reason="ProcessPool non-marshaled may fail."),
            ),
        ),
    ]
)
def exemethod(request):
    """Returns (exemethod, marshal) combinations"""
    parallel, proc_pool, marshal = request.param
    nsharks = None  # number of pool swimmers....

    with tasks_marshalled(marshal):
        if parallel:
            if proc_pool:
                if os.name == "posix":  # Allthough it is the default ...
                    # NOTE: "spawn" DEADLOCKS!.
                    pool = get_context("fork").Pool(nsharks)
                else:
                    pool = Pool(nsharks)
            else:
                pool = mp_dummy.Pool(nsharks)

            with execution_pool(pool), pool:
                yield parallel
        else:
            yield parallel


def scream(*args, **kwargs):
    raise AssertionError(f"Must not have run!\n    args: {args}\n  kwargs: {kwargs}")


def identity(*x):
    return x[0] if len(x) == 1 else x


def filtdict(d, *keys):
    """
    Keep dict items with the given keys

    >>> filtdict({"a": 1, "b": 2}, "b")
    {'b': 2}
    """
    return type(d)(i for i in d.items() if i[0] in keys)


def addall(*a, **kw):
    "Same as a + b + ...."
    return sum(a) + sum(kw.values())


def abspow(a, p):
    c = abs(a) ** p
    return c


def test_solution_finalized():
    sol = Solution(MagicMock(), {})

    sol.finalize()
    with pytest.raises(AssertionError):
        sol.operation_executed(MagicMock(), [])

    sol.finalize()
    with pytest.raises(AssertionError):
        sol.operation_failed(MagicMock(), None)


def test_smoke_test():

    # Sum operation, late-bind compute function
    sum_op1 = operation(name="sum_op1", needs=["a", "b"], provides="sum_ab")(add)

    # sum_op1 is callable
    assert sum_op1(1, 2) == 3

    # Multiply operation, decorate in-place
    @operation(name="mul_op1", needs=["sum_ab", "b"], provides="sum_ab_times_b")
    def mul_op1(a, b):
        return a * b

    # mul_op1 is callable
    assert mul_op1(1, 2) == 2

    # Pow operation
    @operation(
        name="pow_op1", needs="sum_ab", provides=["sum_ab_p1", "sum_ab_p2", "sum_ab_p3"]
    )
    def pow_op1(a, exponent=3):
        return [math.pow(a, y) for y in range(1, exponent + 1)]

    assert pow_op1.compute({"sum_ab": 2}, ["sum_ab_p2"]) == {"sum_ab_p2": 4.0}

    # Partial operation that is bound at a later time
    partial_op = operation(
        name="sum_op2", needs=["sum_ab_p1", "sum_ab_p2"], provides="p1_plus_p2"
    )

    # Bind the partial operation
    sum_op2 = partial_op(add)

    # Sum operation, early-bind compute function
    sum_op_factory = operation(add)

    sum_op3 = sum_op_factory(name="sum_op3", needs=["a", "b"], provides="sum_ab2")

    # sum_op3 is callable
    assert sum_op3(5, 6) == 11

    # compose network
    netop = compose("my network", sum_op1, mul_op1, pow_op1, sum_op2, sum_op3)

    #
    # Running the network
    #

    # get all outputs
    exp = {
        "a": 1,
        "b": 2,
        "p1_plus_p2": 12.0,
        "sum_ab": 3,
        "sum_ab2": 3,
        "sum_ab_p1": 3.0,
        "sum_ab_p2": 9.0,
        "sum_ab_p3": 27.0,
        "sum_ab_times_b": 6,
    }
    assert netop(a=1, b=2) == exp

    # get specific outputs
    exp = {"sum_ab_times_b": 6}
    assert netop.compute({"a": 1, "b": 2}, ["sum_ab_times_b"]) == exp

    # start with inputs already computed
    exp = {"sum_ab_times_b": 2}
    assert netop.compute({"sum_ab": 1, "b": 2}, ["sum_ab_times_b"]) == exp

    with pytest.raises(ValueError, match="Unknown output node"):
        netop.compute({"sum_ab": 1, "b": 2}, "bad_node")
    with pytest.raises(ValueError, match="Unknown output node"):
        netop.compute({"sum_ab": 1, "b": 2}, ["b", "bad_node"])


def test_network_plan_execute():
    def powers_in_range(a, exponent):
        outputs = []
        for y in range(1, exponent + 1):
            p = math.pow(a, y)
            outputs.append(p)
        return outputs

    sum_op1 = operation(name="sum1", provides=["sum_ab"], needs=["a", "b"])(add)
    mul_op1 = operation(name="mul", provides=["sum_ab_times_b"], needs=["sum_ab", "b"])(
        mul
    )
    pow_op1 = operation(
        name="pow",
        needs=["sum_ab", "exponent"],
        provides=["sum_ab_p1", "sum_ab_p2", "sum_ab_p3"],
    )(powers_in_range)
    sum_op2 = operation(
        name="sum2", provides=["p1_plus_p2"], needs=["sum_ab_p1", "sum_ab_p2"]
    )(add)

    net = network.Network(sum_op1, mul_op1, pow_op1, sum_op2)
    net.compile()
    net.compile(net.needs)
    net.compile(net.needs, net.provides)
    net.compile(outputs=net.provides)

    #
    # Running the network
    #

    # get all outputs
    exp = {
        "a": 1,
        "b": 2,
        "exponent": 3,
        "p1_plus_p2": 12.0,
        "sum_ab": 3,
        "sum_ab_p1": 3.0,
        "sum_ab_p2": 9.0,
        "sum_ab_p3": 27.0,
        "sum_ab_times_b": 6,
    }

    inputs = {"a": 1, "b": 2, "exponent": 3}
    outputs = None
    plan = net.compile(outputs=outputs, inputs=inputs.keys())
    sol = plan.execute(inputs)
    assert sol == exp
    sol = plan.execute(inputs, outputs)
    assert sol == exp

    # get specific outputs
    exp = {"sum_ab_times_b": 6}
    outputs = ["sum_ab_times_b"]
    plan = net.compile(outputs=outputs, inputs=list(inputs))
    sol = plan.execute(inputs)
    assert sol == exp
    sol = plan.execute(inputs, outputs)
    assert sol == exp

    # start with inputs already computed
    inputs = {"sum_ab": 1, "b": 2, "exponent": 3}
    exp = {"sum_ab_times_b": 2}
    outputs = ["sum_ab_times_b"]
    plan = net.compile(outputs=outputs, inputs=inputs)
    with pytest.raises(ValueError, match=r"Plan needs more inputs:"):
        sol = plan.execute(named_inputs={"sum_ab": 1})
    sol = plan.execute(inputs)
    assert sol == exp
    sol = plan.execute(inputs, outputs)
    assert sol == exp


def test_network_simple_merge():

    sum_op1 = operation(name="sum_op1", needs=["a", "b"], provides="sum1")(add)
    sum_op2 = operation(name="sum_op2", needs=["a", "b"], provides="sum2")(add)
    sum_op3 = operation(name="sum_op3", needs=["sum1", "c"], provides="sum3")(add)
    net1 = compose("my network 1", sum_op1, sum_op2, sum_op3)

    exp = {"a": 1, "b": 2, "c": 4, "sum1": 3, "sum2": 3, "sum3": 7}
    sol = net1(a=1, b=2, c=4)
    assert sol == exp

    sum_op4 = operation(name="sum_op1", needs=["d", "e"], provides="a")(add)
    sum_op5 = operation(name="sum_op2", needs=["a", "f"], provides="b")(add)

    net2 = compose("my network 2", sum_op4, sum_op5)
    exp = {"a": 3, "b": 7, "d": 1, "e": 2, "f": 4}
    sol = net2(**{"d": 1, "e": 2, "f": 4})
    assert sol == exp

    net3 = compose("merged", net1, net2)
    exp = {
        "a": 3,
        "b": 7,
        "c": 5,
        "d": 1,
        "e": 2,
        "f": 4,
        "sum1": 10,
        "sum2": 10,
        "sum3": 15,
    }
    sol = net3(c=5, d=1, e=2, f=4)
    assert sol == exp

    assert repr(net3).startswith(
        "NetworkOperation('merged', needs=['a', 'b', 'sum1', 'c', 'd', 'e', 'f'], "
        "provides=['sum1', 'sum2', 'sum3', 'a', 'b'], x5 ops"
    )


def test_network_deep_merge():
    sum_op1 = operation(
        name="sum_op1", needs=[vararg("a"), vararg("b")], provides="sum1"
    )(addall)
    sum_op2 = operation(name="sum_op2", needs=[vararg("a"), "b"], provides="sum2")(
        addall
    )
    sum_op3 = operation(name="sum_op3", needs=["sum1", "c"], provides="sum3")(add)
    net1 = compose("my network 1", sum_op1, sum_op2, sum_op3)
    exp = {"a": 1, "b": 2, "c": 4, "sum1": 3, "sum2": 3, "sum3": 7}
    assert net1(a=1, b=2, c=4) == exp
    assert repr(net1).startswith(
        "NetworkOperation('my network 1', needs=[optional('a'), 'b', 'sum1', 'c'], "
        "provides=['sum1', 'sum2', 'sum3'], x3 ops"
    )

    sum_op4 = operation(name="sum_op1", needs=[vararg("a"), "b"], provides="sum1")(
        addall
    )
    sum_op5 = operation(name="sum_op4", needs=["sum1", "b"], provides="sum2")(add)
    net2 = compose("my network 2", sum_op4, sum_op5)
    exp = {"a": 1, "b": 2, "sum1": 3, "sum2": 5}
    assert net2(**{"a": 1, "b": 2}) == exp
    assert repr(net2).startswith(
        "NetworkOperation('my network 2', needs=[optional('a'), 'b', 'sum1'], provides=['sum1', 'sum2'], x2 ops"
    )

    net3 = compose("merged", net1, net2, merge=True)
    exp = {"a": 1, "b": 2, "c": 4, "sum1": 3, "sum2": 5, "sum3": 7}
    assert net3(a=1, b=2, c=4) == exp

    assert repr(net3).startswith(
        "NetworkOperation('merged', needs=[optional('a'), 'b', 'sum1', 'c'], provides=['sum1', 'sum2', 'sum3'], x4 ops"
    )

    ## Reverse ops, change results and `needs` optionality.
    #
    net3 = compose("merged", net2, net1, merge=True)
    exp = {"a": 1, "b": 2, "c": 4, "sum1": 3, "sum2": 3, "sum3": 7}
    assert net3(**{"a": 1, "b": 2, "c": 4}) == exp

    assert repr(net3).startswith(
        "NetworkOperation('merged', needs=[optional('a'), 'b', 'sum1', 'c'], provides=['sum1', 'sum2', 'sum3'], x4 ops"
    )


def test_network_merge_in_doctests():
    graphop = compose(
        "graphop",
        operation(name="mul1", needs=["a", "b"], provides=["ab"])(mul),
        operation(name="sub1", needs=["a", "ab"], provides=["a_minus_ab"])(sub),
        operation(
            name="abspow1", needs=["a_minus_ab"], provides=["abs_a_minus_ab_cubed"]
        )(partial(abspow, p=3)),
    )

    another_graph = compose(
        "another_graph",
        operation(name="mul1", needs=["a", "b"], provides=["ab"])(mul),
        operation(name="mul2", needs=["c", "ab"], provides=["cab"])(mul),
    )
    merged_graph = compose("merged_graph", graphop, another_graph, merge=True)
    assert merged_graph.needs
    assert merged_graph.provides

    assert repr(merged_graph).startswith(
        "NetworkOperation('merged_graph', "
        "needs=['a', 'b', 'ab', 'a_minus_ab', 'c'], "
        "provides=['ab', 'a_minus_ab', 'abs_a_minus_ab_cubed', 'cab'], x4 ops"
    )


def test_aliases(exemethod):
    op = compose(
        "test_net",
        operation(lambda: "A", name="op1", provides="a", aliases={"a": "b"})(),
        operation(lambda x: x * 2, name="op2", needs="b", provides="c")(),
        parallel=exemethod,
    )
    assert op() == {"a": "A", "b": "A", "c": "AA"}


@pytest.fixture
def samplenet():
    # Set up a network such that we don't need to provide a or b d if we only
    # request sum3 as output and if we provide sum2.
    sum_op1 = operation(name="sum_op1", needs=["a", "b"], provides="sum1")(add)
    sum_op2 = operation(name="sum_op2", needs=["c", "d"], provides="sum2")(add)
    sum_op3 = operation(name="sum_op3", needs=["c", "sum2"], provides="sum3")(add)
    return compose("test_net", sum_op1, sum_op2, sum_op3)


def test_node_predicate_based_prune():
    netop = compose(
        "N",
        operation(name="A", needs=["a"], provides=["aa"], node_props={"color": "red"})(
            identity
        ),
        operation(
            name="B", needs=["b"], provides=["bb"], node_props={"color": "green"}
        )(identity),
        operation(name="C", needs=["c"], provides=["cc"])(identity),
        operation(
            name="SUM",
            needs=[optional(i) for i in ("aa", "bb", "cc")],
            provides=["sum"],
        )(addall),
    )
    inp = {"a": 1, "b": 2, "c": 3}
    assert netop(**inp)["sum"] == 6
    assert len(netop.net.graph.nodes) == 11

    pred = lambda n, d: d.get("color", None) != "red"
    assert netop.withset(predicate=pred)(**inp)["sum"] == 5
    assert len(netop.withset(predicate=pred).compile().dag.nodes) == 9

    pred = lambda n, d: "color" not in d
    assert netop.withset(predicate=pred)(**inp)["sum"] == 3
    assert len(netop.withset(predicate=pred).compile().dag.nodes) == 7


def test_input_based_pruning():
    # Tests to make sure we don't need to pass graph inputs if we're provided
    # with data further downstream in the graph as an input.

    sum1 = 2
    sum2 = 5

    # Set up a net such that if sum1 and sum2 are provided directly, we don't
    # need to provide a and b.
    sum_op1 = operation(name="sum_op1", needs=["a", "b"], provides="sum1")(add)
    sum_op2 = operation(name="sum_op2", needs=["a", "b"], provides="sum2")(add)
    sum_op3 = operation(name="sum_op3", needs=["sum1", "sum2"], provides="sum3")(add)
    net = compose("test_net", sum_op1, sum_op2, sum_op3)

    results = net(**{"sum1": sum1, "sum2": sum2})

    # Make sure we got expected result without having to pass a or b.
    assert "sum3" in results
    assert results["sum3"] == add(sum1, sum2)


def test_output_based_pruning(samplenet):
    # Tests to make sure we don't need to pass graph inputs if they're not
    # needed to compute the requested outputs.

    c = 2
    d = 3

    results = samplenet.compute({"a": 0, "b": 0, "c": c, "d": d}, ["sum3"])

    # Make sure we got expected result without having to pass a or b.
    assert "sum3" in results
    assert results["sum3"] == add(c, add(c, d))


def test_deps_pruning_vs_narrowing(samplenet):
    # Tests to make sure we don't need to pass graph inputs if they're not
    # needed to compute the requested outputs or of we're provided with
    # inputs that are further downstream in the graph.

    c = 2
    sum2 = 5

    results = samplenet.compute({"c": c, "sum2": sum2}, ["sum3"])

    # Make sure we got expected result without having to pass a, b, or d.
    assert "sum3" in results
    assert results["sum3"] == add(c, sum2)

    # Compare with both `withset()`.
    net = samplenet.withset(outputs=["sum3"])
    assert net(c=c, sum2=sum2) == results

    # Make sure we got expected result without having to pass a, b, or d.
    assert "sum3" in results
    assert results["sum3"] == add(c, sum2)


def test_pruning_raises_for_bad_output(samplenet):
    # Make sure we get a ValueError during the pruning step if we request an
    # output that doesn't exist.

    # Request two outputs we can compute and one we can't compute.  Assert
    # that this raises a ValueError.
    with pytest.raises(ValueError) as exinfo:
        samplenet.compute({"a": 1, "b": 2, "c": 3, "d": 4}, ["sum1", "sum3", "sum4"])
    assert exinfo.match("sum4")


def test_pruning_not_overrides_given_intermediate(exemethod):
    # Test #25: v1.2.4 overwrites intermediate data when no output asked
    pipeline = compose(
        "pipeline",
        operation(name="not run", needs=["a"], provides=["overridden"])(scream),
        operation(name="op", needs=["overridden", "c"], provides=["asked"])(add),
        parallel=exemethod,
    )

    inputs = {"a": 5, "overridden": 1, "c": 2}
    exp = {"a": 5, "overridden": 1, "c": 2, "asked": 3}
    # v1.2.4.ok
    assert pipeline.compute(inputs, "asked") == filtdict(exp, "asked")
    # FAILs
    # - on v1.2.4 with (overridden, asked): = (5, 7) instead of (1, 3)
    # - on #18(unsatisfied) + #23(ordered-sets) with (overridden, asked) = (5, 7) instead of (1, 3)
    # FIXED on #26
    assert pipeline(**inputs) == exp

    ## Test OVERWRITES
    #
    solution = pipeline.compute(inputs, ["asked"])
    assert solution == filtdict(exp, "asked")
    assert solution.overwrites == {}  # unjust must have been pruned

    solution = pipeline(**inputs)
    assert solution == exp
    assert solution.overwrites == {}  # unjust must have been pruned


def test_pruning_multiouts_not_override_intermediates1(exemethod):
    # Test #25: v.1.2.4 overwrites intermediate data when a previous operation
    # must run for its other outputs (outputs asked or not)
    pipeline = compose(
        "graph",
        operation(name="must run", needs=["a"], provides=["overridden", "calced"])(
            lambda x: (x, 2 * x)
        ),
        operation(name="add", needs=["overridden", "calced"], provides=["asked"])(add),
        parallel=exemethod,
    )

    inp1 = {"a": 5, "overridden": 1}
    inp2 = {"a": 5, "overridden": 1, "c": 2}
    exp = {"a": 5, "overridden": 5, "calced": 10, "asked": 11}
    exp2 = filtdict(exp, "asked")

    # FAILs
    # - on v1.2.4 with (overridden, asked) = (5, 15) instead of (1, 11)
    # - on #18(unsatisfied) + #23(ordered-sets) like v1.2.4.
    # FIXED on #26
    # - on v4.0.0 (overridden, asked) := (5, 11)
    solution = pipeline.compute(inp1)
    assert solution == exp
    assert solution.overwrites == {"overridden": [5, 1]}

    # FAILs
    # - on v1.2.4 with KeyError: 'e',
    # - on #18(unsatisfied) + #23(ordered-sets) with empty result.
    # FIXED on #26
    solution = pipeline.compute(inp2, "asked")
    assert solution == exp2
    assert solution.overwrites == {}

    ## Test OVERWRITES
    #
    solution = pipeline.compute(inp1)
    assert solution == exp
    assert solution.overwrites == {"overridden": [5, 1]}

    # Check plotting Overwrites.
    assert "SkyBlue" in str(solution.plot())

    solution = pipeline.compute(inp1, "asked")
    assert solution.overwrites == {}

    # Check not plotting Overwrites.
    assert "SkyBlue" not in str(solution.plot())


@pytest.mark.xfail(
    sys.version_info < (3, 6),
    reason="PY3.5- have unstable dicts."
    "E.g. https://travis-ci.org/ankostis/graphtik/jobs/595841023",
)
def test_pruning_multiouts_not_override_intermediates2(exemethod):
    # Test #25: v.1.2.4 overrides intermediate data when a previous operation
    # must run for its other outputs (outputs asked or not)
    # SPURIOUS FAILS in < PY3.6 due to unordered dicts,
    # eg https://travis-ci.org/ankostis/graphtik/jobs/594813119
    pipeline = compose(
        "pipeline",
        operation(name="must run", needs=["a"], provides=["overridden", "e"])(
            lambda x: (x, 2 * x)
        ),
        operation(name="op1", needs=["overridden", "c"], provides=["d"])(add),
        operation(name="op2", needs=["d", "e"], provides=["asked"])(mul),
        parallel=exemethod,
    )

    inputs = {"a": 5, "overridden": 1, "c": 2}
    exp = {"a": 5, "overridden": 5, "c": 2, "d": 3, "e": 10, "asked": 30}
    # FAILs
    # - on v1.2.4 with (overridden, asked) = (5, 70) instead of (1, 30)
    # - on #18(unsatisfied) + #23(ordered-sets) like v1.2.4.
    # FIXED on #26
    # - on v4.0.0 (overridden, asked) := (5, 30)
    assert pipeline(**inputs) == exp
    # FAILs
    # - on v1.2.4 with KeyError: 'e',
    # - on #18(unsatisfied) + #23(ordered-sets) with empty result.
    assert pipeline.compute(inputs, "asked") == filtdict(exp, "asked")
    # FIXED on #26

    ## Test OVERWRITES
    #
    solution = pipeline.compute(inputs)
    assert solution == exp
    assert solution.overwrites == {"overridden": [5, 1]}
    # No overwrites when evicted.
    #
    solution = pipeline.compute(inputs, "asked")
    assert solution == filtdict(exp, "asked")
    assert solution.overwrites == {}
    # ... but overrites collected if asked.
    #
    solution = pipeline.compute(inputs, ["asked", "overridden"])
    assert solution == filtdict(exp, "asked", "overridden")
    assert solution.overwrites == {"overridden": [5, 1]}


def test_pruning_with_given_intermediate_and_asked_out(exemethod):
    # Test #24: v1.2.4 does not prune before given intermediate data when
    # outputs not asked, but does so when output asked.
    pipeline = compose(
        "pipeline",
        operation(name="unjustly pruned", needs=["given-1"], provides=["a"])(identity),
        operation(name="shortcut-ed", needs=["a", "b"], provides=["given-2"])(add),
        operation(name="good_op", needs=["a", "given-2"], provides=["asked"])(add),
        parallel=exemethod,
    )

    inps = {"given-1": 5, "b": 2, "given-2": 2}
    exp = {"given-1": 5, "given-2": 2, "a": 5, "b": 2, "asked": 7}

    # v1.2.4 is ok
    assert pipeline(**inps) == exp
    # FAILS
    # - on v1.2.4 with KeyError: 'a',
    # - on #18 (unsatisfied) with no result.
    # FIXED on #18+#26 (new dag solver).
    assert pipeline.compute(inps, "asked") == filtdict(exp, "asked")

    ## Test OVERWRITES
    #
    solution = pipeline.compute(inps)
    assert solution == exp
    assert solution.overwrites == {}

    solution = pipeline.compute(inps, "asked")
    assert solution == filtdict(exp, "asked")
    assert solution.overwrites == {}


def test_same_outputs_operations_order():
    # Test operations providing the same output ordered as given.
    op1 = operation(name="add", needs=["a", "b"], provides=["ab"])(add)
    op2 = operation(name="sub", needs=["a", "b"], provides=["ab"])(sub)
    addsub = compose("add_sub", op1, op2)
    subadd = compose("sub_add", op2, op1)

    inp = {"a": 3, "b": 1}
    # assert addsub(**inp) == {"a": 3, "b": 1, "ab": 4}
    # assert addsub.compute(inp, "ab") == {"ab": 4}
    # assert subadd(**inp) == {"a": 3, "b": 1, "ab": 2}
    # assert subadd.compute(inp, "ab") == {"ab": 2}

    # ## Check it does not duplicate evictions
    # assert len(subadd.last_plan.steps) == 4

    ## Add another step to test evictions
    #
    op3 = operation(name="pipe", needs=["ab"], provides=["AB"])(identity)
    addsub = compose("add_sub", op1, op2, op3)
    subadd = compose("sub_add", op2, op1, op3)

    # Notice that `ab` assumed as 2 for `AB` but results in `2`
    solution = addsub.compute(inp)
    assert solution == {"a": 3, "b": 1, "ab": 2, "AB": 4}
    assert solution.overwrites == {"ab": [2, 4]}
    solution = addsub.compute(inp, "AB")
    assert solution == {"AB": 4}
    assert solution.overwrites == {}

    solution = subadd.compute(inp)
    assert solution == {"a": 3, "b": 1, "ab": 4, "AB": 2}
    assert solution.overwrites == {"ab": [4, 2]}
    solution = subadd.compute(inp, "AB")
    assert solution == {"AB": 2}
    assert solution.overwrites == {}

    assert subadd.compute(inp, "AB") == {"AB": 2}
    assert len(subadd.last_plan.steps) == 6


def test_same_inputs_evictions():
    # Test operations providing the same output ordered as given.
    pipeline = compose(
        "add_sub",
        operation(name="x2", needs=["a", "a"], provides=["2a"])(add),
        operation(name="pipe", needs=["2a"], provides=["@S"])(identity),
    )

    inp = {"a": 3}
    assert pipeline(**inp) == {"a": 3, "2a": 6, "@S": 6}
    assert pipeline.compute(inp, "@S") == {"@S": 6}
    ## Check it does not duplicate evictions
    assert len(pipeline.last_plan.steps) == 4


def test_unsatisfied_operations(exemethod):
    # Test that operations with partial inputs are culled and not failing.
    pipeline = compose(
        "pipeline",
        operation(name="add", needs=["a", "b1"], provides=["a+b1"])(add),
        operation(name="sub", needs=["a", "b2"], provides=["a-b2"])(sub),
        parallel=exemethod,
    )

    exp = {"a": 10, "b1": 2, "a+b1": 12}
    assert pipeline(**{"a": 10, "b1": 2}) == exp
    assert pipeline.compute({"a": 10, "b1": 2}, ["a+b1"]) == filtdict(exp, "a+b1")
    assert pipeline.withset(outputs=["a+b1"])(**{"a": 10, "b1": 2}) == filtdict(
        exp, "a+b1"
    )

    exp = {"a": 10, "b2": 2, "a-b2": 8}
    assert pipeline(**{"a": 10, "b2": 2}) == exp
    assert pipeline.compute({"a": 10, "b2": 2}, ["a-b2"]) == filtdict(exp, "a-b2")


def test_unsatisfied_operations_same_out(exemethod):
    # Test unsatisfied pairs of operations providing the same output.
    pipeline = compose(
        "pipeline",
        operation(name="mul", needs=["a", "b1"], provides=["ab"])(mul),
        operation(name="div", needs=["a", "b2"], provides=["ab"])(floordiv),
        operation(name="add", needs=["ab", "c"], provides=["ab_plus_c"])(add),
        parallel=exemethod,
    )

    #  Parallel FAIL! in #26
    exp = {"a": 10, "b1": 2, "c": 1, "ab": 20, "ab_plus_c": 21}
    assert pipeline(**{"a": 10, "b1": 2, "c": 1}) == exp
    assert pipeline.compute({"a": 10, "b1": 2, "c": 1}, ["ab_plus_c"]) == filtdict(
        exp, "ab_plus_c"
    )

    #  Parallel FAIL! in #26
    exp = {"a": 10, "b2": 2, "c": 1, "ab": 5, "ab_plus_c": 6}
    assert pipeline(**{"a": 10, "b2": 2, "c": 1}) == exp
    assert pipeline.compute({"a": 10, "b2": 2, "c": 1}, ["ab_plus_c"]) == filtdict(
        exp, "ab_plus_c"
    )


def test_optional():
    # Test that optional() needs work as expected.

    # Function to add two values plus an optional third value.
    def addplusplus(a, b, c=0):
        return a + b + c

    sum_op = operation(name="sum_op1", needs=["a", "b", optional("c")], provides="sum")(
        addplusplus
    )

    net = compose("test_net", sum_op)

    # Make sure output with optional arg is as expected.
    named_inputs = {"a": 4, "b": 3, "c": 2}
    results = net(**named_inputs)
    assert "sum" in results
    assert results["sum"] == sum(named_inputs.values())

    # Make sure output without optional arg is as expected.
    named_inputs = {"a": 4, "b": 3}
    results = net(**named_inputs)
    assert "sum" in results
    assert results["sum"] == sum(named_inputs.values())


@pytest.mark.parametrize("reverse", [0, 1])
def test_narrow_and_optionality(reverse):
    op1 = operation(name="op1", needs=[optional("a"), optional("bb")], provides="sum1")(
        addall
    )
    op2 = operation(name="op2", needs=["a", optional("bb")], provides="sum2")(addall)
    ops = [op1, op2]
    provides = "'sum1', 'sum2'"
    if reverse:
        ops = list(reversed(ops))
        provides = "'sum2', 'sum1'"
    netop_str = f"NetworkOperation('t', needs=['a', optional('bb')], provides=[{provides}], x2 ops"

    netop = compose("t", *ops)
    assert repr(netop).startswith(netop_str)

    ## IO & predicate do not affect network, but solution.

    ## Compose with `inputs`
    #
    netop = compose("t", *ops)
    assert repr(netop).startswith(netop_str)
    assert repr(netop.compile("a")).startswith(
        f"ExecutionPlan(needs=['a'], provides=[{provides}], x2 steps:"
    )
    #
    netop = compose("t", *ops)
    assert repr(netop).startswith(netop_str)
    assert repr(netop.compile(["bb"])).startswith(
        "ExecutionPlan(needs=[optional('bb')], provides=['sum1'], x1 steps:"
    )

    ## Narrow by `provides`
    #
    netop = compose("t", *ops, outputs="sum1")
    assert repr(netop).startswith(netop_str)
    assert repr(netop.compile("bb")).startswith(
        "ExecutionPlan(needs=[optional('bb')], provides=['sum1'], x3 steps:"
    )
    assert repr(netop.compile("bb")) == repr(netop.compute({"bb": 1}).plan)

    netop = compose("t", *ops, outputs=["sum2"])
    assert repr(netop).startswith(netop_str)
    assert not netop.compile("bb").steps
    assert len(netop.compile("a").steps) == 3
    assert repr(netop.compile("a")).startswith(
        "ExecutionPlan(needs=['a'], provides=['sum2'], x3 steps:"
    )

    ## Narrow by BOTH
    #
    netop = compose("t", *ops, outputs=["sum1"])
    assert repr(netop.compile(inputs="a")).startswith(
        "ExecutionPlan(needs=[optional('a')], provides=['sum1'], x3 steps:"
    )

    netop = compose("t", *ops, outputs=["sum2"])
    with pytest.raises(ValueError, match="Unsolvable graph:"):
        netop.compute({"bb": 11})


# Function without return value.
def _box_extend(box, *args):
    box.extend([1, 2])


def _box_increment(box):
    for i in range(len(box)):
        box[i] += 1


@pytest.fixture(params=[0, 1])
def netop_sideffect1(request) -> NetworkOperation:
    ops = [
        operation(
            name="extend", needs=["box", sideffect("a")], provides=[sideffect("b")]
        )(_box_extend),
        operation(
            name="increment", needs=["box", sideffect("b")], provides=sideffect("c")
        )(_box_increment),
    ]
    if request.param:
        ops = reversed(ops)
    # Designate `a`, `b` as sideffect inp/out arguments.
    graph = compose("sideffect1", *ops)

    return graph


def test_sideffect_no_real_data(exemethod, netop_sideffect1: NetworkOperation):
    sidefx_fail = is_marshal_tasks() and not isinstance(
        get_execution_pool(), types.FunctionType  # mp_dummy.Pool
    )

    graph = netop_sideffect1.withset(parallel=exemethod)
    inp = {"box": [0], "a": True}

    ## Normal data must not match sideffects.
    #
    with pytest.raises(ValueError, match="Unknown output node"):
        graph.compute(inp, ["a"])
    with pytest.raises(ValueError, match="Unknown output node"):
        graph.compute(inp, ["b"])

    ## Cannot compile due to missing inputs/outputs
    #
    with pytest.raises(ValueError, match="Unsolvable graph"):
        assert graph(**inp) == inp
    with pytest.raises(ValueError, match="Unsolvable graph"):
        assert graph.compute(inp)

    with pytest.raises(ValueError, match="Unsolvable graph"):
        graph.compute(inp, ["box", sideffect("b")])

    with pytest.raises(ValueError, match="Unsolvable graph"):
        # Cannot run, since no sideffect inputs given.
        graph.compute(inp)

    box_orig = [0]

    ## OK INPUT SIDEFFECTS
    #
    # ok, no asked out
    sol = graph.compute({"box": [0], sideffect("a"): True})
    assert sol == {"box": box_orig if sidefx_fail else [1, 2, 3], sideffect("a"): True}
    #
    # bad, not asked the out-sideffect
    with pytest.raises(ValueError, match="Unsolvable graph"):
        graph.compute({"box": [0], sideffect("a"): True}, "box")
    #
    # ok, asked the 1st out-sideffect
    sol = graph.compute({"box": [0], sideffect("a"): True}, ["box", sideffect("b")])
    assert sol == {"box": box_orig if sidefx_fail else [0, 1, 2]}
    #
    # ok, asked the 2nd out-sideffect
    sol = graph.compute({"box": [0], sideffect("a"): True}, ["box", sideffect("c")])
    assert sol == {"box": box_orig if sidefx_fail else [1, 2, 3]}


@pytest.mark.parametrize("reverse", [0, 1])
def test_sideffect_real_input(reverse, exemethod):
    sidefx_fail = is_marshal_tasks() and not isinstance(
        get_execution_pool(), types.FunctionType  # mp_dummy.Pool
    )

    ops = [
        operation(name="extend", needs=["box", "a"], provides=[sideffect("b")])(
            _box_extend
        ),
        operation(name="increment", needs=["box", sideffect("b")], provides="c")(
            _box_increment
        ),
    ]
    if reverse:
        ops = reversed(ops)
    # Designate `a`, `b` as sideffect inp/out arguments.
    graph = compose("mygraph", *ops, parallel=exemethod)

    box_orig = [0]
    assert graph(**{"box": [0], "a": True}) == {
        "a": True,
        "box": box_orig if sidefx_fail else [1, 2, 3],
        "c": None,
    }
    assert graph.compute({"box": [0], "a": True}, ["box", "c"]) == {
        "box": box_orig if sidefx_fail else [1, 2, 3],
        "c": None,
    }


def test_sideffect_steps(exemethod, netop_sideffect1: NetworkOperation):
    sidefx_fail = is_marshal_tasks() and not isinstance(
        get_execution_pool(), types.FunctionType  # mp_dummy.Pool
    )

    netop = netop_sideffect1.withset(parallel=exemethod)
    box_orig = [0]
    sol = netop.compute({"box": [0], sideffect("a"): True}, ["box", sideffect("c")])
    assert sol == {"box": box_orig if sidefx_fail else [1, 2, 3]}
    assert len(netop.last_plan.steps) == 4

    ## Check sideffect links plotted as blue
    #  (assumes color used only for this!).
    dot = netop.net.plot()
    assert "blue" in str(dot)


def test_sideffect_NO_RESULT(caplog):
    sfx = sideffect("b")
    op = operation(lambda: NO_RESULT, provides=sfx)()
    netop = compose("t", op)
    sol = netop.compute({}, outputs=sfx)
    assert sol == {}
    assert op in sol.executed

    ## If NO_RESULT were not translated,
    #  a warning of unknown out might have emerged.
    caplog.clear()
    netop = compose("t", operation(lambda: 1, provides=sfx)())
    netop.compute({}, outputs=sfx)
    for record in caplog.records:
        if record.levelname == "WARNING":
            assert "Ignoring result(1) because no `provides`" in record.message

    caplog.clear()
    netop = compose("t", operation(lambda: NO_RESULT, provides=sfx)())
    netop.compute({}, outputs=sfx)
    for record in caplog.records:
        assert record.levelname != "WARNING"


@pytest.mark.xfail(
    sys.version_info < (3, 6),
    reason="PY3.5- have unstable dicts."
    "E.g. https://travis-ci.org/ankostis/graphtik/jobs/595793872",
)
def test_optional_per_function_with_same_output(exemethod):
    # Test that the same need can be both optional and not on different operations.
    #
    ## ATTENTION, the selected function is NOT the one with more inputs
    # but the 1st satisfiable function added in the network.

    add_op = operation(name="add", needs=["a", "b"], provides="a+-b")(add)
    sub_op_optional = operation(
        name="sub_opt", needs=["a", optional("b")], provides="a+-b"
    )(lambda a, b=10: a - b)

    # Normal order
    #
    pipeline = compose("partial_optionals", add_op, sub_op_optional, parallel=exemethod)
    #
    named_inputs = {"a": 1, "b": 2}
    assert pipeline(**named_inputs) == {"a": 1, "a+-b": -1, "b": 2}
    assert pipeline.compute(named_inputs, ["a+-b"]) == {"a+-b": -1}
    #
    named_inputs = {"a": 1}
    assert pipeline.compute(named_inputs) == {"a": 1, "a+-b": -9}
    assert pipeline.compute(named_inputs, ["a+-b"]) == {"a+-b": -9}

    # Inverse op order
    #
    pipeline = compose("partial_optionals", sub_op_optional, add_op, parallel=exemethod)
    #
    named_inputs = {"a": 1, "b": 2}
    assert pipeline(**named_inputs) == {"a": 1, "a+-b": 3, "b": 2}
    assert pipeline.compute(named_inputs, ["a+-b"]) == {"a+-b": 3}
    #
    named_inputs = {"a": 1}
    assert pipeline(**named_inputs) == {"a": 1, "a+-b": -9}
    assert pipeline.compute(named_inputs, ["a+-b"]) == {"a+-b": -9}


def test_evicted_optional():
    # Test that _EvictInstructions included for optionals do not raise
    # exceptions when the corresponding input is not provided.

    # Function to add two values plus an optional third value.
    def addplusplus(a, b, c=0):
        return a + b + c

    # Here, a _EvictInstruction will be inserted for the optional need 'c'.
    sum_op1 = operation(
        name="sum_op1", needs=["a", "b", optional("c")], provides="sum1"
    )(addplusplus)
    sum_op2 = operation(name="sum_op2", needs=["sum1", "sum1"], provides="sum2")(add)
    net = compose("test_net", sum_op1, sum_op2)

    # _EvictInstructions are used only when a subset of outputs are requested.
    results = net.compute({"a": 4, "b": 3}, ["sum2"])
    assert "sum2" in results


def test_evict_instructions_vary_with_inputs():
    # Check #21: _EvictInstructions positions vary when inputs change.
    def count_evictions(steps):
        return sum(isinstance(n, network._EvictInstruction) for n in steps)

    pipeline = compose(
        "pipeline",
        operation(name="a free without b", needs=["a"], provides=["aa"])(identity),
        operation(name="satisfiable", needs=["a", "b"], provides=["ab"])(add),
        operation(name="optional ab", needs=["aa", optional("ab")], provides=["asked"])(
            lambda a, ab=10: a + ab
        ),
    )

    inp = {"a": 2, "b": 3}
    exp = inp.copy()
    exp.update({"aa": 2, "ab": 5, "asked": 7})
    res = pipeline(**inp)
    assert res == exp  # ok
    steps11 = pipeline.net.compile(inp).steps
    res = pipeline.compute(inp, ["asked"])
    assert res == filtdict(exp, "asked")  # ok
    steps12 = pipeline.net.compile(inp, ["asked"]).steps

    inp = {"a": 2}
    exp = inp.copy()
    exp.update({"aa": 2, "asked": 12})
    res = pipeline(**inp)
    assert res == exp  # ok
    steps21 = pipeline.net.compile(inp).steps
    res = pipeline.compute(inp, ["asked"])
    assert res == filtdict(exp, "asked")  # ok
    steps22 = pipeline.net.compile(inp, ["asked"]).steps

    # When no outs, no evict-instructions.
    assert steps11 != steps12
    assert count_evictions(steps11) == 0
    assert steps21 != steps22
    assert count_evictions(steps21) == 0

    # Check steps vary with inputs
    #
    # FAILs in v1.2.4 + #18, PASS in #26
    assert steps11 != steps21

    # Check evicts vary with inputs
    #
    # FAILs in v1.2.4 + #18, PASS in #26
    assert count_evictions(steps12) != count_evictions(steps22)


def test_skip_eviction_flag():
    graph = compose(
        "graph",
        operation(name="add1", needs=["a", "b"], provides=["ab"])(add),
        operation(name="add2", needs=["a", "ab"], provides=["aab"])(add),
    )
    with evictions_skipped(True):
        exp = {"a": 1, "b": 3, "ab": 4, "aab": 5}
        assert graph.compute({"a": 1, "b": 3}, "aab") == exp


@pytest.mark.parametrize(
    "endurance, endured", [(None, True), (True, None), (False, True), (1, 1)]
)
def test_execution_endurance(exemethod, endurance, endured):
    with operations_endured(endurance):
        opb = operation(
            scream, needs=["a", "b"], provides=["a+b", "c"], endured=endured
        )
        scream1 = opb(name="scream1")
        scream2 = opb(name="scream2")
        add1 = operation(name="add1", needs=["a", "b"], provides=["a+b"])(add)
        add2 = operation(name="add2", needs=["a+b", "b"], provides=["a+2b"])(add)
        canceled = operation(name="canceled", needs=["c"], provides="cc")(identity)
        graph = compose(
            "graph", scream1, add1, scream2, add2, canceled, parallel=exemethod
        )

        inp = {"a": 1, "b": 2}
        sol = graph(**inp)
        assert sol.is_failed(scream1) and sol.is_failed(scream2)
        assert "Must not have run!" in str(sol.executed[scream1])
        assert sol == {"a+b": 3, "a+2b": 5, **inp}
        with pytest.raises(IncompleteExecutionError, match="x2 failures"):
            assert sol.scream_if_incomplete()

        sol = graph.withset(outputs="a+2b")(**inp)
        assert sol.is_failed(scream1) and sol.is_failed(scream2)
        assert "Must not have run!" in str(sol.executed[scream1])
        assert sol == {"a+2b": 5}

        # SILENTLY failing asked outputs
        sol = graph.compute(inp, outputs=["a+2b", "cc"])
        assert sol == {"a+2b": 5}

        # Check plotting Fail & Cancel.
        #
        dot = str(sol.plot())
        assert "LightCoral" in dot  # failed
        assert "Grey" in dot  # Canceled


@pytest.mark.parametrize(
    "resched, rescheduled", [(None, True), (True, None), (None, True), (1, 1)]
)
def test_rescheduling(exemethod, resched, rescheduled):
    canc = operation(lambda: None, name="canc", needs=["b"], provides="cc")()
    op = compose(
        "netop",
        operation(lambda: [1], name="op1", provides=["a", "b"], rescheduled=1)(),
        canc,
        operation(lambda: NO_RESULT, name="op2", provides=["c"], rescheduled=1)(),
        operation(
            lambda *args: sum(args),
            name="op3",
            needs=["a", optional("b"), optional("c")],
            provides=["d"],
        )(),
        parallel=exemethod,
    )
    sol = op()
    assert sol == {"a": 1, "d": 1}
    assert list(sol.canceled) == [canc]
    dot = str(sol.plot())
    assert "Grey" in dot  # Canceled
    assert "penwidth=4" in dot  # Rescheduled
    with pytest.raises(IncompleteExecutionError, match="x2 partial-ops"):
        assert sol.scream_if_incomplete()

    ## Check if modified state fails the 2nd time.
    assert op() == {"a": 1, "d": 1}


def test_rescheduling_NO_RESULT(exemethod):
    partial = operation(lambda: NO_RESULT, name="op1", provides=["a"], rescheduled=1)()
    canc = operation(lambda: None, name="canc", needs="a", provides="b")()
    op = compose("netop", partial, canc, parallel=exemethod)
    sol = op()
    assert canc in sol.canceled
    assert partial in sol.executed
    with pytest.raises(IncompleteExecutionError, match="x1 partial-ops"):
        assert sol.scream_if_incomplete()


@pytest.mark.xfail(reason="Spurious copied-reversed graphs, with dubious cause....")
def test_multithreading_plan_execution():
    # Compose the mul, sub, and abspow operations into a computation graph.
    # From Huygn's test-code given in yahoo/graphkit#31
    graph = compose(
        "graph",
        operation(name="mul1", needs=["a", "b"], provides=["ab"])(mul),
        operation(name="sub1", needs=["a", "ab"], provides=["a_minus_ab"])(sub),
        operation(
            name="abspow1", needs=["a_minus_ab"], provides=["abs_a_minus_ab_cubed"]
        )(partial(abspow, p=3)),
    )

    with mp_dummy.Pool(int(2 * cpu_count())) as pool, execution_pool(pool):
        pool.map(
            # lambda i: graph.withset(name='graph').compute(
            lambda i: graph.compute(
                {"a": 2, "b": 5}, ["a_minus_ab", "abs_a_minus_ab_cubed"]
            ),
            range(300),
        )


@pytest.mark.slow
def test_parallel_execution(exemethod):
    if not exemethod:
        return

    delay = 0.5

    def fn(x):
        time.sleep(delay)
        print("fn %s" % (time.time() - t0))
        return 1 + x

    def fn2(a, b):
        time.sleep(delay)
        print("fn2 %s" % (time.time() - t0))
        return a + b

    def fn3(z, k=1):
        time.sleep(delay)
        print("fn3 %s" % (time.time() - t0))
        return z + k

    pipeline = compose(
        "l",
        # the following should execute in parallel under threaded execution mode
        operation(name="a", needs="x", provides="ao")(fn),
        operation(name="b", needs="x", provides="bo")(fn),
        # this should execute after a and b have finished
        operation(name="c", needs=["ao", "bo"], provides="co")(fn2),
        operation(name="d", needs=["ao", optional("k")], provides="do")(fn3),
        operation(name="e", needs=["ao", "bo"], provides="eo")(fn2),
        operation(name="f", needs="eo", provides="fo")(fn),
        operation(name="g", needs="fo", provides="go")(fn),
        merge=True,
    )

    t0 = time.time()
    result_threaded = pipeline.withset(parallel=True).compute(
        {"x": 10}, ["co", "go", "do"]
    )
    # print("threaded result")
    # print(result_threaded)

    t0 = time.time()
    pipeline = pipeline.withset(parallel=False)
    result_sequential = pipeline.compute({"x": 10}, ["co", "go", "do"])
    # print("sequential result")
    # print(result_sequential)

    # make sure results are the same using either method
    assert result_sequential == result_threaded


@pytest.mark.slow
@pytest.mark.xfail(reason="Spurious copied-reversed graphs, with dubious cause....")
def test_multi_threading_computes():
    import random

    def op_a(a, b):
        time.sleep(random.random() * 0.02)
        return a + b

    def op_b(c, b):
        time.sleep(random.random() * 0.02)
        return c + b

    def op_c(a, b):
        time.sleep(random.random() * 0.02)
        return a * b

    pipeline = compose(
        "pipeline",
        operation(name="op_a", needs=["a", "b"], provides="c")(op_a),
        operation(name="op_b", needs=["c", "b"], provides="d")(op_b),
        operation(name="op_c", needs=["a", "b"], provides="e")(op_c),
        merge=True,
    )

    def infer(i):
        # data = open("616039-bradpitt.jpg").read()
        outputs = ["c", "d", "e"]
        results = pipeline.compute({"a": 1, "b": 2}, outputs)
        assert tuple(sorted(results.keys())) == tuple(sorted(outputs)), (
            outputs,
            results,
        )
        return results

    N = 33
    for i in range(13, 61):
        with mp_dummy.Pool(i) as pool:
            pool.map(infer, range(N))


@pytest.mark.parametrize("bools", range(4))
def test_compose_another_network(exemethod, bools):
    # Code from `compose.rst` examples
    if not exemethod:
        return

    parallel1 = bools >> 0 & 1
    parallel2 = bools >> 1 & 1

    graphop = compose(
        "graphop",
        operation(name="mul1", needs=["a", "b"], provides=["ab"])(mul),
        operation(name="sub1", needs=["a", "ab"], provides=["a_minus_ab"])(sub),
        operation(
            name="abspow1", needs=["a_minus_ab"], provides=["abs_a_minus_ab_cubed"]
        )(partial(abspow, p=3)),
        parallel=parallel1,
    )

    assert graphop(a_minus_ab=-8) == {"a_minus_ab": -8, "abs_a_minus_ab_cubed": 512}

    bigger_graph = compose(
        "bigger_graph",
        graphop,
        operation(
            name="sub2", needs=["a_minus_ab", "c"], provides="a_minus_ab_minus_c"
        )(sub),
        parallel=parallel2,
    )

    sol = bigger_graph.compute({"a": 2, "b": 5, "c": 5}, ["a_minus_ab_minus_c"])
    assert sol == {"a_minus_ab_minus_c": -13}


def test_abort(exemethod):
    pipeline = compose(
        "pipeline",
        operation(name="A", needs=["a"], provides=["b"])(identity),
        operation(name="B", needs=["b"], provides=["c"])(lambda x: abort_run()),
        operation(name="C", needs=["c"], provides=["d"])(identity),
        parallel=exemethod,
    )
    with pytest.raises(AbortedException) as exinfo:
        pipeline(a=1)

    exp = {"a": 1, "b": 1, "c": None}
    solution = exinfo.value.args[0]
    assert solution == exp
    assert exinfo.value.jetsam["solution"] == exp
    executed = {op.name: val for op, val in solution.executed.items()}
    assert executed == {"A": None, "B": None}

    pipeline = compose(
        "pipeline",
        operation(name="A", needs=["a"], provides=["b"])(identity),
        parallel=exemethod,
    )
    assert pipeline.compute({"a": 1}) == {"a": 1, "b": 1}
