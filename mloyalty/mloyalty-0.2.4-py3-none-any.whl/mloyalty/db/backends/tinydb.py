from tinydb import TinyDB, Query


class MloyaltyTinyDB:
    """
    Класс для сохранения и получения данных из однофайловой базы данных TinyDB.
    """
    data = None

    def save(self):
        with TinyDB('db.json') as db:
            db.purge()
            doc_id = db.insert(
                {
                    'name': 'mloyalty',
                    'access_token': self.data['access_token'],
                    'token_type': self.data['token_type'],
                    'expires_in': self.data['expires_in'],
                    'refresh_token': self.data['refresh_token'],
                 }
            )

        return doc_id

    @staticmethod
    def get(doc_id=None):
        with TinyDB('db.json') as db:
            query = Query()
            if doc_id:
                mloyalty = db.get(doc_id=doc_id)
            else:
                mloyalty = db.get(query.name == 'mloyalty')

        return mloyalty
