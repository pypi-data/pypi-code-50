import numpy as np

__all__ = ['complete_the_triangle', 'format_angle', 'format_length', 'pretty_format_triangle',
           'triangle_error']


def sin(angle_in_degrees):
    # Internal use just to reduce visual clutter
    return np.sin(np.deg2rad(angle_in_degrees))


def cos(angle_in_degrees):
    # Internal use just to reduce visual clutter
    return np.cos(np.deg2rad(angle_in_degrees))


def asin(sin_of_angle):
    # Internal use just to reduce visual clutter
    return np.rad2deg(np.arcsin(sin_of_angle))


def format_length(length, precision=4):
    """
    Returns a string version of the length argument rounded to the specified precision.

    :param length: unitless length parameter
    :param precision: number of digits in fractional part of answer
    :return: formatted string
    """
    return f'{length:0.{precision}f}'


def format_angle(angle_degrees, form='d', precision=2):
    """
    Returns a string version of the argument in one of four forms rounded to given precision.

    When angle_degrees is 43.567855, the various formats (at default precision=4) are ...
    form = 'r'   (radians     format) example: 0.7604r
    form = 'd'   (degree      format) example: 43.5679d
    form = 'dm'  (deg-min     format) example: 43d 34.0713m
    form = 'dms' (deg-min-sec format) example: 43d 34m 4.2780s

    :param angle_degrees: angle (in degrees)
    :param form: form string
    :param precision: number of digits in fractional part of answer
    :return: formatted string
    """

    if form == 'd':
        return f'{angle_degrees:.{precision}f}d'

    if form == 'r':
        angle_radians = np.deg2rad(angle_degrees)
        return f'{angle_radians:0.{precision}f}r'

    if form == 'dm':
        angle_int_part = int(angle_degrees)
        angle_frac_part = angle_degrees - angle_int_part
        angle_minutes = angle_frac_part * 60
        return f'{angle_int_part}d {angle_minutes:.{precision}f}m'

    if form == 'dms':
        angle_int_part = int(angle_degrees)
        angle_frac_part = angle_degrees - angle_int_part
        angle_minutes = int(angle_frac_part * 60)
        angle_seconds = (angle_frac_part * 60 - angle_minutes) * 60
        return f'{angle_int_part}d {angle_minutes}m {angle_seconds:.{precision}f}s'

    raise ValueError("'form' parameter not in ['d', 'r', 'dm', 'dms']")


def pretty_format_triangle(a=None, b=None, c=None, A=None, B=None, C=None,
                           angle_form='d', length_precision=4, angle_precision=2):
    """
    Returns triangle elements as a formatted string

    :param a: length of side a
    :param b: length of side b
    :param c: length of side c
    :param A: angle (degrees) subtended by side a
    :param B: angle (degrees) subtended by side b
    :param C: angle (degrees) subtended by side c
    :param angle_form: angle format specifier from ['r', 'd', 'dm', 'dms']
    :param length_precision: number of digits in fractional part of length
    :param angle_precision:  number of digits in fractional part of angle
    :return: formatted string
    """
    a_str = b_str = c_str = A_str = B_str = C_str = None
    if a is not None:
        a_str = format_length(a, precision=length_precision)

    if b is not None:
        b_str = format_length(b, precision=length_precision)

    if c is not None:
        c_str = format_length(c, precision=length_precision)

    if A is not None:
        A_str = format_angle(A, form=angle_form, precision=angle_precision)

    if B is not None:
        B_str = format_angle(B, form=angle_form, precision=angle_precision)

    if C is not None:
        C_str = format_angle(C, form=angle_form, precision=angle_precision)

    lengths_str = 'a: ' + a_str + ' b: ' + b_str + ' c: ' + c_str
    angles_str = 'A: ' + A_str + ' B: ' + B_str + ' C: ' + C_str

    return lengths_str + '   ' + angles_str


def solve_aaas_triangle(a, b, c, A, B, C):
    # This is an internally used routine
    if A is not None and B is not None and C is not None:
        if not sum(x is not None for x in (a, b, c)) >= 1:
            return 'Error: no side(s) given for aaas triangle solver', a, b, c, A, B, C
        if a is not None:
            b = a * sin(B) / sin(A)
            c = a * sin(C) / sin(A)
        if b is not None:
            a = b * sin(A) / sin(B)
            c = b * sin(C) / sin(B)
        if c is not None:
            a = c * sin(A) / sin(C)
            b = c * sin(B) / sin(C)
        return '', a, b, c, A, B, C
    else:
        raise ValueError('aaas triangle solver called without 3 defined angles.')


