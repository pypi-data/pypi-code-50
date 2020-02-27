from __future__ import absolute_import
import random
import string
import math


def is_prime(num):
    if num < 0:
        raise Exception("must be a positive number")
    try:
        if num == 1 or num == 0:
            raise Exception("not a prime number or a composite number")
        sr_num = int(num ** 0.5 + 1)
        tem = sr_num
        for i in range(sr_num):
            if (num % tem) == 0:
                break
            tem -= 1
        if tem == 1:
            return True
        else:
            return False
    except TypeError:
        raise Exception("unknown error")


def is_square(num):
    try:
        if num >= 0:
            if abs(num ** 0.5 - int(num ** 0.5)) < 10 ** -10:
                return True
            else:
                return False
        else:
            raise Exception("must be a positive number")
    except TypeError:
        raise Exception("not an integer")


def quad_equation_1unknown(a, b, c):
    if a == 0:
        if b == 0:
            return "not a equation"
        else:
            return -c / b
    else:
        temp_q = b ** 2 - 4 * a * c
        if temp_q < 0:
            return None
        elif temp_q == 0:
            return -b / (2 * a)
        else:
            return (-b + math.sqrt(temp_q)) / (2 * a), (-b - math.sqrt(temp_q)) / (2 * a)


def line_equation_2unknown(a_, b, u, c, d, v):
    if [0] not in [a_, b, c, d]:
        try:
            return (d * u - b * v) / (a_ * d - b * c), (a_ * v - u * c) / (a_ * d - b * c)
        except ZeroDivisionError:
            return None
    else:
        raise Exception("not a 2unknown equation")


def fib(num):
    try:
        f_a, f_b = 1, 1
        for i in range(num - 1):
            f_a, f_b = f_b, f_a + f_b
        return f_a
    except TypeError:
        raise Exception("unknown error")


def random_method1(len1):
    m1_a = ""
    if len1 < 1:
        raise Exception("length must be bigger than 0")
    for i in range(int(len1)):
        m1_a = m1_a + random.choice(string.ascii_letters)
    return m1_a


def random_method2(len1):
    m2_a = ""
    if len1 < 1:
        raise Exception("length must be bigger than 0")
    for i in range(int(len1)):
        b = string.ascii_letters + string.digits
        m2_a = m2_a + random.choice(b)
    return m2_a


def random_all(len1):
    a_a = ""
    if len1 < 1:
        raise Exception("length must be bigger than 0")
    for i in range(int(len1)):
        b = string.printable
        b_r = random.choice(b)
        if b_r in string.whitespace or b_r in [" ", "\t", "\n"]:
            a_a = a_a + "e"
            continue
        a_a = a_a + b_r
    return a_a


def level(string1):
    s = list(string1)
    ll = d = t = ul = 0
    list1 = r'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    length = len(string1)

    for items in s:
        if items in string.ascii_lowercase:
            ll += 1
        if items in string.ascii_uppercase:
            ul += 1
        if items in string.digits:
            d += 1
        if items in list1:
            t += 1

    st = _level_store(ll, ul, d, t, length)
    if st >= 90:
        return "perfect"
    elif st >= 80:
        return " very good"
    elif st >= 70:
        return "very strong"
    elif st >= 60:
        return "strong"
    elif st >= 50:
        return "average"
    elif st >= 25:
        return "low"
    else:
        return "too low"


def _level_store(ll, ul, d, t, length):
    store = 0
    if d == 1:
        store += 10
    elif d > 1:
        store += 20
    else:
        pass
    if t == 1:
        store += 10
    elif t > 1:
        store += 25
    else:
        pass
    if ll == 0 and ul == 0:
        pass
    elif ll != 0 and ul != 0:
        store += 20
    else:
        store += 1
    if length < 5:
        store += 5
    elif length < 8:
        store += 10
    else:
        store += 20
    if ((ll and ul) and d) and t:
        store += 5
    elif ((ll or ul) and d) and t:
        store += 3
    else:
        store += 2
    if length > 50:
        store += 50
    elif length > 40:
        store += 40
    elif length > 30:
        store += 30
    elif length > 20:
        store += 20
    else:
        pass
    return store


def encode1(st):
    e1_a, b = random_all(10), random_all(10)
    lst = list(st)
    st1 = ""
    for items in lst:
        ord1 = ord(items) + 1
        st1 = st1 + chr(ord1)
    st = st1
    st = e1_a + st + b
    return st


def base_convert(before, after, num):
    num = str(num)
    result = 0

    if before > 62 or after > 62:
        raise Exception("base cannot be bigger than 62")
    if before < 2 or after < 2:
        raise Exception("base cannot be smaller than 2")
    # errors
    li = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
          'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
          'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
          'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
          'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
          'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
          'Y', 'Z']
    s = []
    for i in range(len(num)):
        s.append(num[i])
        if str(num[i]) not in li[0:(before - 1)]:
            raise Exception("invalid number!")
    # str to list
    t = len(s)
    for i in s:
        result += li.index(i) * (before ** (t - 1))
        t -= 1
    del t, s
    # decimal

    s = result
    result = []
    quotient = remainder = 1
    while quotient != 0:
        quotient, remainder = s // after, s % after
        s = quotient
        result.append(li[remainder])
    return "".join(result[::-1])


if __name__ == '__main__':
    print(base_convert(62, 10, "536"))
