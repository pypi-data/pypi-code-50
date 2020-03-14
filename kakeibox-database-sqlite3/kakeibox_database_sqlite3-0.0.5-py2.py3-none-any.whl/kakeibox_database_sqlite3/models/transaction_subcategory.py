from kakeibox_database_sqlite3.models.base import BaseModel
from kakeibox_database_sqlite3.models.transaction_category import \
    TransactionCategoryModel
from kakeibox_database_sqlite3.storage import database
from peewee import CharField, AutoField, ForeignKeyField
import copy


class TransactionSubcategoryModel(BaseModel):
    class Meta:
        database = database
        table_name = "kakeibox_core_transaction_subcategory"

    id = AutoField(unique=True, primary_key=True, null=False)
    transaction_category_id = ForeignKeyField(
        model=TransactionCategoryModel, field='id', null=False, lazy_load=True,
        on_delete='RESTRICT', on_update='CASCADE')
    code = CharField(unique=True, max_length=3, null=False)
    name = CharField(max_length=128, null=False)

    def to_dictionary(self):
        transaction_category_code = self.transaction_category_id.code
        dict_record = super(TransactionSubcategoryModel, self).to_dictionary()
        del dict_record['transaction_category_id']
        dict_record['transaction_category_code'] = transaction_category_code
        return dict_record

    def to_update_values_dict(self):
        transaction_category_id = self.transaction_category_id.id
        dict_record = super(TransactionSubcategoryModel, self).to_dictionary()
        dict_record['transaction_category_id'] = transaction_category_id
        return dict_record

    @classmethod
    def from_dictionary(cls, dict_data):
        dict_data = copy.deepcopy(dict_data)
        dict_data['transaction_category_id'] = \
            cls._get_transaction_category(
            dict_data['transaction_category_code']
        ).id
        cls.clean_dictionary(dict_data)
        return cls(**dict_data)

    @staticmethod
    def _get_transaction_category(code):
        model = TransactionCategoryModel
        return model.get(TransactionCategoryModel.code == code)

    @staticmethod
    def clean_dictionary(dict_data):
        cleaned_data = BaseModel.clean_dictionary(dict_data)
        if 'transaction_category_code' in cleaned_data:
            del cleaned_data['transaction_category_code']
        return cleaned_data

    @staticmethod
    def get_transaction_category_by_code(code):
        return TransactionCategoryModel.get(
            TransactionCategoryModel.code == code)
