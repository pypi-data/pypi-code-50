from kakeibox_database_sqlite3.models.transaction_category \
    import TransactionCategoryModel


def test_transaction_category_model_from_dictionary(transaction_category_data):
    data = next(iter(transaction_category_data.values()))
    model = TransactionCategoryModel.from_dictionary(data)

    assert data['code'] == model.code
    assert data['name'] == model.name


def test_transaction_category_to_dictionary(transaction_category_data):
    data = next(iter(transaction_category_data.values()))
    model = TransactionCategoryModel.from_dictionary(data)
    model_dict = model.to_dictionary()

    assert data == model_dict
