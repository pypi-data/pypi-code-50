import curses
import json
import socket
import sys
import threading
from typing import Any
from typing import Dict


class PresenterView:
    def __init__(self, port):
        self.port = port

        self.commands = []
        # Set this to None so we print the first command, even if it's at 0.
        self.command_index = None
        self.command_offset = 0
        self.paused = False
        self.exiting = False

        self.e = threading.Event()

    def process_command(self, command: Dict[str, Any]):
        """
        Process a command that came in through the socket.
        """
        if command["command"] == "initial":
            self.commands = command["data"]
        elif command["command"] == "exit":
            self.exiting = True
        elif command["command"] == "cursor":
            update_screen = self.command_index != command["index"]

            self.command_index = command["index"]
            self.command_offset = command["offset"]

            if update_screen:
                # Only update the screen if the command index changed.
                self.draw_screen()
        elif command["command"] == "pause":
            self.paused = True
            self.draw_screen()
        elif command["command"] == "resume":
            self.paused = False
            self.draw_screen()

    def run_client(self):
        """
        Run the TCP client.
        """
        s = socket.socket()
        s.connect(("127.0.0.1", self.port))

        # Wait for a signal that curses is done initializing.
        self.e.wait()

        BUF_SIZE = 2 ** 12
        data = b""
        while True:
            d = s.recv(BUF_SIZE)

            if not d:
                break

            data += d

            if len(d) == BUF_SIZE:
                continue

            for line in data.decode().strip("\n").split("\n"):
                self.process_command(json.loads(line))
            data = b""
        s.close()

    def draw_screen(self):
        """
        Draw the screen based on the current status.
        """
        self.screen.clear()
        y, x = self.screen.getmaxyx()
        self.screen.border()

        top_margin = 1
        left_margin = 1

        # Draw the current command marker.
        midheight = y // 2
        self.screen.addstr(midheight, 1, "->", curses.color_pair(1))

        # Calculate where rows should be.
        first_command_row = max(top_margin, midheight - self.command_index)
        last_command_row = min(
            y - top_margin * 2, midheight + len(self.commands) - self.command_index
        )

        first_command_offset = max(0, self.command_index - midheight + top_margin)

        # Draw the commands themselves.
        for c, i in enumerate(
            range(first_command_row, last_command_row), start=first_command_offset
        ):
            formatted_command = repr(self.commands[c].rstrip("\n"))[1:-1].encode()

            # Draw comments in green.
            if self.commands[c].startswith("##"):
                pair = 2
            else:
                pair = 0

            self.screen.addstr(
                i,
                left_margin + 3,
                formatted_command[: max(0, x - left_margin * 2 - 3)],
                curses.color_pair(pair),
            )

        self.screen.refresh()

        if self.paused:
            # Draw the "Paused" window.
            win = curses.newwin(5, 20, y // 2 - 2, x // 2 - 10)
            win.border()
            win.addstr(2, 7, "PAUSED", curses.color_pair(1))
            win.refresh()

    def curses_main(self, stdscr):
        """
        Set up curses and run the main loop.
        """
        # Set up curses.
        self.screen = stdscr
        curses.curs_set(0)
        self.screen.erase()

        # Set up colors.
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)

        # Notify the client that it can begin connecting, to avoid a race condition
        # that corrupts the screen.
        self.e.set()

        while True:
            key = self.screen.getkey()
            if key == "KEY_RESIZE":
                self.draw_screen()
            elif key == "q" or self.exiting:
                sys.exit("Bye!")

    def run(self):
        threading.Thread(target=self.run_client, daemon=True).start()
        curses.wrapper(self.curses_main)


def run_presenter_view(port: int):
    PresenterView(port=port).run()
