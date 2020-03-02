from __future__ import annotations
from typing import Any, Dict, Optional

import copy
import multiprocessing as mp
import networkx as nx
import queue
import threading

from .actions import ActionSignal

__all__ = ["Workflow"]


class Workflow:
    def __init__(self, *tasks: materia.Task) -> None:
        self.tasks = copy.deepcopy(tasks)
        self.links = {}
        for i, t in enumerate(self.tasks):
            reqs, named_reqs = t.requirements
            self.links[i] = [(None, self.tasks.index(p)) for p in reqs] + [
                (k, self.tasks.index(p)) for k, p in named_reqs.items()
            ]

    def run(
        self, num_consumers: Optional[int] = 1, thread: Optional[bool] = True
    ) -> Dict[int, Any]:
        if thread:
            tasks = list(self.tasks)
            links = self.links

            # NOTE: holds nodes corresponding to tasks waiting to be run by a process
            task_queue = queue.Queue()
            # NOTE: record task outputs for handler checking and passing to successor tasks
            results = {}
            # NOTE: lookup table to track which tasks have been completed
            done = {node: False for node in range(len(tasks))}
            # NOTE: hold nodes corresponding to tasks waiting to be recognized as done by the producer
            done_queue = queue.Queue()
            # NOTE: holds nodes corresponding to tasks currently being held by a consumer
            tracker = []
            quit_producer = False

            producer_kwargs = {
                "tasks": tasks,
                "links": links,
                "task_queue": task_queue,
                "done": done,
                "done_queue": done_queue,
                "tracker": tracker,
                "quit_producer": quit_producer,
            }
            producer = threading.Thread(target=_produce, kwargs=producer_kwargs)

            consumer_kwargs = {
                "tasks": tasks,
                "links": links,
                "task_queue": task_queue,
                "results": results,
                "done_queue": done_queue,
                "quit_producer": quit_producer,
            }
            consumers = tuple(
                threading.Thread(target=_consume, kwargs=consumer_kwargs, daemon=True)
                for _ in range(num_consumers)
            )
        else:
            # NOTE: for freeze support on Windows - does nothing if not in frozen application or if not on Windows
            mp.freeze_support()
            m = mp.Manager()
            tasks = m.list(self.tasks)
            links = m.dict(self.links)

            task_queue = (
                m.Queue()
            )  # holds nodes corresponding to tasks waiting to be run by a process
            results = (
                m.dict()
            )  # record task outputs for handler checking and passing to successor tasks
            done = m.dict(
                {node: False for node in range(len(tasks))}
            )  # lookup table to track which tasks have been completed
            done_queue = (
                m.Queue()
            )  # hold nodes corresponding to tasks waiting to be recognized as done by the producer
            tracker = (
                m.list()
            )  # holds nodes corresponding to tasks currently being held by a consumer
            quit_producer = mp.Value("i", 0)

            producer_kwargs = {
                "tasks": tasks,
                "links": links,
                "task_queue": task_queue,
                "done": done,
                "done_queue": done_queue,
                "tracker": tracker,
                "quit_producer": quit_producer,
            }
            producer = mp.Process(target=_produce, kwargs=producer_kwargs)

            # start consumers
            consumer_kwargs = {
                "tasks": tasks,
                "links": links,
                "task_queue": task_queue,
                "results": results,
                "done_queue": done_queue,
                "quit_producer": quit_producer,
            }
            consumers = tuple(
                mp.Process(target=_consume, kwargs=consumer_kwargs, daemon=True)
                for _ in range(num_consumers)
            )

        # start producer
        producer.start()

        # start consumers
        for c in consumers:
            c.start()

        # synchronize - wait until producer is done (i.e. all tasks are done)
        producer.join()

        # signal consumers to finish
        for _ in range(num_consumers):
            task_queue.put(None)

        return dict(results)


def _produce(tasks, links, task_queue, done, done_queue, tracker, quit_producer):
    _queue_tasks(
        tasks=tasks, links=links, task_queue=task_queue, done=done, tracker=tracker
    )
    while not (all(done.values()) or quit_producer):
        try:
            node, actions = done_queue.get(block=False)
        except queue.Empty:
            continue

        # run rest of loop only if a job was marked as done

        # NOTE: nothing bad can happen in between the try block and now,
        # since only _queue_tasks cares about done_queue, done, or tracker,
        # and _queue_tasks cannot possibly be running here since there is
        # only one producer process

        done[node] = True
        for action in actions:
            action.run(node=node, tasks=tasks, links=links, done=done)

        tracker.remove(node)
        _queue_tasks(
            tasks=tasks, links=links, task_queue=task_queue, done=done, tracker=tracker
        )


def _consume(tasks, links, task_queue, results, done_queue, quit_producer):
    while True:
        try:
            try:
                node = task_queue.get()
            except queue.Empty:
                continue

            # NOTE: node = None signals consumer to stop
            if node is None:
                break

            # NOTE: this is safe because the node assigned to a task never changes while the workflow runs
            task = tasks[node]
            # NOTE: this is safe because 1.) the dependencies of each task can only be changed by tasks which precede it, i.e. by the time a task is running, no actions can alter its dependencies, and 2.) only one consumer will write to results[node] at a time because only one consumer is running a particular task at a time
            result = task.run(
                **{k: results[v] for k, v in links[node] if k is not None}
            )
            try:
                for h in task.handlers:
                    h.run(result=result, task=task)

                results[node] = result
                actions = []
            except ActionSignal as a:
                results[node] = a.result
                actions = a.actions

            done_queue.put((node, actions))
        except Exception as e:
            quit_producer = 1
            raise e


# _PRODUCE HELPER FUNCTIONS


def _queue_tasks(tasks, links, task_queue, done, tracker):
    dag = _build_dag(tasks=tasks, links=links)
    for node in dag.nodes:
        if _task_is_ready(node=node, done=done, dag=dag, tracker=tracker):
            tracker.append(node)
            task_queue.put(node)


def _build_dag(tasks, links):
    # convert tasks and links into a NetworkX directed graph
    dag = nx.DiGraph()
    dag.add_nodes_from(range(len(tasks)))
    dag.add_edges_from((head, tail) for tail, v in links.items() for _, head in v)

    # a cyclic dependency graph can't be run - something must have gone wrong, so raise an error
    if not nx.is_directed_acyclic_graph(dag):
        raise ValueError("Workflow does not form a directed acyclic graph.")

    return dag


def _task_is_ready(node, done, dag, tracker):
    return (
        (not done[node])
        and all(done[ancestor] for ancestor in nx.ancestors(dag, node))
        and (node not in tracker)
    )
