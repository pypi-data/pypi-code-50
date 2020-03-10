#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse
import unittest
from spaceone.core.unittest.runner import RichTestRunner


def main():
    parser = argparse.ArgumentParser(description="SpaceONE Unit Tests")
    parser.add_argument("-f", "--failfast", action="store_true", help="fast failure flag")
    parser.add_argument("-c", "--config", help="Config file")
    parser.add_argument("-s", "--scenario", help="Scenario file")
    parser.add_argument("-d", "--dir", action="store", type=str,
                        help="directory containing test files")
    parser.add_argument("-p", "--parameters",
                        nargs="*",
                        help="Custom parameters to override a scenario file. "
                             "ex) -p domain.domain.name=new_name options.update_mode=false")

    args = parser.parse_args()
    failfast = args.failfast
    descriptions = True

    verbose = 1

    if args.dir:
        dir = args.dir
    else:
        pwd = os.getcwd()
        dir = pwd

    if args.config:
        os.environ["TEST_CONFIG"] = args.config

    if args.scenario:
        os.environ["TEST_SCENARIO"] = args.scenario

    if args.parameters:
        result = ''
        for item in args.parameters:
            result = result + item + ','
        os.environ["TEST_SCENARIO_PARAMS"] = result

    # suites are not hashable, need to use list
    loader = unittest.TestLoader()
    suites = loader.discover(dir)

    full_suite = unittest.TestSuite()
    full_suite.addTests(suites)
    result = RichTestRunner(verbosity=verbose, failfast=failfast).run(full_suite)

    # TODO: summary result


if __name__ == "__main__":
    run()
