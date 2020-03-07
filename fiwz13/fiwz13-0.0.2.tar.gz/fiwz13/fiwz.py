class Fiwz:
    def __init__(self):
        self.name = 'Worawut'
        self.lastname = 'Tunsukee'
        self.nickname = 'Fiw'
        
    def WhoIAm(self):
        '''
        This is a function show the name.
        '''
        print('My name is : {}'.format(self.name))
        print('My lastname is : {}'.format(self.lastname))
        print('My nickname is : {}'.format(self.nickname))

    @property
    def email(self):
        '''
        This function show a email
        '''
        
        return 'email : {}.{}@gmail.com'.format(self.name.lower(),self.lastname.lower())
    
    def thainame(self):
        print('วรวุฒิ ตันสุขี')
        return'วรวุฒิ ตันสุขี'

        
    def __str__(self):
        return 'This is a zfiw class'

if __name__ == '__main__':
    
    myme = Fiwz()

    print(help(myme.WhoIAm))

    print(myme)
    print(myme.name)
    print(myme.lastname)
    print(myme.nickname)
    print(myme.thainame())

    myme.WhoIAm()
    mymeemail = myme.email
    print(mymeemail)


    print('-------------')
    myyou = Fiwz()

    myyou.name = 'Rattya'
    myyou.lastname = 'KP'
    myyou.nickname = 'Bell'
    myyou.WhoIAm()

    print(myyou.name)
    print(myyou.lastname)
    print(myyou.nickname)

