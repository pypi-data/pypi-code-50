""" list"""


def print_list(l_list, level=0):
    """递归打印list"""
    for i in l_list:
        if isinstance(i, list):
            print_list(i, level+1)
        else:
            for j in range(0, level):
                print("\t", end="")
            print(i)
