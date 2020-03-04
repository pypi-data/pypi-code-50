#!/usr/bin/env python3
import argparse
import array
import errno
import fcntl
import os
import pty
import re
import select
import signal
import socket
import struct
import sys
import termios
import tty
from pathlib import Path
from typing import List

from .version import __version__


def strip_ansi(text: bytes) -> bytes:
    """
    Strip all ANSI sequences from `text`.
    """
    ansi_escape = re.compile(rb"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    return ansi_escape.sub(b"", text)


def load_file(filename: Path) -> List[str]:
    """
    Load the commands from a file.
    """
    with filename.expanduser().open("r") as infile:
        cmd_list = infile.read().rstrip("\n").split("\n")

    return cmd_list


def load_commands(filename: Path) -> List[str]:
    """
    Load commands from a file, processing them as required.
    """
    new_list = []
    cmd_list = load_file(filename)
    filename = filename.expanduser()
    for command in cmd_list:
        include = re.match(r"^##@include\s+(?P<filename>.*?)$", command)
        if include:
            include_file_name = Path(
                os.path.join(
                    filename.parent, Path(include.group("filename")).expanduser()
                )
            ).resolve()
            if not include_file_name.exists():
                sys.exit("%s does not exist." % include_file_name)
            new_list.extend(load_file(include_file_name))
        else:
            new_list.append(command)

    return new_list


class Raw:
    def __init__(self, fd):
        self.fd = fd
        self.restore = False

    def __enter__(self):
        try:
            self.mode = tty.tcgetattr(self.fd)
            tty.setraw(self.fd)
            self.restore = True
        except tty.error:  # This is the same as termios.error
            pass

    def __exit__(self, type, value, traceback):
        if self.restore:
            tty.tcsetattr(self.fd, tty.TCSAFLUSH, self.mode)


class Player:
    def __init__(self, command_filename: Path, env=os.environ.copy(), speed=1):
        self.master_fd = None
        self.paused = False
        # Which command in the list we're at.
        self.command_index = 0
        # Where in the command we currently are.
        self.command_offset = 0
        self.env = env
        self.speed = max(0, int(speed))

        # Read the commands from the file into a list of one per line.
        commands = load_commands(command_filename)
        # Strip all blank lines except the last one.
        self.commands = commands + [""]

    def _send_udp_packet(self, data):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(data, ("127.0.0.1", 5345))

    @property
    def _current_command(self) -> str:
        return self.commands[self.command_index]

    def _send_command(self):
        """
        Send the current command over the UDP socket.
        """
        formatted_command = (
            repr(self._current_command.rstrip("\n"))[1:-1].encode() + b"\n"
        )
        self._send_udp_packet(formatted_command)

    def _reset_command(self):
        """
        Reset the current command to the beginning and send it.
        """
        if self.command_index >= len(self.commands):
            sys.exit()

        self.command_offset = 0

        self._send_command()

    def _next_command(self):
        """
        Change the command index to the next command.
        """
        while True:
            self.command_index += 1
            self._reset_command()

            # Skip over comments, but still send them.
            if not self._current_command.startswith("##"):
                break

    def _previous_command(self):
        """
        Change the command index to the previous command.
        """
        while True:
            self.command_index = max(0, self.command_index - 1)

            if not self._current_command.startswith("##"):
                self._reset_command()
                break

    def _set_pty_size(self):
        """
        Sets the window size of the child pty based on the window size
        of our own controlling terminal.
        """
        # Get the terminal size of the real terminal, set it on the pseudoterminal.
        if os.isatty(pty.STDOUT_FILENO):
            buf = array.array("h", [0, 0, 0, 0])
            fcntl.ioctl(pty.STDOUT_FILENO, termios.TIOCGWINSZ, buf, True)
        else:
            buf = array.array("h", [24, 80, 0, 0])

        fcntl.ioctl(self.master_fd, termios.TIOCSWINSZ, buf)

    def _write_stdout(self, data):
        """Writes to stdout as if the child process had written the data."""
        os.write(pty.STDOUT_FILENO, data)

    def _handle_master_read(self, data):
        """Handles new data on child process stdout."""
        self._write_stdout(data)

    def _write_master(self, data, passthrough=False):
        """Writes to the child process from its controlling terminal."""

        command_end = False
        if passthrough:
            while data:
                n = os.write(self.master_fd, data)
                data = data[n:]
            return

        data = strip_ansi(data)
        if not data:
            # Sometimes we get pure ANSI sequences, just ignore those.
            return

        next_char = self._current_command[
            self.command_offset : self.command_offset + self.speed
        ]
        if not next_char:
            if b"\r" not in data and b"\n" not in data:
                return
            else:
                next_char = "\n"
                command_end = True

        os.write(self.master_fd, next_char.encode())
        self.command_offset += self.speed
        if command_end:
            self._next_command()

    def _handle_stdin_read(self, data):
        """Handles new data on child process stdin."""
        if data == b"\x10":  # Ctrl+p
            self.paused = not self.paused
            return

        # If we aren't paused, accept commands.
        if self.paused:
            self._write_master(data, passthrough=True)
        else:
            if data == b"\x04":  # Ctrl+d
                sys.exit("Abort!")
            elif data == b"\x05":  # Ctrl+e
                # Type the rest of the command by setting the speed to the entire command,
                # then emitting a single character so it types everything up to the newline.
                speed_backup = self.speed
                self.speed = len(self._current_command.encode())
                self._write_master(b"a")
                self.speed = speed_backup
            elif data == b"\x15":  # Ctrl+u
                # Pass it through.
                self._write_master(data, passthrough=True)
                self._reset_command()
            elif data == b"\x06":  # Ctrl+f
                # Fast-forward to the next newline.
                self._next_command()
            elif data == b"\x02":  # Ctrl+b
                # Rewind to the last newline.
                self._previous_command()
            else:
                self._write_master(data)

    def _signals(self, signal_list):
        old_handlers = []
        for sig, handler in signal_list:
            old_handlers.append((sig, signal.signal(sig, handler)))
        return old_handlers

    def _copy(self, signal_fd):
        """Main select loop.

        Passes control to _master_read() or _stdin_read()
        when new data arrives.
        """

        fds = [self.master_fd, pty.STDIN_FILENO, signal_fd]

        while True:
            try:
                rfds, wfds, xfds = select.select(fds, [], [])
            except OSError as e:  # Python >= 3.3
                if e.errno == errno.EINTR:
                    continue
            except select.error as e:  # Python < 3.3
                if e.args[0] == 4:
                    continue

            if self.master_fd in rfds:
                data = os.read(self.master_fd, 1024)
                if not data:  # Reached EOF.
                    fds.remove(self.master_fd)
                else:
                    self._handle_master_read(data)

            if pty.STDIN_FILENO in rfds:
                data = os.read(pty.STDIN_FILENO, 1024)
                if not data:
                    fds.remove(pty.STDIN_FILENO)
                else:
                    self._handle_stdin_read(data)

            if signal_fd in rfds:
                data = os.read(signal_fd, 1024)
                if data:
                    signals = struct.unpack("%uB" % len(data), data)
                    for sig in signals:
                        if sig in [
                            signal.SIGCHLD,
                            signal.SIGHUP,
                            signal.SIGTERM,
                            signal.SIGQUIT,
                        ]:
                            os.close(self.master_fd)
                            return
                        elif sig == signal.SIGWINCH:
                            self._set_pty_size()

    def play(self, command=None):
        """
        Start the player.
        """
        if command is None:
            command = os.environ.get("SHELL") or "sh"

        self._reset_command()

        command = ["sh", "-c", command]
        pid, self.master_fd = pty.fork()

        if pid == pty.CHILD:
            os.execvpe(command[0], command, self.env)

        pipe_r, pipe_w = os.pipe()
        flags = fcntl.fcntl(pipe_w, fcntl.F_GETFL, 0)
        flags = flags | os.O_NONBLOCK
        flags = fcntl.fcntl(pipe_w, fcntl.F_SETFL, flags)

        signal.set_wakeup_fd(pipe_w)

        old_handlers = self._signals(
            map(
                lambda s: (s, lambda signal, frame: None),
                [
                    signal.SIGWINCH,
                    signal.SIGCHLD,
                    signal.SIGHUP,
                    signal.SIGTERM,
                    signal.SIGQUIT,
                ],
            )
        )

        self._set_pty_size()

        with Raw(pty.STDIN_FILENO):
            try:
                self._copy(pipe_r)
            except (IOError, OSError):
                pass

        self._signals(old_handlers)

        os.waitpid(pid, 0)


def main():
    parser = argparse.ArgumentParser(description="It's a live.")
    parser.add_argument(
        "command_file",
        metavar="command_file",
        type=str,
        help="The command file to read.",
    )
    parser.add_argument(
        "-s",
        "--speed",
        dest="speed",
        type=int,
        default=1,
        help="set the typing speed (default: %(default)s",
    )
    parser.add_argument(
        "--version", action="version", version="%(prog)s " + __version__
    )

    args = parser.parse_args()
    Player(Path(args.command_file), speed=args.speed).play()


if __name__ == "__main__":
    main()
