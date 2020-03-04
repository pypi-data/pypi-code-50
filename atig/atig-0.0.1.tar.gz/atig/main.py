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

        if self.is_in_alembic_directory():
            # first run ls, get all self.migrations and all hashes
            self.migrations = os.listdir('alembic/versions/')
            self.migrations = map(lambda x: Migration('alembic/versions/' + x),
                             filter(self.valid_migration.match, self.migrations)
            )
            self.migration_collection = MigrationCollection(list(self.migrations))

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

    def event_loop(self):
        # Initialization
        self.stdscr.clear()
        self.height, self.width = self.stdscr.getmaxyx()
        # Loop where k is the last character pressed

        while (self.k != ord('q')):
            if self.k == curses.KEY_DOWN:
                self.cursor_y = self.cursor_y + 1
            elif self.k == curses.KEY_UP:
                self.cursor_y = self.cursor_y - 1

            self.cursor_x = max(0, self.cursor_x)
            self.cursor_x = min(self.width-1, self.cursor_x)

            self.cursor_y = max(0, self.cursor_y)
            self.cursor_y = min(self.height-1, self.cursor_y)


            # check if we are in the right directory
            if self.is_in_alembic_directory():
                self.fetch_migration_information()
            else:
                self.render_error()

            self.stdscr.move(self.cursor_y, self.cursor_x)
            # Refresh the screen
            self.stdscr.refresh()

            # Wait for next input
            self.k = self.stdscr.getch()
    


    def fetch_migration_information(self):
        title = "Alembic Migrations"[:self.width-1]
        start_x_title = int((self.width // 2) - (len(title) // 2) - len(title) % 2)
        # Turning on attributes for title
        self.stdscr.attron(curses.color_pair(2))
        self.stdscr.attron(curses.A_BOLD)

        # Rendering title
        self.stdscr.addstr(0, start_x_title, title)

        # Turning off attributes for title
        self.stdscr.attroff(curses.color_pair(2))
        self.stdscr.attroff(curses.A_BOLD)

        # finally we need to render them on the screen
        for i, migration in enumerate(self.migration_collection.list_migrations()):
            self.stdscr.addstr(1 + i, 0, migration.date, curses.color_pair(0))
            if self.migration_collection.current in migration.name:
                self.stdscr.attron(curses.color_pair(2))
                self.stdscr.attron(curses.A_BOLD)
                self.stdscr.addstr(1 + i, 20, migration.stringify() + ' (curr)', curses.color_pair(2))
                self.stdscr.attroff(curses.color_pair(2))
                self.stdscr.attroff(curses.A_BOLD)
            else:
                self.stdscr.addstr(1 + i, 20, migration.stringify(), curses.color_pair(1))
            


    def render_error(self):
        # Declaration of strings
        title = "Not In Valid Alembic Directory"[:self.width-1]
        keystr = "Press q to exit"[:self.width-1]
        # Centering calculations
        start_x_title = int((self.width // 2) - (len(title) // 2) - len(title) % 2)
        start_x_keystr = int((self.width // 2) - (len(keystr) // 2) - len(keystr) % 2)
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






def main():
    atig = Atig()
    curses.wrapper(atig.init_screen)

if __name__ == "__main__":
    main()
