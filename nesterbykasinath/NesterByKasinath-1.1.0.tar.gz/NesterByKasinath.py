""" This module is written to demostrate recursion of nested list data structure"""
def PrintList(items, level):
    """ Iterate through each item in the list to identify if it's a list type
        If it's a list, recall the function again
        Else print the item in the list """
    for item in items:
        if(isinstance(item, list)):
            PrintList(item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(item)

