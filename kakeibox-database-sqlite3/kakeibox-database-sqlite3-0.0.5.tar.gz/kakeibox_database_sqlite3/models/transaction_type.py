from kakeibox_database_sqlite3.models.base import BaseModel
from kakeibox_database_sqlite3.storage import database
from peewee import CharField, AutoField


class TransactionTypeModel(BaseModel):
    class Meta:
        database = database
        table_name = "kakeibox_core_transaction_type"

    id = AutoField(unique=True, primary_key=True, null=False)
    code = CharField(unique=True, max_length=3, null=False)
    name = CharField(max_length=128, null=False)
