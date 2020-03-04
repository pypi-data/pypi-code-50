import sys
import os
import re
import curses
from atig.migration import Migration, MigrationCollection


class Atig():
    def __init__(self):
        self.valid_migration = re.compile(r'[0-9a-f]{12}\_.*\.py')
        self.migrations = None
        self.migration_collection = None
        self.debug_message = 'Welcome to ATIG 8^)'
        self.window_open = False
        self.display_window_contents = []
        self.close_atig = False

        if self.is_in_alembic_directory() and self.alembic_is_installed():
            # first run ls, get all self.migrations and all hashes
            self.migrations = os.listdir('alembic/versions/')
            self.migrations = map(
                lambda x: Migration('alembic/versions/' + x),
                filter(self.valid_migration.match, self.migrations))
            self.migration_collection = MigrationCollection(
                list(self.migrations))
            self.migrations = list(self.migration_collection.list_migrations())

    def init_screen(self, stdscr):
        self.stdscr = stdscr

        self.k = 0
        self.cursor_x = 0
        self.cursor_y = 0

        # Clear and refresh the screen for a blank canvas
        self.stdscr.clear()
        self.stdscr.refresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        self.event_loop()

    def process_input(self):
        if self.k == curses.KEY_DOWN:
            self.cursor_y = self.cursor_y + 1
        elif self.k == curses.KEY_UP:
            self.cursor_y = self.cursor_y - 1
        elif self.k == curses.KEY_RIGHT:
            self.cursor_x = self.cursor_x + 1
        elif self.k == curses.KEY_LEFT:
            self.cursor_x = self.cursor_x - 1
        elif self.k in [curses.KEY_ENTER, 10, 13]:
            self.debug_message = ''
            self.window_open = True
            self.display_window = curses.newwin(0, self.width // 2, 0,
                                                self.width // 2)
            if self.cursor_y >= 1 and self.cursor_y <= len(self.migrations):
                curr = self.migrations[self.cursor_y - 1]
                self.debug_message = curr.hash
                self.display_window_contents = curr.contents.split(
                    '\n')[:self.height - 2]
            else:
                self.debug_message = 'no migration selected'
        elif self.k == ord('q'):
            if self.window_open:
                self.window_open = False
                self.display_window.erase()
                self.display_window.refresh()
                self.debug_message = ''
                self.display_window_contents = []
            else:
                self.close_atig = True
        self.cursor_x = max(0, self.cursor_x)
        self.cursor_x = min(self.width - 1, self.cursor_x)
        self.cursor_y = max(0, self.cursor_y)
        self.cursor_y = min(self.height - 1, self.cursor_y)

    def render_status_bar(self):
        statusbarstr = f"Press 'q' to exit | {self.debug_message} | Pos: {self.cursor_x}, {self.cursor_y}"

        # Render status bar
        self.stdscr.attron(curses.color_pair(3))
        self.stdscr.addstr(self.height - 1, 0, statusbarstr)
        self.stdscr.addstr(self.height - 1, len(statusbarstr),
                           " " * (self.width - len(statusbarstr) - 1))
        self.stdscr.attroff(curses.color_pair(3))

    def event_loop(self):
        # Initialization
        self.stdscr.clear()
        self.height, self.width = self.stdscr.getmaxyx()
        # Loop where k is the last character pressed

        while (not self.close_atig):
            self.render_status_bar()
            if not self.alembic_is_installed():
                self.render_alembic_install_error()
            # check if we are in the right directory
            elif self.is_in_alembic_directory():
                self.fetch_migration_information()
            else:
                self.render_directory_error()

            self.stdscr.move(self.cursor_y, self.cursor_x)
            # Refresh the screen
            self.stdscr.refresh()
            if self.window_open:
                for i, row in enumerate(self.display_window_contents):
                    self.display_window.addstr(i + 1, 1,
                                               row[:(self.width // 2) - 2])
                self.display_window.border()
                self.display_window.refresh()

            # Wait for next input
            self.k = self.stdscr.getch()
            self.process_input()
        curses.endwin()

    def fetch_migration_information(self):
        title = "Alembic Migrations"[:self.width - 1]
        start_x_title = int((self.width // 2) - (len(title) // 2) -
                            len(title) % 2)
        # Turning on attributes for title
        self.stdscr.attron(curses.color_pair(2))
        self.stdscr.attron(curses.A_BOLD)

        # Rendering title
        self.stdscr.addstr(0, start_x_title, title)

        # Turning off attributes for title
        self.stdscr.attroff(curses.color_pair(2))
        self.stdscr.attroff(curses.A_BOLD)

        # finally we need to render them on the screen
        for i, migration in enumerate(
                self.migration_collection.list_migrations()):
            self.stdscr.addstr(1 + i, 0, migration.date, curses.color_pair(0))
            if self.migration_collection.current in migration.name:
                self.stdscr.attron(curses.color_pair(2))
                self.stdscr.attron(curses.A_BOLD)
                self.stdscr.addstr(1 + i, 20,
                                   migration.stringify() + ' (curr)',
                                   curses.color_pair(2))
                self.stdscr.attroff(curses.color_pair(2))
                self.stdscr.attroff(curses.A_BOLD)
            else:
                self.stdscr.addstr(1 + i, 20, migration.stringify(),
                                   curses.color_pair(1))

    def render_alembic_install_error(self):
        self.render_error("Alembic is not Installed")

    def render_directory_error(self):
        self.render_error("Not In Valid Alembic Directory")

    def render_error(self, message):
        # Declaration of strings
        title = message[:self.width - 1]
        keystr = "Press q to exit"[:self.width - 1]
        # Centering calculations
        start_x_title = int((self.width // 2) - (len(title) // 2) -
                            len(title) % 2)
        start_x_keystr = int((self.width // 2) - (len(keystr) // 2) -
                             len(keystr) % 2)
        start_y = int((self.height // 2) - 2)

        # Turning on attributes for title
        self.stdscr.attron(curses.color_pair(2))
        self.stdscr.attron(curses.A_BOLD)

        # Rendering title
        self.stdscr.addstr(start_y, start_x_title, title)

        # Turning off attributes for title
        self.stdscr.attroff(curses.color_pair(2))
        self.stdscr.attroff(curses.A_BOLD)

        # Print rest of text
        self.stdscr.addstr(start_y + 3, (self.width // 2) - 2, '-' * 4)
        self.stdscr.addstr(start_y + 5, start_x_keystr, keystr)

    def is_in_alembic_directory(self):
        return os.path.exists('alembic') and \
           os.path.exists('alembic/versions')

    def alembic_is_installed(self):
        return os.popen('which alembic').read() != ''


def main():
    atig = Atig()
    curses.wrapper(atig.init_screen)


if __name__ == "__main__":
    main()
