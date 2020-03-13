import yaml

from apparatus import base


class Constant:
    COMMAND = "config"


def handle(settings, remainder):
    # pylint: disable=unused-argument
    config = base.read_config()
    print(yaml.dump(config))


def init():
    parser = base.SUBPARSERS.add_parser(Constant.COMMAND)
    parser.set_defaults(fn=handle)
    return parser.parse_known_args()


init()
