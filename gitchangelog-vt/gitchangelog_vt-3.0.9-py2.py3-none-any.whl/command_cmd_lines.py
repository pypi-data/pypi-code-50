import sys
from warnings import warn


def parse_cmd_line(usage, description, epilog, exname, version):

    import argparse
    kwargs = dict(usage=usage,
                  description=description,
                  epilog="\n" + epilog,
                  prog=exname,
                  formatter_class=argparse.RawTextHelpFormatter)

    try:
        parser = argparse.ArgumentParser(version=version, **kwargs)
    except TypeError:  ## compat with argparse from python 3.4
        parser = argparse.ArgumentParser(**kwargs)
        parser.add_argument('-v', '--version',
                            help="show program's version number and exit",
                            action="version", version=version)

    parser.add_argument('-d', '--debug',
                        help="Enable debug mode (show full tracebacks).",
                        action="store_true", dest="debug")
    parser.add_argument('revlist', nargs='*', action="store", default=[])

    parser.add_argument('-c', '--clean', nargs="*", help="Requires "
                                                         "keywords (Ex. -c Item)", action="store")

    parser.add_argument('-t', '--title', nargs="*", help="To change the "
                                                         "changelog title.", action="store")

    parser.add_argument('-s', '--show', nargs="*", help="To show the "
                                                        "commits preferred.", action="store")

    parser.add_argument('-u', '--url', nargs="*", help="To change or add the "
                                                       "jira url.", action="store")

    parser.add_argument('-f', '--file', nargs="*", help="Generate the file name "
                                                        "with markdown extension.", action="store")

    parser.add_argument('-tm', '--template', nargs="*", help="Use a new"
                                                             " template.", action="store")

    parser.add_argument('-m', '--module', nargs="*", help="Use a new"
                                                             " module.", action="store")

    ## Remove "show" as first argument for compatibility reason.

    argv = []
    for i, arg in enumerate(sys.argv[1:]):
        if arg.startswith("-"):
            argv.append(arg)
            continue
        if arg == "show":
            warn("'show' positional argument is deprecated.")
            argv += sys.argv[i + 2:]
            break
        else:
            argv += sys.argv[i + 1:]
            break

    return parser.parse_args(argv)
