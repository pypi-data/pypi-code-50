"""Construct an array from an index array and a set of arrays to choose from."""
import numpy
import numpoly

from .common import implements


@implements(numpy.choose)
def choose(a, choices, out=None, mode="raise"):
    """
    Construct an array from an index array and a set of arrays to choose from.

    First of all, if confused or uncertain, definitely look at the Examples -
    in its full generality, this function is less simple than it might
    seem from the following code description (below ndi =
    `numpy.lib.index_tricks`):

    ``np.choose(a,c) == np.array([c[a[I]][I] for I in ndi.ndindex(a.shape)])``.

    But this omits some subtleties. Here is a fully general summary:

    Given an "index" array (`a`) of integers and a sequence of `n` arrays
    (`choices`), `a` and each choice array are first broadcast, as necessary,
    to arrays of a common shape; calling these *Ba* and *Bchoices[i], i =
    0,...,n-1* we have that, necessarily, ``Ba.shape == Bchoices[i].shape``
    for each `i`.  Then, a new array with shape ``Ba.shape`` is created as
    follows:

    * if ``mode=raise`` (the default), then, first of all, each element of
      `a` (and thus `Ba`) must be in the range `[0, n-1]`; now, suppose that
      `i` (in that range) is the value at the `(j0, j1, ..., jm)` position
      in `Ba` - then the value at the same position in the new array is the
      value in `Bchoices[i]` at that same position;

    * if ``mode=wrap``, values in `a` (and thus `Ba`) may be any (signed)
      integer; modular arithmetic is used to map integers outside the range
      `[0, n-1]` back into that range; and then the new array is constructed
      as above;

    * if ``mode=clip``, values in `a` (and thus `Ba`) may be any (signed)
      integer; negative integers are mapped to 0; values greater than `n-1`
      are mapped to `n-1`; and then the new array is constructed as above.

    Args:
        a (int, numpy.ndarray):
            This array must contain integers in `[0, n-1]`, where `n` is the
            number of choices, unless ``mode=wrap`` or ``mode=clip``, in which
            cases any integers are permissible.
        choices (Sequence[numpoly.ndpoly]):
            Choice arrays. `a` and all of the choices must be broadcastable to
            the same shape.  If `choices` is itself an array (not recommended),
            then its outermost dimension (i.e., the one corresponding to
            ``choices.shape[0]``) is taken as defining the "sequence".
        out (Optional[numpoly.ndpoly]):
            If provided, the result will be inserted into this array. It should
            be of the appropriate shape and dtype. Note that `out` is always
            buffered if `mode='raise'`; use other modes for better performance.
        mode (Optional[str]):
            {'raise' (default), 'wrap', 'clip'}, optional
            Specifies how indices outside `[0, n-1]` will be treated:

              * 'raise' : an exception is raised
              * 'wrap' : value becomes value mod `n`
              * 'clip' : values < 0 are mapped to 0, values > n-1 are mapped to n-1

    Returns:
        merged_array (numpoly.ndpoly):
            The merged result.

    Raises:
        ValueError: shape mismatch
            If `a` and each choice array are not all broadcastable to the same
            shape.

    Notes:
        To reduce the chance of misinterpretation, even though the following
        "abuse" is nominally supported, `choices` should neither be, nor be
        thought of as, a single array, i.e., the outermost sequence-like
        container should be either a list or a tuple.

    Examples:
        >>> choices = numpoly.outer(numpoly.monomial(3, names="x"),
        ...                         numpoly.monomial(3, names="y"))
        >>> choices
        polynomial([[1, y, y**2],
                    [x, x*y, x*y**2],
                    [x**2, x**2*y, x**2*y**2]])
        >>> numpoly.choose([1, 2, 0], choices)
        polynomial([x, x**2*y, y**2])
        >>> numpoly.choose([1, 3, 0], choices, mode="clip")
        polynomial([x, x**2*y, y**2])
        >>> numpoly.choose([1, 3, 0], choices, mode="wrap")
        polynomial([x, y, y**2])

    """
    choices = numpoly.aspolynomial(choices)
    result = numpy.choose(a, choices=choices.values, out=out, mode=mode)
    return numpoly.aspolynomial(result, names=choices.indeterminants)
