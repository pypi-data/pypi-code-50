class Kanchit:

    def __init__(self):
        self.name ='Kanchit'
        self.lastname = 'Kulnoy'
        self.nickname = 'Tum'

    def WhoIAm(self):
        '''
        นี่คือฟังชั่นในการแสดงชื่อคลาส This is a function will show the name
        '''
        print('My name is: {}'.format(self.name))
        print('My lastname is: {}'.format(self.lastname))
        print('My nikname is: {}'.format(self.nickname))

    @property
    def email(self):
        return 'email: {}.{}@gmail.com'.format(self.name.lower(), self.lastname.lower())
    def thainame(self):
        print('ครรชิต กุลน้อย')
        return('ครรชิต กุลน้อย')
    
    def __str__(self):
        return 'This is a myname Class '


if __name__ == '__main__':

    myname = Kanchit()
    print(myname.name)
    myname.WhoIAm()
    #mail = myname.email()
    print(myname.email)
    print(myname)
    myname.thainame()

    print(help(myname.WhoIAm))

    #mynong = Kanchit() #การใช้คลาสเป็นชื่ออื่น
    #mynong.name = 'Ton'
    #print(mynong.name)
    #print(myname.name)
    #mynong.WhoIAm()
