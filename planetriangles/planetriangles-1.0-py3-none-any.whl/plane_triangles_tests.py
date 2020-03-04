from planetriangles.plane_triangles import *

ALLOWED_TRIANGLE_ERROR = 1E-12

err, a, b, c, AA, BB, CC = complete_the_triangle(a=6, b=4, c=7)
if not err:
    print('1. C = ' + format_angle(CC, form='dm', precision=1))
    assert format_angle(CC, form='dm', precision=1) == '86d 25.0m'
else:
    print('1. ' + err)

assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
# print(triangle_error(a, b, c, AA, BB, CC))

err, a, b, c, AA, BB, CC = complete_the_triangle(a=5, b=3, C=43)
if not err:
    print('2. c = ' + format_length(c, precision=3))
    assert format_length(c, precision=3) == '3.473'
else:
    print('2. ' + err)

assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
# print(triangle_error(a, b, c, AA, BB, CC))

err, a, b, c, AA, BB, CC = complete_the_triangle(a=7, b=9, C=110)
if not err:
    print('3. B = ' + format_angle(BB, form='dm', precision=1))
    assert format_angle(BB, form='dm', precision=1) == '40d 0.1m'
else:
    print('3. ' + err)

assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
# print(triangle_error(a, b, c, AA, BB, CC))

err, a, b, c, AA, BB, CC = complete_the_triangle(a=4, b=5, A=29)
if err.startswith('Other'):
    print('4a. c = ' + format_length(c, precision=3))
    assert format_length(c, precision=3) == '7.555'
    assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
    # print(triangle_error(a, b, c, AA, BB, CC))
    err, a, b, c, AA, BB, CC = complete_the_triangle(a=4, b=5, A=29, ssa_flag='other')
    if not err:
        print('4b. c = ' + format_length(c, precision=3))
        assert format_length(c, precision=3) == '1.191'
        assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
        # print(triangle_error(a, b, c, AA, BB, CC))
    else:
        print('4b. ' + err)
else:
    print('4. ' + err)

err, a, b, c, AA, BB, CC = complete_the_triangle(a=5, b=7, A=37)
if err.startswith('Other'):
    print('5a. B = ' + format_angle(BB, form='dm', precision=1))
    assert format_angle(BB, form='dm', precision=1) == '57d 24.6m'
    assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
    # print(triangle_error(a, b, c, AA, BB, CC))
    err, a, b, c, AA, BB, CC = complete_the_triangle(a=5, b=7, A=37, ssa_flag='other')
    if not err:
        print('5b. B = ' + format_angle(BB, form='dm', precision=1))
        assert format_angle(BB, form='dm', precision=1) == '122d 35.4m'
        assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
        # print(triangle_error(a, b, c, AA, BB, CC))
    else:
        print('5b. ' + err)
else:
    print('5. ' + err)

err, a, b, c, AA, BB, CC = complete_the_triangle(a=8, b=5, A=54)
assert not err.startswith('Other')
if err.startswith('Other'):
    print('6a. C = ' + format_angle(CC, form='dm', precision=1))
    assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
    # print(triangle_error(a, b, c, AA, BB, CC))
    err, a, b, c, AA, BB, CC = complete_the_triangle(a=8, b=5, A=54, ssa_flag='other')
    if not err:
        print('6b. C = ' + format_angle(CC, form='dm', precision=1))
        assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
        # print(triangle_error(a, b, c, AA, BB, CC))
    else:
        print('6b. ' + err)
else:
    if not err:
        print('6. C = ' + format_angle(CC, form='dm', precision=1))
        assert format_angle(CC, form='dm', precision=1) == '95d 37.6m'
        assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
        # print(triangle_error(a, b, c, AA, BB, CC))
    else:
        print('6. ' + err)

err, a, b, c, AA, BB, CC = complete_the_triangle(A=64, B=37, C=180 - 64 - 37, c=1)
if not err:
    print('7. a/c = ' + format_length(a, precision=4) + ' b/c = ' + format_length(b, precision=4))
    assert format_length(a, precision=4) == '0.9156'
    assert format_length(b, precision=4) == '0.6131'
    assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
    # print(triangle_error(a, b, c, AA, BB, CC))
else:
    print('7. ' + err)

