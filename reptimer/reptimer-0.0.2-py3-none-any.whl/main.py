#!/usr/bin/env python
import subprocess
import time
import os

sound: str = os.path.join(os.sep, "System", "Library", "Sounds", "Tink.aiff")


def timer(seconds: int) -> None:
    """timer sleeps for some seconds and then plays a sound."""
    time.sleep(seconds)
    subprocess.run(["afplay", sound, "-v", "20"])
    return True
