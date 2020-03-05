import os
import sys
import reptimer


def main() -> None:
    """Repeats a timer indefinitely. Inputs are minutes and seconds.
    """
    try:
        minutes: str
        seconds: str
        minutes, seconds = sys.argv[1:]
    except:
        doc: str = os.path.join(os.path.dirname(__file__), "doc.txt")
        with open(doc, "r") as f:
            print(f.read())
        return

    try:
        while True:
            reptimer.timer(int(minutes) * 60 + int(seconds))
    except KeyboardInterrupt:
        print("\rStopping timer.")  # \r flushes ^C
