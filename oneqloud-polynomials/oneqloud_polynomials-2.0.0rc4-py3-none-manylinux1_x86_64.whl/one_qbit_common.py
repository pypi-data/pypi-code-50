
from . import _qdk_loader
from ._qdk_loader import *
for name in [n for n in _qdk_loader.__dict__ if n.startswith('_') and not n.startswith('__')]:
  globals()[name] = getattr(_qdk_loader, name)
globals()['__builtin__'] = getattr(_qdk_loader, '__builtin__')

del _qdk_loader
del name

def _swig_repr(self):
  try:
    strthis = "proxy of " + self.this.__repr__()
  except __builtin__.Exception:
    strthis = ""
  return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


class RandomGenerator(_object):
    """

    This class defines a random number generator capable of generating uniform
    samples of type int/float.

    Attributes:
        seed (int): the seed of an already seeded random generator.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RandomGenerator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RandomGenerator, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _qdk.new_RandomGenerator(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def get_binary_uniform(self):
        """

        Get a random sample from a uniform distribution on the binary set { 0 , 1 }.

        This function has the following signature: ::

            get_binary_uniform(self)

        Returns:
            bool: An boolean value sampled uniformly.

        """
        return _qdk.RandomGenerator_get_binary_uniform(self)


    def get_int_uniform(self, *args):
        """

        Get a random sample from uniform distribution on the integer range [0, max_exclusive)
        or [min,max).

        This function has the following signature: ::

            get_int_uniform(self,max_exclusive)
            get_int_uniform(self,min,max)

        Args:
            max_exclusive (int): upper bound on the interval for random number generation.
            min (int): inclusive lower bound of the range.
            max (int): exclusive upper bound of the range.

        Returns:
            int: Between [lower bound, upper bound)

        """
        return _qdk.RandomGenerator_get_int_uniform(self, *args)


    def get_double_uniform(self, *args):
        return _qdk.RandomGenerator_get_double_uniform(self, *args)

    def get_double_positive_uniform(self):
        """

        Get a random sample from the uniform distribution on (0, 1).


        This function has the following signature: ::

            get_double_positive_uniform(self)

        Returns:
            float: a non-zero double between 0,1 (exclusively on both ends).

        """
        return _qdk.RandomGenerator_get_double_positive_uniform(self)

    __swig_setmethods__["seed"] = _qdk.RandomGenerator_seed_set
    __swig_getmethods__["seed"] = _qdk.RandomGenerator_seed_get
    if _newclass:
        seed = _swig_property(_qdk.RandomGenerator_seed_get, _qdk.RandomGenerator_seed_set)
    __swig_destroy__ = _qdk.delete_RandomGenerator
    __del__ = lambda self: None
RandomGenerator_swigregister = _qdk.RandomGenerator_swigregister
RandomGenerator_swigregister(RandomGenerator)

class Timing(_object):
    """

    A set of timing information for a single action.

    Attributes:
        cpu_time (int): The total cpu time for the action to occur taking into
          account whether the action ran on multiple threads.
        elapsed_time (int): The total elapsed real time for the action to occur.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Timing, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Timing, name)
    __repr__ = _swig_repr

    def has_custom_time(self, key):
        return _qdk.Timing_has_custom_time(self, key)

    def get_custom_time(self, key):
        return _qdk.Timing_get_custom_time(self, key)

    def get_custom_times(self):
        val = _qdk.Timing_get_custom_times(self)

        return val.asdict()


        return val


    def get_included_timings(self):
        """

        Returns the timing objects of any actions performed within this action.,

        Return:
            list: The list of all included timing objects.

        """
        val = _qdk.Timing_get_included_timings(self)

        return list(val)


        return val


    def __repr__(self):
      res = "Timing (cpu_time: " + str(self.cpu_time)
      res += "ms, elapsed_time: " + str(self.elapsed_time)
      res += "ms, custom_times: " + str(self.get_custom_times())
      res += ", included_timings: " + str(self.get_included_timings())
      res += ")"
      return res

    __swig_getmethods__["cpu_time"] = _qdk.Timing_cpu_time_get
    if _newclass:
        cpu_time = _swig_property(_qdk.Timing_cpu_time_get)
    __swig_getmethods__["elapsed_time"] = _qdk.Timing_elapsed_time_get
    if _newclass:
        elapsed_time = _swig_property(_qdk.Timing_elapsed_time_get)

    def __init__(self):
        this = _qdk.new_Timing()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_Timing
    __del__ = lambda self: None
Timing_swigregister = _qdk.Timing_swigregister
Timing_swigregister(Timing)

class TimingVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, TimingVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, TimingVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _qdk.TimingVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _qdk.TimingVector___nonzero__(self)

    def __bool__(self):
        return _qdk.TimingVector___bool__(self)

    def __len__(self):
        return _qdk.TimingVector___len__(self)

    def __getslice__(self, i, j):
        return _qdk.TimingVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _qdk.TimingVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _qdk.TimingVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _qdk.TimingVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _qdk.TimingVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _qdk.TimingVector___setitem__(self, *args)

    def pop(self):
        return _qdk.TimingVector_pop(self)

    def append(self, x):
        return _qdk.TimingVector_append(self, x)

    def empty(self):
        return _qdk.TimingVector_empty(self)

    def size(self):
        return _qdk.TimingVector_size(self)

    def swap(self, v):
        return _qdk.TimingVector_swap(self, v)

    def begin(self):
        return _qdk.TimingVector_begin(self)

    def end(self):
        return _qdk.TimingVector_end(self)

    def rbegin(self):
        return _qdk.TimingVector_rbegin(self)

    def rend(self):
        return _qdk.TimingVector_rend(self)

    def clear(self):
        return _qdk.TimingVector_clear(self)

    def get_allocator(self):
        return _qdk.TimingVector_get_allocator(self)

    def pop_back(self):
        return _qdk.TimingVector_pop_back(self)

    def erase(self, *args):
        return _qdk.TimingVector_erase(self, *args)

    def __init__(self, *args):
        this = _qdk.new_TimingVector(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _qdk.TimingVector_push_back(self, x)

    def front(self):
        return _qdk.TimingVector_front(self)

    def back(self):
        return _qdk.TimingVector_back(self)

    def assign(self, n, x):
        return _qdk.TimingVector_assign(self, n, x)

    def resize(self, *args):
        return _qdk.TimingVector_resize(self, *args)

    def insert(self, *args):
        return _qdk.TimingVector_insert(self, *args)

    def reserve(self, n):
        return _qdk.TimingVector_reserve(self, n)

    def capacity(self):
        return _qdk.TimingVector_capacity(self)
    __swig_destroy__ = _qdk.delete_TimingVector
    __del__ = lambda self: None
TimingVector_swigregister = _qdk.TimingVector_swigregister
TimingVector_swigregister(TimingVector)


