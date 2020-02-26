import os

import psycopg2

from meeshkan_hosted_secrets import access_secret_string


def connect_to_db():
    db_user = "postgres"
    db_name = "postgres"

    if os.environ.get("GAE_ENV") == "standard":
        db_connection_name = "sound-electron-268214:europe-west1:meeshkan"
        db_password = access_secret_string("cloud-sql-password")
        host = "/cloudsql/{}".format(db_connection_name)
    else:
        db_password = os.environ.get("MEESHKAN_CLOUD_SQL_PASSWORD")
        host = "127.0.0.1"
    return psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=host
    )
