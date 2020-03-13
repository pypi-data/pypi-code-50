"""Module for the first tab."""

from opentea.noob.noob import nob_get, nob_set
from opentea.process_utils import process_tab


def custom_fun(nob_in):
    """Update the result."""
    nob_out = nob_in.copy()
    operation = nob_get(nob_in, "operand")
    nb1 = nob_get(nob_in, "number_1")
    nb2 = nob_get(nob_in, "number_2")

    res = None
    if operation == "+":
        res = nb1 + nb2
    elif operation == "-":
        res = nb1 - nb2
    elif operation == "*":
        res = nb1 * nb2
    elif operation == "/":
        res = nb1 / nb2
    else:
        res = None

    # raise RuntimeError("Tahiti a plante ce processus")

    nob_set(nob_out, res, "result")
    return nob_out


if __name__ == "__main__":
    process_tab(custom_fun)
