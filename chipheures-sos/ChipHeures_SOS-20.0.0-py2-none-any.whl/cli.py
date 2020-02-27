# coding: utf-8
"""
Command Line Interface
"""
import sys

import click

from chipheures_sos import __version__
from chipheures_sos.app import App


@click.group()
@click.version_option(__version__)
@click.option("--debug/--no-debug", default=False)
@click.pass_context
def cli(ctx, debug):
    """
    Tool for database maintenance of the Chip'heures web application.

    \f
    :param ctx:
    :param debug: debug flag
    """
    ctx.ensure_object(App)
    ctx.obj.debug = debug


@cli.command(name="list")
@click.argument("database", metavar="DB")
@click.pass_context
def list_tables(ctx, database):
    """
    List the database tables and show record counts.

    \b
    DB   path to the SQlite database to read.

    \f
    :param ctx:
    :param database: path to the database
    """
    #: :type app: chipheures_sos.app.App
    app = ctx.obj
    app.list_tables(database)


@cli.command(name="backup")
@click.argument("database", metavar="DB")
@click.pass_context
def backup_database(ctx, database):
    """
    Backup the database

    \b
    DB   path to the SQlite database to read.

    \f
    :param ctx:
    :param database: path to the database
    """
    #: :type app: chipheures_sos.app.App
    app = ctx.obj
    app.backup_database(database)


@cli.command(name="list_orders")
@click.argument("database", metavar="DB")
@click.option(
    "--closed/--not-closed", default=None, help=u"Display only closed/not closed orders", show_default=True,
)
@click.pass_context
def list_orders(ctx, database, closed):
    """
    List the orders and show the close date.

    \b
    DB   path to the SQlite database to read.

    \f
    :param ctx:
    :param database: path to the database
    """
    #: :type app: chipheures_sos.app.App
    app = ctx.obj
    app.list_orders(database, closed)


@cli.command(name="close_orders")
@click.argument("database", metavar="DB")
@click.option(
    "-d",
    "--date",
    "max_date",
    type=click.DateTime(["%Y-%m-%d"]),
    default=None,
    help=u"Close orders which are older than this date, if missing the date is detected by examining the tracked times",
)
@click.option(
    "--dry-run/--run", default=True, help=u"Dry run", show_default=True,
)
@click.option(
    "--period",
    "period_days",
    type=click.IntRange(1, 3650),
    default=365 // 2,
    help=u"Period (in days) from which we can consider an order is old",
    show_default=True,
    metavar="PERIOD",
)
@click.pass_context
def close_orders(ctx, database, max_date, dry_run, period_days):
    """
    Close the "old" orders.

    \b
    DB   path to the SQlite database to read.

    \f
    :param ctx:
    :param database: path to the database
    :param max_date: maximum date use to close an order (UTC time).
    :param dry_run: If ``True``, only show action, don't run it (database is preserved).
    :param period_days: Period (in days) from which we can consider an order is old
    """
    #: :type app: chipheures_sos.app.App
    app = ctx.obj
    app.dry_run = dry_run
    app.close_orders(database, max_date, period_days)


if __name__ == "__main__":
    cli(sys.argv[1:])
