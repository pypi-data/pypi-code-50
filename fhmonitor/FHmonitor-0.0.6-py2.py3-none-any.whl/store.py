#
#

from FHmonitor.error_handling import handle_exception
import pymongo  # Have implemented for mongodb.
import logging
logger = logging.getLogger(__name__)


class Store:
    """The Store class is used as an abstract class so that
    different back ends - for example, mongodb ,CSV, or Firestore -
    can be used to store the active and reactive power readings
    from Circuit Setup's atm90e32 meter.
    """

    def __init__(self):
        pass

    def save(self):

        pass

################################################


class MongoDB(Store):

    """Implements the Store base class for mongo db.

    The __init__ method initializes a connection to the mongodb
    collection.  An exception occurs if the path_str does
    not connect to a running mongodb service.

    :param path_str: e.g.: "mongodb://localhost:27017/"
    :param db_str: Name of the db in mongodb, e.g.: "FitHome".
    :param collection_str: Name of the collection within the mongodb db
        e.g.: "aggregate"
    """

    def __init__(self, path_str, db_str, collection_str):
        super().__init__()
        self.collection = None
        try:
            client = pymongo.MongoClient(path_str)
            client.server_info()  # will throw an exception
        except Exception as err:
            e = f'Cannot connect.  The error is: {err}'
            handle_exception(e)
        db = client[db_str]
        self.collection = db[collection_str]

    def save(self, data):
        """Save the data to the connected mongo db.

        :param data: Dictionary containing active and
            reactive power readings.  e.g.:
            reading = {"Pa": Pa, "Pr": Pr, }
            Where Pa and Pr values were obtained using the
            FHmonitor module.

        :return: True if the readings are inserted into the
            collection. False if the collection does not
            exist or if inserting the readings fails.
        """

        if self.collection is None:
            # The text generates an error with make html.  Ignore it.
            # logger.error(
            #     "The aggregate collection is set to None." /
            #     "Most likely Mongo DB is not running." /
            #     "Readings are not saved.")

            return False
        try:
            self.collection.insert_one(data)
        except TypeError as e:
            handle_exception(e)
            return False

        return True


class FirebaseDB(Store):
    """Storing to Firebase is not implemented at this time.
    """
    # TBD: We started using Firebase before Mongo which led to thinking
    # about abstracting where the readings were stored....
    # The path is set to the Firebase path...
    #   ts_str = str(int(time.time()))
    #     return 'https://' + self.project_id+'.firebaseio.com/' + \
    #         self.monitor_name+'/device_readings/'+plug_name+'/'+ts_str+'/.json'
    #

    pass
