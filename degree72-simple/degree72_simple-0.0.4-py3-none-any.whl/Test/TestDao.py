from Core.DaoBase import DaoBase


class TestDao(DaoBase):
    def __init__(self, **kwargs):
        super(TestDao, self).__init__(**kwargs)
        self.connect_to_mongo()


    def save(self, source_block):
        self.save_to_mongo(source_block)

    def save_to_mongo(self, data_block):
        self.db= self.mongo_client['GoogleMapPopularity']
        self.collection = self.db['data']
        self.collection.insert_one(data_block)
