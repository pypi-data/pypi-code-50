import sqlite3
import random
import os
import time


default_filename = 'sqlite_counter.db'

class SqliteCounter():
    def __init__(self, filename):
        if not os.path.isfile(filename):
            self.db_init(filename)
        else:
            self.con = sqlite3.connect(filename)

    def next(self):
        with self.con:
            self.con.execute('UPDATE counter SET value = (value + 1) % 4294967295')
            for row in self.con.execute('SELECT value FROM counter WHERE name="stg"'):
                return row[0]

    def db_init(self, filename):
        self.con = sqlite3.connect(filename)
        with self.con:
            self.con.execute('CREATE TABLE counter (id PRIMARY KEY, value integer, name varchar)')
            self.con.execute('INSERT INTO counter VALUES (1,0,"stg")')

def work():
    counter = SqliteCounter(default_filename)
    pid = os.getpid()
    for num in range(1, 25):
        wait_time = random.randint(0, 2)
        time.sleep(wait_time/100.0)
        res = counter.next()
        print('{}: {}'.format(pid, res))

if __name__ == '__main__':
    work()
