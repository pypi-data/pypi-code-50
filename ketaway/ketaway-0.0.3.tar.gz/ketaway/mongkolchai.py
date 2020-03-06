class Ketaway:

    def __init__(self):
        self.name = 'Mongkolchai'
        self.lastname = 'Worakhajee'
        self.nickname = 'Ket'

    def WhoIAm(self):
        '''
        นี่คือฟังชั่นที่ใช้แสดงชื่อของผม
        This is function will show my description.
        '''
        print('My name is: {}'.format(self.name))
        print('My lastname is: {}'.format(self.lastname))
        print('My nickname is: {}'.format(self.nickname))
        self.thainame()
        
    @property
    def email(self):
        '''

        This is function will show email.
        '''
        return 'email: {}.{}@gmail.com'.format(self.name, self.lastname).lower()

    def thainame(self):
        print('ชื่อภาษาไทย : มงคลชัย วรขะจี')
        return 'มงคลชัย วรขะจี'
    
    def __str__(self):
        return 'This is a Ketaway class'

class Test_Update:

    def __init__(self):
        self.name = 'Firstname'
        self.lastname = 'Lastname'
        self.nickname = 'Test'

    def WhoIAm(self):
        '''
        นี่คือฟังชั่นที่ใช้แสดงชื่อของผม
        This is function will show my description.
        '''
        print('My name is: {}'.format(self.name))
        print('My lastname is: {}'.format(self.lastname))
        print('My nickname is: {}'.format(self.nickname))
        self.thainame()

    @property
    def email(self):
        '''

        This is function will show email.
        '''
        return 'email: {}.{}@hotmail.com'.format(self.name, self.lastname).lower()

    def thainame(self):
        print('ชื่อภาษาไทย : ชื่อ นามสกุล')
        return 'ชื่อ นามสกุล'
    
    def __str__(self):
        return 'This is a Test_Update class'
        

if __name__ == '__main__':
    
    mylib = Ketaway()
    print(help(mylib.WhoIAm))
    print(mylib)
    print(mylib.name)
    print(mylib.lastname)
    print(mylib.nickname)

    mylib.WhoIAm()
    print(mylib.email)


    mylib1 = Test_Update()
    print(help(mylib1.WhoIAm))
    print(mylib1)
    print(mylib1.name)
    print(mylib1.lastname)
    print(mylib1.nickname)

    mylib1.WhoIAm()
    print(mylib1.email)
