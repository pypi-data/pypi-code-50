"""This is the "nester.py" module, which prints the contents of a list, including any additional nested lists."""

def printLol(theList, indent=False, level=0):
        """This function takes a positional argument called "theList", which is any Python list (of, possibly, nested lists).
        It also takes an argument "indent", which gives the user the option to use indentation for nested items, or not.  It is a boolean value. Default value is false.
        The third argument "level" indicates the number of tab-stops specified in the input variable. Default value is 0.
        If the item is not a list, print the item to screen.  
        If it is a list, call the function printLol() again to recursively parse the nested list, printing each item on its own line."""
        
        for item in theList:
                if isinstance(item, list):
                        printLol(item,indent,level+1)
                else:
                        if indent:
                                for num in range(level):
                                        print("\t", end='')
                        print(item)

