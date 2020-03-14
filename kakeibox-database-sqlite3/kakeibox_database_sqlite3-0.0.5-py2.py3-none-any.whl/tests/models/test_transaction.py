from kakeibox_database_sqlite3.models.transaction import TransactionModel
from kakeibox_database_sqlite3.utils.datetime import from_timestamp_to_datetime
from copy import deepcopy


def test_transaction_model_from_dictionary(transaction_data):
    data = deepcopy(transaction_data)
    dict_transaction = next(iter(data.values()))
    transaction = deepcopy(dict_transaction)
    model = TransactionModel.from_dictionary(transaction)

    assert dict_transaction['uuid'] == model.uuid
    assert dict_transaction['account_uuid'] == model.account_id.uuid
    assert dict_transaction['description'] == model.description
    assert dict_transaction['amount'] == model.amount
    assert from_timestamp_to_datetime(dict_transaction['timestamp']) == \
        model.timestamp
    assert dict_transaction['reference_number'] == model.reference_number
    assert dict_transaction['record_hash'] == model.record_hash
    assert dict_transaction['transaction_type_code'] == \
        model.transaction_type_id.code
    assert dict_transaction['transaction_subcategory_code'] == model.\
        transaction_subcategory_id.code


def test_transaction_model_to_dictionary(transaction_data):
    data = deepcopy(transaction_data)
    dict_transaction = next(iter(data.values()))
    transaction = deepcopy(dict_transaction)
    model = TransactionModel.from_dictionary(transaction)
    model_dict = model.to_dictionary()

    assert dict_transaction == model_dict
