#!/usr/bin/env python3
# Similar to Linux time utility for the Windows Command Prompt
import subprocess
import sys
import time

def main():
    command = ' '.join(sys.argv[1:])

    start = time.monotonic()
    subprocess.run(command, shell=True)
    end = time.monotonic()

    seconds = round(end - start)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)

    print('Elapsed Time: {:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds))

if __name__ == "__main__":
    main()