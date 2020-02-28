import datetime
import os
from odoo_backup.utils import backup_name_from_datetime
from odoo_backup.models import Server
from odoo_backup.config import DATA_DIR

def generate_fake_data(number=30):
    server = Server.all()[0]
    database_name = list(server.databases)[0]

    for i in range(number):
        dt = datetime.datetime(2019, 12, 31) - datetime.timedelta(days=i)
        filename = backup_name_from_datetime(dt)
        path = os.path.join(DATA_DIR, server.name, database_name, filename)
        print("Creating fake zip at", path)
        with open(path, 'wb') as file:
            file.write(b"1")

if __name__ == "__main__":
    generate_fake_data()