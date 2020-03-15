class BaseDatatypeMapper(object):
    def __init__(self, datatype):
        self.datatype = datatype

    def map(self, value):
        """return the value and its condition_type
        ---
        ex) {"S": "Zac"}

        """
        res = {}
        res[self.datatype.condition_type] = self.resolve(value)
        return res

    def resolve(value):
        """returns the value resolved for dynamodb
        that is to say it is how the database expects
        it to be passed for all of the operations
        """
        pass

    def parse(self, mapped_dict):
        """extract the value from the mapped_dict
        This is the opposite of mapping. So when given
        {"S": "Zac"} it will return "Zac"
        """
        if mapped_dict.get('NULL') == True:
            return None
        return mapped_dict[self.datatype.condition_type]
