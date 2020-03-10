import argparse
from typing import List


class DockerArgumentParserError(Exception):
    pass


class DockerArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise DockerArgumentParserError(message)


def _add_run_subparser(subparsers):
    run_parser = subparsers.add_parser("run", add_help=False)
    run_parser.add_argument("-a", "--attach", type=str)
    run_parser.add_argument("--add-host", type=str, action="append")
    run_parser.add_argument("--blkio-weight", type=int)
    run_parser.add_argument("--blkio-weight-device", type=str)
    run_parser.add_argument("--cap-add", type=str, action="append")
    run_parser.add_argument("--cap-drop", type=str, action="append")
    run_parser.add_argument("--cgroup-parent", type=str)
    run_parser.add_argument("--cidfile", type=str)
    run_parser.add_argument("--cpu-count", type=int)
    run_parser.add_argument("--cpu-percent", type=int)
    run_parser.add_argument("--cpu-period", type=int)
    run_parser.add_argument("--cpuset-cpus", type=str)
    run_parser.add_argument("--cpuset-mems", type=str)
    run_parser.add_argument("-d", "--detach", action='store_true')
    run_parser.add_argument("--device", type=str)
    run_parser.add_argument("--device-cgroup-rule", type=str)
    run_parser.add_argument("--dns", type=str, action="append")
    run_parser.add_argument("-e", "--env", type=str, action="append")
    run_parser.add_argument("--entrypoint", type=str)
    run_parser.add_argument("--env-file", type=str)
    run_parser.add_argument("--expose", type=str)
    run_parser.add_argument("--help", action="store_true")
    run_parser.add_argument("-h", "--hostname", type=str)
    run_parser.add_argument("-i", "--interactive", action='store_true')
    run_parser.add_argument("--init", action="store_true")
    run_parser.add_argument("--ipc", type=str)
    run_parser.add_argument("--isolation", type=str)
    run_parser.add_argument("-l", "--label", type=str, action="append")
    run_parser.add_argument("--label-file", type=str)
    run_parser.add_argument("--link", type=str, action="append")
    run_parser.add_argument("--mac-address", type=str)
    run_parser.add_argument("-m", "--memory", type=str)
    run_parser.add_argument("--memory-reservation", type=str)
    run_parser.add_argument("--name", type=str)
    run_parser.add_argument("--network", type=str)
    run_parser.add_argument("--oom-kill-disable", action='store_true')
    run_parser.add_argument("--pids-limit", type=int)
    run_parser.add_argument("-P", "--publish-all", action='store_true')
    run_parser.add_argument("-p", "--publish", type=str, action="append")
    run_parser.add_argument("--privileged", action='store_true')
    run_parser.add_argument("--read-only", action='store_true')
    run_parser.add_argument("--rm", action='store_true')
    run_parser.add_argument("--stop-signal", type=str)
    run_parser.add_argument("--stop-timeout", type=int)
    run_parser.add_argument("--memory-swappiness", type=int)
    run_parser.add_argument("-t", "--tty", action='store_true')
    run_parser.add_argument("-u", "--user", type=str)
    run_parser.add_argument("-v", "--volume", type=str, action="append")
    run_parser.add_argument("--volumes-from", type=str, action="append")
    run_parser.add_argument("-w", "--workdir", type=str)
    run_parser.add_argument("image", type=str)
    run_parser.add_argument("args", type=str, nargs=argparse.REMAINDER)


def docker_run_argument_parser() -> DockerArgumentParser:
    """
    Returns a parser suitable for parsing the docker-run subcommand
    """

    ap = DockerArgumentParser(prog="docker", add_help=False)
    subparsers = ap.add_subparsers()
    _add_run_subparser(subparsers)
    return ap


def docker_container_run_parser():
    """
    Returns a parser suitable for parsing the docker-container-run subcommand
    """

    ap = DockerArgumentParser(prog="docker", add_help=False)
    subparsers = ap.add_subparsers()
    container = subparsers.add_parser("container", add_help=False)
    container_subparsers = container.add_subparsers()
    _add_run_subparser(container_subparsers)
    return ap


def parse_args_as_run_command(args: List[str]):
    """
    Parses a list of arguments as a docker-run or docker-container-run command

    Raises ValueError if the command is not either of 'docker run' or 'docker container run'
    """
    if args[0] == "run":
        return docker_run_argument_parser().parse_args(args)
    elif args[0] == "container" and args[1] == "run":
        return docker_container_run_parser().parse_args(args)
    cmd = args[0] if args[0] != "container" else f"{args[0]} {args[1]}"
    raise ValueError(
        f"expected 'docker run' or 'docker container run', got 'docker {cmd}'"
    )


def parse_as_run_command(command):
    """
    Parses a command as a docker-run or docker-container-run command

    Raises ValueError if the command is not either of 'docker run' or 'docker container run'
    """
    command_words = list(map(lambda node: node.word, filter(lambda node: node.kind == "word", command.parts)))
    return parse_args_as_run_command(command_words[1:])
