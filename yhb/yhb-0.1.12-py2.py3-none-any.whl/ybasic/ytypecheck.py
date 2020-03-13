def y_isdigit(s):
    # 判断是否是int型数字
    try:
        int(s)
        return True
    except ValueError:
        return False


def y_isfloat(s):
    # 判断是否是float型数字
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    n = "-inf"
    print(y_isdigit(n))
    print(y_isfloat(n))
