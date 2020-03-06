class Samree:

    def __init__(self):
        self.name = 'Samree'
        self.lastname = 'Tira'
        self.nickname = 'Sam'
        
    def WhoIAm(self):
        '''
        Function is Class name Samree
        '''
        print('My name is : {}'.format(self.name))
        print('My lastname is : {}'.format(self.lastname))
        print('My nickname is : {}'.format(self.nickname))

    @property
    def email(self):
        '''
        Function  show email
        '''
        return 'email : {}.{}@gmail.com'.format(self.name.lower(),self.lastname.lower())

    def thainame(self):
        print("ซามรี    ทิลา")
        return  "ซามรี    ทิลา"
    def __str__(self):
        return 'This is a Samree Class'

if __name__ == '__main__' :

    mysamree = Samree()
    print(mysamree)
    print(mysamree.name)
    print(mysamree.lastname)
    print(mysamree.nickname)
    mysamree.WhoIAm()
    print(mysamree.email)
    print('-------------')

    mypaa = Samree()
    mypaa.name = 'Somsri'
    mypaa.lastname = 'Konthai'
    mypaa.nickname = 'Sri'
    mypaa.WhoIAm()

    print(mypaa.name)
    print(mypaa.lastname)
    print(mypaa.nickname)
