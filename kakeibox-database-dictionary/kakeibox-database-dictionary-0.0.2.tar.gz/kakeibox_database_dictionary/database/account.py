from kakeibox_database_dictionary.engine import TableAccount


class AccountDatabase(object):

    def list(self):
        accounts = TableAccount()
        return [item for item in accounts.table.values()]

    def new(self, new_data_dictionary):
        uuid = new_data_dictionary['uuid']
        accounts = TableAccount()
        accounts.table[uuid] = new_data_dictionary
        return accounts.table[uuid]

    def delete(self, uuid):
        try:
            accounts = TableAccount()
            del accounts.table[uuid]
            return True
        except Exception:
            return False

    def get_by_uuid(self, uuid):
        accounts = TableAccount()
        return accounts.table[uuid]

    def update(self, uuid, update_dict_data):
        accounts = TableAccount()
        if uuid in accounts.table:
            accounts.table[uuid] = update_dict_data
        return accounts.table[uuid]
