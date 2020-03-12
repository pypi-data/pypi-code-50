# -*- coding: utf-8 -*-
"""
Translate an options data structure into command line args
"""

# Import python libs
import sys
import inspect
import argparse
import functools
import collections

DEFAULT = "c17b9912c892bf60e7933ed1c912df4bc768e9cb25d0e0a5d7e5bebbca1c3dec"


def _keys(opts):
    """
    Return the keys in the right order
    """
    return sorted(opts, key=lambda k: (opts[k].get("display_priority", sys.maxsize), k))


def gather(hub, raw, cli, parse_cli):
    """
    Return the cli arguments as they are parsed
    """
    if not parse_cli:
        return {}
    raw_cli = hub.config.args.get_cli(raw, cli)
    hub.config.args.init_parser()
    hub.config.args.subparsers(raw, cli)
    defaults = hub.config.args.setup(raw_cli)
    cli_args = hub.config.args.parse()
    cli_args = hub.config.args.clean_defaults(cli_args)
    return cli_args, raw_cli


def clean_defaults(hub, cli_args):
    """
    If anyone did not pass an an argumentm then the key will match the
    bad default and needs to be removed
    """
    ret = {}
    for key, val in cli_args.items():
        if val != DEFAULT:
            ret[key] = val
    return ret


def init_parser(hub):
    if "parser" not in hub.config.ARGS:
        # Instantiate the parser
        hub.config.ARGS["parser"] = argparse.ArgumentParser()


def get_cli(hub, raw, cli):
    """
    Gather the arguments that need to be parsed by the CLI
    """
    ret = {}
    main = raw.get(cli, {}).get("CLI_CONFIG")
    main_raw = raw.get(cli, {}).get("CONFIG")
    for key, data in main.items():
        ret[key] = {}
        hub.pop.dicts.update(ret[key], data)
        if key in main_raw:
            hub.pop.dicts.update(ret[key], main_raw[key])
        if "source" in data:
            src = raw.get(data["source"], {}).get("CONFIG", {}).get(key)
            if src:
                hub.pop.dicts.update(ret[key], src)
        if "default" in ret[key]:
            ret[key]["default"] = DEFAULT
    ret.update(hub.config.version.CONFIG)
    return ret


def subparsers(hub, raw, cli):
    """
    Look over the data and extract and set up the subparsers for subcommands
    """
    subs = raw.get(cli, {}).get("SUBCOMMANDS")
    if not subs:
        return True
    hub.config.ARGS["sub"] = hub.config.ARGS["parser"].add_subparsers(
        dest="_subparser_"
    )
    hub.config.ARGS["subs"] = {}
    for arg in _keys(subs):
        if arg in ("_argparser_",):
            continue
        comps = subs[arg]
        kwargs = {}
        if "help" in comps:
            kwargs["help"] = comps["help"]
        if "desc" in comps:
            kwargs["description"] = comps["desc"]
        hub.config.ARGS["subs"][arg] = hub.config.ARGS["sub"].add_parser(arg, **kwargs)
    return True


def setup(hub, raw_cli):
    """
    Take in a pre-defined dict and translate it to args

    opts dict:
        <arg>:
            [group]: foo
            [default]: bar
            [action]: store_true
            [options]: # arg will be turned into --arg
              - '-A'
              - '--cheese'
            [choices]:
              - foo
              - bar
              - baz
            [nargs]: +
            [type]: int
            [dest]: cheese
            help: Some great help message
    """
    # TODO: This should be broken up
    defaults = {}
    groups = {}
    ex_groups = {}
    for arg in _keys(raw_cli):
        if arg in ("_argparser_",):
            continue
        comps = raw_cli[arg]
        positional = comps.pop("positional", False)
        if positional:
            args = [arg]
        else:
            long_opts = set(["--{}".format(arg.replace("_", "-"))])
            short_opts = set()
            for o_str in comps.get("options", []):
                if not o_str.startswith("--") and o_str.startswith("-"):
                    short_opts.add(o_str)
                elif o_str.startswith("--"):
                    long_opts.add(o_str)
                elif len(o_str) == 1:
                    short_opts.add(f"-{o_str}")
                else:
                    long_opts.add(f"--{o_str}")
            args = sorted(list(short_opts.union(long_opts)))
        kwargs = {}
        kwargs["action"] = action = comps.get("action", None)

        if action is None:
            # Non existing option defaults to a StoreAction in argparse
            action = hub.config.ARGS["parser"]._registry_get("action", action)

        if isinstance(action, str):
            signature = inspect.signature(
                hub.config.ARGS["parser"]._registry_get("action", action).__init__
            )
        else:
            signature = inspect.signature(action.__init__)

        for param in signature.parameters:
            if param == "self" or param not in comps:
                continue
            if param == "dest":
                kwargs["dest"] = comps.get("dest", arg)
                continue
            if param == "help":
                kwargs["help"] = comps.get("help", "THIS NEEDS SOME DOCUMENTATION!!")
                continue
            if param == "default":
                defaults[comps.get("dest", arg)] = comps[param]
            kwargs[param] = comps[param]

        if "group" in comps:
            group = comps["group"]
            if group not in groups:
                groups[group] = hub.config.ARGS["parser"].add_argument_group(group)
            groups[group].add_argument(*args, **kwargs)
            continue
        if "ex_group" in comps:
            group = comps["ex_group"]
            if group not in ex_groups:
                ex_groups[group] = hub.config.ARGS[
                    "parser"
                ].add_mutually_exclusive_group()
            ex_groups[group].add_argument(*args, **kwargs)
            continue
        if "subcommands" in comps:
            subs = comps["subcommands"]
            if not isinstance(subs, list):
                subs = [subs]
            for sub in subs:
                sparse = hub.config.ARGS["subs"].get(sub)
                if not sparse:
                    # Maybe raise exception here? Malformed config?
                    continue
                sparse.add_argument(*args, **kwargs)
            continue
        hub.config.ARGS["parser"].add_argument(*args, **kwargs)
    return defaults


def parse(hub, args=None, namespace=None, only_parse_known_arguments=False):
    """
    Parse the command line options
    """
    if only_parse_known_arguments:
        opts, unknown_args = hub.config.ARGS["parser"].parse_known_args(args, namespace)
        opts_dict = opts.__dict__
        opts_dict["_unknown_args_"] = unknown_args
    else:
        opts = hub.config.ARGS["parser"].parse_args(args, namespace)
        opts_dict = opts.__dict__
    return opts_dict


# TODO: SHOULD THIS GO HERE?
def render(hub, defaults, cli_opts, explicit_cli_args):
    """
    For options specified as such, take the string passed into the cli and
    render it using the specified render flag
    """
    for key in explicit_cli_args:
        rend = defaults.get(key, {}).get("render")
        if rend:
            ref = f"conf.{rend}.render"
            cli_opts[key] = getattr(hub, ref)(cli_opts[key])
    return cli_opts