def finish_triangle_with_three_sides_defined(a, b, c, A, B, C):
    # An internally used routine.
    # Solution using 3 sides.  If an angle is also given, it/they are left unchanged.  This is because
    # this routine is used to solve triangles with 2 sides plus the included angle by first computing
    # the missing side using the cosine law then calling this routine.
    if a + b <= c or b + c <= a or a + c <= b:
        error = 'Error: the 3 sides given do not form a triangle'
        return error, a, b, c, A, B, C

    argA = (b * b + c * c - a * a) / (2.0 * b * c)
    argB = (a * a + c * c - b * b) / (2.0 * a * c)
    argC = (a * a + b * b - c * c) / (2.0 * a * b)
    A_radians = np.arccos(argA)
    B_radians = np.arccos(argB)
    C_radians = np.arccos(argC)
    if A is None:
        A = np.rad2deg(A_radians)
    if B is None:
        B = np.rad2deg(B_radians)
    if C is None:
        C = np.rad2deg(C_radians)
    rounding_error = 180.0 - A - B - C
    A += rounding_error / 3
    B += rounding_error / 3
    C += rounding_error / 3
    error = ''
    return error, a, b, c, A, B, C


def triangle_error(a, b, c, A, B, C):
    """
    Checks the validity of a fully specified triangle (all sides and angles defined)

    Returns the following (which should be very very small, ideally zero)

    err1 = abs(b * b + c * c - a * a - 2 * b * c * cos(A))

    err2 = abs(a * a + c * c - b * b - 2 * a * c * cos(B))

    err3 = abs(a * a + b * b - c * c - 2 * a * b * cos(C))

    :param a: side a
    :param b: side b
    :param c: side c
    :param A: angle A (degrees) subtended by side a
    :param B: angle B (degrees) subtended by side b
    :param C: angle C (degrees) subtended by side c
    :return: max(err1, err2, err3), err1, err2, err3
    """
    if None in (a, b, c, A, B, C):
        raise ValueError('The triangle contains some undefined (i.e. None) elements')
    err1 = abs(b * b + c * c - a * a - 2 * b * c * cos(A))
    err2 = abs(a * a + c * c - b * b - 2 * a * c * cos(B))
    err3 = abs(a * a + b * b - c * c - 2 * a * b * cos(C))
    return max(err1, err2, err3), err1, err2, err3


def ssa(a, b, c, A, B, C, flag='regular'):
    # Internal routine used to solve a triangle where only a, b, and A are available.
    # This is called by a routine that sorts the original arguments so that a, b, and A are
    # filled in.  That routine then resorts the results back to the original parameter order.
    sinB = sin(A) * b / a
    if sinB > 1:
        return 'Error: no such triangle', a, b, c, A, B, C
    B = asin(sinB)
    if flag == 'other':
        B = 180 - B
        C = 180 - A - B
        c = b * sin(C) / sinB
        return '', a, b, c, A, B, C
    else:
        C = 180 - A - B
        c = b * sin(C) / sinB
        if a < b:
            return 'Other solution available', a, b, c, A, B, C
        else:
            return '', a, b, c, A, B, C


