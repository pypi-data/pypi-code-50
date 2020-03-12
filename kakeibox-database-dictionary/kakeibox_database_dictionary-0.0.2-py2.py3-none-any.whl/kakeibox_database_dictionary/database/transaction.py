from kakeibox_database_dictionary.engine import TableTransaction


class TransactionDatabase(object):

    def list(self, start_time, end_time):
        result = []
        transactions = TableTransaction()
        for key, item in transactions.table.items():
            if int(start_time) <= int(item['timestamp']) <= int(end_time):
                result.append(item)
        return result

    def list_per_type(self, start_time, end_time, transaction_type):
        result = []
        transactions = TableTransaction()
        for key, item in transactions.table.items():
            if int(start_time) <= int(item['timestamp']) <= int(end_time) and \
                    item['transaction_type_code'] == transaction_type:
                result.append(item)
        return result

    def new(self, new_data_dictionary):
        uuid = new_data_dictionary['uuid']
        transactions = TableTransaction()
        transactions.table[uuid] = new_data_dictionary
        return transactions.table[uuid]

    def update(self, uuid, update_dict_data):
        transactions = TableTransaction()
        if uuid in transactions.table:
            transactions.table[uuid].update(update_dict_data)
        return transactions.table[uuid]

    def delete(self, uuid):
        try:
            transactions = TableTransaction()
            del transactions.table[uuid]
            return True
        except Exception:
            return False

    def get_by_uuid(self, uuid):
        transactions = TableTransaction()
        return transactions.table[uuid]
