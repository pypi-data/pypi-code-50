"""Return the product of array elements over a given axis."""
import numpy
import numpoly

from .common import implements


@implements(numpy.prod, numpy.product)
def prod(a, axis=None, dtype=None, out=None, keepdims=False, **kwargs):
    """
    Return the product of array elements over a given axis.

    Args:
        a : array_like
            Input data.
        axis : None or int or tuple of ints, optional
            Axis or axes along which a product is performed.  The default,
            axis=None, will calculate the product of all the elements in the
            input array. If axis is negative it counts from the last to the
            first axis. If axis is a tuple of ints, a product is performed on
            all of the axes specified in the tuple instead of a single axis or
            all the axes as before.
        dtype : dtype, optional
            The type of the returned array, as well as of the accumulator in
            which the elements are multiplied.  The dtype of `a` is used by
            default unless `a` has an integer dtype of less precision than the
            default platform integer.  In that case, if `a` is signed then the
            platform integer is used while if `a` is unsigned then an unsigned
            integer of the same precision as the platform integer is used.
        out : ndarray, optional
            Alternative output array in which to place the result. It must have
            the same shape as the expected output, but the type of the output
            values will be cast if necessary.
        keepdims : bool, optional
            If this is set to True, the axes which are reduced are left in the
            result as dimensions with size one. With this option, the result
            will broadcast correctly against the input array.
        initial : scalar, optional
            The starting value for this product.
        where : array_like of bool, optional
            Elements to include in the product.

    Returns:
        (numpoly.ndpoly):
            An array shaped as `a` but with the specified axis removed.
            Returns a reference to `out` if specified.

    Examples:
        >>> x, y = numpoly.symbols("x y")
        >>> poly = numpoly.polynomial([[[1, x, x**2], [x+y, y, y]]])
        >>> numpoly.prod(poly)
        polynomial(x**3*y**3+x**4*y**2)
        >>> numpoly.prod(poly, keepdims=True)
        polynomial([[[x**3*y**3+x**4*y**2]]])
        >>> numpoly.prod(poly, axis=1)
        polynomial([[y+x, x*y, x**2*y]])
        >>> numpoly.prod(poly, axis=2, keepdims=True)
        polynomial([[[x**3],
                     [y**3+x*y**2]]])
        >>> numpoly.prod(poly, axis=[1, 2])
        polynomial([[[x**3*y**3+x**4*y**2]]])

    """
    assert out is None
    if keepdims:
        if axis is None:
            out = _prod(a.flatten(), axis=0)
            out = out.reshape((1,)*len(a.shape))
            return out
        elif isinstance(axis, int):
            axis = [axis]

    if axis is None:
        out = _prod(a.flatten(), axis=0)

    elif isinstance(axis, int):
        out = _prod(a, axis=axis)

    else:
        for idx in axis:
            a = _prod(a, axis=idx)
            a = a[(slice(None),)*idx+(numpy.newaxis,)]
        out = a

    return out


def _prod(a, axis):
    """
    Backend for the product function.

    Args:
        a (numpoly.ndpoly):
            Input data.
        axis (int):
            The axis to take product over.

    Returns:
        (numpoly.ndpoly):
            An array shaped as `a` but with the specified axis removed.

    """
    axis = axis+a.ndim if axis < 0 else axis
    assert a.ndim > axis, (a, axis)
    indices = (slice(None),)*axis
    out = a[indices+(0,)]
    for idx in range(1, a.shape[axis]):
        out = numpoly.multiply(out, a[indices+(idx,)])
    assert len(out.shape)+1 == len(a.shape)
    return out