def complete_the_triangle(a=None, b=None, c=None, A=None, B=None, C=None, ssa_flag='regular'):
    """
    Given a partially defined triangle, fill in (complete) the other entries, if possible.

    :param a: length of side a (side opposite angle A)
    :param b: length of side b (side opposite angle B)
    :param c: length of side c (side opposite angle C)
    :param A: angle (degrees) subtended by side a
    :param B: angle (degrees) subtended by side b
    :param C: angle (degrees) subtended by side c
    :param ssa_flag: a value of 'other' asks for the return of the alternate solution (possible in ssa triangle)
    :return: err_msg, a, b, c, A, B, C

    If 3 parameters from a realizable triangle are provided, at least one 'solution' will be returned.

    If only 2 angles are given, the third is computed using 180 - angle1 - angle2

    3 angles given without a side is a special case - such a triangle has no scale. To provide for a scale, one
    length with value equal 1 is added to the parameter set.

    If err_msg starts with the string 'Other', the triangle specification allows for two solutions.  To
    get that second solution, call this routine with ssa_flag='other'

    If a solution has been found, then err_msg == ''

    Any other string in err_msg indicates the type of error that has occurred.
    """

    # Validate angles provided ...  (lengths are validated in the 3 sides solver)
    if A is not None and A <= 0:
        err_msg = 'Error: angle A is <= 0.0'
        return err_msg, a, b, c, A, B, C
    if B is not None and B <= 0:
        err_msg = 'Error: angle B is <= 0.0'
        return err_msg, a, b, c, A, B, C
    if C is not None and C <= 0:
        err_msg = 'Error: angle C is <= 0.0'
        return err_msg, a, b, c, A, B, C

    angle_sum = 0
    angle_count = 0
    if A is not None:
        angle_sum += A
        angle_count += 1
    if B is not None:
        angle_sum += B
        angle_count += 1
    if C is not None:
        angle_sum += C
        angle_count += 1

    if angle_count == 3:
        if not angle_sum == 180.0:
            err_msg = 'Error: 3 angles given that do not sum to exactly 180.0 degrees'
            return err_msg, a, b, c, A, B, C
    elif angle_count > 0:
        if not angle_sum < 180.0:
            err_msg = 'Error: 2 angles given that do not sum to less than 180.0 degrees'
            return err_msg, a, b, c, A, B, C

    # ... end angle validation

    # =============== 3 sides given problems =================================

    if a is not None and b is not None and c is not None:
        # Solution using 3 sides  If angles were also given, they are left untouched.  That's not relevant
        # for this call, but that property is used in the solution of 2 sides with included angle triangles.
        return finish_triangle_with_three_sides_defined(a, b, c, A, B, C)

    # =============== 2 sides and included angle problems ====================

    if a is not None and b is not None and C is not None:
        # Solution from a, b, and C (included angle)
        c = np.sqrt(a * a + b * b - 2.0 * a * b * cos(C))
        return finish_triangle_with_three_sides_defined(a, b, c, A, B, C)

    if b is not None and c is not None and A is not None:
        # Solution from b, c, and A (included angle)
        a = np.sqrt(b * b + c * c - 2.0 * b * c * cos(A))
        return finish_triangle_with_three_sides_defined(a, b, c, A, B, C)

    if a is not None and c is not None and B is not None:
        # Solution from a, c, and B (included angle)
        b = np.sqrt(a * a + c * c - 2.0 * a * c * cos(B))
        return finish_triangle_with_three_sides_defined(a, b, c, A, B, C)

    # =============== 2 sides and opposite angle problems ====================

    # The key is to call the ssa() routine with a, b, and A filled in properly
    # from the user supplied parameters.  The results are put back where they belong
    # during distribution of the results from the ssa() call and then returned in
    # the order expected by the user.

    if a is not None and b is not None and A is not None:
        err_, a_, b_, c_, A_, B_, C_ = ssa(a, b, c, A, B, C, ssa_flag)
        return err_, a_, b_, c_, A_, B_, C_

    if a is not None and b is not None and B is not None:
        err_, b_, a_, c_, B_, A_, C_ = ssa(b, a, c, B, A, C, ssa_flag)
        return err_, a_, b_, c_, A_, B_, C_

    if b is not None and c is not None and B is not None:
        err_, b_, c_, a_, B_, C_, A_ = ssa(b, c, a, B, C, A, ssa_flag)
        return err_, a_, b_, c_, A_, B_, C_

    if b is not None and c is not None and C is not None:
        err_, c_, b_, a_, C_, B_, A_ = ssa(c, b, a, C, B, A, ssa_flag)
        return err_, a_, b_, c_, A_, B_, C_

    if a is not None and c is not None and A is not None:
        err_, a_, c_, b_, A_, C_, B_ = ssa(a, c, b, A, C, B, ssa_flag)
        return err_, a_, b_, c_, A_, B_, C_

    if a is not None and c is not None and C is not None:
        err_, c_, a_, b_, C_, A_, B_ = ssa(c, a, b, C, A, B, ssa_flag)
        return err_, a_, b_, c_, A_, B_, C_

    # =============== end: 2 sides and opposite angle problems ==================

    # =============== check for 2 angles (one missing angle) ====================

    if sum(angle is None for angle in (A, B, C)) == 1:
        # We calculate the missing angle and fall through to the aaas case
        if A is None and B is not None and C is not None:
            A = 180.0 - B - C
            if A <= 0:
                return 'Error: cannot solve with those starting conditions', a, b, c, A, B, C
        if B is None and A is not None and C is not None:
            B = 180.0 - A - C
            if B <= 0:
                return 'Error: cannot solve with those starting conditions', a, b, c, A, B, C
        if C is None and A is not None and B is not None:
            C = 180.0 - A - B
            if C <= 0:
                return 'Error: cannot solve with those starting conditions', a, b, c, A, B, C

    # ================ At this point, we're left only with aaas as a solvable triangle =======

    if sum(angle is not None for angle in (A, B, C)) == 3:
        # We've got three angles
        if sum(x is None for x in (a, b, c)) == 3:
            a = 1.0
        return solve_aaas_triangle(a, b, c, A, B, C)

    return 'Error: cannot solve with those starting conditions', a, b, c, A, B, C
