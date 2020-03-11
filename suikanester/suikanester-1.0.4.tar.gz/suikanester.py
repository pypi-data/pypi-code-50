"""
This is the "suikanester.py" module, and it provides one function called print_lol()
which prints lists that may or may not include nested lists.
"""


def print_lol(the_list, indent):
    # This is the indent for every level of the param 'the_list'
    i_string = ''
    i = 0
    while i < indent:
        i_string = i_string + '  '
        i = i + 1
    """This function takes a positional argument called "the_list", which is any
    python lis (of, possibly, nested lists). Each data item in the provided list is
    (recursively) printed to the screen on its own line."""
    for item in the_list:
        if isinstance(item, list):
            print(i_string + '[')
            print_lol(item, indent + 1)
            print(i_string + ']')
        else:
            print(i_string + str(item))
