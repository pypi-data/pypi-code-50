import getpass
import threading
import time
import sys

class io:

  color_red = '\033[31m'
  color_green = '\033[32m'
  color_yellow = '\033[33m'
  color_reset = '\033[39m'

  symbol_warn = '!'
  symbol_fail = '\u2717'
  symbol_success = '\u2713'

  argv = sys.argv
  argc = len(argv)

  process_index = 0
  process_symbols = ['\u28bf', '\u28fb', '\u28fd', '\u28fe', '\u28f7', '\u28ef', '\u28df', '\u287f']

  process_terminated = False
  process_text = ""

  @staticmethod
  def __format_text(text, start, end):

    formatted_text = ""

    find_star = False
    for character in text:
      if character == '*':
        if find_star:
          formatted_text += end
          find_star = False
        else:
          formatted_text += start
          find_star = True
      else:
        formatted_text += character

    if find_star:
      formatted_text += end

    return formatted_text

  @staticmethod
  def process(text):
    io.process_text = "[ ] " + text

  @staticmethod
  def cursor_up():
    print("\033[A\r\033[F")

  @staticmethod
  def new_line():
    io.process_text = ""
    print("\r\033[J")

  @staticmethod
  def clear_line():
    io.process_text = ""
    print("\r\033[J", end="")

  @staticmethod
  def __print(text):
    io.process_text = ""
    print("\r\033[J" + text)

  @staticmethod
  def info(text):
    io.__print("[ ] " + text)

  @staticmethod
  def warn(text):
    io.__print(io.__format_text("*[" + io.symbol_warn + "]* " + text, io.color_yellow, io.color_reset))

  @staticmethod
  def fail(text):
    io.__print(io.__format_text("*[" + io.symbol_fail + "]* " + text, io.color_red, io.color_reset))

  @staticmethod
  def success(text):
    io.__print(io.__format_text("*[" + io.symbol_success + "]* " + text, io.color_green, io.color_reset))

  @staticmethod
  def info_list(text):
    io.__print("    - " + text)

  @staticmethod
  def warn_list(text):
    io.__print(io.__format_text("    *" + io.symbol_warn + "* " + text, io.color_yellow, io.color_reset))

  @staticmethod
  def fail_list(text):
    io.__print(io.__format_text("    *" + io.symbol_fail + "* " + text, io.color_red, io.color_reset))

  @staticmethod
  def success_list(text):
    io.__print(io.__format_text("    *" + io.symbol_success + "* " + text, io.color_green, io.color_reset))

  @staticmethod
  def ask(text):
    io.process_text = ""
    return input(io.__format_text("\r\033[J*[" + io.symbol_warn + "]* " + text + " ", io.color_yellow, io.color_reset))

  @staticmethod
  def ask_secret(text):
    io.process_text = ""
    return getpass.getpass(io.__format_text("\r\033[J*[" + io.symbol_warn + "]* " + text + " ", io.color_yellow, io.color_reset))

  @staticmethod
  def terminate(*texts):
    io.process_terminated = True
    if len(texts) == 0:
      sys.exit(0)
    else:
      io.clear_line()
      io.new_line()
      for text in texts:
        io.fail(text)
      sys.exit(1)


def __process_callback():
  while not io.process_terminated:
    if len(io.process_text) > 0:
      process_symbol = io.process_symbols[io.process_index]
      print("\r\033[J" + io.process_text + " " + process_symbol, end="")
      io.process_index = (io.process_index + 1) % len(io.process_symbols)
    else:
      io.process_index = 0

    time.sleep(0.10)

__process_thread = threading.Thread(target=__process_callback)
__process_thread.start()