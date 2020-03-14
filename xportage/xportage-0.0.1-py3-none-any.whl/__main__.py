# __main__.py

import argparse
import os

from portage import portage

HOME = os.path.expanduser('~')


def main(options):
    portage_home = portage.PortageHome(options.home, options.cfg)
    portage_home.print_configuration()
    portage_home.print_summary()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('home', type=str, help='Path to PORTAGE_HOME.')
    parser.add_argument('--cfg', default=os.path.join(HOME, '.portage', 'cfg.json'), type=str, help='Path to PORTAGE_CFG.')
    options = parser.parse_args()

    main(options)
