Ans='''"""

def insertion_sort(integers):
    """Iterate over the list of integers. With each iteration,
    place the new element into its sorted position by shifting
    over elements to the left of the pointer until the correct
    location is found for the new element.
    Sorts the list in place. O(n^2) running time, O(1) space. 
    """
    integers_clone = list(integers)
    for i in range(1, len(integers_clone)):
        j = i
        while integers_clone[j] < integers_clone[j - 1] and j > 0:
            integers_clone[j], integers_clone[j-1] = integers_clone[j-1], integers_clone[j]
            j -= 1
            
    return integers_clone

"""
'''
