"""Datatypes class."""
from glob import iglob
from itertools import chain
from csv import DictReader
from csv import reader as CsvReader
from dataclasses import dataclass
import os

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DATATYPES_FILE = os.path.join(DIR_PATH, "datatypes", "datatypes.csv")
VALUE_DELIMITOR = ','


class NoSuchDatatype(Exception):
    """No datatype with that id."""

    pass


class Datatype:
    """Declare class."""

    pass


@dataclass
class Datavalue(object):
    """Data class for values."""

    id: str
    datatype: Datatype

    def translate(self, dialect):
        """Return translation."""
        return self.datatype.translate(self.id, dialect)


class Datatype(object):
    """Represent a datatype, initiated by id."""

    def __init__(self, id: str, domain: str = None):
        """Id is a datatype from datatypes.csv."""
        self.id = id
        self.domain = domain
        self.allowed_values = []
        self.translations = {}

        data = None
        with open(DATATYPES_FILE, "r") as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                if row["id"] == id:
                    data = row
                    break
        if data is None:
            raise(NoSuchDatatype)
        self.value_type = data["value_type"]
        self.description = data["description"]
        av = data["allowed_values"]
        # if domain:
        #     av += "/" + domain
        if av:
            for file_ in self._get_csv_files(av):
                with open(file_, "r") as csvfile:
                    reader = DictReader(csvfile)
                    dialect_names = [x[8:]
                                     for x in reader.fieldnames
                                     if x.startswith("dialect:")]
                    for row in reader:
                        translations = {x: None for x in dialect_names}
                        for d in dialect_names:
                            # parse this cell as a csv row
                            csvreader = CsvReader([row["dialect:" + d]],
                                                  delimiter=VALUE_DELIMITOR,
                                                  skipinitialspace=True,
                                                  strict=True)
                            values = next(csvreader)
                            translations[d] = values
                        value = Datavalue(row["id"], self)
                        self.allowed_values.append(value)
                        self.translations[row["id"]] = translations

    def _get_csv_files(self, domain):
        domain = os.path.join(*domain.split("/"))

        # We are fetching both by filename and dir name
        # so that regions/kenya will match anything in
        # `datatypes/values/regions/kenya/*.csv`
        # and/or `datatypes/values/regions/kenya.csv`
        #
        # There is probably an easier way to do this
        # FIXME the below function fetches /foo/bar/regions/kenya as well, but we probably want ^regions/kenya
        value_path_1 = os.path.join(DIR_PATH, "datatypes", "values", domain)
        value_path_2 = os.path.join(DIR_PATH, "datatypes", "values")
        files_1 = chain.from_iterable(iglob(os.path.join(root, '*.csv'))
                                      for root, dirs, files in os.walk(value_path_1))
        files_2 = chain.from_iterable(iglob(os.path.join(root, domain + '.csv'))
                                      for root, dirs, files in os.walk(value_path_2))
        for f in chain(files_1, files_2):
            yield f

    def translate(self, value, dialect):
        """Lookup a value in the translation dictionary."""
        return self.translations[value][dialect][0]

    def __str__(self):
        """Print as id."""
        return str(self.id)

    def __repr__(self):
        """Represent."""
        suffix = str(self)
        if self.domain:
            suffix += ":" + self.domain
        return f"<Datatype: {suffix}>"
