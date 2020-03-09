class MyList(object):
     def __init__(self):
            self.container = []
     def add(self, item):
             self.container.append(item)
     def __iter__(self):
            """返回一个迭代器"""
             # 我们暂时忽略如何构造一个迭代器对象
            pass

mylist = MyList()
from collections import Iterable
print(isinstance(mylist, Iterable))