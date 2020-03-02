import itertools

import click
from dateutil.parser import parse
from tabulate import tabulate

from pyqalx.core.signals import QalxSignal


def _get_bot_for_termination(qalx_session, name):
    """
    A utility function that, given a qalx_session and a bot name, will prompt
    the user for the specific bot that they wish to terminate
    :param qalx_session:An instance of QalxSession
    :param name:The name a of the bot that the user wishes to terminate
    :return:An instance of ~entities.bot.Bot
    """
    # First query to get all the bots that match the given name and have workers.
    # We will not have worker signal data at this point
    bots_with_name_and_workers = qalx_session.bot.find(
        query={
            "name": name,
            "workers": {"$exists": True, "$not": {"$size": 0}},
        },
        fields=["workers"],
    )

    potential_bots = []
    # Because we don't unpack when doing a `find` we need to do
    # an extra reload query for each bot so we can get the signal data
    for bot in bots_with_name_and_workers["data"]:
        potential_bots.append(qalx_session.bot.reload(bot))

    def _has_non_terminated_workers(_bot):
        # For each bot, we only return it if any of the
        # workers ARE NOT terminated.  As a separate function to avoid
        # nested lambdas
        # import pdb ;pdb.set_trace()
        return list(
            itertools.filterfalse(
                lambda x: QalxSignal(x).terminate, _bot["workers"]
            )
        )

    # We then filter the bots to only be those that have any workers that
    # don't have a terminated signal.
    bots_for_prompt = list(filter(_has_non_terminated_workers, potential_bots))

    if len(bots_for_prompt) == 1:
        # Only a single bot found matching the name and with active workers.
        # Just terminate it without showing the user the table of bots
        return bots_for_prompt[0]
    elif not len(bots_for_prompt):
        # No bots found.  Nothing to do!
        click.echo(f"No bots found called `{name}` that have active workers")
    else:
        # Many bots found matching the name and with active workers.
        # Create a table to allow the user to pick which they want
        table = []

        # Massage the remaining bots into a nice format for presentation
        for index, bot in enumerate(bots_for_prompt, start=1):
            created_on = parse(bot["info"]["created"]["on"]).strftime(
                "%d/%m/%Y %H:%M:%S"
            )
            table.append(
                [
                    index,
                    bot["name"],
                    bot["status"],
                    bot["host"].get("platform"),
                    bot["host"].get("node"),
                    len(bot["workers"]),
                    created_on,
                    bot["info"]["created"]["by"]["email"],
                ]
            )
        # We then display the remaining bots to the user in a list, and prompt them
        # for an index for the specific one they wish to shutdown.
        headers = [
            "Index",
            "Name",
            "Status",
            "Platform",
            "Node",
            "No. Workers",
            "Created On",
            "Created By",
        ]
        # Display a table of bots
        click.echo(tabulate(table, headers))
        index = 0
        # Wait until they choose an option that is valid.
        while index == 0 or index > len(table):
            index = click.prompt(
                "Please choose a bot index to terminate", type=int
            )

        # Get the bot from the index (-1 because the index the user chooses starts
        # at 1)
        return bots_for_prompt[index - 1]
