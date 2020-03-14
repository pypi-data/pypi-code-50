from kakeibox_database_dictionary.engine import TableTransactionCategory
from kakeibox_database_dictionary.database.transaction_category import \
    TransactionCategoryDatabase
from faker import Faker


def _before_execute_test():
    database = TableTransactionCategory()
    database.table = {}


def test_transaction_category_new(transaction_category_data):
    _before_execute_test()
    count = 1
    for dictionary in transaction_category_data.values():
        bridge = TransactionCategoryDatabase()
        result = bridge.new(dictionary)
        assert isinstance(result, dict)

        database = TableTransactionCategory()
        assert count == len(database.table)

        expected = database.table[dictionary['code']]
        assert expected == dictionary
        count += 1


def test_transaction_category_list(transaction_category_data):
    _before_execute_test()
    database = TableTransactionCategory()
    database.table = transaction_category_data

    bridge = TransactionCategoryDatabase()
    item_list = bridge.list()

    assert len(database.table) == len(item_list)

    for element in item_list:
        expected = database.table[element['code']]
        assert expected == element
        assert isinstance(element, dict)


def test_transaction_category_update(transaction_category_data):
    _before_execute_test()
    faker = Faker()
    database = TableTransactionCategory()
    database.table = transaction_category_data
    code = list(transaction_category_data)[0]

    item = transaction_category_data[code]
    item['code'] = faker.month()
    item['name'] = faker.name()

    bridge = TransactionCategoryDatabase()
    result = bridge.update(code, item)

    assert isinstance(result, dict)
    assert result == item


def test_transaction_category_delete(transaction_category_data):
    _before_execute_test()
    database = TableTransactionCategory()
    database.table = transaction_category_data
    total = len(database.table)
    code = list(transaction_category_data)[0]
    assert code in database.table

    bridge = TransactionCategoryDatabase()
    result = bridge.delete(code)
    assert isinstance(result, bool)

    assert code not in database.table
    assert (total - 1) == len(database.table)
