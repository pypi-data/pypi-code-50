from limic.route import CONFIG as ROUTE_CONFIG
from limic.init import CONFIG as INIT_CONFIG
from limic.merge import CONFIG as MERGE_CONFIG
from limic.convert import CONFIG as CONVERT_CONFIG
from limic.prune import CONFIG as PRUNE_CONFIG
from limic.select import CONFIG as SELECT_CONFIG
from limic.length import CONFIG as LENGTH_CONFIG
from limic.fill import CONFIG as FILL_CONFIG
from limic.extract import CONFIG as EXTRACT_CONFIG
from limic.test import CONFIG as TEST_CONFIG
CONFIG = [
    (("-v","--verbosity"),{'type':int,'default':1,'dest':'verbosity','help':"set verbosity level to LEVEL (default: 1)",'metavar':'LEVEL'}),
    ("init",{'help':"Initialize the data files.",'args':INIT_CONFIG}),
    ("route",{'help':"Route from one power tower to another.",'args':ROUTE_CONFIG}),
    ("convert",{'help':"Convert graphs/caches.",'args':CONVERT_CONFIG}),
    ("merge",{'help':"Merge graphs/caches.",'args':MERGE_CONFIG}),
    ("prune",{'help':"Prune graph by geometry.",'args':PRUNE_CONFIG}),
    ("select",{'help':"Select area from graph by geometry.",'args':SELECT_CONFIG}),
    ("length",{'help':"Compute total length of non-air edges.",'args':LENGTH_CONFIG}),
    ("fill",{'help':"Fill a cache with map data.",'args':FILL_CONFIG}),
    ("extract",{'help':"Exgract NX graph from cache with map data.",'args':EXTRACT_CONFIG}),
    ("test",{'help':"Extensive self tests.",'args':TEST_CONFIG}),
]

if __name__ == "__main__":
    from argparse import ArgumentParser
    from limic.util import set_verbosity, parse_config
    from importlib import import_module
    parser = ArgumentParser(description="Powerlines as drone highways.")
    parse_config(CONFIG, parser, [])
    args = parser.parse_args()
    set_verbosity(args.verbosity)
    module = import_module(args.mod)
    func = vars(module)[args.func]
    del args.verbosity, args.mod, args.func, args.command
    func(**vars(args))
