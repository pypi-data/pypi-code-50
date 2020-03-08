class Snoopfluke:
    def __init__(self):
        self.name = 'Thanasak'
        self.lastname = 'Yaemburi'
        self.nickname = 'FLUKE'
    def WhoIAM(self):
        print('My name is: {}'.format(self.name))
        print('My lastname is: {}'.format(self.lastname))
        print('My nickname is: {}'.format(self.nickname))
        
    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.name.lower(),self.lastname.lower())

    def __str__(self):
        return 'This is a Fluke'


myfluke = Snoopfluke()
print(myfluke.name)
print(myfluke.lastname)
print ('---------')
mytest = Snoopfluke()
mytest.name = 'HIHI'
mytest.lastname = 'EIEI'
mytest.nickname = 'HAHA'
mytest.WhoIAM()
print(myfluke.email)
print(mytest.name)
print(myfluke)
