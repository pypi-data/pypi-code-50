class Yatima:
    def __init__(self): #selt = this in java
        self.name = 'Yatima'
        self.lastname = 'Chooruang'
        self.nickname = 'Noodang'

    def WhoIAm(self):
        '''
        This is function will show the name
        '''
        print('My name is: {}'.format(self.name))
        print('My lastname is: {}'.format(self.lastname))
        print('My nickname is: {}'.format(self.nickname))

    @property #want to be function not verb 
    def email(self):
        return 'email: {}.{}@gmail.com'.format(self.name.lower(),self.lastname.lower())

    def thainame(self):
        print('ญาติมา ชูเรือง')
        return 'ญาติมา ชูเรือง'
        
    def __str__(self):
        return 'This is a Yatima class'

    
    
if __name__ == '__main__':
    
    myLi = Yatima()
    #print(help(myLi.WhoIAm))
    print(myLi)
    #print(myLi.name)
    #print(myLi.lastname)
    myLi.WhoIAm()
    print(myLi.email)
    myLi.thainame()


    print('------------------')
    mypaa = Yatima()
    mypaa.name = 'Chaipichit'
    mypaa.lastname = 'Cumpim'
    mypaa.nickname = 'Chit'
    mypaa.WhoIAm()
    print(mypaa.name)
    print(mypaa.lastname)



