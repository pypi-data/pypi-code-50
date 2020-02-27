"""
Definition of the Add/Subtract Component.
"""
import collections
from six import string_types

import numpy as np
from scipy import sparse as sp

from openmdao.core.explicitcomponent import ExplicitComponent


class AddSubtractComp(ExplicitComponent):
    r"""
    Compute a vectorized element-wise addition or subtraction.

    Use the add_equation method to define any number of add/subtract relations
    User defines the names of the input and output variables using
    add_equation(output_name='my_output', input_names=['a','b', 'c', ...])

    .. math::
        result = a * \textrm{scaling factor}_a + b * \textrm{scaling factor}_b +
        c * \textrm{scaling factor}_c + ...

    where all inputs  shape (vec_size, n)
          b is of shape (vec_size, n)
          c is of shape (vec_size, n)
          result is of shape (vec_size, n)

    All input vectors must be of the same shape, specified by the options 'vec_size' and 'length'.
    Use scaling factor -1 for subtraction.

    Attributes
    ----------
    _add_systems : list
        List of equation systems to be initialized with the system.
    """

    def __init__(self, output_name=None, input_names=None, vec_size=1, length=1,
                 val=1.0, scaling_factors=None, **kwargs):
        """
        Allow user to create an addition/subtracton system with one-liner.

        Parameters
        ----------
        output_name : str
            (required) name of the result variable in this component's namespace.
        input_names : iterable of str
            (required) names of the input variables for this system
        vec_size : int
            Length of the first dimension of the input and output vectors
            (i.e number of rows, or vector length for a 1D vector)
            Default is 1
        length : int
            Length of the second dimension of the input and ouptut vectors (i.e. number of columns)
            Default is 1 which results in input/output vectors of size (vec_size,)
        scaling_factors : iterable of numeric
            Scaling factors to apply to each input.
            Use [1,1,...] for addition, [1,-1,...] for subtraction
            Must be same length as input_names
            Default is None which results in a scaling factor of 1 on
            each input (element-wise addition)
        val : float or list or tuple or ndarray
            The initial value of the variable being added in user-defined units. Default is 1.0.
        **kwargs : str
            Any other arguments to pass to the addition system
            (same as add_output method for ExplicitComponent)
            Examples include units (str or None), desc (str)
        """
        super(AddSubtractComp, self).__init__()

        self._add_systems = []

        if isinstance(output_name, string_types):
            self._add_systems.append((output_name, input_names, vec_size, length, val,
                                      scaling_factors, kwargs))
        elif isinstance(output_name, collections.Iterable):
            raise NotImplementedError(self.msginfo + ': Declaring multiple addition systems '
                                      'on initiation is not implemented.'
                                      'Use a string to name a single addition relationship or use '
                                      'multiple add_output calls')
        elif output_name is None:
            pass
        else:
            raise ValueError(self.msginfo + ": first argument to adder init must be either of "
                             "type `str' or 'None'")

    def initialize(self):
        """
        Declare options.

        Parameters
        ----------
        complex : Boolean
            Set True to enable complex math (e.g. for complex step verification)
        """
        self.options.declare('complex', types=bool, default=False,
                             desc="Allocate as complex (e.g. for complex-step verification)")

    def add_equation(self, output_name, input_names, vec_size=1, length=1, val=1.0,
                     units=None, res_units=None, desc='', lower=None, upper=None, ref=1.0,
                     ref0=0.0, res_ref=None, scaling_factors=None):
        """
        Add an addition/subtraction relation.

        Parameters
        ----------
        output_name : str
            (required) name of the result variable in this component's namespace.
        input_names : iterable of str
            (required) names of the input variables for this system
        vec_size : int
            Length of the first dimension of the input and output vectors
            (i.e number of rows, or vector length for a 1D vector)
            Default is 1
        length : int
            Length of the second dimension of the input and ouptut vectors (i.e. number of columns)
            Default is 1 which results in input/output vectors of size (vec_size,)
        scaling_factors : iterable of numeric
            Scaling factors to apply to each input.
            Use [1,1,...] for addition, [1,-1,...] for subtraction
            Must be same length as input_names
            Default is None which results in a scaling factor of 1 on
            each input (element-wise addition)
        val : float or list or tuple or ndarray
            The initial value of the variable being added in user-defined units. Default is 1.0.
        units : str or None
            Units in which the output variables will be provided to the component during execution.
            Default is None, which means it has no units.
        res_units : str or None
            Units in which the residuals of this output will be given to the user when requested.
            Default is None, which means it has no units.
        desc : str
            description of the variable.
        lower : float or list or tuple or ndarray or Iterable or None
            lower bound(s) in user-defined units. It can be (1) a float, (2) an array_like
            consistent with the shape arg (if given), or (3) an array_like matching the shape of
            val, if val is array_like. A value of None means this output has no lower bound.
            Default is None.
        upper : float or list or tuple or ndarray or or Iterable None
            upper bound(s) in user-defined units. It can be (1) a float, (2) an array_like
            consistent with the shape arg (if given), or (3) an array_like matching the shape of
            val, if val is array_like. A value of None means this output has no upper bound.
            Default is None.
        ref : float or ndarray
            Scaling parameter. The value in the user-defined units of this output variable when
            the scaled value is 1. Default is 1.
        ref0 : float or ndarray
            Scaling parameter. The value in the user-defined units of this output variable when
            the scaled value is 0. Default is 0.
        res_ref : float or ndarray
            Scaling parameter. The value in the user-defined res_units of this output's residual
            when the scaled value is 1. Default is 1.
        """
        kwargs = {'units': units, 'res_units': res_units, 'desc': desc,
                  'lower': lower, 'upper': upper, 'ref': ref, 'ref0': ref0,
                  'res_ref': res_ref}
        self._add_systems.append((output_name, input_names, vec_size, length, val,
                                  scaling_factors, kwargs))

    def add_output(self):
        """
        Use add_equation instead of add_output to define equation systems.
        """
        raise NotImplementedError(self.msginfo + ': Use add_equation method, not add_output '
                                  'method to create an addition/subtraction relation')

    def _post_configure(self):
        """
        Set up the addition/subtraction system at run time.
        """
        # set static mode to False because we are doing things that would normally be done in setup
        self._static_mode = False

        for (output_name, input_names, vec_size, length, val,
             scaling_factors, kwargs) in self._add_systems:
            if isinstance(input_names, string_types):
                input_names = [input_names]

            units = kwargs['units']
            desc = kwargs['desc']

            if scaling_factors is None:
                scaling_factors = np.ones(len(input_names))

            if len(scaling_factors) != len(input_names):
                raise ValueError(self.msginfo + ': Scaling factors list needs to be same length '
                                 'as input names')
            if length == 1:
                shape = (vec_size,)
            else:
                shape = (vec_size, length)

            super(AddSubtractComp, self).add_output(output_name, val, shape=shape, **kwargs)

            for i, input_name in enumerate(input_names):
                self.add_input(input_name, shape=shape, units=units,
                               desc=desc + '_inp_' + input_name)
                sf = scaling_factors[i]
                self.declare_partials([output_name], [input_name],
                                      val=sf * sp.eye(vec_size * length, format='csc'))

        self._static_mode = True

        super(AddSubtractComp, self)._post_configure()

    def compute(self, inputs, outputs):
        """
        Compute the element wise addition or subtraction of inputs using numpy + operator.

        Parameters
        ----------
        inputs : Vector
            unscaled, dimensional input variables read via inputs[key]
        outputs : Vector
            unscaled, dimensional output variables read via outputs[key]
        """
        complexify = self.options['complex']
        for (output_name, input_names, vec_size, length, val, scaling_factors,
             kwargs) in self._add_systems:
            if isinstance(input_names, string_types):
                input_names = [input_names]

            if scaling_factors is None:
                scaling_factors = np.ones(len(input_names))
            if length == 1:
                shape = (vec_size,)
            else:
                shape = (vec_size, length)

            if complexify:
                temp = np.zeros(shape, dtype=np.complex_)
            else:
                temp = np.zeros(shape)

            for i, input_name in enumerate(input_names):
                sf = scaling_factors[i]
                temp = temp + inputs[input_name] * sf

            outputs[output_name] = temp
