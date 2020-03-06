# vim: expandtab tabstop=4 shiftwidth=4

from pylint_beergarden.checker import BeergardenCommandChecker

def register(linter):
    linter.register_checker(BeergardenCommandChecker(linter))
