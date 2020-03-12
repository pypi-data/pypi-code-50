#!/usr/bin/env python3
import os
import argparse
from didtoday.commands import add, show
from datetime import date


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add", help="Add a new bullet point to today")
    add_parser.set_defaults(func=add)
    add_parser.add_argument("content", type=str, help="bar help")

    show_parser = subparsers.add_parser(
        "show",
        help="Shows contents of file for a specific day (or today if none is provided)",
    )
    show_parser.set_defaults(func=show)
    show_parser.add_argument(
        "date",
        type=str,
        help="bar help",
        nargs="?",
        default=date.today().strftime("%Y-%m-%d"),
    )

    args = parser.parse_args()
    args.func(args)
