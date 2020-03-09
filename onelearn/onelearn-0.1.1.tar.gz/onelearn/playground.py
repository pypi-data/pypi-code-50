# Authors: Stephane Gaiffas <stephane.gaiffas@gmail.com>
# License: BSD 3 clause


def run_playground():
    import streamlit.cli as cli
    import sys
    import onelearn

    filename = onelearn.__file__.replace("__init__.py", "playground_decision.py")
    sys.argv = ["0", "run", filename]
    cli.main()
