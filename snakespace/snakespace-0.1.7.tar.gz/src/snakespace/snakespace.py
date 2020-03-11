import sys
import _collections_abc
from functools import wraps

class SnakeSpace(_collections_abc.Sequence):
    """
    SnakeSpace is a class that constructs strings from attributes, args, and kwargs

    SnakeSpaces can also be operated on with other SnakeSpaces like namespaces
    """
    
    def __init__(self, seq=[], seperator='.', prefix=False, suffix=False):
        """Initialize a SnakeSpace object
        """

        self.__seperator = seperator

        ## Initialize 
        if isinstance(seq, str):
            self.___data = seq.split(seperator)
        elif isinstance(seq, SnakeSpace):
            self.___data = seq.___data
        else:
            self.___data = seq

        ## Add prefix based if it's a bool, else make it custom
        if isinstance(prefix, bool):
            self.__prefix = __seperator if prefix else ""
        else:
            self.__prefix = prefix

        ## Add suffix based if it's a bool, else make it custom
        if isinstance(suffix, bool):
            self.__suffix = __seperator if suffix else ""
        else:
            self.__suffix = suffix
    
    @property
    def seperator(self):
        """seperator is the value between each piece of data
        """
        return self.__seperator
    
    @seperator.setter
    def seperator(self, val):
        """set the value for the seperator
        """
        self.__seperator = val
    
    @property
    def __data(self):
        """Accessing the data joins it as a string
        """
        return self.__prefix + self.__seperator.join(self.___data) + self.__suffix
        
    def __getattr__(self, attr):
        """Getting an attribute creates a new copy of SnakeSpace adding the attribute
        """
        return SnakeSpace(self.___data + [attr], self.__seperator, self.__prefix, self.__suffix)
        
    def s(self, *args, **kwargs):
        """Create a new SnakeSpace adding the string representation of args/kwargs
        """
        result_str = list(args) + list(kwargs.values())
        if len(result_str):
            return SnakeSpace(SnakeSpace(self.___data + list(map(str, result_str))),
                              self.__seperator,
                              self.__prefix,
                              self.__suffix)
        return SnakeSpace(self.___data,
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)
    
    def __str__(self):
        """Return the string representation of the data
        """
        return str(self.__data)

    def __repr__(self):
        """Return the representation of the data
        """
        return repr(self.__data)

    def __int__(self):
        """Return the int representation of the data
        """
        return int(self.__data)

    def __float__(self):
        """Return the float representation of the data
        """
        return float(self.__data)

    def __complex__(self):
        """Return the complex representation of the data
        """
        return complex(self.__data)

    def __hash__(self):
        """Return the hash representation of the data
        """
        return hash(self.__data)
    
    def __eq__(self, string):
        """Equate SnakeSpace data or the string
        """
        if isinstance(string, SnakeSpace):
            return self.__data == string.__data
        return self.__data == string

    def __ne__(self, string):
        """Opposite of eq
        """
        return not (self.__data == string)
    
    def __lt__(self, string):
        """Compare SnakeSpace data or string
        """
        if isinstance(string, SnakeSpace):
            return self.__data < string.__data
        return self.__data < string
    
    def __le__(self, string):
        """Compare SnakeSpace data or string
        """
        if isinstance(string, SnakeSpace):
            return self.__data <= string.__data
        return self.__data <= string
    
    def __gt__(self, string):
        """Compare SnakeSpace data or string
        """
        if isinstance(string, SnakeSpace):
            return self.__data > string.__data
        return self.__data > string
    
    def __ge__(self, string):
        """Compare SnakeSpace data or string
        """
        if isinstance(string, SnakeSpace):
            return self.__data >= string.__data
        return self.__data >= string
    
    def __contains__(self, char):
        """Compare SnakeSpace data or string
        """
        if isinstance(char, SnakeSpace):
            return self.___data == char.___data[:len(self.___data)]
        return char in self.__data

    def __len__(self):
        """Get the length not of the string, but of the underlying data
        """
        return len(self.___data)
    
    def __getitem__(self, index):
        """Get the item not of the string but the underlying data
        """
        return self.___data[index]
    
    def __add__(self, other):
        """Add SnakeSpace data together, otherwise string concat
        """
        if isinstance(other, SnakeSpace):
            return SnakeSpace(self.___data + other.___data,
                              self.__seperator,
                              self.__prefix,
                              self.__suffix)
        return self.__data + str(other)

    def __radd__(self, other):
        """Add snakespaces together like list concat, add string with string concat
        """
        if isinstance(other, SnakeSpace):
            return SnakeSpace(other.___data + self.___data,
                              other.__seperator,
                              other.__prefix,
                              other.__suffix)
        return str(other) + self.__data

    def __mod__(self, args):
        """Check if arg is the start of a snakespace without the prefix
        """
        return self.startswith(args)
    
    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return SnakeSpace(list(s.capitalize() for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def casefold(self):
        return SnakeSpace(list(s.casefold() for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def encode(self, encoding='utf-8', errors='strict'):
        encoding = 'utf-8' if encoding is None else encoding
        errors = 'strict' if errors is None else errors
        return self.__data.encode(encoding, errors)

    def endswith(self, suffix, start=0, end=sys.maxsize):
        if isinstance(suffix, SnakeSpace):
            return SnakeSpace(self.___data[start:end][-len(suffix):],
                              self.__seperator,
                              suffix.__prefix,
                              suffix.__suffix) == suffix
        return self.__data.endswith(suffix, start, end)

    def find(self, sub, start=0, end=sys.maxsize):
        """Find which space sub can be found in
        """
        return next((i for i, s in enumerate(self.___data)
                     if s[start:end].find(str(sub)) >= 0), -1)

    def index(self, sub, start=0, end=sys.maxsize):
        """Index without seperatros or normal string
        """
        result = self.find(sub, start, end)
        if result == -1:
            raise ValueError("Cannot find index for substring")
        return result

    def isalpha(self):
        return all(map(lambda s:s.isalpha(), self.___data))

    def isalnum(self):
        return all(map(lambda s:s.isalnum(), self.___data))

    def isascii(self):
        return all(map(lambda s:s.isascii(), self.___data))

    def isdecimal(self):
        return all(map(lambda s:s.isdecimal(), self.___data))

    def isdigit(self):
        return all(map(lambda s:s.isdigit(), self.___data))

    def isidentifier(self):
        return all(map(lambda s:s.isidentifier(), self.___data))

    def islower(self):
        return all(map(lambda s:s.islower(), self.___data))

    def isnumeric(self):
        return all(map(lambda s:s.isnumeric(), self.___data))

    def isprintable(self):
        return all(map(lambda s:s.isprintable(), self.___data))

    def isspace(self):
        return all(map(lambda s:s.isspace(), self.___data))

    def istitle(self): return all(map(lambda s:s.istitle(), self.___data))

    def isupper(self): return all(map(lambda s:s.isupper(), self.___data))

    def ljust(self, width, *args):
        return SnakeSpace(list(s.ljust(width, *args) for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def lower(self):
        return SnakeSpace(list(s.lower() for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def lstrip(self, chars=None):
        return SnakeSpace(list(s.lstrip() for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def partition(self, sep=None):
        """Partition each element and create a new SnakeSpace from the partitions
        """
        if sep == None:
            return self

        elements = list(list(filter(lambda s:s, s.partition(str(sep)))) for s in self.___data)
        return SnakeSpace(sum(elements, []),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def replace(self, old, new, maxsplit=sys.maxsize):
        """Replace spaces in SnakeSpace that match 'old' with 'new' in the same position 
        """
        indexes = list(i for i, s in enumerate(self.___data)
                       if s.find(str(old)) >= 0)

        if len(indexes):
            [self.___data.__setitem__(i, str(new)) for i in indexes[:maxsplit]]
        return self

    def rfind(self, sub, start=0, end=sys.maxsize):
        """Find which space sub can be found in, from the right
        """
        return next((i for i, s in reversed(list(enumerate(self.___data)))
                     if s[start:end].find(str(sub)) >= 0), -1)
    
    def rindex(self, sub, start=0, end=sys.maxsize):
        """Index which space sub can be found in, from the right
        """
        result = self.rfind(sub, start, end)
        if result == -1:
            raise ValueError("Cannot find index for substring")
        return result

    def rjust(self, width, *args):
        return SnakeSpace(list(s.rjust(width, *args) for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def rpartition(self, sep=None):
        if sep == None:
            return self

        elements = list(list(filter(lambda s:s, s.rpartition(str(sep))))
                        for s in self.___data[::-1])
        return SnakeSpace(sum(elements[::-1], []),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def rstrip(self, chars=None):
        return SnakeSpace(list(s.rstrip() for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)    

    def startswith(self, prefix, start=0, end=sys.maxsize):
        """Same at str.startswith but with string representation of __data
        """
        space = SnakeSpace(self.___data[start:end][:len(prefix)],
                           self.__seperator,
                           self.__prefix,
                           self.__suffix)
        if isinstance(prefix, SnakeSpace):
            return space == prefix
        return str(space) == prefix

    def strip(self, chars=None):
        return SnakeSpace(list(s.strip(chars) for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)    

    def swapcase(self):
        return SnakeSpace(list(s.swapcase() for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def title(self):
        return SnakeSpace(list(s.title() for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)
        
    def translate(self, *args):
        space = list(s.translate(s.maketrans(*map(str,args)))
                     for s in self.___data
                     if len(s.translate(s.maketrans(*map(str,args)))) > 0)
        return SnakeSpace(space,
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)

    def upper(self):
        return SnakeSpace(list(s.upper() for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)


    def zfill(self, width):
        return SnakeSpace(list(s.zfill(width) for s in self.___data),
                          self.__seperator,
                          self.__prefix,
                          self.__suffix)
