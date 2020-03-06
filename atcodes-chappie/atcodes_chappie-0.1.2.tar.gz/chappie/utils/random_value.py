import random
import string


class RandomValue(object):
    """
    Generate a random value by 
    """
    def __init__(self, *args, **kwargs):
        super(RandomValue, self).__init__(*args, **kwargs)

    
    def string_digits(self, string_length=6):
        """
        Generate a random string of letters and digits
        By default string length is 6, could by customized
        """
        letters_and_digits = string.ascii_letters + string.digits
        return ''.join(random.choice(letters_and_digits) for i in range(string_length))

    def string(self, string_length=10):
        """
        Generate a random string of fixed length
        By default string length is 10, could by customized
        """
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for i in range(string_length))

    def string_lower(self, string_length=8):
        """Generate a random string of fixed length """
        letters= string.ascii_lowercase
        return ''.join(random.sample(letters, string_length))

    def rand_string(self, string_length=5, text='abcdefghi'):
        """
        Generate a random string of specific characters 
        """
        return ''.join((random.choice(your_letters) for i in range(string_length)))

    def rand_password(self, string_length=8):
        """
        Generate a random string of letters, digits and special characters
        """
        password_characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(password_characters) for i in range(string_length))
