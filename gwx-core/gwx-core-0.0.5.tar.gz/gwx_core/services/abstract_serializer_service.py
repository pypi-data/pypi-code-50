import datetime


class AbstractSerializerService:
    """The serializer class that will handle the formatting of data to readable formats:
    ie: json, dict, List.
    """

    # The list of field enlisted for serialization.
    __serializable__: list = None

    # The list of default values regardless of the object defined.
    __default__fields__: list = None

    def __init__(self):
        if self.__serializable__ is None:
            raise NotImplementedError('Serializable attribute is None, serializable fields must be defined.')

        if self.__default__fields__ is None:
            self.__default__fields__ = []

    def __get_serializable(self):
        return self.__serializable__ + self.__default__fields__

    @staticmethod
    def __to_date(date: datetime.datetime, date_only=False) -> str:
        """Date.date obj converter, returns string value of formatted datetime.datetime obj.

        note: We will mode this method to gwx-core/utils package

        :param date: The datetime.datetime object
        :param date_only: bool flag, decides if the return value is only date or includes it's timestamp
        :return:
        """
        return str(date).split('.')[0]

    def to_json(self) -> dict:
        """Converts the obj to a serialized dict obj as {key: value}.

        :return: serialized attributes as dict obj
        """
        result = {}
        filters = self.__serializable__ + self.__default__fields__

        for key in dir(self):
            if key in filters:
                value = self.__getattribute__(key)

                result.update([(key, value)])

                if type(value) == datetime.datetime:
                    result.update([(key, self.__to_date(value))])

        return result
