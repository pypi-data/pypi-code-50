from .cmd import cmd
from .io import io

class tmux:

  @staticmethod
  def session_exist(session):
    return cmd.run_muted("tmux ls | cut -d ':' -f 1 | grep -x '" + session + "'")

  @staticmethod
  def detach():
    return cmd.run_muted("tmux detach")

  @staticmethod
  def session_kill(session):
    return cmd.run_muted("tmux kill-session -t '" + session + "'")

  @staticmethod
  def session_run(command):
    session_id = 0
    while tmux.session_exist("bushi-" + str(session_id)):
      session_id += 1

    process_text = io.get_process_tex()
    if len(process_text) < 1:
      process_text = "process..."

    session = "bushi-" + str(session_id)
    runner_command = "tmux new-session -s " + session
    runner_command += " bushi-tmux-runner '" + process_text + "' '" + command + "'"

    io.process_stop()
    cmd.run_muted(runner_command)
    if tmux.session_exist(session):
      tmux.session_kill(session)
      return False

    return True
