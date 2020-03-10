import argparse
import re
from typing import List, Optional


class DockerArgumentParserError(Exception):
    pass


class DockerArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise DockerArgumentParserError(message)


class VolumeArgument:
    def __init__(self, host_path: Optional[str], container_path: str, options: Optional[str]):
        self.host_path = host_path
        self.container_path = container_path
        self.options = options

    def is_anonymous_volume(self) -> bool:
        return self.host_path is None

    def is_named_volume(self) -> bool:
        named_pattern = r"[a-zA-Z0-9][a-zA-Z0-9_.-]"
        return not self.is_anonymous_volume() and re.fullmatch(named_pattern, self.host_path) is not None

    def is_bind_mount_volume(self) -> bool:
        return not self.is_anonymous_volume() and not self.is_named_volume()

    def __repr__(self):
        return f"VolumeArgument(host_path={self.host_path}, container_path={self.container_path}, options={self.options})"

    @staticmethod
    def parse(arg: str) -> 'VolumeArgument':
        splitted = arg.split(":")
        if 1 <= len(splitted) <= 3:
            options = None
            host_path = None
            if len(splitted) == 1:
                # '-v /CONTAINER-PATH' case
                container_path = splitted[0]
            else:
                # '-v HOST_PATH:/CONTAINER-PATH[:OPTIONS]' case
                host_path = splitted[0]
                container_path = splitted[1]
                if len(splitted) == 3:
                    options = splitted[2]
            return VolumeArgument(host_path, container_path, options)
        raise ValueError("invalid argument for -v/--volume")


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
    run_parser.add_argument("-v", "--volume", type=VolumeArgument.parse, action="append")
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
