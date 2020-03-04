import datetime
from odoo_backup.models import Server
from odoo_backup.utils import backup_name_from_datetime
from odoo_backup.config import DATA_DIR

import os

def erase_backup(server_name, database_name, file_name):
    file_path = os.path.join(DATA_DIR, server_name, database_name, file_name)
    print('\tRemoving', file_path)
    os.remove(file_path)

def purge_duplicate_backup():
    servers = Server.all()
    cleared = 0
    for server in servers:
        print("Checking for duplicate backups for", server.name)
        for database_name in server.databases:
            backups_remaining = server.list_backups(database_name)
            while backups_remaining:
                # Take a backup
                backup = backups_remaining.pop()
                date = backup[0].date()
                # Compute the list of all backups of the same date
                backups_checking = [backup]
                i = 0
                while i < len(backups_remaining):
                    if backups_remaining[i][0].date() == date:
                        backups_checking.append(backups_remaining.pop(i))
                    i += 1
                if len(backups_checking) == 1:
                    continue
                print("Found {} duplicate backups for {}:{} at {}".format(
                    len(backups_checking),
                    server.name,
                    database_name,
                    date
                ))
                # Keep the oldest
                latest_backup_datetime = (max(backups_checking)[0])
                print("Only keep", latest_backup_datetime)
                # Remove the others from file system
                for b in backups_checking:
                    if b[0] != latest_backup_datetime:
                        file_name = backup_name_from_datetime(b[0])
                        erase_backup(server.name, database_name, file_name)
                        cleared += 1
    print("Duplicate backup purging finished: {} backups removed".format(cleared))


def purge_backups_retention(server, database_name):
    """Creates a list of backups to keep then erase others"""
    # Order all backups by chronological
    avail_backups = list(reversed(sorted(server.list_backups(database_name))))
    print("{}:{} has {} backups".format(server.name, database_name, len(avail_backups)))
    retention_config = server.databases.get(database_name)
    if retention_config is None:
        print("Retention policy not configured for {}:{}".format(server.name, database_name))
        exit(1)
    to_keep_backups = []
    # We assume the daily duplicate has already run
    # DAYS
    day = 0
    ind = 0
    last_date = None
    while day <= retention_config.getint('days') and ind < len(avail_backups):
        backup_datetime, _ = avail_backups[ind]
        if not last_date or backup_datetime <= last_date - datetime.timedelta(days=1):
            to_keep_backups.append(backup_datetime)
            last_date = backup_datetime
            day += 1
        ind += 1
    # WEEKS
    week = 0
    ind = 0
    last_date = None
    while week <= retention_config.getint('weeks') and ind < len(avail_backups):
        backup_datetime, _ = avail_backups[ind]
        if not last_date or backup_datetime <= last_date - datetime.timedelta(days=7):
            to_keep_backups.append(backup_datetime)
            last_date = backup_datetime
            week += 1
        ind += 1
    # MONTHS
    month = 0
    ind = 0
    last_date = None
    while month <= retention_config.getint('months') and ind < len(avail_backups):
        backup_datetime, _ = avail_backups[ind]
        if not last_date or backup_datetime < last_date - datetime.timedelta(days=30):
            to_keep_backups.append(backup_datetime)
            last_date = backup_datetime
            month += 1
        ind += 1
    print('found', day, 'days,', week, 'weeks and', month, 'months')
    # Now erase
    count = 0
    for b, _ in avail_backups:
        if b not in to_keep_backups:
            count += 1
            erase_backup(server.name, database_name, backup_name_from_datetime(b))
    print(count, "backups erased")


if __name__ == "__main__":
    purge_duplicate_backup()
    for server in Server.all():
        for database_name in server.databases:
            purge_backups_retention(server, database_name)
