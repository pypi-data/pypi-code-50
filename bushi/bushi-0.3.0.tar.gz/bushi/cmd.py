from .io import io
import subprocess
import threading

class cmd:

  @staticmethod
  def run(command):
    try:
      io.process_stop()
      result = subprocess.run(command, shell=True)
      return result.returncode == 0
    except ProcessLookupError:
      return False

  @staticmethod
  def run_muted(command):
    try:
      result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
      return result.returncode == 0
    except ProcessLookupError:
      return False