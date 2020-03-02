"""Hello world program"""
class Main:
    """Class that returns and prints a string output"""
    def __init__(self, message=""):
        self.__message = message

    def inputter(self):
        """Method that creates string variable name and adds it to string variable message"""
        name = input(str("Name: ")).title()
        message = "Hello, " + name + "!"
        Main().output(message)

    def output(self, message):
        """Method that takes string input message and prints it"""
        print(message)

Main().inputter()
