from kakeibox_database_sqlite3.models.base import BaseModel
from kakeibox_database_sqlite3.models.transaction_subcategory \
    import TransactionSubcategoryModel
from kakeibox_database_sqlite3.models.account import AccountModel
from kakeibox_database_sqlite3.models.transaction_type \
    import TransactionTypeModel
from kakeibox_database_sqlite3.storage import database
from kakeibox_database_sqlite3.utils.datetime import from_timestamp_to_datetime
from peewee import CharField, AutoField, ForeignKeyField, \
    TextField, DoubleField, TimestampField
from datetime import datetime
import copy


class TransactionModel(BaseModel):
    class Meta:
        database = database
        table_name = "kakeibox_core_transaction"

    id = AutoField(unique=True, primary_key=True, null=False)
    account_id = ForeignKeyField(
        model=AccountModel, field='id', null=False,
        lazy_load=True, on_delete='RESTRICT', on_update='CASCADE')
    transaction_subcategory_id = ForeignKeyField(
        model=TransactionSubcategoryModel, field='id', null=False,
        lazy_load=True, on_delete='RESTRICT', on_update='CASCADE')
    transaction_type_id = ForeignKeyField(
        model=TransactionTypeModel, field='id', null=False, lazy_load=True,
        on_delete='RESTRICT', on_update='CASCADE')
    uuid = CharField(max_length=36, unique=True, null=False)
    description = TextField(null=False)
    reference_number = CharField(null=True, max_length=128)
    amount = DoubleField(null=False)
    record_hash = CharField(null=False, max_length=64)
    timestamp = TimestampField(null=False)

    def to_dictionary(self):
        transaction_type_code = self.transaction_type_id.code
        transaction_subcategory_code = self.transaction_subcategory_id.code
        account_uuid = self.account_id.uuid
        dict_record = super(TransactionModel, self).to_dictionary()
        del dict_record['transaction_type_id']
        del dict_record['transaction_subcategory_id']
        del dict_record['account_id']
        dict_record['transaction_subcategory_code'] = \
            transaction_subcategory_code
        dict_record['transaction_type_code'] = transaction_type_code
        dict_record['account_uuid'] = account_uuid
        if isinstance(self.timestamp, datetime):
            dict_record['timestamp'] = int(self.timestamp.timestamp())
        dict_record['uuid'] = str(self.uuid)
        return dict_record

    def to_update_values_dict(self):
        transaction_type_id = self.transaction_type_id.id
        transaction_subcategory_id = self.transaction_subcategory_id.id
        account_id = self.account_id.id
        dict_record = super(TransactionModel, self).to_dictionary()
        dict_record['transaction_type_id'] = transaction_type_id
        dict_record['transaction_subcategory_id'] = transaction_subcategory_id
        dict_record['account_id'] = account_id
        if isinstance(self.timestamp, datetime):
            dict_record['timestamp'] = int(self.timestamp.timestamp())
        dict_record['uuid'] = str(self.uuid)
        return dict_record

    @classmethod
    def from_dictionary(cls, dict_data):
        dict_data = copy.deepcopy(dict_data)
        dict_data['account_id'] = cls._get_account_by_uuid(
            dict_data['account_uuid']
        ).id
        dict_data['transaction_type_id'] = cls._get_transaction_type_by_code(
            dict_data['transaction_type_code']
        ).id
        dict_data['transaction_subcategory_id'] = \
            cls._get_transaction_subcategory_by_code(
            dict_data['transaction_subcategory_code']
        ).id
        dict_data['timestamp'] = from_timestamp_to_datetime(
            dict_data['timestamp'])
        return cls(**dict_data)

    @staticmethod
    def _get_account_by_uuid(uuid):
        return AccountModel.get(AccountModel.uuid == uuid)

    @staticmethod
    def _get_transaction_type_by_code(code):
        return TransactionTypeModel.get(TransactionTypeModel.code == code)

    @staticmethod
    def _get_transaction_subcategory_by_code(code):
        return TransactionSubcategoryModel.get(
            TransactionSubcategoryModel.code == code)

    @staticmethod
    def _get_account_by_code(code):
        return TransactionSubcategoryModel.get(
            TransactionSubcategoryModel.code == code)

    @staticmethod
    def clean_dictionary(dict_data):
        cleaned_data = BaseModel.clean_dictionary(dict_data)
        del cleaned_data['transaction_type_code']
        del cleaned_data['transaction_subcategory_code']
        return cleaned_data

    @staticmethod
    def get_transaction_type_by_code(code):
        return TransactionTypeModel.get(
            TransactionTypeModel.code == code)
