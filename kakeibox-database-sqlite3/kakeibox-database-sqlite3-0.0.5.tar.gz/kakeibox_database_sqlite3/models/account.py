from kakeibox_database_sqlite3.models.base import BaseModel
from kakeibox_database_sqlite3.storage import database
from peewee import AutoField, CharField, TextField


class AccountModel(BaseModel):
    class Meta:
        database = database
        table_name = "kakeibox_core_account"

    id = AutoField(unique=True, primary_key=True, null=False)
    uuid = CharField(max_length=36, unique=True, null=False)
    name = TextField(null=False)
    description = TextField(null=False)
