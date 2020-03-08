class Teammy:

    def __init__(self):
        self.name = 'T3ammy'
        self.lastname = 'Sit_Uncle_Engineer'
        self.nickname = 'teammy'

    def WhoIAM(self):
        ''' 
        นี่คือฟังชั่่นที่ใช้ในการแสดงชื่อของคราสนี้
        '''
        print('My name is: {}'.format(self.name))
        print('My lastname is: {}'.format(self.lastname))
        print('My nickname is: {}'.format(self.nickname))

    @property
    def email(self):
        '''
        This function will show my email
        '''
        return '{}.{}@teammy.engineer.com'.format(self.name.lower(),self.lastname.lower())
    def thainame(self):
        print('ทีมมี่ ศิษย์ลุงวิศวกร')
        return 'ทีมมี่ ศิษย์ลุงวิศวกร'
        
    def __str__(self):
        return 'This is my first library'

class Spiderman:
    
    def __init__(self):
        self.name = 'Peter'
        self.lastname = 'Parker'
        self.nickname = 'peter'
        self.thainame = 'ปีเตอร์'
    

if __name__ == '__main__':

    myName = Teammy()
    print(help(myName.WhoIAM))
    print('-------------')

    print(myName) # __str__ work when call variable
    print('-------------')

    print(myName.name)
    print(myName.lastname)
    print(myName.nickname)
    print('-------------')
    
    myName.thainame()
    print('-------------')

    myName.WhoIAM()
    print('-------------')

    print(myName.email) # is Property not use ()
    print('-------------')

    myFriend = Teammy()
    myFriend.WhoIAM()
    print('-------------')

    myFriend.name = 'Peter'
    myFriend.lastname = 'Parker'
    myFriend.nickname = 'peter'
    myFriend.WhoIAM()
    print('-------------')

    print(myFriend.name)
    print(myFriend.lastname)
    print(myFriend.nickname)
    print('-------------')

    pt = Spiderman()
    print(pt.name)
    print(pt.thainame)


    
