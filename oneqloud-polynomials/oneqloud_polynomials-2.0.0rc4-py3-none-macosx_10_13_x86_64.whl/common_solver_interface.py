
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



from .binary_polynomial import RandomQBPGenerator

class UPSolution(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UPSolution, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UPSolution, name)
    __repr__ = _swig_repr

    def release(self):
        return _qdk.UPSolution_release(self)
    __swig_destroy__ = _qdk.delete_UPSolution
    __del__ = lambda self: None

    def __init__(self):
        this = _qdk.new_UPSolution()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
UPSolution_swigregister = _qdk.UPSolution_swigregister
UPSolution_swigregister(UPSolution)

class Solution(_object):
    """

    A binary configuration which is a list of variables and their binary values.

    This constructor has the following signature: ::

        Solution(self, configuration, energy = float('inf'), frequency = 1)

    Args:
        configuration (dict): The configuration for the binary
          solution as a dictionary of the variable indices (int) mapped to their
          binary values (bool).
        energy (float): The energy of the configuration (default inf).
        frequency (int): The amount of times this solution configuration appears
         in the ``SolutionList`` to which it belongs (default 1).

    Attributes:
        configuration (dict): The configuration for the Solution as a
          dictionary of the variable indices (int) mapped to their binary
          values (bool). The energy of this solution will be set to 0 when a new
          configuration is set.
        energy (float): The energy of the configuration (default 'None').
        frequency (int): The number of occurrences of this solution.
        has_energy (bool): Returns True if the energy for the current configuration
          has been obtained.
        search_time (float) : The net amount of time it took to search for
          this solution from the result of running ``minimize``.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Solution, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Solution, name)

    def __init__(self, configuration, energy, frequency):
        this = _qdk.new_Solution(configuration, energy, frequency)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def __init__(self, configuration, energy=float("inf"), frequency=1):
        this = _qdk.new_Solution(configuration, energy, frequency)
        try:
            self.this.append(this)
        except Exception:
            self.this = this


    def _get_configuration(self):
        val = _qdk.Solution__get_configuration(self)

        return val.asdict()


        return val


    def get_spins(self):
        """

        Return the spins at the solution.

        This function has the following signatures: ::

            get_spins(self, configuration)

        Return:
            dict: Map of variable indices (int) to their corresponding spins (bool).
             The spin values are represented as either +1 (True) or -1 (False).

        """
        val = _qdk.Solution_get_spins(self)

        return val.asdict()


        return val


    def _get_energy(self):
        return _qdk.Solution__get_energy(self)

    def __repr__(self):
        return _qdk.Solution___repr__(self)

    def __getitem__(self, idx):
        """

        Get the Nth term of this polynomial. This function gets called by the object's
        ``__getitem()__`` method.

        This function has the following signature: ::

            __getitem__(self, index)

        Args:
            index (int): The index to retrieve.

        Return:
            bool: Returns True if the variable at the given index is set.

        """
        return _qdk.Solution___getitem__(self, idx)


    def __eq__(self, other):
        return _qdk.Solution___eq__(self, other)

    def __ne__(self, other):
        return _qdk.Solution___ne__(self, other)

    __swig_getmethods__["configuration"] = _get_configuration
    if _newclass: configuration = _swig_property(
        _get_configuration)

    __swig_getmethods__["energy"] = _get_energy
    if _newclass: energy = _swig_property(
        _get_energy)

    def __reduce__(self):
      ret = {}
      ret["configuration"] = self.configuration
      ret["has_energy"] = self.has_energy
      if self.has_energy:
        ret["energy"] = self.energy
      ret["frequency"] = self.frequency
      return self.__class__, ({},), ret

    def __setstate__(self, state):
      self.frequency = state["frequency"]
      self.configuration = state["configuration"]
      if state["has_energy"]:
        self.energy = state["energy"]

    __swig_getmethods__["has_energy"] = _qdk.Solution_has_energy_get
    if _newclass:
        has_energy = _swig_property(_qdk.Solution_has_energy_get)
    __swig_getmethods__["frequency"] = _qdk.Solution_frequency_get
    if _newclass:
        frequency = _swig_property(_qdk.Solution_frequency_get)
    __swig_getmethods__["search_time"] = _qdk.Solution_search_time_get
    if _newclass:
        search_time = _swig_property(_qdk.Solution_search_time_get)
    __swig_destroy__ = _qdk.delete_Solution
    __del__ = lambda self: None
Solution_swigregister = _qdk.Solution_swigregister
Solution_swigregister(Solution)

class VectorSolutionPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorSolutionPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorSolutionPtr, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _qdk.VectorSolutionPtr_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _qdk.VectorSolutionPtr___nonzero__(self)

    def __bool__(self):
        return _qdk.VectorSolutionPtr___bool__(self)

    def __len__(self):
        return _qdk.VectorSolutionPtr___len__(self)

    def __getslice__(self, i, j):
        return _qdk.VectorSolutionPtr___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _qdk.VectorSolutionPtr___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _qdk.VectorSolutionPtr___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _qdk.VectorSolutionPtr___delitem__(self, *args)

    def __getitem__(self, *args):
        return _qdk.VectorSolutionPtr___getitem__(self, *args)

    def __setitem__(self, *args):
        return _qdk.VectorSolutionPtr___setitem__(self, *args)

    def pop(self):
        return _qdk.VectorSolutionPtr_pop(self)

    def append(self, x):
        return _qdk.VectorSolutionPtr_append(self, x)

    def empty(self):
        return _qdk.VectorSolutionPtr_empty(self)

    def size(self):
        return _qdk.VectorSolutionPtr_size(self)

    def swap(self, v):
        return _qdk.VectorSolutionPtr_swap(self, v)

    def begin(self):
        return _qdk.VectorSolutionPtr_begin(self)

    def end(self):
        return _qdk.VectorSolutionPtr_end(self)

    def rbegin(self):
        return _qdk.VectorSolutionPtr_rbegin(self)

    def rend(self):
        return _qdk.VectorSolutionPtr_rend(self)

    def clear(self):
        return _qdk.VectorSolutionPtr_clear(self)

    def get_allocator(self):
        return _qdk.VectorSolutionPtr_get_allocator(self)

    def pop_back(self):
        return _qdk.VectorSolutionPtr_pop_back(self)

    def erase(self, *args):
        return _qdk.VectorSolutionPtr_erase(self, *args)

    def __init__(self, *args):
        this = _qdk.new_VectorSolutionPtr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _qdk.VectorSolutionPtr_push_back(self, x)

    def front(self):
        return _qdk.VectorSolutionPtr_front(self)

    def back(self):
        return _qdk.VectorSolutionPtr_back(self)

    def assign(self, n, x):
        return _qdk.VectorSolutionPtr_assign(self, n, x)

    def resize(self, *args):
        return _qdk.VectorSolutionPtr_resize(self, *args)

    def insert(self, *args):
        return _qdk.VectorSolutionPtr_insert(self, *args)

    def reserve(self, n):
        return _qdk.VectorSolutionPtr_reserve(self, n)

    def capacity(self):
        return _qdk.VectorSolutionPtr_capacity(self)
    __swig_destroy__ = _qdk.delete_VectorSolutionPtr
    __del__ = lambda self: None
VectorSolutionPtr_swigregister = _qdk.VectorSolutionPtr_swigregister
VectorSolutionPtr_swigregister(VectorSolutionPtr)

class VectorSharedSolutionPtr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, VectorSharedSolutionPtr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, VectorSharedSolutionPtr, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _qdk.VectorSharedSolutionPtr_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _qdk.VectorSharedSolutionPtr___nonzero__(self)

    def __bool__(self):
        return _qdk.VectorSharedSolutionPtr___bool__(self)

    def __len__(self):
        return _qdk.VectorSharedSolutionPtr___len__(self)

    def __getslice__(self, i, j):
        return _qdk.VectorSharedSolutionPtr___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _qdk.VectorSharedSolutionPtr___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _qdk.VectorSharedSolutionPtr___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _qdk.VectorSharedSolutionPtr___delitem__(self, *args)

    def __getitem__(self, *args):
        return _qdk.VectorSharedSolutionPtr___getitem__(self, *args)

    def __setitem__(self, *args):
        return _qdk.VectorSharedSolutionPtr___setitem__(self, *args)

    def pop(self):
        return _qdk.VectorSharedSolutionPtr_pop(self)

    def append(self, x):
        return _qdk.VectorSharedSolutionPtr_append(self, x)

    def empty(self):
        return _qdk.VectorSharedSolutionPtr_empty(self)

    def size(self):
        return _qdk.VectorSharedSolutionPtr_size(self)

    def swap(self, v):
        return _qdk.VectorSharedSolutionPtr_swap(self, v)

    def begin(self):
        return _qdk.VectorSharedSolutionPtr_begin(self)

    def end(self):
        return _qdk.VectorSharedSolutionPtr_end(self)

    def rbegin(self):
        return _qdk.VectorSharedSolutionPtr_rbegin(self)

    def rend(self):
        return _qdk.VectorSharedSolutionPtr_rend(self)

    def clear(self):
        return _qdk.VectorSharedSolutionPtr_clear(self)

    def get_allocator(self):
        return _qdk.VectorSharedSolutionPtr_get_allocator(self)

    def pop_back(self):
        return _qdk.VectorSharedSolutionPtr_pop_back(self)

    def erase(self, *args):
        return _qdk.VectorSharedSolutionPtr_erase(self, *args)

    def __init__(self, *args):
        this = _qdk.new_VectorSharedSolutionPtr(*args)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def push_back(self, x):
        return _qdk.VectorSharedSolutionPtr_push_back(self, x)

    def front(self):
        return _qdk.VectorSharedSolutionPtr_front(self)

    def back(self):
        return _qdk.VectorSharedSolutionPtr_back(self)

    def assign(self, n, x):
        return _qdk.VectorSharedSolutionPtr_assign(self, n, x)

    def resize(self, *args):
        return _qdk.VectorSharedSolutionPtr_resize(self, *args)

    def insert(self, *args):
        return _qdk.VectorSharedSolutionPtr_insert(self, *args)

    def reserve(self, n):
        return _qdk.VectorSharedSolutionPtr_reserve(self, n)

    def capacity(self):
        return _qdk.VectorSharedSolutionPtr_capacity(self)
    __swig_destroy__ = _qdk.delete_VectorSharedSolutionPtr
    __del__ = lambda self: None
VectorSharedSolutionPtr_swigregister = _qdk.VectorSharedSolutionPtr_swigregister
VectorSharedSolutionPtr_swigregister(VectorSharedSolutionPtr)

class UPSolutionList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UPSolutionList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UPSolutionList, name)
    __repr__ = _swig_repr

    def release(self):
        return _qdk.UPSolutionList_release(self)
    __swig_destroy__ = _qdk.delete_UPSolutionList
    __del__ = lambda self: None

    def __init__(self):
        this = _qdk.new_UPSolutionList()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
UPSolutionList_swigregister = _qdk.UPSolutionList_swigregister
UPSolutionList_swigregister(UPSolutionList)

class SolutionList(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SolutionList, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SolutionList, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined")

    def empty(self):
        return _qdk.SolutionList_empty(self)

    def __repr__(self):
        return _qdk.SolutionList___repr__(self)

    def __len__(self):
        return _qdk.SolutionList___len__(self)

    def get_minimum_energy_solution(self):
        """

        This allows the caller to get a copy of the solution with the minimum energy.

        This function has the following signature: ::

            get_minimum_energy_solution(self)

        Returns:
            Solution: The Solution from the solution list with the minimum
             energy.

        """
        return _qdk.SolutionList_get_minimum_energy_solution(self)


    def get_solution_list(self):
        """

        This allows the caller to get a copy of the solutions inside this list.

        This function has the following signature: ::

            get_solution_list(self)

        Return:
            list: A list of all the ``Solution``\ s.

        """
        val = _qdk.SolutionList_get_solution_list(self)

        val = list(val)


        return val


    def __iter__(self):
      solutions = self.get_solution_list()
      for sol in solutions:
        yield sol

    def __reduce__(self):
      ret = { "solution_list" : self.get_solution_list() }
      return self.__class__, (), ret

    def __setstate__(self, state):
      for sol in state["solution_list"]:
        self.insert(sol)

    __swig_destroy__ = _qdk.delete_SolutionList
    __del__ = lambda self: None
SolutionList_swigregister = _qdk.SolutionList_swigregister
SolutionList_swigregister(SolutionList)


import warnings
warnings.simplefilter('always', DeprecationWarning)

class QUSolver(_object):
    """

    The abstract solver in charge of finding the configuration that
    minimizes a Quadratic Unconstrained Binary Polynomial.

    Attributes:
        energy_tolerance (float): The precision used to compare energies in the
          solution list (default: 1e-9).
        has_timeout (bool): True if a timeout is set for the solver.
        result_status (str): The result of running ``minimize``. Can be either ``'SUCCESS'``, ``'CANCELLED'``, or ``'TIMEOUT'``.
        timeout (int): Timeout (ms) for the qubo solver, 0 is unlimited.

    """

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, QUSolver, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, QUSolver, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_QUSolver
    __del__ = lambda self: None

    def minimize(self, quad_poly):
        """

        Finds the minimum energy solution. Solvers can return multiple configurations
        that minimize the QUBO. Multiple configurations can also be returned if a
        heuristic solver is used and a list of solutions is needed.

        This function has the following signature: ::

            minimize(QuadraticBinaryPolynomial)

        Args:
           quad_poly (QuadraticBinaryPolynomial): QUBO.

        Return:
            SolutionList: The list of ``Solutions``.

        """
        return _qdk.QUSolver_minimize(self, quad_poly)


    def minimize_compact(self, poly):
        return _qdk.QUSolver_minimize_compact(self, poly)

    def disable_timeout(self):
        """

        Disable the timeout for this solver.

        This function has the following signature: ::

            disable_timeout()

        """
        return _qdk.QUSolver_disable_timeout(self)


    def _result_status(self):
        return _qdk.QUSolver__result_status(self)

    def get_timings(self):
        return _qdk.QUSolver_get_timings(self)

    __swig_getmethods__["result_status"] = _result_status
    if _newclass: result_status = _swig_property(_result_status)


    def __reduce__(self):
      ret = {"has_timeout" : self.has_timeout}
      if self.has_timeout:
        ret["timeout"] = self.timeout
      return self.__class__, (), ret

    def __setstate__(self, state):
      if state["has_timeout"]:
        self.timeout = state["timeout"]

    __swig_setmethods__["energy_tolerance"] = _qdk.QUSolver_energy_tolerance_set
    __swig_getmethods__["energy_tolerance"] = _qdk.QUSolver_energy_tolerance_get
    if _newclass:
        energy_tolerance = _swig_property(_qdk.QUSolver_energy_tolerance_get, _qdk.QUSolver_energy_tolerance_set)
    __swig_getmethods__["has_timeout"] = _qdk.QUSolver_has_timeout_get
    if _newclass:
        has_timeout = _swig_property(_qdk.QUSolver_has_timeout_get)
    __swig_setmethods__["timeout"] = _qdk.QUSolver_timeout_set
    __swig_getmethods__["timeout"] = _qdk.QUSolver_timeout_get
    if _newclass:
        timeout = _swig_property(_qdk.QUSolver_timeout_get, _qdk.QUSolver_timeout_set)
    __swig_getmethods__["random_generator"] = _qdk.QUSolver_random_generator_get
    if _newclass:
        random_generator = _swig_property(_qdk.QUSolver_random_generator_get)
QUSolver_swigregister = _qdk.QUSolver_swigregister
QUSolver_swigregister(QUSolver)

class GrayExhaustiveSolver(QUSolver):
    """

    This is an implementation of a Gray Exhausive Solver.

    This constructor has the following signature: ::

        GrayExhaustiveSolver(self)


    """

    __swig_setmethods__ = {}
    for _s in [QUSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, GrayExhaustiveSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [QUSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, GrayExhaustiveSolver, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_GrayExhaustiveSolver
    __del__ = lambda self: None

    def __reduce__(self):
      return super(GrayExhaustiveSolver, self).__reduce__()
    def __setstate__(self, state):
      super(GrayExhaustiveSolver, self).__setstate__(state)


    def _repr(self):
        return _qdk.GrayExhaustiveSolver__repr(self)

    def __repr__(self):
        return self._repr()

    __swig_setmethods__["parallelized"] = _qdk.GrayExhaustiveSolver_parallelized_set
    __swig_getmethods__["parallelized"] = _qdk.GrayExhaustiveSolver_parallelized_get
    if _newclass:
        parallelized = _swig_property(_qdk.GrayExhaustiveSolver_parallelized_get, _qdk.GrayExhaustiveSolver_parallelized_set)

    def __init__(self):
        """

        This is an implementation of a Gray Exhausive Solver.

        This constructor has the following signature: ::

            GrayExhaustiveSolver(self)


        """
        this = _qdk.new_GrayExhaustiveSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
GrayExhaustiveSolver_swigregister = _qdk.GrayExhaustiveSolver_swigregister
GrayExhaustiveSolver_swigregister(GrayExhaustiveSolver)

class Tabu1OptSolver(QUSolver):
    """

    This is an implementation of the Tabu-Search explained in section.
    2.4 of this paper:
    http://www.info.univ-angers.fr/pub/hao/papers/UBQP2010.pdf.

    This constructor  has the following signature: ::

        Tabu1OptSolver(self, collect_explored_solutions=False)

    Args:
        collect_explored_solutions (bool): True if each explored energy solution is
          to be collected for each iteration.

    Attributes:
        collect_explored_solutions (bool): True if each explored energy solution is
          to be collected for each iteration (default: 'False').
        energy_tolerance (float): The precision used to compare energies in the
          solution list (default: 1e-9).
        has_timeout (bool): True if a timeout is set for the solver (default: 'False').
        improvement_cutoff (int): The number of iterations that the solver will
          attempt with no improvement before stopping.
        improvement_tolerance (float): The minimum value by which the solution has
          to improve in an iteration to be considered (default '1e-9').
        iterations_count (int): The number of iterations the solver took in the
          minimization.
        result_status (str): The result of running ``minimize``. Can be either
          ``'SUCCESS'``, ``'CANCELLED'``, or ``'TIMEOUT'``.
        tabu_tenure (int): The Tabu tenure prevents a flipped variable from being
          flipped again for the set amount of iterations. This is the parameter
          named tt in the paper.
          ``TabuTenure(i) = tt + rand(tabu_tenure_rand_max_)``
        tabu_tenure_rand_max (int): The upper bound of the random number
          being used for calculating the tabu_tenure.
        timeout (int): Timeout (ms) for the qubo solver (default: '0'). Setting this
          to 0 will disable timeout.
        timing (int): The number of milliseconds for the minimization.
        guidance_values (dictionary): The starting solution for all anneals.

    Raises:
        RuntimeError: `tabu_tenure_rand_maxs` > 200000.

    """

    __swig_setmethods__ = {}
    for _s in [QUSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tabu1OptSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [QUSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, Tabu1OptSolver, name)
    __repr__ = _swig_repr

    def __init__(self, collect_explored_solutions=False):
        this = _qdk.new_Tabu1OptSolver(collect_explored_solutions)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def _set_parameter_strategy(self, strategy):
        """

        This allows the user to set a Tabu1Opt parameter strategy to use.

        This function has the following signature: ::

            set_parameter_strategy(self, strategy)

        Args:
            strategy (Tabu1OptParameterStrategy): The parameter choosing strategy for
              the solver.

        """
        return _qdk.Tabu1OptSolver__set_parameter_strategy(self, strategy)


    def _get_parameter_strategy(self):
        return _qdk.Tabu1OptSolver__get_parameter_strategy(self)

    def _set_guidance_values(self, solution):
        return _qdk.Tabu1OptSolver__set_guidance_values(self, solution)

    def _get_guidance_values(self):
        return _qdk.Tabu1OptSolver__get_guidance_values(self)

    def clear_guidance_values(self):
        return _qdk.Tabu1OptSolver_clear_guidance_values(self)

    def has_guidance_values(self):
        return _qdk.Tabu1OptSolver_has_guidance_values(self)
    __swig_destroy__ = _qdk.delete_Tabu1OptSolver
    __del__ = lambda self: None

    def _repr(self):
        return _qdk.Tabu1OptSolver__repr(self)

    def __repr__(self):
        return self._repr()


    __swig_getmethods__["parameter_strategy"] = _qdk.Tabu1OptSolver__get_parameter_strategy
    __swig_setmethods__["parameter_strategy"] = _set_parameter_strategy
    if _newclass: parameter_strategy = _swig_property(
        _qdk.Tabu1OptSolver__get_parameter_strategy,
        _set_parameter_strategy)

    __swig_getmethods__["guidance_values"] = _qdk.Tabu1OptSolver__get_guidance_values
    __swig_setmethods__["guidance_values"] = _set_guidance_values
    if _newclass: guidance_values = _swig_property(
        _qdk.Tabu1OptSolver__get_guidance_values,
        _set_guidance_values)

    __swig_setmethods__["collect_explored_solutions"] = _qdk.Tabu1OptSolver_collect_explored_solutions_set
    __swig_getmethods__["collect_explored_solutions"] = _qdk.Tabu1OptSolver_collect_explored_solutions_get
    if _newclass:
        collect_explored_solutions = _swig_property(_qdk.Tabu1OptSolver_collect_explored_solutions_get, _qdk.Tabu1OptSolver_collect_explored_solutions_set)
    __swig_setmethods__["improvement_cutoff"] = _qdk.Tabu1OptSolver_improvement_cutoff_set
    __swig_getmethods__["improvement_cutoff"] = _qdk.Tabu1OptSolver_improvement_cutoff_get
    if _newclass:
        improvement_cutoff = _swig_property(_qdk.Tabu1OptSolver_improvement_cutoff_get, _qdk.Tabu1OptSolver_improvement_cutoff_set)
    __swig_setmethods__["tabu_tenure"] = _qdk.Tabu1OptSolver_tabu_tenure_set
    __swig_getmethods__["tabu_tenure"] = _qdk.Tabu1OptSolver_tabu_tenure_get
    if _newclass:
        tabu_tenure = _swig_property(_qdk.Tabu1OptSolver_tabu_tenure_get, _qdk.Tabu1OptSolver_tabu_tenure_set)
    __swig_setmethods__["tabu_tenure_rand_max"] = _qdk.Tabu1OptSolver_tabu_tenure_rand_max_set
    __swig_getmethods__["tabu_tenure_rand_max"] = _qdk.Tabu1OptSolver_tabu_tenure_rand_max_get
    if _newclass:
        tabu_tenure_rand_max = _swig_property(_qdk.Tabu1OptSolver_tabu_tenure_rand_max_get, _qdk.Tabu1OptSolver_tabu_tenure_rand_max_set)
    __swig_getmethods__["iterations_count"] = _qdk.Tabu1OptSolver_iterations_count_get
    if _newclass:
        iterations_count = _swig_property(_qdk.Tabu1OptSolver_iterations_count_get)
Tabu1OptSolver_swigregister = _qdk.Tabu1OptSolver_swigregister
Tabu1OptSolver_swigregister(Tabu1OptSolver)

class Tabu1OptParameterStrategy(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Tabu1OptParameterStrategy, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Tabu1OptParameterStrategy, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _qdk.delete_Tabu1OptParameterStrategy
    __del__ = lambda self: None

    def get_improvement_cutoff(self, *args):
        return _qdk.Tabu1OptParameterStrategy_get_improvement_cutoff(self, *args)

    def get_tabu_tenure(self, *args):
        return _qdk.Tabu1OptParameterStrategy_get_tabu_tenure(self, *args)

    def get_tabu_tenure_rand_max(self, *args):
        return _qdk.Tabu1OptParameterStrategy_get_tabu_tenure_rand_max(self, *args)

    def __init__(self):
        this = _qdk.new_Tabu1OptParameterStrategy()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
Tabu1OptParameterStrategy_swigregister = _qdk.Tabu1OptParameterStrategy_swigregister
Tabu1OptParameterStrategy_swigregister(Tabu1OptParameterStrategy)

class PathRelinkingSolver(QUSolver):
    """

    This is an implementation of the path relinking algorithm explained in
    this paper:
    http://www.info.univ-angers.fr/pub/hao/papers/UBQP2010.pdf

    This constructor  has the following signature: ::

        PathRelinkingSolver(self, ref_set_count = 10)

    Args:
        ref_set_count (int): Size of the initial reference set to build (must be greater than 1).

    Attributes:
        greedy_path_relinking (bool): True if a greedy approach to path relinking
          should be used.
        distance_scale (float): The percentage of the start and end of the
          relinked path to discount.
        iterations_count (int): The total number of times Tabu1Opt was run.

    """

    __swig_setmethods__ = {}
    for _s in [QUSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PathRelinkingSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [QUSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PathRelinkingSolver, name)
    __repr__ = _swig_repr

    def __init__(self, ref_set_count=10):
        this = _qdk.new_PathRelinkingSolver(ref_set_count)
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_PathRelinkingSolver
    __del__ = lambda self: None

    def _repr(self):
        return _qdk.PathRelinkingSolver__repr(self)

    def __repr__(self):
        return self._repr()

    __swig_setmethods__["greedy_path_relinking"] = _qdk.PathRelinkingSolver_greedy_path_relinking_set
    __swig_getmethods__["greedy_path_relinking"] = _qdk.PathRelinkingSolver_greedy_path_relinking_get
    if _newclass:
        greedy_path_relinking = _swig_property(_qdk.PathRelinkingSolver_greedy_path_relinking_get, _qdk.PathRelinkingSolver_greedy_path_relinking_set)
    __swig_setmethods__["distance_scale"] = _qdk.PathRelinkingSolver_distance_scale_set
    __swig_getmethods__["distance_scale"] = _qdk.PathRelinkingSolver_distance_scale_get
    if _newclass:
        distance_scale = _swig_property(_qdk.PathRelinkingSolver_distance_scale_get, _qdk.PathRelinkingSolver_distance_scale_set)
    __swig_setmethods__["ref_set_count"] = _qdk.PathRelinkingSolver_ref_set_count_set
    __swig_getmethods__["ref_set_count"] = _qdk.PathRelinkingSolver_ref_set_count_get
    if _newclass:
        ref_set_count = _swig_property(_qdk.PathRelinkingSolver_ref_set_count_get, _qdk.PathRelinkingSolver_ref_set_count_set)
    __swig_getmethods__["iterations_count"] = _qdk.PathRelinkingSolver_iterations_count_get
    if _newclass:
        iterations_count = _swig_property(_qdk.PathRelinkingSolver_iterations_count_get)
PathRelinkingSolver_swigregister = _qdk.PathRelinkingSolver_swigregister
PathRelinkingSolver_swigregister(PathRelinkingSolver)

class SASolver(QUSolver):
    __swig_setmethods__ = {}
    for _s in [QUSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, SASolver, name, value)
    __swig_getmethods__ = {}
    for _s in [QUSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, SASolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _qdk.new_SASolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_SASolver
    __del__ = lambda self: None

    def _mc_probs(self):
        return _qdk.SASolver__mc_probs(self)

    def add_schedule_entry(self, temperature, sweeps):
        return _qdk.SASolver_add_schedule_entry(self, temperature, sweeps)

    def clear_anneal_schedule(self):
        return _qdk.SASolver_clear_anneal_schedule(self)

    def _set_num_runs(self, num_runs):
        return _qdk.SASolver__set_num_runs(self, num_runs)

    def _set_num_sweeps_per_run(self, num_sweeps_per_run):
        return _qdk.SASolver__set_num_sweeps_per_run(self, num_sweeps_per_run)

    def populate_anneal_schedule(self, anneal_type):
        return _qdk.SASolver_populate_anneal_schedule(self, anneal_type)

    def _sweeps_to_best_per_run(self):
        return _qdk.SASolver__sweeps_to_best_per_run(self)

    def _time_to_best_per_run(self):
        return _qdk.SASolver__time_to_best_per_run(self)

    def _proposal_scheme(self):
        return _qdk.SASolver__proposal_scheme(self)

    def _set_proposal_scheme(self, scheme):
        return _qdk.SASolver__set_proposal_scheme(self, scheme)

    def _schedule_type(self):
        return _qdk.SASolver__schedule_type(self)

    def _set_schedule_type(self, as_type):
        return _qdk.SASolver__set_schedule_type(self, as_type)

    def _repr(self):
        return _qdk.SASolver__repr(self)

    def __repr__(self):
        return self._repr()


    def custom_schedule(self, temperature_sweeps_array):
        """
        ``temperature_sweeps_array``: Anneal schedule where each entry consists of a pair of values:  temperature and a sweep count.

        Args:
            temperature_sweeps_array (numpy.ndarray): User-defined anneal schedule passed as 2D array.
        """

        try:
            import numpy
            import sys
        except ImportError:
            raise ImportError('Failed to import module')
            return

        if not isinstance(temperature_sweeps_array, numpy.ndarray):
            raise Exception('Argument is not an object of type numpy.ndarray')

        if (temperature_sweeps_array.ndim != 2) or (temperature_sweeps_array.size < 2):
            raise Exception('Anneal schedule must be non-empty 2D array')

        self.clear_anneal_schedule()

        for row in range(len(temperature_sweeps_array)):
            if temperature_sweeps_array[row][1] > 0 :
                self.add_schedule_entry(temperature_sweeps_array[row][0], temperature_sweeps_array[row][1])
            else:
                """ portable write() works in Python 2 and 3 """
                sys.stderr.write("ERROR: Invalid sweep count " + str(temperature_sweeps_array[row][1]) + "\n")

        self.populate_anneal_schedule(0)   # zero is qdk::AnnealSchedule::Type::CUSTOM


    __swig_getmethods__["mc_probs"] = _qdk.SASolver__mc_probs
    if _newclass: mc_probs = _swig_property(
        _qdk.SASolver__mc_probs)


    __swig_setmethods__["num_runs"] = _qdk.SASolver__set_num_runs
    if _newclass: num_runs = _swig_property(
        _qdk.SASolver__set_num_runs)


    __swig_setmethods__["num_sweeps_per_run"] = _qdk.SASolver__set_num_sweeps_per_run
    if _newclass: num_sweeps_per_run = _swig_property(
        _qdk.SASolver__set_num_sweeps_per_run)


    __swig_getmethods__["proposal_scheme"] = _qdk.SASolver__proposal_scheme
    __swig_setmethods__["proposal_scheme"] = _qdk.SASolver__set_proposal_scheme
    if _newclass: proposal_scheme = _swig_property(
        _qdk.SASolver__proposal_scheme,
        _qdk.SASolver__set_proposal_scheme)


    __swig_getmethods__["schedule_type"] = _qdk.SASolver__schedule_type
    __swig_setmethods__["schedule_type"] = _qdk.SASolver__set_schedule_type
    if _newclass: schedule_type = _swig_property(
        _qdk.SASolver__schedule_type,
        _qdk.SASolver__set_schedule_type)


    __swig_getmethods__["sweeps_to_best_per_run"] = _qdk.SASolver__sweeps_to_best_per_run
    if _newclass: sweeps_to_best_per_run = _swig_property(
        _qdk.SASolver__sweeps_to_best_per_run)


    __swig_getmethods__["time_to_best_per_run"] = _qdk.SASolver__time_to_best_per_run
    if _newclass: time_to_best_per_run = _swig_property(
        _qdk.SASolver__time_to_best_per_run)

    __swig_getmethods__["num_runs"] = _qdk.SASolver_num_runs_get
    if _newclass:
        num_runs = _swig_property(_qdk.SASolver_num_runs_get)
    __swig_getmethods__["num_sweeps_per_run"] = _qdk.SASolver_num_sweeps_per_run_get
    if _newclass:
        num_sweeps_per_run = _swig_property(_qdk.SASolver_num_sweeps_per_run_get)
    __swig_setmethods__["temperature_final"] = _qdk.SASolver_temperature_final_set
    __swig_getmethods__["temperature_final"] = _qdk.SASolver_temperature_final_get
    if _newclass:
        temperature_final = _swig_property(_qdk.SASolver_temperature_final_get, _qdk.SASolver_temperature_final_set)
    __swig_setmethods__["temperature_interval"] = _qdk.SASolver_temperature_interval_set
    __swig_getmethods__["temperature_interval"] = _qdk.SASolver_temperature_interval_get
    if _newclass:
        temperature_interval = _swig_property(_qdk.SASolver_temperature_interval_get, _qdk.SASolver_temperature_interval_set)
    __swig_setmethods__["temperature_initial"] = _qdk.SASolver_temperature_initial_set
    __swig_getmethods__["temperature_initial"] = _qdk.SASolver_temperature_initial_get
    if _newclass:
        temperature_initial = _swig_property(_qdk.SASolver_temperature_initial_get, _qdk.SASolver_temperature_initial_set)
    __swig_setmethods__["parallelized"] = _qdk.SASolver_parallelized_set
    __swig_getmethods__["parallelized"] = _qdk.SASolver_parallelized_get
    if _newclass:
        parallelized = _swig_property(_qdk.SASolver_parallelized_get, _qdk.SASolver_parallelized_set)
    __swig_getmethods__["sweeps_to_best"] = _qdk.SASolver_sweeps_to_best_get
    if _newclass:
        sweeps_to_best = _swig_property(_qdk.SASolver_sweeps_to_best_get)
    __swig_getmethods__["time_to_best"] = _qdk.SASolver_time_to_best_get
    if _newclass:
        time_to_best = _swig_property(_qdk.SASolver_time_to_best_get)
SASolver_swigregister = _qdk.SASolver_swigregister
SASolver_swigregister(SASolver)

class PTICMSolver(QUSolver):
    """

    This is an implementation of the PTICM solver presented in the paper
    borealis - A generalized global update algorithm for Boolean optimization problems:
    https://arxiv.org/abs/1605.09399

    Note:
          PTICM stands for Parallel Tempering - Iso-energetic Cluster Moves.

    Note:
          The PTICM algorithm is sensitive to having a temperature range that
          roughly matches the delta energy of the problem set. If the maximum
          temperature is too low, the algorithm may fail to explore the full range
          of energies. If the minimum temperature is too high, then the algorithm may
          fail to dig deep enough to find good local minima.
          The best values for the temperature bounds should be obtained by experimentation.
          A helper function is provided which tries to automatically guess reasonable
          temperature bounds (auto_set_temperatures [default True]).

    Note:
          The energy_tolerance needs to be adjusted based on the nature of the QUBO
          being solved. The energy_tolerance should be at most 1/10th of the
          smallest, non-zero coefficient of the QUBO. Also, if the coefficients are
          very large relative to the energy_tolerance, the limitations of floating
          point arithmetic will introduce rounding errors. Using
          set_scaling_type('MEDIAN') can bring the range of coefficients into a
          range that is more reasonable for the default energy_tolerance.

    Attributes:
        auto_set_temperatures (bool): Should the temperature range be auto-calculated. This is overidden/ ignored when a manual high/low temperature is set.
        elite_threshold (double): Fraction of the best solutions used for variable fixing with SPVAR.
        frac_icm_thermal_layers (double): Fraction of temperatures for which ICM will be performed (only if num_replicas > 1).
        frac_sweeps_fixing (double): Fraction of sweeps used for variable fixing.
        frac_sweeps_idle (double): Fraction of sweeps to wait before variable fixing.
        frac_sweeps_stagnation (double): Fraction of sweeps without improvement that triggers a restart.
        high_temp (double): Highest temperature. Setting this value will cause auto_set_temperatures to be set to false.
        low_temp (double): Lowest temperature.Setting this value will cause auto_set_temperatures to be set to false.
        max_samples_per_layer (unsigned): Maximum samples collected per replica.
        max_total_sweeps (unsigned): Total number of sweeps before termination.
        num_elite_temps (unsigned): Number of elite temperature used for variable fixing with persistency.
        num_replicas (unsigned): Number of replicas at each temperature.
        num_sweeps_per_run (unsigned): Number of Monte Carlo sweeps before restarting the algorithm.
        num_temps (unsigned): Number of temperatures. num_temps will be ignored if manual_temperatures is set.
        pticm_goal (string): What results are expected. Valid values are `OPTIMIZE` or `SAMPLE`.
        scaling_type (string): Should the QUBO be automatically scaled.  Valid values are `MEDIAN` or `NO_SCALING`.
        var_fixing_type (string): Should variables be set to fixed values.  Valid values are `PERSISTENCY`, `SPVAR` or `NO_FIXING`.
        verbose (bool): Should additional data be printed.

    Note:
          Setting num_temps or num_replicas to a high value (100+) can result in
          memory issues and poor performance.

    Note:
          While num_temps and num_replicas serve similar roles in increasing the
          number of simulations, their specific usage is quite different.
          num_temps increases the number of different temperature ranges that are
          used. num_replicas merely duplicates the existing temperature ranges and is
          only necessary for the ICM component of the algorithm.

    Note:
          The ICM component of the algorithm can help for some problems, but not all.
          Turning off ICM will reduce overhead, possibly at the cost of a longer
          optimal solution time. Try experimenting with and without ICM to see if your
          results are significantly improved.

    Read-Only Attributes:
        scaling_factor (double): How much was the qubo scaled.
        runs_counter (unsigned): How many runs (restarts) occurred.
        sweeps_to_best (unsigned): How many sweeps occurred before the best solution was found.
        time_to_best (double): Elapsed time till the best solution was found.
        total_sweeps (unsigned): How many sweeps were performed in total, for all runs (restarts).

    Raises:
        RuntimeError: `high_temp` < 0.
        RuntimeError: `low_temp` < 0.
        RuntimeError: `frac_sweeps_fixing` < 0 or > 1.
        RuntimeError: `frac_sweeps_idle` < 0 or > 1.
        RuntimeError: `num_replicas` < 1 or > 1024.
        RuntimeError: `num_sweeps_per_run` < 1.
        RuntimeError: `num_temps` < 2.
        RuntimeError: `num_elite_temps` < 1.
        RuntimeError: `elite_threshold` < 0 or > 1.
        RuntimeError: `max_samples_per_layer` < 1.
        RuntimeError: `max_total_sweeps` < 1.
        RuntimeError: `frac_sweeps_stagnation` < 0 or > 1.
        RuntimeError: `frac_icm_thermal_layers` < 0 or > 1.

    Note:
          Other RuntimeErrors are possible based on the logical state of the parameters and nature of the QUBO.

    The constructor has the following signature: ::

        PTICMSolver(self)

    """

    __swig_setmethods__ = {}
    for _s in [QUSolver]:
        __swig_setmethods__.update(getattr(_s, '__swig_setmethods__', {}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, PTICMSolver, name, value)
    __swig_getmethods__ = {}
    for _s in [QUSolver]:
        __swig_getmethods__.update(getattr(_s, '__swig_getmethods__', {}))
    __getattr__ = lambda self, name: _swig_getattr(self, PTICMSolver, name)
    __repr__ = _swig_repr

    def __init__(self):
        this = _qdk.new_PTICMSolver()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _qdk.delete_PTICMSolver
    __del__ = lambda self: None

    def get_energy_target(self):
        return _qdk.PTICMSolver_get_energy_target(self)

    def set_energy_target(self, is_benchmark, expected_optimal):
        return _qdk.PTICMSolver_set_energy_target(self, is_benchmark, expected_optimal)

    def get_collected_data(self):
        return _qdk.PTICMSolver_get_collected_data(self)

    def get_manual_temperatures(self):
        """

        Get the user defined temperature schedule.

        This function has the following signature: ::

            get_manual_temperatures()

        Returns:
            list(float) User defined temperatures, sorted in ascending order.

        """
        return _qdk.PTICMSolver_get_manual_temperatures(self)


    def set_manual_temperatures(self, manual_temperatures):
        """

        Set the user defined temperature schedule.

        This function has the following signature: ::

            set_manual_temperatures(temperatures)

        Param:
            temperatures - list(float) - User defined temperatures

        Notes:
          - set_manual_temperatures will sort temperatures automatically.
          - A list of less than 2 temperatures is invalid.


        """
        return _qdk.PTICMSolver_set_manual_temperatures(self, manual_temperatures)


    def clear_manual_temperatures(self):
        """

        Clear all user defined temperatures.

        This function has the following signature: ::

            clear_manual_temperatures()


        """
        return _qdk.PTICMSolver_clear_manual_temperatures(self)


    def _mc_probs(self):
        return _qdk.PTICMSolver__mc_probs(self)

    def _pt_probs(self):
        return _qdk.PTICMSolver__pt_probs(self)

    def _repr(self):
        return _qdk.PTICMSolver__repr(self)

    def __repr__(self):
        return self._repr()


    __swig_getmethods__["mc_probs"] = _qdk.PTICMSolver__mc_probs
    if _newclass: mc_probs = _swig_property(
              _qdk.PTICMSolver__mc_probs)


    __swig_getmethods__["pt_probs"] = _qdk.PTICMSolver__pt_probs
    if _newclass: pt_probs = _swig_property(
              _qdk.PTICMSolver__pt_probs)

    __swig_setmethods__["auto_set_temperatures"] = _qdk.PTICMSolver_auto_set_temperatures_set
    __swig_getmethods__["auto_set_temperatures"] = _qdk.PTICMSolver_auto_set_temperatures_get
    if _newclass:
        auto_set_temperatures = _swig_property(_qdk.PTICMSolver_auto_set_temperatures_get, _qdk.PTICMSolver_auto_set_temperatures_set)
    __swig_setmethods__["pticm_goal"] = _qdk.PTICMSolver_pticm_goal_set
    __swig_getmethods__["pticm_goal"] = _qdk.PTICMSolver_pticm_goal_get
    if _newclass:
        pticm_goal = _swig_property(_qdk.PTICMSolver_pticm_goal_get, _qdk.PTICMSolver_pticm_goal_set)
    __swig_setmethods__["scaling_type"] = _qdk.PTICMSolver_scaling_type_set
    __swig_getmethods__["scaling_type"] = _qdk.PTICMSolver_scaling_type_get
    if _newclass:
        scaling_type = _swig_property(_qdk.PTICMSolver_scaling_type_get, _qdk.PTICMSolver_scaling_type_set)
    __swig_setmethods__["var_fixing_type"] = _qdk.PTICMSolver_var_fixing_type_set
    __swig_getmethods__["var_fixing_type"] = _qdk.PTICMSolver_var_fixing_type_get
    if _newclass:
        var_fixing_type = _swig_property(_qdk.PTICMSolver_var_fixing_type_get, _qdk.PTICMSolver_var_fixing_type_set)
    __swig_setmethods__["elite_threshold"] = _qdk.PTICMSolver_elite_threshold_set
    __swig_getmethods__["elite_threshold"] = _qdk.PTICMSolver_elite_threshold_get
    if _newclass:
        elite_threshold = _swig_property(_qdk.PTICMSolver_elite_threshold_get, _qdk.PTICMSolver_elite_threshold_set)
    __swig_setmethods__["frac_icm_thermal_layers"] = _qdk.PTICMSolver_frac_icm_thermal_layers_set
    __swig_getmethods__["frac_icm_thermal_layers"] = _qdk.PTICMSolver_frac_icm_thermal_layers_get
    if _newclass:
        frac_icm_thermal_layers = _swig_property(_qdk.PTICMSolver_frac_icm_thermal_layers_get, _qdk.PTICMSolver_frac_icm_thermal_layers_set)
    __swig_setmethods__["frac_sweeps_fixing"] = _qdk.PTICMSolver_frac_sweeps_fixing_set
    __swig_getmethods__["frac_sweeps_fixing"] = _qdk.PTICMSolver_frac_sweeps_fixing_get
    if _newclass:
        frac_sweeps_fixing = _swig_property(_qdk.PTICMSolver_frac_sweeps_fixing_get, _qdk.PTICMSolver_frac_sweeps_fixing_set)
    __swig_setmethods__["frac_sweeps_idle"] = _qdk.PTICMSolver_frac_sweeps_idle_set
    __swig_getmethods__["frac_sweeps_idle"] = _qdk.PTICMSolver_frac_sweeps_idle_get
    if _newclass:
        frac_sweeps_idle = _swig_property(_qdk.PTICMSolver_frac_sweeps_idle_get, _qdk.PTICMSolver_frac_sweeps_idle_set)
    __swig_setmethods__["frac_sweeps_stagnation"] = _qdk.PTICMSolver_frac_sweeps_stagnation_set
    __swig_getmethods__["frac_sweeps_stagnation"] = _qdk.PTICMSolver_frac_sweeps_stagnation_get
    if _newclass:
        frac_sweeps_stagnation = _swig_property(_qdk.PTICMSolver_frac_sweeps_stagnation_get, _qdk.PTICMSolver_frac_sweeps_stagnation_set)
    __swig_setmethods__["high_temp"] = _qdk.PTICMSolver_high_temp_set
    __swig_getmethods__["high_temp"] = _qdk.PTICMSolver_high_temp_get
    if _newclass:
        high_temp = _swig_property(_qdk.PTICMSolver_high_temp_get, _qdk.PTICMSolver_high_temp_set)
    __swig_setmethods__["low_temp"] = _qdk.PTICMSolver_low_temp_set
    __swig_getmethods__["low_temp"] = _qdk.PTICMSolver_low_temp_get
    if _newclass:
        low_temp = _swig_property(_qdk.PTICMSolver_low_temp_get, _qdk.PTICMSolver_low_temp_set)
    __swig_setmethods__["max_samples_per_layer"] = _qdk.PTICMSolver_max_samples_per_layer_set
    __swig_getmethods__["max_samples_per_layer"] = _qdk.PTICMSolver_max_samples_per_layer_get
    if _newclass:
        max_samples_per_layer = _swig_property(_qdk.PTICMSolver_max_samples_per_layer_get, _qdk.PTICMSolver_max_samples_per_layer_set)
    __swig_setmethods__["max_total_sweeps"] = _qdk.PTICMSolver_max_total_sweeps_set
    __swig_getmethods__["max_total_sweeps"] = _qdk.PTICMSolver_max_total_sweeps_get
    if _newclass:
        max_total_sweeps = _swig_property(_qdk.PTICMSolver_max_total_sweeps_get, _qdk.PTICMSolver_max_total_sweeps_set)
    __swig_setmethods__["num_elite_temps"] = _qdk.PTICMSolver_num_elite_temps_set
    __swig_getmethods__["num_elite_temps"] = _qdk.PTICMSolver_num_elite_temps_get
    if _newclass:
        num_elite_temps = _swig_property(_qdk.PTICMSolver_num_elite_temps_get, _qdk.PTICMSolver_num_elite_temps_set)
    __swig_setmethods__["num_replicas"] = _qdk.PTICMSolver_num_replicas_set
    __swig_getmethods__["num_replicas"] = _qdk.PTICMSolver_num_replicas_get
    if _newclass:
        num_replicas = _swig_property(_qdk.PTICMSolver_num_replicas_get, _qdk.PTICMSolver_num_replicas_set)
    __swig_setmethods__["num_sweeps_per_run"] = _qdk.PTICMSolver_num_sweeps_per_run_set
    __swig_getmethods__["num_sweeps_per_run"] = _qdk.PTICMSolver_num_sweeps_per_run_get
    if _newclass:
        num_sweeps_per_run = _swig_property(_qdk.PTICMSolver_num_sweeps_per_run_get, _qdk.PTICMSolver_num_sweeps_per_run_set)
    __swig_setmethods__["num_temps"] = _qdk.PTICMSolver_num_temps_set
    __swig_getmethods__["num_temps"] = _qdk.PTICMSolver_num_temps_get
    if _newclass:
        num_temps = _swig_property(_qdk.PTICMSolver_num_temps_get, _qdk.PTICMSolver_num_temps_set)
    __swig_setmethods__["verbose"] = _qdk.PTICMSolver_verbose_set
    __swig_getmethods__["verbose"] = _qdk.PTICMSolver_verbose_get
    if _newclass:
        verbose = _swig_property(_qdk.PTICMSolver_verbose_get, _qdk.PTICMSolver_verbose_set)
    __swig_setmethods__["parallelized"] = _qdk.PTICMSolver_parallelized_set
    __swig_getmethods__["parallelized"] = _qdk.PTICMSolver_parallelized_get
    if _newclass:
        parallelized = _swig_property(_qdk.PTICMSolver_parallelized_get, _qdk.PTICMSolver_parallelized_set)
    __swig_getmethods__["scaling_factor"] = _qdk.PTICMSolver_scaling_factor_get
    if _newclass:
        scaling_factor = _swig_property(_qdk.PTICMSolver_scaling_factor_get)
    __swig_getmethods__["runs_counter"] = _qdk.PTICMSolver_runs_counter_get
    if _newclass:
        runs_counter = _swig_property(_qdk.PTICMSolver_runs_counter_get)
    __swig_getmethods__["sweeps_to_best"] = _qdk.PTICMSolver_sweeps_to_best_get
    if _newclass:
        sweeps_to_best = _swig_property(_qdk.PTICMSolver_sweeps_to_best_get)
    __swig_getmethods__["time_to_best"] = _qdk.PTICMSolver_time_to_best_get
    if _newclass:
        time_to_best = _swig_property(_qdk.PTICMSolver_time_to_best_get)
    __swig_getmethods__["total_sweeps"] = _qdk.PTICMSolver_total_sweeps_get
    if _newclass:
        total_sweeps = _swig_property(_qdk.PTICMSolver_total_sweeps_get)
    __swig_setmethods__["collect_energies"] = _qdk.PTICMSolver_collect_energies_set
    __swig_getmethods__["collect_energies"] = _qdk.PTICMSolver_collect_energies_get
    if _newclass:
        collect_energies = _swig_property(_qdk.PTICMSolver_collect_energies_get, _qdk.PTICMSolver_collect_energies_set)
PTICMSolver_swigregister = _qdk.PTICMSolver_swigregister
PTICMSolver_swigregister(PTICMSolver)


