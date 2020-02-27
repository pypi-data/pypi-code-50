from __future__ import absolute_import
import random
import string
import math


# 判断是否是质数，输入>=0的数返回true/false
def is_prime(num):
    if num < 0:
        return "must be a positive number"
    try:
        if num == 1 or num == 0:
            return "not a prime number or a composite number"
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


# 判断是否是平方数，输入>=0的数返回true/false
def is_square(num):
    try:
        if num >= 0:
            if abs(num ** 0.5 - int(num ** 0.5)) < 10 ** -10:
                return True
            else:
                return False
        else:
            return "must be a positive number"
    except TypeError:
        return "not an integer"


# 一元二次方程 ax^2+bx+c=0
def quad_equation_1unknown(a, b, c):
    if a == 0:
        if b == 0:
            return "not a equation"
        else:
            return -c/b
    else:
        temp_q = b**2 - 4*a*c
        if temp_q < 0:
            return None
        elif temp_q == 0:
            return -b/(2*a)
        else:
            return (-b+math.sqrt(temp_q))/(2*a), (-b-math.sqrt(temp_q))/(2*a)


# 斐波那契数列的第n项
def fib(num):
    try:
        f_a, f_b = 1, 1
        for i in range(num - 1):
            f_a, f_b = f_b, f_a + f_b
        return f_a
    except TypeError:
        raise Exception("unknown error")


# 随机字母密码
def random_method1(len1):
    m1_a = ""
    if len1 < 1:
        return "length must be bigger than 0"
    for i in range(int(len1)):
        m1_a = m1_a + random.choice(string.ascii_letters)
    return m1_a


# 随机字母和数字密码
def random_method2(len1):
    m2_a = ""
    if len1 < 1:
        return "length must be bigger than 0"
    for i in range(int(len1)):
        b = string.ascii_letters + string.digits
        m2_a = m2_a + random.choice(b)
    return m2_a


# 随机密码，包括所有字符
def random_all(len1):
    a_a = ""
    if len1 < 1:
        return "length must be bigger than 0"
    for i in range(int(len1)):
        b = string.printable
        b_r = random.choice(b)
        if b_r in string.whitespace or b_r in [" ", "\t", "\n"]:
            a_a = a_a + "e"
            continue
        a_a = a_a + b_r
    return a_a


# 密码强度（perfect,very good,very strong,average,low,too low）
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
    st = level_store(ll, ul, d, t, length)
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


# 密码强度得分
def level_store(ll, ul, d, t, length):
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


# 加密字符串
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


# 多项式对象
class Func:
    # 初始化
    def __init__(self, func_len):
        self.func_len = func_len
        self.func_coe_list = [0]*func_len
        self.func_power_list = list(range(1, func_len + 1))

    # 加入一项参数
    def add_thing(self, coefficient, power):
        self.func_coe_list[power-1] = coefficient

    # 输出多项式,reverse控制是否反向输出，默认false
    def print(self, reverse=False):
        if reverse is False:
            p_a = ""
            for i in range(1, self.func_len + 1):
                if int(self.func_coe_list[-i]) == 0:
                    continue
                else:
                    p_a = p_a + str(self.func_coe_list[-i]) + "x^" + str(self.func_power_list[-i]) + " + "
            print(p_a[:-2])
        elif reverse is True:
            p_a = ""
            for i in range(self.func_len):
                if int(self.func_coe_list[i]) == 0:
                    continue
                else:
                    p_a = p_a + str(self.func_coe_list[i]) + "x^" + str(self.func_power_list[i]) + " + "
            print(p_a[:-2])
        else:
            print("error")


if __name__ == '__main__':
    print(quad_equation_1unknown(21, 43, -99))
