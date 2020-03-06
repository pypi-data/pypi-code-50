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


if __name__ == '__main__':
    
    mylib = Ketaway()
    print(help(mylib.WhoIAm))
    print(mylib)
    print(mylib.name)
    print(mylib.lastname)
    print(mylib.nickname)

    mylib.WhoIAm()
    print(mylib.email)
