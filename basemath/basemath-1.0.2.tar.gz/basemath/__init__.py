import string
import warnings
import functools

ORDER = [l for l in string.digits + string.ascii_uppercase + string.ascii_lowercase]
for i in range(1000): ORDER = ORDER + ['!'+str(i+1)+o for o in string.ascii_uppercase + string.ascii_lowercase]

@functools.total_ordering
class bNUM:
    """
    Create object to work with number of base you want
    bNUM object operates with list ORDER that consists of all possible
    elements to represent any-base numbers

    Parameters
    ----------
    - value (str/int/list or any iterable):
        if int  - decimal number you want to convert to base (# 0, 1, 2, 3, 4, 5, ...)
        if str  - string representation of converted decimal number (# '1010', 'FFFF', '11', '42aA', ...)
        if list or any iterable - list of chars and ints to represent converted decimal number.
        Also you can pass array of objects of class bNUM
        (# ['F', 'F', 'F'], ['1', '0', '1', '0'])
        Using str/list the highest bit need to be on the left

    - base (int):
        base of number to convert and use

    - length = None (int):
        the length of the resulting bnum (# len('03FC') == 4)

    - cut = None (int):
        the length to cutdown resulting bnum
    """
    def __init__(self, value : (int,str,list,'...'), base : int, length : int=None, cut : int=None):
        if type(base) != int or base < 0:
            raise Exception('base type needs to be int, got {}'.format(type(base)))
        super(bNUM, self).__setattr__('base', base)
        if type(value) == str:
            value = value.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', '')
            super(bNUM, self).__setattr__('array', [str(si) for si in value])
        elif type(value) == int:
            if value == 0:
                super(bNUM, self).__setattr__('array', ['0'])
            else:
                super(bNUM, self).__setattr__('array', de2array(value, base))
        elif hasattr(value, '__iter__') and type(value) != str:
            if any(isinstance(si, bNUM) for si in value):
                array = []
                for si in value:
                    if isinstance(si, bNUM): array += si.array
                    else: array.append(si)
                super(bNUM, self).__setattr__('array', array)
            else:
                super(bNUM, self).__setattr__('array', value.copy())
        else:
            raise Exception('value type needs to be str, int or iterable (or list of bNUMs), got {}'.format(type(value)))
        if length != None:
            if len(self) != length: self.copy_here(self.to_len(length))
        if cut != None:
            self.copy_here(self.cutdown(cut))

    def copy(self) -> 'bNUM':
        """
        Returns bnum with the same parameters

        Returns : bNUM
        -------
        """
        array = self.array
        return bNUM(array, self.base, len(array))
    
    def copy_here(self, bnum : 'bNUM') -> None:
        """
        Copies parameters of 'bnum' to this one

        Parameters
        ----------
            - bnum (bNUM):
                bnum with parameters to copy to this bnum
        """
        super(bNUM, self).__setattr__('array', bnum.array)
        super(bNUM, self).__setattr__('base', bnum.base)

    def cutdown(self, length : int) -> 'bNUM':
        """
        Cut bnum to length = 'length' using the operation of convolution:
        Until len(bnum) != 'length':
            create bnum with elements, that make the length of this bnum be bigger than 'length'
            create bnum with the rest elements of origin bnum
            get sum of created bnums
            cutdown resulting sum to length = 'length'

        # '11001'.2 -> cutdown(4) -> '1001'.2 + '0001'.2 = '1010'.2
        # '20'.10 -> cutdown(1) -> '2'.10 + '0'.10 = '3'.10

        Parameters
        ----------
            - length (int):
                the length of resulting bnum
        """
        bnum = self.copy()
        while len(bnum) > length:
            diff = len(bnum)-length
            rest = bnum[:length]
            bnum = bnum[length:]
            bnum = (rest + bnum).to_len(length)
        return bnum

    def split(self, k : int, length : int) -> list:
        """
        Return k bnums with length = 'length'

        Parameters
        ----------
            - k (int):
                the number by which to divide this bnum

            - length (int):
                the length of all resulting bnums

        Returns : list of bnums
        -------

        Examples
        --------
            bNUM('123456789', 10).split(9, 1) -> [(1).10, (2).10, (3).10, ..., (8).10, (9).10]
        """
        bnums = []
        for i in range(k):
            bnums.append(self.from_end(slice(i*length,(i+1)*length)))
        return bnums

    def cutzeros(self) -> 'bNUM':
        """
        Remove zeros from top ranks

        Returns : bNUM
        -------

        Examples
        --------
            bNUM('00000001', 2).cutzeros() -> bNUM('1', 2)
        """
        if self.get_decimal() == 0:
            return bNUM(0, self.base)
        new_array = self.array
        new_array = [str(si) for si in new_array]
        while True:
            index = -1
            try:
                index = new_array.index('0')
            except:
                break
            if index == 0:
                new_array.remove('0')
            else:
                break
        return bNUM(new_array, self.base)

    def from_end(self, index : (int, slice)) -> 'bNUM':
        """
        Get items by index starting for the highest rank

        Parameters
        ----------
            - index (int/slice):
                index of type int or slice to get item

        Returns : bNUM
        -------

        Examples
        --------
            bNUM('1011', 2).from_end(slice(0,2)) -> bNUM('10', 2)

            but bNUM('1011', 2)[0:2] -> bNUM('11', 2)
        """
        array = self.array
        return bNUM(array[index], self.base)

    def fill(self, value : (str, int)) -> None:
        """
        Fill this bnum with the 'value'
        Every element of this bnum will be replaced by 'value'

        Parameters
        ----------
            - value (int/str):
                string representation of value of actual integet to fill this bnum with
        """
        value = ORDER[ORDER.index(str(value))]
        for i in range(len(self)):
            self[i] = value

    def to_len(self, length : int, cutdown : bool=False) -> 'bNUM':
        """
        Cut this bnum to the length = 'length'
        The result length is different if there are zeros in the top rank (see examples)

        Parameters
        ----------
            - length (int):
                length of resulting bnum if it can be less than this bnum (see examples)

            - cutdown (bool):
                use cutdown operation to resulting bnum to cut it down to length = 'length'

        Returns : bNUM
        -------

        Examples
        --------
            bNUM('00042', 10, 5).to_len(2) -> bNUM('42', 10)
            but
            bNUM('123', 10).to_len(1) -> bNUM('123', 10)
            and
            bNUM('123', 10).to_len(1, True) -> (1 + 23 = 24; 2 + 4 = 6) -> bNUM('6', 10)

        See also
        --------
            bNUM.cutdown
        """
        cur_length = len(self)
        new_array  = self.array
        if cur_length < length:
            for i in range(length-cur_length):
                new_array = [0] + new_array
            return bNUM(new_array, self.base)
        return self.copy()

    def to_base(self, base : int) -> 'bNUM':
        """
        Return bnum with new base

        Parameters
        ----------
            - base (int):
                base of resulting bnum

        Returns : bNUM
        -------
        """
        decimal = self.get_decimal()
        return bNUM(decimal, base)

    def insert(self, index : int, value : (int, str)) -> None:
        """
        Inserts value into place with index using ranks increment to the left

        Parameters
        ----------
            - index (int):
                list like index

            - value (str/int):
                string representation of value you want to insert, or actually and integer from 0 to 9
        """
        index = self._revertindex(index)
        if type(value) == int:
            value = value % self.base
        else:
            value = ORDER.index(str(value))
        array = self.array
        array.insert(index, ORDER[value])
        super(bNUM, self).__setattr__('array', array)
            

    def append(self, value : (int, str)) -> None:
        """
        Append value to bnum, like in python list

        Parameters
        ----------
            - value (int/str):
                string representation of value you want to insert, or actually and integer from 0 to 9
        """
        self.insert(len(self), value)

    def get_decimal(self) -> int:
        """
        Get decimal of actual number of bnum

        Returns : int
        -------
        """
        result = 0
        array = self.array
        if all([str(si).isdigit() for si in array]):
            if all([int(si) == 0 for si in array]):
                return 0
        for i,s in enumerate(self):
            result += s()*(self.base**i)
        return result

    def shift(self, amount : int) -> 'bNUM':
        """
        Add amount of zeros to the start of number

        Parameters
        ----------
            - amount (int):
                The amount of zeros to append

        Returns : bNUM
        -------
        """
        new_array = self.array
        for i in range(amount): new_array += [0]
        return bNUM(new_array, self.base)

    def __iter__(self):
        array = reversed(self.array)
        array = [bNUM(si, self.base) for si in array]
        return iter(array)

    def _revertindex(self, index):
        if type(index) == slice:
            start = index.start if index.start == None  else (len(self) - index.start - 1 if index.start != 0 else None)
            stop  = index.stop  if index.stop  == None  else (len(self) - index.stop  - 1 if index.stop  != 0 else None)
            step  = -1          if index.step  == None  else -index.step
            index = slice(start, stop, step)
            return index
        else:
            if index < 0:
                return abs(index + 1)    
            return len(self) - index - 1

    def __getitem__(self, index, revert=True):
        if revert: index = self._revertindex(index)
        array = self.array[index]
        if hasattr(array, 'reverse'):
            array.reverse()
        return bNUM(array, self.base)

    def __setitem__(self, index, value):
        index = self._revertindex(index)
        if type(value) == int: value = value % self.base
        else: value = ORDER.index(str(value))
        array = self.array
        array[index] = ORDER[value]
        super(bNUM, self).__setattr__('array', array)

    def __getattr__(self, name):
        if name == 'array':   return self.__dict__[name].copy()
        if name == 'decimal': return self.get_decimal()
        if name == 'string':
            array = self.__dict__['array'].copy()
            return ''.join(str(si) for si in array)
        if name in self.__dict__: return self.__dict__[name]
        else: raise AttributeError('no attribute {}'.format(name))

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError('{} readonly attribute'.format(name))

    def __call__(self, value : (int,str)=0) -> int:
        """
        Return index of list ORDER

        Returns : int
        -------
        """
        return ORDER.index(self[value].__repr__())

    def __len__(self):
        return len(self.array)

    def __eq__(self, other : ('bNUM', str, int, list, 'iterable')):
        if type(other) == int: return self.get_decimal() == other
        if other == None: return False
        ready_self, ready_other = _prepare(self, other, self.base)
        if len(ready_self) == len(ready_other):
            for i in range(len(ready_self)):
                if str(ready_self.array[i]) != str(ready_other.array[i]):
                    return False
        else: return False
        return True

    def __gt__(self, other : ('bNUM', str, int, list, 'iterable')):
        if type(other) == int: return self.get_decimal() > other
        ready_self, ready_other = _prepare(self, other, base=self.base)
        if len(ready_self) > len(ready_other): return True
        if len(ready_other) > len(ready_self): return False
        if len(ready_self) == len(ready_other):
            for s,o in zip(ready_self, ready_other):
                s_n = s()
                o_n = o()
                if s_n > o_n:   return True
                elif s_n < o_n: return False
        return True

    def __add__(self, other : ('bNUM', str, int, list, 'iterable')) -> 'bNUM':
        ready_self, ready_other = _prepare(self, other, self.base)
        min_len  = min(len(ready_self), len(ready_other))
        rest     = 0
        result   = ready_self.copy() if min_len == len(ready_other) else ready_other.copy()
        result_i = None
        for i in range(min_len):
            result_i  = ready_self(i) + ready_other(i) + rest
            rest      = 1 if result_i >= self.base else 0
            result_i %= self.base
            result[i] = ORDER[result_i]
        if rest == 1:
            if i+1 == len(result):
                result.append(1)
            else:
                for k in range(i+1, len(result)):
                    result_i  = result(k) + rest
                    rest      = 1 if result_i >= self.base else 0
                    result_i %= self.base
                    result[k] = ORDER[result_i]
                    if rest == 0: break
        return result

    def __and__(self, other : ('bNUM', str, int, list, 'iterable')):
        """
        Bitwise multiplication
        """
        ready_self, ready_other = _prepare(self, other, self.base)
        min_len = min(len(ready_self), len(ready_other))
        result  = ready_self.copy() if min_len == len(ready_self) else ready_other
        for i in range(min_len):
            result[i] = (ready_self(i)*ready_other(i)) % self.base
        return result

    def __xor__(self, other : ('bNUM', str, int, list, 'iterable')):
        """
        Bitwise xor operation
        """
        ready_self, ready_other = _prepare(self, other, self.base)
        min_len = min(len(ready_self), len(ready_other))
        result  = ready_self.copy() if min_len != len(ready_self) else ready_other
        for i in range(min_len):
            result[i] = (ready_self(i)+ready_other(i)) % self.base
        return result

    def __or__(self, other : ('bNUM', str, int, list, 'iterable')):
        """
        Bitwise OR operation
        """
        ready_self, ready_other = _prepare(self, other, self.base)
        min_len = min(len(ready_self), len(ready_other))
        result  = ready_self.copy() if min_len != len(ready_self) else ready_other
        for i in range(min_len):
            result[i] = (ready_self(i) | ready_other(i)) % self.base
        return result

    def __sub__(self, other : ('bNUM', str, int, list, 'iterable')):
        ready_self, ready_other = _prepare(self, other, self.base)
        if len(ready_self) < len(ready_other):
            return self.decimal - other.decimal
        rest     = 0
        result   = self.copy()
        result_i = None
        for i in range(len(ready_other)):
            result_i = ready_self(i) - ready_other(i) - rest
            if result_i < 0:
                result_i = self.base - result_i
                rest = 1
            else:
                rest = 0
            result[i] = ORDER[result_i]
        if rest == 1:
            for k in range(i+1, len(result)):
                result_i = result[k] - rest
                if result_i < 0:
                    result_i = self.base - result_i
                    rest = 1
                else:
                    rest = 0
                result[k] = ORDER[result_i]
                if rest == 0: break
        return result

    def __mul__(self, other : ('bNUM', str, int, list, 'iterable')):
        ready_self, ready_other = _prepare(self, other, self.base)
        min_len   = min(len(ready_self), len(ready_other))
        results   = []
        rest      = 0
        min_array = ready_self  if len(ready_self) == min_len else ready_other
        max_array = ready_other if min_array == ready_self else ready_self
        for i,mi in enumerate(min_array):
            add_result = []
            if mi == 0: continue
            for ma in max_array:
                result_i  = mi()*ma()+rest
                rest      = int(result_i/self.base) if result_i >= self.base else 0
                result_i %= self.base
                add_result.insert(0, ORDER[result_i])
            if rest != 0:
                add_result.insert(0, ORDER[rest])
                rest = 0
            results.append(bNUM(add_result, self.base).shift(i))
        result = bNUM(0, self.base)
        for ri in results:
            result += ri
        return result

    def __str__(self):
        return '({}).{}'.format(self.string, self.base)

    def __repr__(self):
        return self.string
    