err, a, b, c, AA, BB, CC = complete_the_triangle(a=3, b=8, c=4)
assert err == 'Error: the 3 sides given do not form a triangle'
if not err:
    print('8. C = ' + format_angle(CC, form='dm', precision=1))
    assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
    # print(triangle_error(a, b, c, AA, BB, CC))
else:
    print('8. ' + err)

err, a, b, c, AA, BB, CC = complete_the_triangle(a=4, b=11, A=26)
assert err == 'Error: no such triangle'
if not err:
    print('9. c = ' + format_length(c, precision=4))
    assert triangle_error(a, b, c, AA, BB, CC)[0] < ALLOWED_TRIANGLE_ERROR
    # print(triangle_error(a, b, c, AA, BB, CC))
else:
    print('9. ' + err)

"""
print('='*50)

err, a, b, c, AA, BB, CC = complete_the_triangle(a=8, b=5, A=54, B=23.6266, C=180-54-23.6266)
print(f'err: {err}')
print(pretty_format_triangle(a, b, c, AA, BB, CC))
print(triangle_error(a, b, c, AA, BB, CC))

err, a, b, c, AA, BB, CC = complete_the_triangle(a=8, b=5, A=54, B=95.6266, C=180-54-95.6266)
print(f'err: {err}')

print(pretty_format_triangle(a, b, c, AA, BB, CC))
print(triangle_error(a, b, c, AA, BB, CC))

print('='*50)
err, a, b, c, AA, BB, CC = complete_the_triangle(a=5, b=7, A=37, B=57.41, C=180-37-57.41)
print(f'err: {err}')

print(pretty_format_triangle(a, b, c, AA, BB, CC))
print(triangle_error(a, b, c, AA, BB, CC))

err, a, b, c, AA, BB, CC = complete_the_triangle(a=5, b=7, A=37, B=122.59, C=180-37-122.59)
print(f'err: {err}')

print(pretty_format_triangle(a, b, c, AA, BB, CC))
print(triangle_error(a, b, c, AA, BB, CC))

err, a, b, c, AA, BB, CC = complete_the_triangle(a=5, b=7, A=37)
print(pretty_format_triangle(a, b, c, AA, BB, CC))

if err.startswith('Other'):
    print('5a. B = ' + format_angle(BB, form='dm', precision=1))
    # print(triangle_error(a, b, c, AA, BB, CC))
    err, a, b, c, AA, BB, CC = complete_the_triangle(a=5, b=7, A=37, ssa_flag='other')
    print(pretty_format_triangle(a, b, c, AA, BB, CC))

    if not err:
        print('5b. B = ' + format_angle(BB, form='dm', precision=1))
        # print(triangle_error(a, b, c, AA, BB, CC))
    else:
        print('5b. ' + err)
else:
    print('5. ' + err)

err, a, b, c, AA, BB, CC = complete_the_triangle(a=7, b=5, B=37)
print(pretty_format_triangle(a, b, c, AA, BB, CC))

if err.startswith('Other'):
    print('5a. A = ' + format_angle(AA, form='dm', precision=1))
    # print(triangle_error(a, b, c, AA, BB, CC))
    err, a, b, c, AA, BB, CC = complete_the_triangle(a=7, b=5, B=37, ssa_flag='other')
    print(pretty_format_triangle(a, b, c, AA, BB, CC))

    if not err:
        print('5b. A = ' + format_angle(AA, form='dm', precision=1))
        # print(triangle_error(a, b, c, AA, BB, CC))
    else:
        print('5b. ' + err)
else:
    print('5. ' + err)

err, a, b, c, AA, BB, CC = complete_the_triangle(a=7, c=5, C=37)
print(pretty_format_triangle(a, b, c, AA, BB, CC))

if err.startswith('Other'):
    print('5a. A = ' + format_angle(AA, form='dm', precision=1))
    # print(triangle_error(a, b, c, AA, BB, CC))
    err, a, b, c, AA, BB, CC = complete_the_triangle(a=7, c=5, C=37, ssa_flag='other')
    print(pretty_format_triangle(a, b, c, AA, BB, CC))

    if not err:
        print('5b. A = ' + format_angle(AA, form='dm', precision=1))
        # print(triangle_error(a, b, c, AA, BB, CC))
    else:
        print('5b. ' + err)
else:
    print('5. ' + err)

err, a, b, c, AA, BB, CC = complete_the_triangle(a=a, b=b, c=c, A=AA, B=BB, C=CC)
print(pretty_format_triangle(a, b, c, AA, BB, CC))
"""
