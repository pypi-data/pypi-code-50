"""
Pykrete main
Author: Shai Bennathan - shai.bennathan@gmail.com
(C) 2020
"""

import sys
import click


@click.group()
def main():
    """Pykrete's main function"""
    print('in main')
    print('called with: ' + str(sys.argv))


@main.command()
def generate():
    """Generate something"""
    print("Generate something")


if __name__ == '__main__':
    main()
