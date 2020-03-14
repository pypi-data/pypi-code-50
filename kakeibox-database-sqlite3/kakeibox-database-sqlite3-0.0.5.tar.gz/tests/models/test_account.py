from kakeibox_database_sqlite3.models.account import AccountModel


def test_account_model_from_dictionary(account_data):
    model = AccountModel.from_dictionary(account_data)

    assert account_data['uuid'] == model.uuid
    assert account_data['name'] == model.name
    assert account_data['description'] == model.description


def test_account_to_dictionary(account_data):
    model = AccountModel.from_dictionary(account_data)
    model_dict = model.to_dictionary()

    assert account_data == model_dict
