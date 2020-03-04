from sclass import sclass

class Test(sclass):
    def __init__(self):
        self.name = "lorenzo"
        self._surname = "bartolini"

    def publicmethod(self):
        return 'Public'

    def _privatemethod(self):
        return 'private'

x = Test()

'''
Feel free to experiment with the possibility of this Superclass

REMEMBER private methods and attributes starts with one and only one '_'.
be careful or if you put twice the '_' at the start with won't be recognized as private

'''

print(x.name)
print(x.publicmethod())
print(x._surname)
print(x._privatemethod())
