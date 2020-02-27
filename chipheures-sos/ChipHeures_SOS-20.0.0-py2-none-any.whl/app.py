# coding: utf-8
"""
Main Application Class
"""
import datetime
import os
from tempfile import mkstemp

import click

from chipheures_sos.db import Database


class App(object):
    debug = False
    dry_run = False

    def echo_debug(self, msg):
        if self.debug:
            click.secho(msg, fg="yellow")

    def list_tables(self, database):
        self.echo_debug("Running list_tables...")
        with Database(database) as db:
            db.list_tables()

    def list_orders(self, database, closed):
        self.echo_debug("Running list_orders...")

        def show_order(order_):
            return closed is None or (closed and order_.close_date) or (not closed and not order_.close_date)

        with Database(database) as db:
            orders = filter(show_order, db.get_orders())
            len_order_ref = max(map(len, (order.order_ref for order in orders)))
            for order in orders:
                if order.close_date:
                    fmt = u'Order #{order.uid:05d} : {order.order_ref:<{len_order_ref}} : {order.close_date:%Y-%m-%d}'
                else:
                    fmt = u'Order #{order.uid:05d} : {order.order_ref:<{len_order_ref}} : –'
                click.echo(fmt.format(len_order_ref=len_order_ref, order=order))

    def close_orders(self, database, max_date, period_days):
        if not self.dry_run:
            self.backup_database(database)
        max_date = max_date or datetime.datetime.now() - datetime.timedelta(days=period_days)
        self.echo_debug("Running close_orders...")
        #: :type db: chipheures_sos.db.Database
        count = 0
        with Database(database) as db:
            orders = db.get_orders()
            for order in orders:
                if order.close_date:
                    self.echo_debug(u"{order} is already closed at {order.close_date}".format(order=order))
                    continue
                last_even_date = db.get_last_event_date(order) or order.creation_date
                if last_even_date < max_date:
                    close_date = last_even_date + datetime.timedelta(days=1)
                    fmt = {
                        True: u"{order} should be closed at {close_date}",
                        False: u"{order} is closed at {close_date}",
                    }[self.dry_run]
                    click.echo(fmt.format(order=order, close_date=close_date))
                    if not self.dry_run:
                        db.close_order(order, close_date)
                    count += 1
                else:
                    self.echo_debug(u"{order} should not be closed".format(order=order))
        # fmt: off
        fmt = {
            True: {
                0: u"No order should be closed.",
                1: u"{count} order should be closed (use `--run` option to close them).",
                2: u"{count} orders should be closed (use `--run` option to close them).",
            },
            False: {
                0: u"No order is close.",
                1: u"{count} order is close.",
                2: u"{count} orders is close.",
            },
        }[self.dry_run][min(2, count)]
        # fmt: on
        click.echo(fmt.format(count=count))

    def backup_database(self, database):
        self.echo_debug("Running backup_database...")
        work_dir, basename = os.path.split(database)
        name, ext = os.path.splitext(basename)
        bak, backup_path = mkstemp(dir=work_dir, prefix="~" + name + ".", suffix=ext, text=False)
        try:
            with open(database, mode="rb") as src:
                os.write(bak, src.read())
        finally:
            os.close(bak)
        click.echo(u"Backup done: {backup_path}".format(backup_path=backup_path))
        return backup_path
