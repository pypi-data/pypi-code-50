# coding: utf-8
"""
Chip'Heures Database
"""
import datetime
import sqlite3

import click

from chipheures_sos.model.oder import Order


def _parse_date_time(date_string):
    return None if date_string is None else datetime.datetime.strptime(date_string[:19], "%Y-%m-%d %H:%M:%S")


class Database(object):
    """Database Connection"""

    excluded_table_names = {u"alembic_version", u"beaker_cache"}

    def __init__(self, database):
        self._database = database
        self._conn = None

    def __enter__(self):
        self._conn = sqlite3.connect(self._database)
        return self

    def __exit__(self, type_, value_, traceback_):
        if self._conn is not None:
            conn = self._conn
            self._conn = None
            conn.close()

    def list_tables(self):
        cursor = self._conn.cursor()
        names = sorted(
            row[0]
            for row in cursor.execute('SELECT name FROM sqlite_master WHERE type = "table"')
            if row[0] not in self.excluded_table_names
        )
        count = len(names)
        msg = {0: u"No tables found.", 1: u"{count} table found:", 2: u"{count} tables found:"}[min(2, count)]
        click.secho(msg.format(count=count), fg="green")
        name_len = max(map(len, names))
        for name in names:
            rows = cursor.execute("SELECT COUNT(*) FROM `{name}`".format(name=name)).fetchall()
            count = rows[0][0]
            click.echo(u"- {name:<{name_len}} : {count:>6}".format(name=name, count=count, name_len=name_len))

    def get_orders(self):
        cursor = self._conn.cursor()
        orders = [
            Order.from_row(*row)
            for row in cursor.execute("SELECT uid, order_ref, project_cat, creation_date, close_date FROM `Order`")
        ]
        return orders

    def get_last_event_date(self, order):
        cursor = self._conn.cursor()
        sql = """
        SELECT CalEvent.event_end
        FROM `OrderPhase` INNER JOIN `CalEvent`
        ON OrderPhase.uid = CalEvent.order_phase_uid
        WHERE OrderPhase.order_uid = {order.uid}
        ORDER BY CalEvent.event_end DESC LIMIT 1
        """.format(
            order=order
        )

        row = next(iter(cursor.execute(sql)), None)
        return None if row is None else _parse_date_time(row[0])

    def close_order(self, order, close_date):
        sql = "UPDATE `Order` SET close_date = ? WHERE uid = ?"
        cursor = self._conn.cursor()
        cursor.execute(sql, (close_date.date().isoformat(), order.uid))
        self._conn.commit()
