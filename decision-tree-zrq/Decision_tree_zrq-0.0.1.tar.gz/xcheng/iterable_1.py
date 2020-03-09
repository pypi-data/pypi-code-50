from collections import Iterable

print(isinstance([], Iterable))


print(isinstance({}, Iterable))

print(isinstance('abc', Iterable))

class MyList(object):
    def __init__(self):
            self.container = []
    def add(self, item):
            self.container.append(item)

mylist = MyList()
mylist.add(1)
mylist.add(1)
mylist.add(1)


print(isinstance(mylist, Iterable))

print(isinstance(100, Iterable))
