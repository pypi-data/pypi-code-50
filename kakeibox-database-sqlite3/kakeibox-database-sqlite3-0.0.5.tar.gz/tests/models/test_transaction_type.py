from kakeibox_database_sqlite3.models.transaction_type \
    import TransactionTypeModel


def test_transaction_type_model_from_dictionary(transaction_type_data):
    data = next(iter(transaction_type_data.values()))
    model = TransactionTypeModel.from_dictionary(data)

    assert data['code'] == model.code
    assert data['name'] == model.name


def test_transaction_type_model_to_dictionary(transaction_type_data):
    data = next(iter(transaction_type_data.values()))
    model = TransactionTypeModel.from_dictionary(data)
    model_dict = model.to_dictionary()

    assert data == model_dict
