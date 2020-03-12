from .io import io
import subprocess
import threading

class cmd:

  @staticmethod
  def run(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    def stdout_callback(process):
      while process.poll() == None:
        line = process.stdout.readline()
        if line:
          io.clear_line()
          io.stream(line.decode('utf-8'))
          io.process_print()

    def stderr_callback(process):
      while process.poll() == None:
        line = process.stderr.readline()
        if line:
          io.clear_line()
          io.stream(line.decode('utf-8'))
          io.process_print()

    stdout_thread = threading.Thread(target=stdout_callback, args=[process])
    stdout_thread.start()

    stderr_thread = threading.Thread(target=stderr_callback, args=[process])
    stderr_thread.start()

    process.wait()

    stdout_thread.join()
    stderr_thread.join()

    return process.returncode == 0

  @staticmethod
  def runmuted(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0