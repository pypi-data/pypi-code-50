"""Hello world program"""
class Main:
    """Class that returns string output"""
    def __init__(self, message='Hello, world!'):
        self.__message = message

    def __str__(self):
        return self.__message

    def output(self):
        """Method that prints string output of variable message"""
        print(self.__message)

Main().output()