def _prepare(value1, value2, base=None):
    if not isinstance(value1, bNUM):
        value1 = bNUM(value1, base)
    if not isinstance(value2, bNUM):
        value2 = bNUM(value2, base)
    if value1.base != value2.base:
        value2 = value2.to_base(value1.base)
    return value1.cutzeros(), value2.cutzeros()

def de2array(decimal : int, base : int) -> list:
    """
    Return list of converted decimal elements
    """
    result = []
    while decimal >= base:
        element = decimal % base
        if element >= 10:
            element = ORDER[element]
        result.append(element)
        decimal = int(decimal/base)
    if decimal >= 10:
        decimal = ORDER[decimal]
    result.append(decimal)
    result.reverse()
    return result

def de2str(decimal : int, base : int) -> str:
    """
    Return string of converted decimal elements
    """
    array = de2array(decimal, base)
    return ''.join([str(si) for si in array])

def zeros(length : int, base : int) -> bNUM:
    """
    Return bNUM with length = 'length' and base = 'base' filled with zeros
    """
    return bNUM([0 for i in range(length)], base, length)

def ones(length : int, base : int) -> bNUM:
    """
    Return bNUM with length = 'length' and base = 'base' filled with ones
    """
    return bNUM([1 for i in range(length)], base, length)

def bnum_sum(bnums : list) -> bNUM:
    """
    Return sum of bnums in list
    """
    result = bnums[0]
    for bnum in bnums[1:]:
        result += bnum
    return result
