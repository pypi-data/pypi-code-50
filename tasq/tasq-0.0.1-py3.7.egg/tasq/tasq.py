#!/usr/bin/env python3

import sys
import jinja2
import yaml
import typer
import subprocess
import braceexpand
import json
import time
import datetime
import os

app = typer.Typer()

tasqpath = os.environ.get("TASQPATH", ".:./tasq")
tasqfiles = os.environ.get("TASQFILES", "Tasqfile.yml:Tasqfile.yaml")
noexec = False
config = {"shell": ["/bin/bash", "-ec"], "python": ["python3"], "kubectl_poll": 3}
tasqfile = None
tasks = {}
pre_tasks = {}
post_tasks = {}
task_types = {}


def yamlquote(value):
    assert isinstance(value, str)
    return yaml.dump(value)


environment = jinja2.Environment()
environment.filters["yamlquote"] = yamlquote


def tasktype(name=None):
    def wrap(f):
        task_types[name] = f
        return f

    return wrap


def check_output(command, *args, **kw):
    try:
        result = subprocess.check_output(command, *args, **kw)
    except subprocess.CalledProcessError as exn:
        print(f"FAILED {str(exn)[:20]}", file=sys.stderr)
        return None
    if isinstance(result, bytes):
        result = result.decode("utf-8")
    return result


@tasktype("doc")
def task_doc(task, params):
    pass


@tasktype("echo")
def task_echo(task, params):
    echo = task.get("echo", "")
    rendered = environment.from_string(echo).render(params)
    print(rendered)


@tasktype("script")
def task_script(task, params):
    script = task.get("script")
    rendered = environment.from_string(script).render(params)
    if noexec:
        print(script)
    else:
        result = check_output(config["shell"] + [rendered])
        print(result)


@tasktype("exec")
def task_exec(task, params):
    script = task.get("exec")
    exec(script, globals(), dict(params=params))


@tasktype("python")
def task_python(task, params):
    script = task.get("python")
    rendered = environment.from_string(script).render(params)
    if noexec:
        print(script)
    else:
        result = check_output(config.python + [rendered])
        print(result)


@tasktype("with_braceexpand")
def task_with_braceexpand(task, params):
    params = dict(params)
    raw = task.get("with_braceexpand")
    param = task.get("param", "item")
    subtasks = task.get("tasks", [])
    for fname in braceexpand.braceexpand(raw):
        print(fname, subtasks)
        params[param] = fname
        execute(subtasks, params)


@tasktype("kubectl_wait")
def task_kubectl_wait(task, params):
    kind = params.get("kind", "jobs")
    prefix = params.get("prefix", "")
    namespace = params.get("namespace", None)
    verbose = params.get("verbose", True)
    while True:
        result = json.loads(check_output(["kubectl", "get", kind, "-o", "json"]))
        nactive = 0
        for item in result["items"]:
            if namespace is not None and item["metadata"]["namespace"] != namespace:
                continue
            if prefix is not None and not item["metadata"]["name"].startswith(prefix):
                continue
            if item["status"].get("active", False):
                nactive += 1
        if verbose:
            now = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
            print(
                f"{now} {namespace} {prefix} nactive {nactive:6d}\r",
                flush=True,
                end="",
                file=sys.stderr,
            )
        if nactive == 0:
            break
        time.sleep(config["kubectl_poll"])


@tasktype("kubectl_apply")
def task_kubectl_apply(task, params):
    params = dict(params)
    if "template" in task:
        template = task["template"]
    if "template_name" in task:
        templates = tasqfile["k8s_templates"]
        template = templates[task["template_name"]]
    params.update(task.get("params", {}))
    rendered = environment.from_string(template).render(params).encode("utf-8")
    if noexec:
        print(rendered)
    else:
        result = check_output(["kubectl", "apply", "-f", "-"], input=rendered)
        print(result)


def execute(task, params):
    if task is None:
        return
    if isinstance(task, dict):
        matching = set(task_types.keys()).intersection(task.keys())
        if len(matching) != 1:
            print(f"{list(task.keys())} don't match a task")
            sys.exit(1)
        task_types[list(matching)[0]](task, params)
    if isinstance(task, list):
        params = dict(params)
        for subtask in task:
            execute(subtask, params)


def global_init():
    global params, tasqfile, config, noexec, pre_tasks, post_tasks, tasks
    tasqfile = None
    for dir in tasqpath.split(":"):
        for fname in tasqfiles.split(":"):
            path = os.path.join(dir, fname)
            if not os.path.exists(path):
                continue
            print("reading", path)
            with open(path) as stream:
                tasqfile = yaml.safe_load(stream)
    if tasqfile is None:
        print(f"no tasqfile found on path {tasqpath}")
        sys.exit(1)
    params = tasqfile.get("params", {})
    config.update(tasqfile.get("params", {}))
    tasks = tasqfile.get("tasks", {})
    tasks.update(tasqfile.get("tasqs", {}))
    pre_tasks = tasqfile.get("pre", {})
    post_tasks = tasqfile.get("post", {})


@app.command("list")
def list_():
    global_init()
    print("available tasks:")
    for k, v in sorted(tasqfile.items()):
        if isinstance(v, list) and len(v) > 0:
            v = v[0]
        if isinstance(v, dict) and "doc" in v:
            docstring = v["doc"]
        else:
            docstring = repr(v)[:50]
        print(k, ":", docstring)


@app.command()
def showparams():
    global_init()
    for k, v in params.items():
        print(k, ":", str(v)[:30])


@app.command()
def showconfig():
    global_init()
    for k, v in config.items():
        print(k, ":", str(v)[:30])


@app.command()
def run(task: str, verbose: bool = False):
    global_init()
    execute(pre_tasks, params)
    try:
        execute(tasks, params)
    finally:
        execute(post_tasks, params)


@app.command()
def dryrun(task: str, verbose: bool = False):
    global noexec
    noexec = True
    run(task, verbose)


if __name__ == "__main__":
    app()
