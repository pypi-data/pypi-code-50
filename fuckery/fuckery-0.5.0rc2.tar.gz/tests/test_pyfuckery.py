import argparse
import os
from fuckery.cli import main

import tests.common as t_common

def test_main():
    fn = 'hello_world.bf'
    fp = t_common.get_file(fn)
    ns = argparse.Namespace()
    ns.verbose = False
    ns.input = fp
    ns.loop_detection = False
    ns.memory_size = 100
    main(options=ns)
