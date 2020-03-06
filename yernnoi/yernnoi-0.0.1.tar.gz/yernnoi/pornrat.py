class Yernnoi: #ชื่อ class
    
    def __init__(self): #เป็น fuction อินนิเชียว
        self.name = 'Pornrat'
        self.lastname = 'B'
        self.nickname = 'Yernnoi'

    def WhoIAM(self):

        '''
        This is a function will show the Yernnoi
        '''
        print('My name is : {}'.format(self.name))
        print('My lastname is : {}'.format(self.lastname))
        print('My nickname is : {}'.format(self.nickname))

    @property #ไม่จำเป็นต้องมี() หลังการเรียกใช้ฟังกชั่นพิเศษ
    def email(self):
        return 'email : {}.{}@gmail.com'.format(self.name.lower(),self.lastname.lower())

    def thainame(self):
        print('พรรัตน์')
        return 'พรรัตน์'
    
    def __str__(self):
        return 'This is a Yernnoi class'


if __name__=='__main__':
        
    myyernnoi = Yernnoi() #ชื่อ Obj

    print(help(myyernnoi.WhoIAM))

    print(myyernnoi.name)
    print(myyernnoi.lastname)
    print(myyernnoi.nickname)

    myyernnoi.WhoIAM()
    myyernnoi.thainame()
    

    print(myyernnoi.email) #ฟังกชั่น  or print #mail = myyernnoi.email()
    print(myyernnoi)    


