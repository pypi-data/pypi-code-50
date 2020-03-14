from kakeibox_database_dictionary.engine import TableTransaction
from kakeibox_database_dictionary.database.transaction import TransactionDatabase
from datetime import datetime
from faker import Faker


def _before_execute_test():
    database = TableTransaction()
    database.table = {}


def test_transaction_new(transaction_data):
    _before_execute_test()
    count = 1
    for dictionary in transaction_data.values():
        bridge = TransactionDatabase()
        result = bridge.new(dictionary)
        assert isinstance(result, dict)

        database = TableTransaction()
        assert count == len(database.table)

        expected = database.table[dictionary['uuid']]
        assert expected == dictionary
        count += 1


def test_transaction_list(transaction_data):
    start_time = int(datetime(2019, 8, 1, 0, 0).timestamp())
    end_time = int(datetime(2019, 8, 30, 23, 59).timestamp())
    _before_execute_test()
    database = TableTransaction()
    database.table = transaction_data

    bridge = TransactionDatabase()
    item_list = bridge.list(start_time, end_time)

    assert 4 == len(item_list)

    for element in item_list:
        expected = database.table[element['uuid']]
        assert expected == element
        assert isinstance(element, dict)


def test_transaction_list_per_category(
        transaction_type_data, transaction_data):
    start_time = int(datetime(2018, 8, 1, 0, 0).timestamp())
    end_time = int(datetime(2020, 8, 30, 23, 59).timestamp())
    _before_execute_test()
    database = TableTransaction()
    database.table = transaction_data
    for transaction_type in transaction_type_data:
        bridge = TransactionDatabase()
        item_list = bridge.list_per_type(
            start_time, end_time, transaction_type)
        for element in item_list:
            assert transaction_type == element['transaction_type_code']
            assert isinstance(element, dict)


def test_transaction_update(transaction_data):
    _before_execute_test()
    faker = Faker()
    database = TableTransaction()
    database.table = transaction_data
    uuid = list(transaction_data)[0]

    item = transaction_data[uuid]
    item["amount"] = faker.pyfloat()
    item["description"] = faker.sentence()
    item["record_hash"] =\
        "5c045367896db776c043ca715c659d41030fab651d9f7cace4da04d280eaaaab"
    item["reference_number"] = "VEJT4503634011670"
    item["timestamp"] = 1564510129
    item["transaction_subcategory_code"] = 'BOK'
    item["transaction_type_code"] = 'INC'

    bridge = TransactionDatabase()
    result = bridge.update(uuid, item)

    assert isinstance(result, dict)
    assert result == item


def test_transaction_delete(transaction_data):
    _before_execute_test()
    database = TableTransaction()
    database.table = transaction_data
    total = len(database.table)
    uuid = list(transaction_data)[0]
    assert uuid in database.table

    bridge = TransactionDatabase()
    result = bridge.delete(uuid)
    assert isinstance(result, bool)
    assert uuid not in database.table
    assert (total - 1) == len(database.table)
