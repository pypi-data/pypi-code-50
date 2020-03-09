import re


class Args:
    options = {}

    def __init__(self):
        """
        Here, we define default value for each variable that can be passed
        to the kwargs.
        """
        self.page_number = None
        self.page_size = 30
        self.sort = None
        self.filter = None
        self.range = None
        self.from_page = None
        self.to_page = None
        self.pretty = False

    def hydrate_values(self, options):
        """
        This function will get from the options passed their values, and if
        they aren't correct, it will throw an error.
        """
        self.page_number = options.get("page_number", -1)
        if not isinstance(self.page_number, int):
            raise TypeError("page_number must be an int")
        if self.page_number > 0:
            self.from_page = self.page_number
            self.to_page = self.page_number
        else:
            self.from_page = options.get("from_page", 1)
            if not isinstance(self.from_page, int):
                raise TypeError("from_page must be an int")

            self.to_page = options.get("to_page", 1800)
            if not isinstance(self.to_page, int):
                raise TypeError("to_page must be an int")
        self.page_size = options.get("page_size", 30)
        if not isinstance(self.page_size, int):
            raise TypeError("page_size must be an int")
        elif self.page_size > 100:
            raise ValueError("page_size must be <= 100")
        if self.check_keywords(options) is False:
            return False
        else:
            self.sort = options.get("sort", False)
            self.filter = options.get("filter", False)
            self.range = options.get("range", False)
        self.check_keywords(options)

    def check_keywords(self, options):
        if "rules" not in options:
            return True
        if "sort" in options and self.sanitize_keyword_string(options.get("sort", "id"), options["rules"]) is False:
            raise ValueError("Wrong value for `sort` parameter: '" + options.get("sort", "id") + "'")
        if "filter" in options and self.sanitize_keyword_brackets(options.get("filter", "id"), options["rules"]) is False:
            raise ValueError("Wrong value for `filter` parameter: '" + options.get("filter", "id") + "'")
        if "range" in options and self.sanitize_keyword_range(options.get("range", "id"), options["rules"]) is False:
            """
            @todo Shorten error messages
            """
            raise ValueError("Wrong value for `range` parameter: '" + options.get("range", "id")[options.get("range", "id").find("[") + 1:options.get("range", "id").find("]")] + "'")
        return True

    def sanitize_keyword_string(self, string, rules):
        if not isinstance(string, str):
            raise ValueError("sort must be a String")
        keyword = string.split(',')
        for i, s in enumerate(keyword):
            keyword[i] = re.sub(r'-', '', s)
        return self.compare_with_rules(rules, keyword)

    def sanitize_keyword_brackets(self, string, rules):
        filter_asked = string[string.find("[") + 1:string.find("]")]
        if filter_asked not in rules:
            return False
        filters = string.split("=")[1]
        if self.are_ranges_ints(filters):
            return True
        else:
            raise ValueError("Error: One parameter for range isn't an string or it isn't in the rules.")

    def sanitize_keyword_range(self, string, rules):
        range_asked = string[string.find("[") + 1:string.find("]")]
        if range_asked not in rules:
            return False
        second = string.split(",")[1]
        first = string.split(",")[0].split("=")[1]
        if not self.is_an_int(first):
            raise ValueError("Error: First parameter for range parameter isn't an int.")
        if not self.is_an_int(second):
            raise ValueError("Error: Second parameter for range parameter isn't an int.")
        return True

    def are_ranges_ints(self, strg, search=re.compile(r'[^a-z0-9,]').search):
        return not bool(search(strg))

    def is_an_int(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def compare_with_rules(self, rules, keywords):
        for i, s in enumerate(keywords):
            if s not in rules:
                return False
        return True