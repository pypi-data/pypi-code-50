from contextlib import contextmanager

from query_diet import context


class NOT_PROVIDED:
    pass


def filter_field_names(field_names):
    return set(name for name in field_names if not name == "id" and not name.endswith("_id"))


def _assert_fitness(analyzer, usage, n1, query_count, assertions):
    assert analyzer.usage.total >= usage, f"[usage] too much query fats ({analyzer.usage.total} < {usage})."
    assert analyzer.n1.total <= n1, f"[n+1] too much query fats ({analyzer.n1.total} > {n1})."
    if query_count is not NOT_PROVIDED:
        assert analyzer.count.queries <= query_count, f"[query count] too much query fats ({analyzer.count.queries} > {query_count})."
    for fn in assertions:
        fn(analyzer)


@contextmanager
def assert_fitness(*, usage=NOT_PROVIDED, n1=NOT_PROVIDED, query_count=NOT_PROVIDED, assertions=NOT_PROVIDED):
    if usage is NOT_PROVIDED:
        usage = context.usage_threshold()
    if n1 is NOT_PROVIDED:
        n1 = context.n1_threshold()
    if assertions is NOT_PROVIDED:
        assertions = []

    with context.tracker.scoped() as tracker:
        try:
            yield
        finally:
            _assert_fitness(tracker.analyze(), usage, n1, query_count, assertions)
