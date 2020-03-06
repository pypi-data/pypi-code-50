__all__ = ('validate_data', )


class __Validate(object):
    def __init__(self, filter_str: str, validate_obj: dict):
        self.parsed_filters = self.__parse_filters(filter_str)
        self.validate_obj = validate_obj

    def __parse_filters(self, filter_str: str):
        """
        :param filter_:
        :return: list of dicts/lists
        """
        parsed_filters = []
        if filter_str:
            filter_values = filter_str.split(",")
            for filters in filter_values:
                if filters:
                    if ";" in filters:  # check 'AND' statement
                        and_filters = []
                        for f in filters.split(";"):
                            and_filters.append(self.__create_filter_row(f.strip()))  # strip string for del spaces
                        parsed_filters.append(and_filters)  # return list of AND filters
                        continue
                    parsed_filters.append(self.__create_filter_row(filters.strip()))  # strip string for del spaces
        return parsed_filters

    # create one query for parse_filters
    def __create_filter_row(self, f: str):
        """
        :param f: string
        :return: dict
        """
        operators = {
            "=@": "in_",
            "!@": "not_in",
            "=$": "end",
            "=^": "start",
            "==": "eq",
            "!=": "not_eq"
        }
        for operator in operators:
            if operator in f:
                set = operators[operator]
                field, value = f.split(operator)
                return {"field": field, "value": value, "set": set}
        else:
            raise ValueError("invalid operator")

    def _validate_row(self, row: dict):
        exclude = False
        exist = False
        if row['field'].startswith('!'):
            exclude = True
            row['field'] = row['field'][1:]
        method = getattr(self, row['set'])
        check_value = self.validate_obj.get(row['field'])
        if check_value:
            exist = method(row['value'], check_value)
        return self.create_filter_result(exist, exclude)

    def validate_data(self):
        validated_result = []
        for filter_row in self.parsed_filters:
            if isinstance(filter_row, list):
                result = [self._validate_row(row) for row in filter_row]
                validated_result.append(all(result))
            else:
                validated_result.append(self._validate_row(filter_row))
        return any(validated_result)

    def in_(self, value, check_value):
        return value in check_value

    def not_in(self, value, check_value):
        return value not in check_value

    def start(self, value, check_value):
        return check_value.startswith(value)

    def end(self, value, check_value):
        return check_value.endswith(value)

    def eq(self, value, check_value):
        return check_value == value

    def not_eq(self, value, check_value):
        return check_value != value

    def create_filter_result(self, exist: bool, exclude: bool):
        """
        :return: bool
        """
        return exist ^ exclude


def validate_data(filter_str: str, validate_obj: dict):
    return __Validate(filter_str, validate_obj).validate_data()
