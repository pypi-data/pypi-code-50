import random
import string

def tf1():
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(random.randrange(15,20)))

def tf2():
    password_characters = string.ascii_letters + string.digits
    return ''.join(random.choice(password_characters) for i in range(random.randrange(15,20)))