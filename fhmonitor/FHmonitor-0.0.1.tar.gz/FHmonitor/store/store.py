#
# The DB class is used as an abstract class so that different
# back ends can be used to store the data.

import pymongo  # Have implemented for mongodb.
import logging
logger = logging.getLogger(__name__)


class DB:
    def __init__(self):
        pass

    def save(self):

        pass

#
# Store the readings into mongodb.  I'm using mongodb that's on the
# same rasp pi that is running this script.
#


class MongoDB(DB):
    # e.g. path: "mongodb://localhost:27017/"
    # e.g. db: "FitHome"
    # e.g. collection: "microwave"
    # MongoDB is pretty accepting, so double check the inputs!
    def __init__(self, path_str, db_str, collection_str):
        super().__init__()
        self.collection = None
        try:
            client = pymongo.MongoClient(path_str)
            client.server_info()  # will throw an exception
        except Exception as err:
            logger.error("""Cannot connet to MongoDB.
                The error is: {}""".format(err))
            raise
        db = client[db_str]
        self.collection = db[collection_str]

    def save(self, data):
        if self.collection is None:
            logger.error(
                """The aggregate collection is set to None.
                Most likely Mongo DB is not running.
                Readings are not saved.""")
            return False
        result = self.collection.insert_one(data)
        return result.acknowledged


class FirebaseDB(DB):
    # TBD: We started using Firebase before Mongo which led to thinking
    # about abstracting where the readings were stored....
    # The path is set to the Firebase path...
    #   ts_str = str(int(time.time()))
    #     return 'https://' + self.project_id+'.firebaseio.com/' + \
    #         self.monitor_name+'/device_readings/'+plug_name+'/'+ts_str+'/.json'
    #

    pass
